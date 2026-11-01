#!/usr/bin/env python3
"""Download daily closes of a market instrument for a story's small chart ("spark").

Usage:
    python3 scripts/series.py SYMBOL [RANGE]
    python3 scripts/series.py BZ=F 6mo

SYMBOL is a Yahoo Finance symbol; RANGE is 3mo, 6mo (default) or 1y. Prints a
JSON list of {"x": "YYYY-MM-DD", "y": number}, ready for the "points" field of
a spark, then the latest close and its date on stderr. Quote the instrument in
the story with that same close and date, so the text and the chart agree.

Useful symbols:
  ^GSPC S&P 500        ^IXIC Nasdaq composite   ^DJI Dow Jones   ^RUT Russell 2000
  ^TNX US 10-year yield (%)   ^FVX US 5-year yield (%)   ^VIX volatility index
  BZ=F Brent futures ($)      CL=F WTI futures ($)       GC=F gold futures ($)
  EURUSD=X dollars per euro   BTC-USD bitcoin ($)        ^STOXX50E Euro Stoxx 50
For official series (Treasury yields, credit spreads, inflation) use
scripts/fred.py instead; FRED is usually a day or more behind the market.
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    symbol = sys.argv[1]
    rng = sys.argv[2] if len(sys.argv) > 2 else "6mo"
    if rng not in ("3mo", "6mo", "1y"):
        sys.exit("series.py: RANGE must be 3mo, 6mo or 1y")
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
           + urllib.parse.quote(symbol, safe="") + f"?range={rng}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    res = data["chart"]["result"][0]
    closes = res["indicators"]["quote"][0]["close"]
    pts = []
    for t, v in zip(res["timestamp"], closes):
        if v is None:
            continue
        day = datetime.fromtimestamp(t, timezone.utc).date().isoformat()
        if pts and pts[-1]["x"] == day:
            pts[-1]["y"] = round(v, 4)
        else:
            pts.append({"x": day, "y": round(v, 4)})
    if len(pts) < 10:
        sys.exit(f"series.py: only {len(pts)} closes for {symbol}")
    json.dump(pts, sys.stdout)
    print()
    sys.stderr.write(f"series.py: {len(pts)} closes for {symbol}, last {pts[-1]['y']} on {pts[-1]['x']}"
                     " (the last point may be today's unfinished session: drop it if the market is open)\n")


if __name__ == "__main__":
    main()
