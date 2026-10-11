#!/usr/bin/env python3
"""Download a data series from FRED (Federal Reserve Bank of St. Louis) as chart points.

Usage:
    python3 scripts/fred.py SERIES_ID START_DATE [END_DATE]
    python3 scripts/fred.py DGS10 2026-07-01

Prints a JSON list of {"x": "YYYY-MM-DD", "y": number}, ready for the "points"
field of a line chart, then the last value and its date on stderr. Missing days
(holidays) are skipped. Useful series:
  DGS10 10-year Treasury yield (%)      DGS2 2-year Treasury yield (%)
  T10Y2Y 10-year minus 2-year (points)  BAMLH0A0HYM2 US high-yield spread (%)
  BAMLC0A0CM US investment-grade spread (%)  VIXCLS VIX volatility index
  SP500 S&P 500 index                   DCOILBRENTEU Brent crude ($ per barrel)
  DEXUSEU dollars per euro              DFF effective federal funds rate (%)
  CPIAUCSL consumer prices (index)      UNRATE unemployment rate (%)
Series page for the source link: https://fred.stlouisfed.org/series/SERIES_ID
"""
import csv
import io
import json
import sys
import urllib.request


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sid, start = sys.argv[1], sys.argv[2]
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={start}"
    if len(sys.argv) > 3:
        url += f"&coed={sys.argv[3]}"
    with urllib.request.urlopen(url, timeout=30) as r:
        text = r.read().decode("utf-8")
    rows = list(csv.reader(io.StringIO(text)))
    pts = []
    for row in rows[1:]:
        if len(row) < 2 or row[1] in ("", "."):
            continue
        pts.append({"x": row[0], "y": float(row[1])})
    if not pts:
        sys.exit(f"fred.py: no data for {sid} from {start}")
    print(json.dumps(pts))
    sys.stderr.write(f"fred.py: {len(pts)} points, last {pts[-1]['y']} on {pts[-1]['x']}\n")


if __name__ == "__main__":
    main()
