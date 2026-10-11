#!/usr/bin/env python3
"""Correct a published story and record the correction publicly.

Usage:
    python3 scripts/correct.py STORY --note "What was wrong and what is right." \
        [--replace "old text" "new text"]...

STORY is the story's file in _stories/ or its address on the site, for example
/stories/2026-10-11-daily-fed-signals-another-hike-probably-not-in-october/.

Each --replace swaps text in the story page and in the edition that links to it
(headline, summary or body). The note is shown at the end of the story, marked
"Corrected", and listed on the corrections page. Write the note in the house
style: "An earlier version of this story said X. It is Y."
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fail(msg):
    sys.stderr.write("correct.py: " + msg + "\n")
    sys.exit(1)


def split(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        fail(f"{path} has no front matter")
    return json.loads(m.group(1)), m.group(2)


def join(front, body):
    return "---\n" + json.dumps(front, ensure_ascii=False, indent=1) + "\n---\n" + body


def swap(obj, old, new, count):
    if isinstance(obj, str):
        if old in obj:
            count[0] += obj.count(old)
            return obj.replace(old, new)
        return obj
    if isinstance(obj, list):
        return [swap(x, old, new, count) for x in obj]
    if isinstance(obj, dict):
        return {k: (v if k in ("url", "story", "edition_url", "layout", "image") else swap(v, old, new, count)) for k, v in obj.items()}
    return obj


def mark(obj, story_url, day):
    """Flag the edition's item that links to the story."""
    if isinstance(obj, list):
        for x in obj:
            mark(x, story_url, day)
    elif isinstance(obj, dict):
        if obj.get("story") == story_url:
            obj["corrected"] = day
        for v in obj.values():
            if isinstance(v, (list, dict)):
                mark(v, story_url, day)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("story")
    ap.add_argument("--note", required=True)
    ap.add_argument("--replace", nargs=2, action="append", default=[], metavar=("OLD", "NEW"))
    a = ap.parse_args()

    name = a.story.strip().rstrip("/").split("/")[-1]
    if name.endswith(".md"):
        name = name[:-3]
    spath = ROOT / "_stories" / f"{name}.md"
    if not spath.exists():
        fail(f"no story file {spath}")
    story, sbody = split(spath)
    story_url = f"/stories/{name}/"

    edition_file = None
    m = re.match(r"^/(\d{4})/(\d{2})/(\d{2})/(daily|weekly)/$", story.get("edition_url", ""))
    if m:
        edition_file = ROOT / "_posts" / f"{m.group(1)}-{m.group(2)}-{m.group(3)}-{m.group(4)}.md"

    old_title = story.get("title")
    count = [0]
    for old, new in a.replace:
        story = swap(story, old, new, count)
    if a.replace and count[0] == 0:
        fail("none of the --replace texts were found in the story")

    now = datetime.now(timezone.utc)
    day = now.strftime("%Y-%m-%d")
    story.setdefault("corrections", []).append({"date": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "note": a.note.strip()})
    story["corrected"] = day
    spath.write_text(join(story, sbody), encoding="utf-8")
    print(spath.relative_to(ROOT))

    if story.get("image") and story.get("title") != old_title:
        # The headline changed: redraw the image shown when the story is shared.
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import share_card
        if story.get("kind") == "paper":
            kicker = "Paper · " + story["tag"] if story.get("tag") else "Paper"
        else:
            kicker = " · ".join(str(story.get("section", "")).split(" · ")[:2])
        d = datetime.strptime(str(story["date"])[:10], "%Y-%m-%d")
        card = ROOT / story["image"].lstrip("/")
        if share_card.make_card(card, story["title"], kicker, f"{d.day} {d.strftime('%B %Y')}"):
            print(card.relative_to(ROOT))

    if edition_file and edition_file.exists():
        front, body = split(edition_file)
        for old, new in a.replace:
            front = swap(front, old, new, [0])
            body = body.replace(old, new)
        mark(front, story_url, day)
        edition_file.write_text(join(front, body), encoding="utf-8")
        print(edition_file.relative_to(ROOT))


if __name__ == "__main__":
    main()
