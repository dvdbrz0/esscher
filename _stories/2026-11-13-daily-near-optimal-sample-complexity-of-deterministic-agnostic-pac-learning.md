---
{
 "layout": "story",
 "title": "Near-Optimal Sample Complexity of Deterministic Agnostic PAC Learning",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/13/daily/",
 "date": "2026-11-13 05:00:00 +0300",
 "summary": "With deterministic labels, every class of VC dimension \\(d\\) and diameter \\(K\\) is learnable from \\(\\widetilde{O}(K^{1/3} d^{2/3}/\\varepsilon)\\) examples, and the bound is tight up to logarithms.",
 "body": [
  "The paper studies agnostic PAC learning when examples are labelled by an arbitrary deterministic function that need not belong to the concept class \\(C\\). The setting captures misspecification without random label noise and sits between the realisable and fully agnostic cases.",
  "For a class with VC dimension \\(d\\) and finite diameter \\(K\\), earlier work improved the classical agnostic rate \\(O(d/\\varepsilon^2)\\) to \\(\\widetilde{O}(K/\\varepsilon)\\) but left a wide gap to the lower bounds. The authors prove that every such class can be learned with\n\\[ \\widetilde{O}\\left(\\frac{K^{1/3} d^{2/3}}{\\varepsilon}\\right) \\]\nexamples, and construct classes for which this is tight up to logarithmic factors.",
  "The upper bounds come from memorisation-based algorithms that exploit the deterministic labels. In the online version of the problem, the minimax regret is again partly governed by the diameter of the class."
 ],
 "published": "2026-11-09",
 "authors": "Ben-David et al.",
 "arxiv": "2611.13210",
 "tag": "Learning theory",
 "topics": [
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "With deterministic labels, every class of VC dimension d and diameter K is learnable from Õ(K^(1/3)d^(2/3)/ε) examples, and the bound is tight up to logarithms.",
 "image": "/assets/og/2026-11-13-daily-near-optimal-sample-complexity-of-deterministic-agnostic-pac-learning.png"
}
---
