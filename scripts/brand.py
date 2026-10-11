#!/usr/bin/env python3
"""Draw the Esscher wordmark, the site icon and the small mark as SVG outlines.

The wordmark is "Esscher" set in Newsreader (display optical size, weight 700),
tightened by hand, with the two s joined. It is drawn as outlines, not set as
live text, so it looks the same everywhere and needs no font to display.

Only needed when the brand changes; the outputs are committed:
  _includes/brand/wordmark.svg   header and footer (inline, takes currentColor)
  _includes/brand/mark.svg       a density and its Esscher tilt (end mark)
  assets/favicon.svg             site icon

Needs: pip install fonttools uharfbuzz
Font: scripts/fonts/Newsreader-Variable.ttf (SIL Open Font License, see OFL-newsreader.txt).
"""
import math
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "scripts" / "fonts" / "Newsreader-Variable.ttf"
AXES = {"opsz": 72, "wght": 700}
TRACKING = -0.008       # of the em, between all letters
JOIN_SS = -0.045        # extra, between the two s, so they touch
INK = "#0F1114"


def outline(text, tracking=0.0, pair_adjust=None):
    """Return (svg path data, bounds) for text, y pointing down, baseline at 0."""
    tt = instantiateVariableFont(TTFont(FONT), AXES, inplace=False)
    upm = tt["head"].unitsPerEm
    font = hb.Font(hb.Face(hb.Blob.from_file_path(str(FONT))))
    font.set_variations(AXES)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    glyphs, order = tt.getGlyphSet(), tt.getGlyphOrder()
    pen, bounds = SVGPathPen(glyphs), BoundsPen(glyphs)
    x = 0
    pair_adjust = pair_adjust or {}
    infos, positions = buf.glyph_infos, buf.glyph_positions
    for i, (info, pos) in enumerate(zip(infos, positions)):
        name = order[info.codepoint]
        for p in (pen, bounds):
            glyphs[name].draw(TransformPen(p, (1, 0, 0, -1, x + pos.x_offset, 0)))
        x += pos.x_advance + tracking * upm
        if i + 1 < len(infos):
            x += pair_adjust.get(i, 0) * upm
    return pen.getCommands(), bounds.bounds


def wordmark():
    d, (x0, y0, x1, y1) = outline("Esscher", TRACKING, {1: JOIN_SS})
    pad = 4
    vb = f"{x0 - pad:.0f} {y0 - pad:.0f} {x1 - x0 + 2 * pad:.0f} {y1 - y0 + 2 * pad:.0f}"
    return (f'<svg class="wm" xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" aria-hidden="true" '
            f'focusable="false"><path fill="currentColor" d="{d}"/></svg>')


def favicon():
    """A white E from the wordmark on an ink square."""
    d, (x0, y0, x1, y1) = outline("E")
    w, h = x1 - x0, y1 - y0
    s = 300 / h                       # cap height 300 of 512
    tx = 256 - (x0 + w / 2) * s
    ty = 256 - (y0 + h / 2) * s
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" fill="{INK}"/>'
            f'<path fill="#FFFFFF" transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f})" d="{d}"/></svg>')


def mark():
    """A Gamma(2, 1) density and its Esscher tilt, the Gamma(2, 1/2) density."""
    def dens(rate, n=60):
        return [(7 * i / n, rate * rate * (7 * i / n) * math.exp(-rate * 7 * i / n)) for i in range(n + 1)]
    top = max(y for _, y in dens(1))
    pts = lambda c: " ".join(f"{x / 7 * 120:.1f},{100 - y / top * 92:.1f}" for x, y in c)
    return ('<svg class="mark" xmlns="http://www.w3.org/2000/svg" viewBox="-8 -8 136 116" aria-hidden="true" focusable="false">'
            '<g fill="none" stroke-width="9" stroke-linejoin="round">'
            f'<polyline class="mk-base" stroke="currentColor" points="{pts(dens(1))}"/>'
            f'<polyline class="mk-tilt" points="{pts(dens(0.5))}"/>'
            '<line stroke="currentColor" x1="0" y1="100" x2="120" y2="100"/></g></svg>')


if __name__ == "__main__":
    (ROOT / "_includes" / "brand").mkdir(parents=True, exist_ok=True)
    (ROOT / "_includes" / "brand" / "wordmark.svg").write_text(wordmark())
    (ROOT / "_includes" / "brand" / "mark.svg").write_text(mark())
    (ROOT / "assets" / "favicon.svg").write_text(favicon())
    print("wrote wordmark.svg, mark.svg, favicon.svg")
