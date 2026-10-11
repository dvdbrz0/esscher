#!/usr/bin/env python3
"""Turn a brief written as JSON into a Jekyll post for the Esscher site.

Usage:
    python3 scripts/new_post.py path/to/brief.json

The JSON format is described in _docs/format.md. The script validates the
input, cleans links, and writes _posts/YYYY-MM-DD-daily.md or
_posts/YYYY-MM-DD-weekly.md, one page per story in _stories/, and the chart of
the day in _includes/charts/. It prints every file it wrote.
"""
import json
import re
import unicodedata
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chart  # noqa: E402
import share_card  # noqa: E402
import typography  # noqa: E402
import mathtext  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WRITTEN = []
LIST_KEYS = ["ai", "markets", "economy", "mathematics", "voices", "papers",
             "mattered", "canon", "read", "debates", "watch"]


def fail(msg):
    sys.stderr.write("new_post.py: " + msg + "\n")
    sys.exit(1)


def clean_url(url):
    """Unwrap tracking redirects (for example Gmail's google.com/url?q=...)."""
    if not isinstance(url, str):
        return url
    url = url.strip()
    parsed = urlparse(url)
    if parsed.netloc.endswith("google.com") and parsed.path == "/url":
        q = parse_qs(parsed.query).get("q")
        if q:
            return q[0]
    return url


def clean(obj):
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "url":
                v = clean_url(v)
            out[k] = clean(v)
        return out
    if isinstance(obj, list):
        return [clean(x) for x in obj]
    if isinstance(obj, str):
        return obj.strip()
    return obj


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?Z)?$")


def check_dates(items, where):
    """Keep "published" only when it is YYYY-MM-DD or YYYY-MM-DDTHH:MM(:SS)Z."""
    for i, it in enumerate(items or []):
        if isinstance(it, dict) and "published" in it:
            if not isinstance(it["published"], str) or not DATE_RE.match(it["published"]):
                sys.stderr.write(f"new_post.py: dropped {where}[{i}].published (use YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)\n")
                del it["published"]


def check_sources(items, where):
    for i, it in enumerate(items or []):
        for s in it.get("sources", []) or []:
            if not s.get("name") or not str(s.get("url", "")).startswith("http"):
                fail(f"{where}[{i}] has a source without a name or an http(s) url")


SECTIONS = {
    "daily": [("must_read", "Must-read", "story"), ("ai", "AI and machine learning", "story"),
              ("markets", "Markets", "story"), ("economy", "Economy", "story"),
              ("mathematics", "Mathematics", "story"), ("papers", "Papers", "paper")],
    "weekly": [("mattered", "What mattered", "story"), ("maths", "The maths behind the news", "explainer"),
               ("read", "Read this week", "paper"),
               ("canon", "Papers that became canon", "paper"), ("debates", "The debates", "story"),
               ("markets", "Quantitative finance and markets", "story"), ("economy", "Economy", "story"),
               ("mathematics", "Mathematics", "story")],
}


def slugify(text, limit=70):
    # "L²" becomes "l2", "Erdős" becomes "erdos".
    text = unicodedata.normalize("NFKD", unicodedata.normalize("NFKC", text)).encode("ascii", "ignore").decode()
    text = text.lower().replace("'", "").replace("’", "")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:limit].rstrip("-") or "story"


def paragraphs(body):
    if isinstance(body, str):
        body = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    return [p.strip() for p in body if isinstance(p, str) and p.strip()]


def load_topics():
    text = (ROOT / "_data" / "topics.yml").read_text(encoding="utf-8")
    return [m.strip().strip('"') for m in re.findall(r"^- name:\s*(.+)$", text, re.M)]


DEFAULT_TOPICS = {"markets": ["Markets"], "economy": ["Economy"], "mathematics": ["Mathematics"], "maths": ["Mathematics"]}


def pick_topics(it, key, allowed):
    topics = it.get("topics") or []
    if isinstance(topics, str):
        topics = [topics]
    good = [t for t in topics if t in allowed]
    for t in topics:
        if t not in allowed:
            sys.stderr.write(f"new_post.py: unknown topic '{t}' dropped (see _data/topics.yml)\n")
    if not good:
        if it.get("tag") in allowed:
            good = [it["tag"]]
        else:
            good = DEFAULT_TOPICS.get(key, [])
    return good[:3]


def plain_titles(obj):
    """Headlines and titles cannot be typeset (page titles, share images, feeds): Unicode mathematics only."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in ("headline", "title") and isinstance(v, str) and ("\\(" in v or "\\[" in v):
                sys.stderr.write(f"new_post.py: LaTeX in a {k} written as Unicode: {v!r}\n")
                v = mathtext.to_plain(v)
            out[k] = plain_titles(v)
        return out
    if isinstance(obj, list):
        return [plain_titles(x) for x in obj]
    return obj


def has_math(obj):
    """True when any string uses the \\( \\) or \\[ \\] math delimiters."""
    if isinstance(obj, str):
        return "\\(" in obj or "\\[" in obj
    if isinstance(obj, dict):
        return any(has_math(v) for v in obj.values())
    if isinstance(obj, list):
        return any(has_math(v) for v in obj)
    return False


def write_stories(front, edition, day):
    """Write one page per story or paper that has a "body", and link it from the edition."""
    stories_dir = ROOT / "_stories"
    stories_dir.mkdir(exist_ok=True)
    prefix = f'{day.strftime("%Y-%m-%d")}-{edition}-'
    for old in stories_dir.glob(prefix + "*.md"):
        old.unlink()
    for old in (ROOT / "assets" / "og").glob(prefix + "*.png"):
        old.unlink()
    nice_day = f"{day.day} {day.strftime('%B %Y')}"
    edition_url = f'/{day.strftime("%Y/%m/%d")}/{edition}/'
    allowed = load_topics()
    used = set()
    for key, label, kind in SECTIONS[edition]:
        items = front.get(key)
        if isinstance(items, dict):
            items = [items]
        for it in items or []:
            body = paragraphs(it.get("body") or [])
            title = it.get("headline") or it.get("title")
            if not body or not title:
                if title:
                    sys.stderr.write(f"new_post.py: no story page for '{title}' (no body)\n")
                continue
            slug = slugify(title)
            n = 2
            while slug in used:
                slug = f"{slugify(title)}-{n}"
                n += 1
            used.add(slug)
            name = prefix + slug
            story = {
                "layout": "story",
                "title": title,
                "kind": kind,
                "section": label,
                "edition": edition,
                "edition_url": edition_url,
                "date": front["date"],
                "summary": it.get("summary") or it.get("dek") or it.get("why") or "",
                "body": body,
            }
            for k in ("why", "sources", "links", "published", "authors", "arxiv", "url", "tag", "status"):
                if it.get(k):
                    story[k] = it[k]
            topics = pick_topics(it, key, allowed)
            if topics:
                story["topics"] = topics
                it["topics"] = topics
            if has_math(story):
                story["math"] = True
            if has_math(story["summary"]):
                story["summary_plain"] = mathtext.to_plain(story["summary"])
            if key == "must_read" and it.get("section"):
                story["section"] = "Must-read · " + it["section"]
            if kind == "paper":
                kicker = "Paper · " + it["tag"] if it.get("tag") else "Paper"
            else:
                kicker = " · ".join(story["section"].split(" · ")[:2])
            card = ROOT / "assets" / "og" / f"{name}.png"
            if share_card.make_card(card, title, kicker, nice_day):
                story["image"] = f"/assets/og/{name}.png"
                WRITTEN.append(card)
            text = "---\n" + json.dumps(story, ensure_ascii=False, indent=1) + "\n---\n"
            (stories_dir / f"{name}.md").write_text(text, encoding="utf-8")
            WRITTEN.append(stories_dir / f"{name}.md")
            it["story"] = f"/stories/{name}/"
            it["body"] = body


def site_url():
    m = re.search(r'^url:\s*"?([^"\n]+)"?', (ROOT / "_config.yml").read_text(encoding="utf-8"), re.M)
    return (m.group(1).rstrip("/") if m else "")


def write_chart(front, edition, day):
    """Validate the chart of the day and draw it as an SVG include."""
    spec = front.get("chart")
    if not spec:
        return
    for k in ("title", "points", "source", "source_url"):
        if not spec.get(k):
            fail(f'chart needs "{k}" (see _docs/format.md)')
    if not str(spec["source_url"]).startswith("http"):
        fail("chart.source_url must be an http(s) link")
    if spec.get("kind", "line") not in ("line", "bar"):
        fail('chart.kind must be "line" or "bar"')
    try:
        svg = chart.render(spec)
    except (ValueError, KeyError, TypeError) as e:
        fail(f"chart could not be drawn: {e}")
    rel = f'charts/{day.strftime("%Y-%m-%d")}-{edition}.svg'
    out = ROOT / "_includes" / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    WRITTEN.append(out)
    pts = spec.pop("points")
    spec["svg"] = rel
    if spec.get("kind", "line") == "line":
        last = max(pts, key=lambda q: q["x"])
        spec.setdefault("latest", last["y"])
        spec.setdefault("latest_date", last["x"])


def feed_body(front, edition):
    """Plain links for feed readers: the lines of the day and every headline."""
    base = site_url()
    out = []
    lines = front.get("three_lines") or front.get("five_lines") or []
    for i, l in enumerate(lines, 1):
        out.append(f"{i}. {mathtext.to_plain(l)}")
    out.append("")
    for key, label, _ in SECTIONS[edition]:
        items = front.get(key)
        if isinstance(items, dict):
            items = [items]
        if not items:
            continue
        out.append(f"**{label}**")
        out.append("")
        for it in items:
            title = it.get("headline") or it.get("title")
            if not title:
                continue
            link = base + it["story"] if it.get("story") else None
            summary = mathtext.to_plain(it.get("summary") or it.get("dek") or it.get("why") or "")
            head = f"[{title}]({link})" if link else title
            out.append(f"- {head}" + (f": {summary}" if summary else ""))
        out.append("")
    return "\n".join(out).strip() + "\n"


def main():
    if len(sys.argv) != 2:
        fail("give exactly one argument: the JSON file")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    data = clean(data)
    data = typography.apply(data)
    data = plain_titles(data)

    edition = data.get("edition")
    if edition not in ("daily", "weekly"):
        fail('"edition" must be "daily" or "weekly"')
    try:
        day = datetime.strptime(data.get("date", ""), "%Y-%m-%d")
    except ValueError:
        fail('"date" must look like 2026-10-12')

    for k in LIST_KEYS:
        if k in data and not isinstance(data[k], list):
            fail(f'"{k}" must be a list')
        check_dates(data.get(k), k)

    if edition == "daily":
        lines = data.get("three_lines")
        if not isinstance(lines, list) or len(lines) != 3:
            fail('"three_lines" must be a list of exactly 3 strings')
        if not data.get("ai"):
            fail('"ai" must have at least one item')
        for k in ("ai", "markets", "economy", "mathematics"):
            check_sources(data.get(k), k)
            for i, it in enumerate(data.get(k) or []):
                if not it.get("headline") or not it.get("summary"):
                    fail(f"{k}[{i}] needs a headline and a summary")
        for i, p in enumerate(data.get("papers") or []):
            if not p.get("title") or not p.get("summary"):
                fail(f"papers[{i}] needs a title and a summary")
        headline = (data.get("must_read") or {}).get("headline") or data["ai"][0]["headline"]
        description = mathtext.to_plain(" ".join(lines))
        front = {"layout": "brief", "title": "Daily Brief"}
    else:
        lines = data.get("five_lines")
        if not isinstance(lines, list) or not lines:
            fail('"five_lines" must be a non-empty list')
        for k in ("mattered", "debates", "markets", "economy", "mathematics"):
            check_sources(data.get(k), k)
        mx = data.get("maths")
        if mx is not None:
            if not isinstance(mx, dict) or not mx.get("headline") or not mx.get("summary") or not mx.get("body"):
                fail('"maths" must be one object with a headline, a summary and a body')
            check_sources([mx], "maths")
        headline = data.get("headline") or ("Week of " + data.get("week_of", ""))
        description = mathtext.to_plain(" ".join(lines))
        front = {"layout": "weekly", "title": "Weekly Review"}

    hour = "05:00:00" if edition == "daily" else "08:00:00"
    front.update({
        "edition": edition,
        "date": f'{day.strftime("%Y-%m-%d")} {hour} +0300',
        "headline": headline,
        "description": description,
    })
    for k, v in data.items():
        if k not in ("edition", "date", "published", "updated"):
            front[k] = v
    if front.get("ticker_asof") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(front["ticker_asof"])):
        fail('"ticker_asof" must look like 2026-10-09')

    out = ROOT / "_posts" / f'{day.strftime("%Y-%m-%d")}-{edition}.md'
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # When the edition first went online, in UTC. A rerun keeps it and records the update.
    previous = None
    if out.exists():
        m = re.match(r"^---\n(.*?)\n---\n", out.read_text(encoding="utf-8"), re.S)
        try:
            previous = json.loads(m.group(1)).get("published") if m else None
        except ValueError:
            previous = None
    front["published"] = previous or now
    if previous:
        front["updated"] = now

    write_chart(front, edition, day)
    write_stories(front, edition, day)
    card = ROOT / "assets" / "og" / f'{day.strftime("%Y-%m-%d")}-{edition}.png'
    kicker = "Daily Brief" if edition == "daily" else "Weekly Review"
    if share_card.make_card(card, headline, kicker, f"{day.day} {day.strftime('%B %Y')}"):
        front["image"] = f'/assets/og/{card.name}'
        WRITTEN.append(card)
    else:
        sys.stderr.write("new_post.py: Pillow not available, pages use the default share image\n")
    if has_math({k: v for k, v in front.items() if k != "body"}):
        front["math"] = True

    # JSON is valid YAML, so the front matter is written as JSON: no quoting pitfalls.
    text = "---\n" + json.dumps(front, ensure_ascii=False, indent=1) + "\n---\n\n" + feed_body(front, edition)

    out.parent.mkdir(exist_ok=True)
    out.write_text(text, encoding="utf-8")
    WRITTEN.append(out)
    for path in WRITTEN:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
