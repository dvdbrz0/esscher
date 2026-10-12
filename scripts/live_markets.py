#!/usr/bin/env python3
"""Delayed quotes for the markets band in the header, written to live.json.

Run by .github/workflows/markets.yml on weekdays while markets are open. The band reads
/live.json from esscher.com itself, so a reader's browser sends no request to third
parties. Instruments, quote links and symbols are in _data/markets.json; entries without
symbols (policy rates) keep the value from the day's edition.

Sources, in order: CNBC's quote service, then Yahoo Finance's chart service. Both are
delayed by at least 15 minutes. A quote is dropped when it is missing, older than four
days, or more than 20% away from the close in the latest edition (10 points for a yield).

    python3 scripts/live_markets.py            write live.json when a quote changed
    python3 scripts/live_markets.py --check    print what each source returns, write nothing

Standard library only.
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "live.json"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
MINUS = "−"


def get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/plain,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).replace(",", "").replace("%", "").replace("$", "").replace(MINUS, "-").strip()
    m = re.match(r"^[+-]?\d+(\.\d+)?$", s)
    return float(s) if m else None


def parse_time(v):
    """CNBC gives times like 2026-10-12T16:00:00.000-0400; Yahoo gives epoch seconds."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return datetime.fromtimestamp(v, timezone.utc)
    s = str(v).strip()
    s = re.sub(r"\.\d+", "", s)
    s = re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", s)
    try:
        t = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else t.replace(tzinfo=timezone.utc)


def from_cnbc(instruments, check=False):
    symbols = [m["cnbc"] for m in instruments if m.get("cnbc")]
    url = ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols="
           + urllib.parse.quote("|".join(symbols), safe="")
           + "&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1")
    data = json.loads(get(url))
    rows = data.get("FormattedQuoteResult", {}).get("FormattedQuote", [])
    if isinstance(rows, dict):
        rows = [rows]
    if check:
        print("CNBC, first row:", json.dumps(rows[:1], indent=1)[:2500])
    out = {}
    for r in rows:
        sym = r.get("symbol")
        last = num(r.get("last"))
        prev = num(r.get("previous_day_closing"))
        change = num(r.get("change"))
        if prev is None and last is not None and change is not None:
            prev = last - change
        when = parse_time(r.get("last_time") or r.get("last_timedate"))
        if sym and last is not None:
            out[sym] = {"last": last, "prev": prev, "time": when}
    return {m["label"]: out[m["cnbc"]] for m in instruments if m.get("cnbc") in out}


def from_yahoo(instruments, check=False):
    out = {}
    for m in instruments:
        if not m.get("yahoo"):
            continue
        url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
               + urllib.parse.quote(m["yahoo"], safe="") + "?range=1d&interval=1d")
        try:
            meta = json.loads(get(url))["chart"]["result"][0]["meta"]
        except Exception as e:  # noqa: BLE001 - one bad symbol must not stop the rest
            if check:
                print(f"Yahoo {m['yahoo']}: {e}")
            continue
        if check and not out:
            print("Yahoo, first meta:", json.dumps(meta, indent=1)[:1500])
        last = num(meta.get("regularMarketPrice"))
        prev = num(meta.get("previousClose") or meta.get("chartPreviousClose"))
        if m.get("kind") == "yield" and last is not None and last > 20:
            last, prev = last / 10, (prev / 10 if prev is not None else None)
        if last is not None:
            out[m["label"]] = {"last": last, "prev": prev, "time": parse_time(meta.get("regularMarketTime"))}
    return out


def edition_closes():
    """Closing levels in the latest daily edition, for the sanity check."""
    posts = sorted((ROOT / "_posts").glob("*-daily.md"))
    if not posts:
        return {}
    m = re.match(r"^---\n(.*?)\n---\n", posts[-1].read_text(encoding="utf-8"), re.S)
    try:
        ticker = json.loads(m.group(1)).get("ticker") or [] if m else []
    except ValueError:
        return {}
    return {t.get("label"): num(t.get("value")) for t in ticker if num(t.get("value")) is not None}


def plausible(m, q, closes, now):
    if q["time"] is None or now - q["time"] > timedelta(days=4) or q["time"] - now > timedelta(hours=1):
        return False
    ref = closes.get(m["label"])
    if ref:
        if m.get("kind") == "yield":
            return abs(q["last"] - ref) <= 10
        return abs(q["last"] / ref - 1) <= 0.2
    return True


def fmt(m, q):
    last, prev = q["last"], q["prev"]
    kind = m.get("kind")
    if kind == "yield":
        value = f"{last:.2f}%"
    elif kind == "dollars":
        value = f"${last:,.{m.get('decimals', 2)}f}"
    else:
        value = f"{last:,.2f}"
    item = {"label": m["label"], "value": value, "time": q["time"].astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if prev:
        if kind == "yield":
            d = round((last - prev) * 100)
            change = f"{'+' if d > 0 else MINUS if d < 0 else ''}{abs(d)} bp"
        else:
            d = round((last / prev - 1) * 100, 1)
            change = f"{'+' if d > 0 else MINUS if d < 0 else ''}{abs(d):.1f}%"
        item["change"] = change
        item["dir"] = "down" if d < 0 else "up" if d > 0 else "flat"
    return item


def main():
    check = "--check" in sys.argv
    instruments = [m for m in json.loads((ROOT / "_data" / "markets.json").read_text(encoding="utf-8"))
                   if m.get("cnbc") or m.get("yahoo")]
    now = datetime.now(timezone.utc)
    closes = edition_closes()
    quotes, used = {}, []
    for name, fetch in (("CNBC", from_cnbc), ("Yahoo Finance", from_yahoo)):
        missing = [m for m in instruments if m["label"] not in quotes]
        if not missing:
            break
        try:
            got = fetch(missing, check)
        except Exception as e:  # noqa: BLE001 - try the next source
            print(f"{name}: {e}")
            continue
        took = False
        for m in missing:
            q = got.get(m["label"])
            if q and plausible(m, q, closes, now):
                quotes[m["label"]] = fmt(m, q)
                took = True
            elif q:
                print(f"{name}: dropped {m['label']} ({q['last']} at {q['time']})")
        if took:
            used.append(name)
        if check:
            print(f"{name}: {sorted(got)}")
    items = [quotes[m["label"]] for m in instruments if m["label"] in quotes]
    if check:
        print(json.dumps(items, indent=1, ensure_ascii=False))
        return
    if not items:
        print("live_markets.py: no usable quotes; live.json left as it is")
        return
    live = {
        "asof": max(i["time"] for i in items),
        "source": ", ".join(used),
        "note": "Delayed by at least 15 minutes.",
        "quotes": items,
    }
    old = None
    if OUT.exists():
        try:
            old = json.loads(OUT.read_text(encoding="utf-8"))
        except ValueError:
            old = None
    if old and old.get("quotes") == live["quotes"] and old.get("source") == live["source"]:
        print("live_markets.py: no change")
        return
    OUT.write_text(json.dumps(live, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"live_markets.py: {len(items)} quotes as of {live['asof']} from {live['source']}")


if __name__ == "__main__":
    main()
