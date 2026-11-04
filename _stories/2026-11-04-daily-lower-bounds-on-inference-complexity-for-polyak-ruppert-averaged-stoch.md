---
{
 "layout": "story",
 "title": "Lower Bounds on Inference Complexity for Polyak-Ruppert Averaged Stochastic Gradient Descent",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "For step sizes with exponent \\(\\gamma\\in(1/2,1)\\), the Gaussian approximation error has order \\(n^{1/2-\\gamma}+n^{\\gamma-1}\\), matching the known upper bound.",
 "body": [
  "The paper asks how fast the distribution of averaged stochastic gradient descent can approach its Gaussian limit. For every fixed \\(\\gamma\\in(1/2,1)\\), one smooth, strongly convex, one-dimensional example attains error of order \\(n^{1/2-\\gamma}+n^{\\gamma-1}\\) in Kolmogorov and convex distances. This matches the existing upper bound across the range, and the nonlinear bias contributes the \\(n^{1/2-\\gamma}\\) term.",
  "With the limiting variance known, reaching error \\(\\varepsilon\\) takes order \\(\\varepsilon^{-4}\\) iterations at the best choice \\(\\gamma=3/4\\). Estimating the variance from one trajectory has relative mean error at least of order \\(n^{-(1-\\gamma)/2}\\) over a scalar quadratic family, so doing both uniformly requires at least order \\(\\varepsilon^{-6}\\) iterations for every fixed \\(\\gamma\\)."
 ],
 "published": "2026-10-31",
 "authors": "Belomestny et al.",
 "arxiv": "2611.01155",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "math": true,
 "summary_plain": "For step sizes with exponent γ ∈ (1/2, 1), the Gaussian approximation error has order n^(1/2−γ)+n^(γ−1), matching the known upper bound.",
 "image": "/assets/og/2026-11-04-daily-lower-bounds-on-inference-complexity-for-polyak-ruppert-averaged-stoch.png"
}
---
