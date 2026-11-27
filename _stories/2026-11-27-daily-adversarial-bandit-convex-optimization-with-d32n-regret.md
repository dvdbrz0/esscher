---
{
 "layout": "story",
 "title": "Adversarial Bandit Convex Optimization with d³ᐟ²√n Regret",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/27/daily/",
 "date": "2026-11-27 05:00:00 +0300",
 "summary": "Regret for adversarial bandit convex optimisation drops to \\(\\tilde O(d^{3/2}\\sqrt{n})\\), the rate conjectured in 2017, leaving a gap of \\(d^{1/6}\\) to the lower bound.",
 "body": [
  "In each of \\(n\\) rounds a learner picks a point in a convex body \\(\\mathcal{K} \\subset \\mathbb{R}^d\\) and sees only a noisy value of a convex loss chosen by an adaptive adversary. The best known regret bound was \\(\\tilde O(d^{5/2}\\sqrt{n})\\). Bakhtiari, Jamieson, Lattimore and Ratliff reduce it to \\(\\tilde O(d^{3/2}\\sqrt{n})\\), the rate conjectured by Bubeck and co-authors in 2017.",
  "With a recent lower bound of \\(\\Omega(d^{4/3}\\sqrt{n})\\), the minimax regret is now pinned down up to a factor of \\(d^{1/6}\\) and logarithms. The algorithm is an online Newton step with Gaussian exploration. Unlike earlier methods of this type, it uses unbiased estimates of the gradient and Hessian of the Gaussian smoothing of the loss itself rather than of an optimistic surrogate."
 ],
 "published": "2026-11-24",
 "authors": "Bakhtiari et al.",
 "arxiv": "2611.33531",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Optimization"
 ],
 "math": true,
 "summary_plain": "Regret for adversarial bandit convex optimisation drops to Õ(d^(3/2)√n), the rate conjectured in 2017, leaving a gap of d^(1/6) to the lower bound.",
 "image": "/assets/og/2026-11-27-daily-adversarial-bandit-convex-optimization-with-d32n-regret.png"
}
---
