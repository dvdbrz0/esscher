#!/usr/bin/env python3
"""Draw the chart of the day as an inline SVG in the Esscher house style.

The title, subtitle and source line are written in HTML by the page template;
this module draws only the plot. Colours come from classes styled in
assets/css/site.css, so the chart follows the light and dark themes.

Two kinds of chart:
  line: "points" is a list of {"x": "YYYY-MM-DD", "y": number}
  bar:  "points" is a list of {"label": "text", "y": number}
"""
import math
from datetime import date
from html import escape

W = 720          # drawing width in SVG units (scaled to the column width)
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def nice_step(span, target=5):
    raw = span / max(target, 1)
    mag = 10 ** math.floor(math.log10(raw)) if raw > 0 else 1
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def fmt(v, decimals, prefix="", suffix=""):
    s = f"{abs(v):,.{decimals}f}"
    sign = "\u2212" if v < 0 else ""  # a true minus sign, as in print
    return f"{sign}{prefix}{s}{suffix}"


def axis_decimals(step):
    for d in range(4):
        if abs(round(step, d) - step) < 1e-9:
            return d
    return 3


def line_chart(spec):
    pts = [(date.fromisoformat(p["x"]), float(p["y"])) for p in spec["points"] if p.get("y") is not None]
    if len(pts) < 2:
        raise ValueError("a line chart needs at least two points")
    pts.sort()
    prefix, suffix = spec.get("prefix", ""), spec.get("unit", "")
    decimals = int(spec.get("decimals", 2))
    H, left, right, top, bottom = 320, 0, 74, 12, 30
    ys = [y for _, y in pts]
    lo, hi = min(ys), max(ys)
    if spec.get("zero"):
        lo = min(lo, 0)
    pad = (hi - lo) * 0.08 or abs(hi) * 0.05 or 1
    step = nice_step(hi - lo + 2 * pad, 4)
    y0 = math.floor((lo - pad) / step) * step
    y1 = math.ceil((hi + pad) / step) * step
    d0, d1 = pts[0][0].toordinal(), pts[-1][0].toordinal()
    pw, ph = W - left - right, H - top - bottom

    def X(d):
        return left + (d.toordinal() - d0) / max(d1 - d0, 1) * pw

    def Y(v):
        return top + (y1 - v) / (y1 - y0) * ph

    out = []
    ad = axis_decimals(step)
    flag_y = Y(pts[-1][1])
    v = y0
    while v <= y1 + step / 1000:
        y = Y(v)
        cls = "chart-zero" if abs(v) < step / 1000 and y0 < 0 else "chart-grid"
        out.append(f'<line class="{cls}" x1="{left}" x2="{W - right}" y1="{y:.1f}" y2="{y:.1f}"/>')
        if abs(y - flag_y) >= 26:  # the latest-value tag covers labels next to it
            out.append(f'<text class="chart-axis" x="{W}" y="{y + 5:.1f}" text-anchor="end">{escape(fmt(v, ad, prefix, suffix))}</text>')
        v += step
    # Month ticks along the bottom; years when the range is long.
    first, last = pts[0][0], pts[-1][0]
    span_days = d1 - d0
    ticks = []
    if span_days > 730:
        for yr in range(first.year + (1 if first.month > 1 or first.day > 1 else 0), last.year + 1):
            ticks.append((date(yr, 1, 1), str(yr)))
        every = max(1, math.ceil(len(ticks) / 8))
        ticks = ticks[::every]
    else:
        m, yr = first.month, first.year
        if first.day > 1:
            m += 1
        months = []
        while True:
            if m > 12:
                m, yr = 1, yr + 1
            d = date(yr, m, 1)
            if d > last:
                break
            months.append(d)
            m += 1
        every = max(1, math.ceil(len(months) / 8))
        for i, d in enumerate(months[::every]):
            label = MONTHS[d.month - 1]
            if d.month == 1 or i == 0:
                label += f" {d.year}"
            ticks.append((d, label))
    for d, label in ticks:
        x = X(d)
        out.append(f'<line class="chart-tick" x1="{x:.1f}" x2="{x:.1f}" y1="{top + ph}" y2="{top + ph + 5}"/>')
        out.append(f'<text class="chart-axis" x="{x:.1f}" y="{H - 8}" text-anchor="start">{escape(label)}</text>')
    out.append(f'<line class="chart-base" x1="{left}" x2="{W - right}" y1="{top + ph}" y2="{top + ph}"/>')
    path = " ".join(f"{'M' if i == 0 else 'L'}{X(d):.1f},{Y(v):.1f}" for i, (d, v) in enumerate(pts))
    out.append(f'<path class="chart-line" d="{path}"/>')
    ld, lv = pts[-1]
    # Latest value in a filled tag on the axis, as on a terminal chart.
    out.append(f'<circle class="chart-dot" cx="{X(ld):.1f}" cy="{Y(lv):.1f}" r="3.5"/>')
    out.append(f'<rect class="chart-flag" x="{W - right + 4}" y="{Y(lv) - 14:.1f}" width="{right - 4}" height="28"/>')
    out.append(f'<text class="chart-flag-text" x="{W - 4}" y="{Y(lv) + 6:.1f}" text-anchor="end">{escape(fmt(lv, decimals, prefix, suffix))}</text>')
    return H, out


def bar_chart(spec):
    pts = [(str(p["label"]), float(p["y"])) for p in spec["points"] if p.get("y") is not None]
    if not pts:
        raise ValueError("a bar chart needs at least one bar")
    prefix, suffix = spec.get("prefix", ""), spec.get("unit", "")
    decimals = int(spec.get("decimals", 1))
    row, label_w, value_w = 34, 190, 70
    H = row * len(pts) + 12
    lo, hi = min(0, min(v for _, v in pts)), max(0, max(v for _, v in pts))
    pad_left = value_w if lo < 0 else 0
    pad_right = value_w if hi > 0 else 8
    pw = W - label_w - pad_left - pad_right
    start = label_w + pad_left

    def X(v):
        return start + (v - lo) / ((hi - lo) or 1) * pw

    out = []
    zx = X(0)
    for i, (label, v) in enumerate(pts):
        y = 6 + i * row
        x_a, x_b = sorted((zx, X(v)))
        out.append(f'<text class="chart-label" x="0" y="{y + 20}">{escape(label)}</text>')
        out.append(f'<rect class="chart-bar{" neg" if v < 0 else ""}" x="{x_a:.1f}" y="{y + 5}" width="{max(x_b - x_a, 1):.1f}" height="{row - 12}"/>')
        if v < 0:
            out.append(f'<text class="chart-value" x="{x_a - 6:.1f}" y="{y + 20}" text-anchor="end">{escape(fmt(v, decimals, prefix, suffix))}</text>')
        else:
            out.append(f'<text class="chart-value" x="{x_b + 6:.1f}" y="{y + 20}">{escape(fmt(v, decimals, prefix, suffix))}</text>')
    out.append(f'<line class="chart-zero" x1="{zx:.1f}" x2="{zx:.1f}" y1="2" y2="{H - 2}"/>')
    return H, out


def render(spec):
    kind = spec.get("kind", "line")
    H, parts = (bar_chart if kind == "bar" else line_chart)(spec)
    label = spec.get("alt") or spec.get("title", "Chart")
    return (f'<svg class="chart is-{kind}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(label)}" '
            f'preserveAspectRatio="xMinYMin meet">\n' + "\n".join(parts) + "\n</svg>\n")
