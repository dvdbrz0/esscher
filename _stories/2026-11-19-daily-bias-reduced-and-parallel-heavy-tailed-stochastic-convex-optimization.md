---
{
 "layout": "story",
 "title": "Bias-Reduced and Parallel Heavy-Tailed Stochastic Convex Optimization in ℓp Geometries",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/19/daily/",
 "date": "2026-11-19 05:00:00 +0300",
 "summary": "Parallel algorithms for convex optimisation in \\(\\ell_p\\) geometries under heavy-tailed gradient noise reach error \\(\\epsilon\\) with query depth \\(\\tilde{O}(d^{p/(2p+2)}\\epsilon^{-p/(p+1)})\\), with matching-style lower bounds.",
 "body": [
  "The paper studies stochastic convex optimisation when several gradient queries can be made in parallel per round, the gradient noise has only bounded moments, and the geometry is \\(\\ell_p\\) for \\(2 \\le p < \\infty\\) rather than Euclidean. It combines bias-reduced estimators with multilevel Monte Carlo and a new generalised-Gaussian gradient estimator.",
  "The resulting methods reach error \\(\\epsilon\\) with query depth \\(\\tilde{O}(d^{p/(2p+2)}\\epsilon^{-p/(p+1)})\\), improving on the sequential \\(O(\\epsilon^{-p})\\) for small enough \\(\\epsilon\\). The authors also prove a lower bound of \\(\\Omega(\\min\\{\\epsilon^{-p}, d^{p/(3p-2)}\\})\\) adaptive rounds for nonsmooth problems on the unit \\(\\ell_p\\) ball."
 ],
 "published": "2026-11-16",
 "authors": "Nie et al.",
 "arxiv": "2611.21844",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "math": true,
 "summary_plain": "Parallel algorithms for convex optimisation in ℓₚ geometries under heavy-tailed gradient noise reach error ϵ with query depth Õ(d^(p/(2p+2))ϵ^(−p/(p+1))), with matching-style lower bounds.",
 "image": "/assets/og/2026-11-19-daily-bias-reduced-and-parallel-heavy-tailed-stochastic-convex-optimization.png"
}
---
