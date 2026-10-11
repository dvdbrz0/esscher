# How an edition is written

Every edition is a JSON file turned into a post by `scripts/new_post.py`:

    python3 scripts/new_post.py /tmp/brief.json

The script validates the file, unwraps tracking links and writes
`_posts/YYYY-MM-DD-daily.md` or `_posts/YYYY-MM-DD-weekly.md`.
Run it again with the same date to replace an edition.

Write everything in English, in your own words. Every string is plain text
(no HTML, no markdown). Every `url` is a full https link to the original source.

Publication dates: every story and paper may carry `"published"`, the date the
original source was published, exactly as shown on the source page (for a paper,
the date on its arXiv abstract page). Format `YYYY-MM-DD`, or
`YYYY-MM-DDTHH:MM:SSZ` in UTC when the page gives a time. If you did not see the
date on the page, leave the field out: never guess. The time the edition itself
goes online is added by the script automatically.

## Daily brief

```json
{
  "edition": "daily",
  "date": "2026-10-12",
  "ticker_label": "Friday close",
  "ticker": [
    {"label": "S&P 500", "value": "7,811.54", "change": "+1.2% wk", "dir": "up"},
    {"label": "US 10Y", "value": "5.25%"}
  ],
  "three_lines": ["...", "...", "..."],
  "must_read": {
    "section": "Mathematics · AI",
    "headline": "...",
    "dek": "One or two sentences.",
    "body": "A short paragraph.",
    "why": "Why it matters, one sentence.",
    "status": "Partly unconfirmed",
    "links": [{"label": "New Scientist: the announcement", "url": "https://..."}]
  },
  "ai": [
    {"headline": "...", "summary": "One or two sentences.", "published": "2026-10-09", "sources": [{"name": "TechCrunch", "url": "https://..."}]}
  ],
  "voices": [{"name": "Yann LeCun", "summary": "...", "url": "https://x.com/..."}],
  "papers_note": "New on arXiv today",
  "papers": [
    {"tag": "Learning theory", "title": "...", "authors": "Hanneke et al.", "summary": "Main result in words.", "arxiv": "2610.10600", "published": "2026-10-09"}
  ],
  "markets": [{"headline": "...", "summary": "...", "sources": [{"name": "...", "url": "https://..."}]}],
  "economy": [{"headline": "...", "summary": "...", "sources": [{"name": "...", "url": "https://..."}]}],
  "mathematics": [{"headline": "...", "summary": "...", "sources": [{"name": "...", "url": "https://..."}]}]
}
```

- `must_read` is optional: leave it out when nothing qualifies.
- The first item of `ai` is shown largest: put the most important story first.
- `ticker` holds only figures taken from a source; leave out anything you do not have. `dir` is "up" or "down".
- `voices`, `mathematics`, `papers_note`, `status` are optional.

## Weekly review

```json
{
  "edition": "weekly",
  "date": "2026-10-18",
  "week_of": "12 October 2026",
  "headline": "A short headline for the week",
  "five_lines": ["...", "...", "...", "...", "..."],
  "mattered": [{"headline": "...", "body": "Two to four sentences.", "sources": [{"name": "...", "url": "https://..."}]}],
  "canon": [{"tag": "...", "title": "...", "authors": "...", "summary": "...", "arxiv": "2610.10600"}],
  "read": [{"title": "...", "authors": "...", "why": "...", "prerequisites": "...", "focus": "Sections 2 and 4", "time": "About 2 hours", "arxiv": "..."}],
  "debates": [{"headline": "...", "body": "...", "sources": [{"name": "...", "url": "https://..."}]}],
  "markets": [{"headline": "...", "body": "...", "sources": [...]}],
  "economy": [{"headline": "...", "body": "...", "sources": [...]}],
  "mathematics": [{"headline": "...", "body": "...", "sources": [...]}],
  "watch": [{"date": "Tue 13 Oct", "item": "IMF World Economic Outlook"}]
}
```
