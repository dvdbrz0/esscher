#!/usr/bin/env python3
"""Typographer's quotes for edition text: "x" becomes “x”, it's becomes it’s.

Text inside KaTeX delimiters, \\( ... \\) and \\[ ... \\], is left exactly as
written, so primes such as f'(x) keep working. Applied by new_post.py to every
text field of an edition and by correct.py to the --replace texts, so writers
can type plain quotes.
"""
import re

MATH = re.compile(r"(\\\(.*?\\\)|\\\[.*?\\\])", re.S)
OPENERS = set(" \t\n([{—–-/ ")
# Fields that hold addresses, identifiers or dates, never prose.
SKIP_KEYS = {"url", "source_url", "arxiv", "image", "story", "published", "date", "edition", "edition_url",
             "layout", "slug", "id", "series", "ticker_asof", "updated", "permalink", "src"}


def _curl(text):
    out = []
    for i, ch in enumerate(text):
        prev = text[i - 1] if i else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if ch == '"':
            out.append("“" if (not prev or prev in OPENERS or prev in "“‘") else "”")
        elif ch == "'":
            if prev and (prev.isalnum() or prev in ".,!?;:)]}%”’"):
                out.append("’")            # apostrophe or closing quote
            elif nxt.isdigit():
                out.append("’")            # '90s
            else:
                out.append("‘")            # opening single quote
        else:
            out.append(ch)
    return "".join(out)


def smart_quotes(text):
    if not isinstance(text, str) or ('"' not in text and "'" not in text):
        return text
    parts = MATH.split(text)
    return "".join(p if MATH.fullmatch(p) else _curl(p) for p in parts)


def apply(obj, key=None):
    """Curl quotes in every prose string of a JSON-like object."""
    if key in SKIP_KEYS:
        return obj
    if isinstance(obj, dict):
        return {k: apply(v, k) for k, v in obj.items()}
    if isinstance(obj, list):
        return [apply(x, key) for x in obj]
    if isinstance(obj, str):
        return smart_quotes(obj)
    return obj


if __name__ == "__main__":
    tests = {
        "OpenAI's 722 papers": "OpenAI’s 722 papers",
        'He said "no" twice.': "He said “no” twice.",
        "The '90s and 'quoted' words": "The ’90s and ‘quoted’ words",
        "Its derivative \\(f'(x)\\) is 'flat'.": "Its derivative \\(f'(x)\\) is ‘flat’.",
        "\"Hello,\" she said.": "“Hello,” she said.",
        "Investors' bets": "Investors’ bets",
        "(\"quoted\")": "(“quoted”)",
    }
    for src, want in tests.items():
        got = smart_quotes(src)
        assert got == want, (src, got, want)
    print("ok")
