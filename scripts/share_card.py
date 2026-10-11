#!/usr/bin/env python3
"""Draw the 1200x630 image shown when a story or an edition is shared
(WhatsApp, X, LinkedIn, Slack, iMessage): wordmark, section, headline, date.

Used by new_post.py and correct.py. Needs Pillow; without it no image is made
and pages fall back to the site-wide share image.

Fonts in scripts/fonts/ are under the SIL Open Font License (see the OFL files).
"""
from pathlib import Path

FONTS = Path(__file__).resolve().parent / "fonts"
BRAND = Path(__file__).resolve().parent / "brand"
W, H = 1200, 630
MARGIN = 72
BG = (15, 17, 20)
INK = (255, 255, 255)
ACCENT = (240, 122, 63)
MUTED = (163, 166, 173)
RULE = (42, 45, 51)


def _font(name, size):
    from PIL import ImageFont
    return ImageFont.truetype(str(FONTS / name), size)


def _wrap(draw, text, font, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = (line + " " + w).strip()
        if draw.textlength(trial, font=font) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def make_card(out_path, title, kicker="", date_text=""):
    """Write the card as a small palette PNG. Returns True when written."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    # Masthead: the drawn wordmark (made by brand.py, rendered once to a white PNG).
    wordmark = Image.open(BRAND / "wordmark-white.png").convert("RGBA")
    im.paste(wordmark, (MARGIN, 56), wordmark)

    # Headline: the largest size whose lines fit between the section label and the footer.
    width = W - 2 * MARGIN
    top, bottom = 204, 522
    for size in (80, 74, 68, 62, 58, 54, 50, 46):
        f = _font("SourceSerif4Display-Semibold.ttf", size)
        lines = _wrap(d, title, f, width)
        lh = int(size * 1.1)
        if len(lines) <= 4 and lh * len(lines) <= bottom - top:
            break
    else:
        lines = lines[:4]
        while lines and d.textlength(lines[-1] + "…", font=f) > width:
            lines[-1] = lines[-1].rsplit(" ", 1)[0]
        lines[-1] += "…"
    if kicker:
        d.text((MARGIN, 146), kicker, font=_font("SourceSans3-Semibold.ttf", 30), fill=ACCENT)
    y = top
    for ln in lines:
        d.text((MARGIN, y), ln, font=f, fill=INK)
        y += lh

    # Footer: rule, address, date.
    d.line([MARGIN, 548, W - MARGIN, 548], fill=RULE, width=2)
    small = _font("SourceSans3-Regular.ttf", 26)
    d.text((MARGIN, 566), "esscher.com", font=small, fill=MUTED)
    if date_text:
        d.text((W - MARGIN - d.textlength(date_text, font=small), 566), date_text, font=small, fill=MUTED)

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.quantize(colors=48, method=Image.Quantize.MEDIANCUT).save(out_path, optimize=True)
    return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        sys.exit("usage: share_card.py OUT.png TITLE [KICKER] [DATE]")
    make_card(sys.argv[1], sys.argv[2], *(sys.argv[3:5]))
