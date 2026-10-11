#!/usr/bin/env python3
"""Turn a published edition into the email newsletter and send it with Buttondown.

Usage:
    python3 scripts/newsletter.py _posts/2026-10-12-daily.md          # print the email
    python3 scripts/newsletter.py _posts/2026-10-12-daily.md --send   # send it

Sending needs the BUTTONDOWN_API_KEY environment variable. It runs from the
GitHub workflow .github/workflows/newsletter.yml whenever a new edition is
pushed, so nobody has to send anything by hand.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from new_post import SECTIONS, site_url  # noqa: E402


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"newsletter.py: {path} has no front matter")
    return json.loads(m.group(1))


def strip_math(s):
    return re.sub(r"\\\(|\\\)|\\\[|\\\]", "", s or "")


def build(front):
    base = site_url()
    day = datetime.strptime(front["date"][:10], "%Y-%m-%d")
    edition = front["edition"]
    url = f'{base}/{day.strftime("%Y/%m/%d")}/{edition}/'
    nice_day = f"{day.strftime('%A')} {day.day} {day.strftime('%B %Y')}"
    if edition == "daily":
        subject = front.get("headline") or f"Daily Brief, {day.day} {day.strftime('%B')}"
        lines, lines_title = front.get("three_lines") or [], "In three lines"
        kicker = f"Daily Brief · {nice_day}"
    else:
        subject = "Weekly Review: " + (front.get("headline") or front.get("week_of", ""))
        lines, lines_title = front.get("five_lines") or [], "The week in five lines"
        kicker = f"Weekly Review · {nice_day}"

    out = [f"*{kicker}* · [Read on esscher.com]({url})", "", f"## {lines_title}", ""]
    for i, l in enumerate(lines, 1):
        out.append(f"{i}. {l}")
    out.append("")
    after_lines = len(out)

    c = front.get("chart")
    chart_block = []
    if c:
        chart_block = ["## Chart of the day", "", f"**[{c['title']}]({url}#chart)**  ",
                       strip_math(c.get("note") or c.get("subtitle") or ""), ""]
    for key, label, _ in SECTIONS[edition]:
        items = front.get(key)
        if isinstance(items, dict):
            items = [items]
        if not items:
            continue
        out += [f"## {label}", ""]
        for it in items:
            title = it.get("headline") or it.get("title")
            if not title:
                continue
            link = base + it["story"] if it.get("story") else (it.get("url") or "")
            summary = it.get("summary") or it.get("dek") or it.get("why") or ""
            out.append(f"**[{title}]({link})**  " if link else f"**{title}**  ")
            meta = []
            if it.get("authors"):
                meta.append(it["authors"])
            if summary:
                meta.append(strip_math(summary))
            out.append(" · ".join(meta) if meta else "")
            out.append("")
        if key == "must_read":
            out += chart_block
    if chart_block and not front.get("must_read"):
        out[after_lines:after_lines] = chart_block
    out += ["---", "", f"[Read this edition on esscher.com]({url}) · [Archive]({base}/archive/) · [About]({base}/about/)", "",
            "*For information only. Not investment advice.*"]
    body = "\n".join(out).strip() + "\n"
    return subject, body, url


def send(subject, body, url):
    key = os.environ.get("BUTTONDOWN_API_KEY")
    if not key:
        sys.exit("newsletter.py: BUTTONDOWN_API_KEY is not set")
    payload = {"subject": subject, "body": body, "status": "about_to_send", "canonical_url": url}
    req = urllib.request.Request("https://api.buttondown.com/v1/emails", data=json.dumps(payload).encode("utf-8"),
                                 headers={"Authorization": f"Token {key}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.loads(r.read().decode("utf-8") or "{}")
            print(f"newsletter.py: queued '{subject}' (status {res.get('status')}, id {res.get('id')})")
    except urllib.error.HTTPError as e:
        sys.exit(f"newsletter.py: Buttondown answered {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    front = load(args[0])
    subject, body, url = build(front)
    if "--send" in sys.argv:
        send(subject, body, url)
    else:
        print("Subject:", subject)
        print()
        print(body)


if __name__ == "__main__":
    main()
