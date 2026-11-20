---
{
 "layout": "story",
 "title": "Taming the Tails of Stochastic Gradient Descent in the Interpolation Regime",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/20/daily/",
 "date": "2026-11-20 05:00:00 +0300",
 "summary": "In the smooth interpolation regime, SGD on convex problems reaches error of order \\(\\log(\\beta^{-1})/n\\) after \\(n\\) steps with probability at least \\(1-\\beta\\), with a matching lower bound in the strongly convex case.",
 "body": [
  "When every sample loss shares a minimiser with the population objective, as in overparameterised models that fit the data exactly, SGD is known to converge fast in expectation. This paper turns those results into high-probability guarantees under the same assumptions.",
  "In the convex case the error after \\(n\\) iterations is of order \\(\\log(\\beta^{-1}) \\cdot n^{-1}\\) with failure probability at most \\(\\beta\\), so the price of high confidence is only logarithmic. In the strongly convex case the authors derive moment-based bounds of order \\(\\beta^{-p} \\exp(-O(p n))\\) for \\(p \\in (0,1]\\) and prove a lower bound showing that this loss in the exponential rate is essentially unavoidable. The analysis covers a broad class of step-size schedules and extends to a low-noise regime and to nonconvex objectives satisfying the Polyak-Lojasiewicz condition."
 ],
 "published": "2026-11-18",
 "authors": "Galli et al.",
 "arxiv": "2611.24562",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "In the smooth interpolation regime, SGD on convex problems reaches error of order log(β⁻¹)/n after n steps with probability at least 1−β, with a matching lower bound in the strongly convex case.",
 "image": "/assets/og/2026-11-20-daily-taming-the-tails-of-stochastic-gradient-descent-in-the-interpolation-r.png"
}
---
