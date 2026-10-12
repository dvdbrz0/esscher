#!/usr/bin/env python3
"""Check that an edition is live on esscher.com and looks right.

Run after scripts/publish.sh. It waits for GitHub Pages to serve the new
edition, then checks every page and image the edition added, that nothing
older went missing, and how the pages render in Chromium on a phone and a
desktop, in light and dark mode. It only reads: it never changes the
repository or the site.

Usage:
  python3 scripts/check_live.py                      # today's edition (Bucharest date)
  python3 scripts/check_live.py 2026-10-12 daily     # a given edition
  options: --wait SECONDS (default 900), --shots DIR (default /tmp/esscher-check),
           --commit REV (the publish commit to inspect for deleted files, default HEAD)

Exit code 0 when every check passed, 1 when something is wrong, 2 when the
edition never appeared. The last line printed is a one-line summary.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

SITE = "https://esscher.com"
ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (esscher-check)"


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return json.loads(parts[1])


def bust(url):
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}check={int(time.time() * 1000)}"


def fetch(url, binary=False):
    """Return (status, content type, body) without raising."""
    req = urllib.request.Request(bust(url), headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            return r.status, r.headers.get("Content-Type", ""), body if binary else body.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", "") if e.headers else "", b"" if binary else ""
    except Exception as e:  # network trouble
        return 0, str(e), b"" if binary else ""


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def og_image(page_html):
    m = re.search(r'<meta property="og:image" content="([^"]+)"', page_html)
    return html.unescape(m.group(1)) if m else None


def img_srcs(page_html):
    out = []
    for m in re.finditer(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", page_html):
        src = html.unescape(m.group(1))
        if src.startswith("data:"):
            continue
        if src.startswith("/"):
            src = SITE + src
        if src.startswith(SITE):
            out.append(src)
    return out


def visual_checks(pages, shots_dir, problems, notes):
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        notes.append("visual checks skipped: Playwright is not installed")
        return []
    shots_dir.mkdir(parents=True, exist_ok=True)
    taken = []
    probe = """() => {
      const out = {};
      out.overflow = document.documentElement.scrollWidth - window.innerWidth;
      out.brokenImages = [...document.images].filter(i => i.complete && i.naturalWidth === 0 && !i.src.startsWith('data:')).map(i => i.src);
      const txt = document.body.innerText;
      out.rawLatex = (txt.match(/\\\\\\(|\\\\\\)|\\\\\\[|\\\\\\]/g) || []).length;
      out.katexErrors = document.querySelectorAll('.katex-error').length;
      const faces = [...document.fonts];
      out.fontErrors = faces.filter(f => f.status === 'error').map(f => f.family);
      out.newsreader = faces.some(f => /Newsreader/.test(f.family) && f.status === 'loaded');
      out.serif = faces.some(f => /Source Serif/.test(f.family) && f.status === 'loaded');
      out.emptySections = [...document.querySelectorAll('main section')].filter(s => s.offsetParent !== null && s.innerText.trim().length < 3).length;
      return out;
    }"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, url in pages:
            for width, height in ((390, 844), (1440, 900)):
                for scheme in ("light", "dark"):
                    tag = f"{name}-{width}-{scheme}"
                    ctx = browser.new_context(viewport={"width": width, "height": height},
                                              color_scheme=scheme, device_scale_factor=1)
                    page = ctx.new_page()
                    errors, failed = [], []
                    page.on("pageerror", lambda e: errors.append(str(e)))
                    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                    page.on("response", lambda r: failed.append(f"{r.status} {r.url}")
                            if r.status >= 400 and r.url.startswith(SITE) else None)
                    try:
                        page.goto(bust(url), wait_until="networkidle", timeout=60000)
                        page.evaluate("document.fonts.ready")
                        page.wait_for_timeout(800)
                        info = page.evaluate(probe)
                    except Exception as e:
                        problems.append(f"{tag}: page did not load in Chromium ({e.__class__.__name__})")
                        ctx.close()
                        continue
                    top = shots_dir / f"{tag}-top.png"
                    page.screenshot(path=str(top))
                    taken.append(str(top))
                    if width == 390 and scheme == "light":
                        full = shots_dir / f"{tag}-full.png"
                        page.screenshot(path=str(full), full_page=True)
                        taken.append(str(full))
                    if errors:
                        problems.append(f"{tag}: JavaScript errors: {'; '.join(errors[:3])}")
                    if failed:
                        problems.append(f"{tag}: requests failed: {'; '.join(failed[:3])}")
                    if info["overflow"] > 1:
                        problems.append(f"{tag}: page scrolls sideways by {info['overflow']} px")
                    if info["brokenImages"]:
                        problems.append(f"{tag}: broken images: {', '.join(info['brokenImages'][:3])}")
                    if info["rawLatex"]:
                        problems.append(f"{tag}: {info['rawLatex']} raw LaTeX delimiters visible")
                    if info["katexErrors"]:
                        problems.append(f"{tag}: {info['katexErrors']} formulas failed to typeset")
                    if info["fontErrors"]:
                        problems.append(f"{tag}: fonts failed to load: {', '.join(sorted(set(info['fontErrors'])))}")
                    if not info["newsreader"] or not info["serif"]:
                        problems.append(f"{tag}: Newsreader or Source Serif 4 not loaded")
                    if info["emptySections"]:
                        problems.append(f"{tag}: {info['emptySections']} empty sections")
                    ctx.close()
        browser.close()
    return taken


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", nargs="?")
    ap.add_argument("edition", nargs="?", choices=["daily", "weekly"])
    ap.add_argument("--wait", type=int, default=900)
    ap.add_argument("--shots", default="/tmp/esscher-check")
    ap.add_argument("--commit", default="HEAD")
    a = ap.parse_args()

    now = dt.datetime.now(ZoneInfo("Europe/Bucharest"))
    day = a.date or now.strftime("%Y-%m-%d")
    edition = a.edition or ("weekly" if dt.date.fromisoformat(day).isoweekday() == 7 else "daily")
    y, m, d = day.split("-")
    stem = f"{day}-{edition}"
    post = ROOT / "_posts" / f"{stem}.md"
    if not post.exists():
        print(f"FAIL: {post.relative_to(ROOT)} is not in the repository")
        sys.exit(2)
    fm = front_matter(post)
    ed_url = f"{SITE}/{y}/{m}/{d}/{edition}/"
    stories = sorted((ROOT / "_stories").glob(f"{stem}-*.md"))
    problems, notes = [], []

    # 1. Wait for GitHub Pages to serve the edition.
    t0, status = time.time(), 0
    while True:
        status, _, body = fetch(ed_url)
        if status == 200:
            break
        if time.time() - t0 > a.wait:
            print(f"FAIL: {ed_url} still answers {status} after {a.wait // 60} minutes")
            sys.exit(2)
        time.sleep(30)
    ed_html = body
    notes.append(f"edition live after {int(time.time() - t0)} s")

    # 2. Front page points at the new edition.
    st, _, front = fetch(SITE + "/")
    path = f"/{y}/{m}/{d}/{edition}/"
    if st != 200:
        problems.append(f"front page answers {st}")
    elif f'href="{path}"' not in front:
        problems.append("front page does not link to the new edition yet")

    # 3. Every story, paper and voice page, its headline and share image.
    pages_html = {"edition": ed_html, "front": front}
    ed_norm = norm(ed_html)
    missing_on_edition = []
    for s in stories:
        sfm = front_matter(s)
        url = f"{SITE}/stories/{s.stem}/"
        st, _, h = fetch(url)
        if st != 200:
            problems.append(f"story page {s.stem} answers {st}")
            continue
        pages_html[s.stem] = h
        title = norm(sfm.get("title", ""))
        if title and title not in norm(h):
            problems.append(f"story page {s.stem} does not show its headline")
        if title and title not in ed_norm:
            missing_on_edition.append(s.stem)
    if missing_on_edition:
        problems.append(f"{len(missing_on_edition)} stories not listed on the edition page: {', '.join(missing_on_edition[:3])}")

    # 4. Images: share images of the new pages, every image on the front and edition pages.
    images = set()
    for key, h in pages_html.items():
        og = og_image(h)
        if og:
            images.add(og)
        elif key != "front":
            problems.append(f"{key}: no share image tag")
        if key in ("front", "edition"):
            images.update(img_srcs(h))
    bad_images = []
    for url in sorted(images):
        st, ctype, _ = fetch(url, binary=True)
        if st != 200 or not ctype.startswith("image/"):
            bad_images.append(f"{url.replace(SITE, '')} ({st})")
    if bad_images:
        problems.append(f"{len(bad_images)} images not served: {', '.join(bad_images[:3])}")
    own_share = [u for u in images if "/assets/og/" in u]
    expected_share = len(stories) + 1
    if (ROOT / "assets" / "og").exists() and len(own_share) < expected_share:
        notes.append(f"{len(own_share)} of {expected_share} pages have their own share image (the rest use the default)")

    # 5. Chart.
    if fm.get("chart"):
        if 'class="chart-day"' not in ed_html or "<svg" not in ed_html:
            problems.append("the chart is in the edition but not on the page")

    # 6. Nothing lost: no deleted files in the publish commit, older pages still served.
    try:
        deleted = subprocess.run(["git", "-C", str(ROOT), "show", "--diff-filter=D", "--name-only",
                                  "--format=", a.commit], capture_output=True, text=True, timeout=60).stdout.split()
    except Exception:
        deleted = []
    if deleted:
        problems.append(f"the publish commit deleted {len(deleted)} files: {', '.join(deleted[:3])}")
    st, _, sitemap = fetch(SITE + "/sitemap.xml")
    if st != 200:
        problems.append(f"sitemap answers {st}")
    else:
        expected = []
        for p_ in (ROOT / "_posts").glob("*.md"):
            yy, mm, dd, rest = p_.stem.split("-", 3)
            expected.append(f"{SITE}/{yy}/{mm}/{dd}/{rest}/")
        expected += [f"{SITE}/stories/{p_.stem}/" for p_ in (ROOT / "_stories").glob("*.md")]
        absent = [u for u in expected if u not in sitemap]
        if absent:
            problems.append(f"{len(absent)} pages missing from the sitemap: {', '.join(u.replace(SITE, '') for u in absent[:3])}")
    older = sorted(p_ for p_ in (ROOT / "_posts").glob("*.md") if p_.stem < stem)
    if older:
        yy, mm, dd, rest = older[-1].stem.split("-", 3)
        st, _, _ = fetch(f"{SITE}/{yy}/{mm}/{dd}/{rest}/")
        if st != 200:
            problems.append(f"the previous edition {older[-1].stem} answers {st}")

    # 7. How it looks.
    visual_pages = [("front", SITE + "/"), ("edition", ed_url)]
    if stories:
        visual_pages.append(("story", f"{SITE}/stories/{stories[0].stem}/"))
    shots = visual_checks(visual_pages, Path(a.shots), problems, notes)

    print(f"Edition: {stem} at {ed_url}")
    print(f"Story pages: {len(stories)}; images checked: {len(images)}; chart: {'yes' if fm.get('chart') else 'no'}")
    for n in notes:
        print(f"Note: {n}")
    if shots:
        print("Screenshots:")
        for s in shots:
            print(f"  {s}")
    if problems:
        print(f"Problems ({len(problems)}):")
        for p_ in problems:
            print(f"  - {p_}")
        print(f"SUMMARY: PROBLEM - {problems[0]}" + (f" (+{len(problems) - 1} more)" if len(problems) > 1 else ""))
        sys.exit(1)
    print(f"SUMMARY: OK - edition live, {len(stories)} story pages, {len(images)} images, nothing missing")


if __name__ == "__main__":
    main()
