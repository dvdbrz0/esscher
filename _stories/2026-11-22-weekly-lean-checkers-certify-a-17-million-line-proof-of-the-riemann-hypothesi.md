---
{
 "layout": "story",
 "title": "Lean checkers certify a 17-million-line proof of the Riemann hypothesis",
 "kind": "story",
 "section": "What mattered",
 "edition": "weekly",
 "edition_url": "/2026/11/22/weekly/",
 "date": "2026-11-22 08:00:00 +0300",
 "summary": "Levent Alpöge, a mathematician at Anthropic, released on 20 November a Lean library that he said he built with Claude and that proves the Riemann hypothesis. A day later the Lean and Mathlib communities certified that the library proves exactly Mathlib’s statement of the hypothesis, together with the generalised version for Dirichlet L-functions. Nobody, including the author, yet understands the argument.",
 "body": [
  "Alpöge’s note says he guided the work to the right setting and that Claude then outpaced him near the end. He released only the Lean code, 14 archive parts depending on nothing but Mathlib, and said a written-out version would be an unreadable document that he will replace with a proper write-up once he understands and simplifies the argument.",
  "The verification followed four public criteria. The statement checked is the definition already in Mathlib: every zero of \\(\\zeta\\) other than \\(-2, -4, -6, \\dots\\) has real part \\(1/2\\). Two independent tools confirmed that the library’s theorem is that statement, dozens of people reproduced the build, and the exported proof was accepted by Lean’s kernel and by independent checkers, two of which, con-leche and con-ron, carry a formal proof relative to set theory that they cannot accept a false proof.",
  "Andrew Sutherland of MIT keeps the most detailed record. As of 04:35 UTC on 22 November all 175,187 modules compiled with no errors, the main theorems used only Lean’s three standard axioms, and a sandboxed rebuild reproduced the 61.6 GB export byte for byte; two kernel runs were still in progress. The checked scope covers \\(\\zeta\\) and Dirichlet L-functions, not Dedekind zeta functions or general automorphic L-functions."
 ],
 "why": "The most famous open problem in mathematics now has a proof that machines accept and humans have yet to read.",
 "sources": [
  {
   "name": "Lean community blog: joint statement",
   "url": "https://leanprover-community.github.io/blog/posts/riemann-hypothesis/"
  },
  {
   "name": "Andrew Sutherland, MIT: verification files",
   "url": "https://math.mit.edu/~drew/grh/"
  },
  {
   "name": "Levent Alpöge: announcement (PDF)",
   "url": "https://alpo.ge/remark.pdf"
  },
  {
   "name": "Terence Tao: What’s new",
   "url": "https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/"
  }
 ],
 "published": "2026-11-21",
 "topics": [
  "Mathematics",
  "Large language models"
 ],
 "math": true,
 "image": "/assets/og/2026-11-22-weekly-lean-checkers-certify-a-17-million-line-proof-of-the-riemann-hypothesi.png"
}
---
