---
{
 "layout": "story",
 "title": "Settling the Burn-in Gap: Sharp Risk Bounds for Tail-Averaged SGD in Linear Regression",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/12/daily/",
 "date": "2026-11-12 05:00:00 +0300",
 "summary": "Matching upper and lower bounds on the excess risk of constant-step tail-averaged SGD in high-dimensional linear regression, explicit in the covariance spectrum \\(\\mathbf{H}\\) and the initial error.",
 "body": [
  "Instance-dependent bounds for tail-averaged stochastic gradient descent, in the spectral framework of Zou et al. (2021), left a gap: the upper bound kept an undamped contribution from the initial error in the leading eigendirections, while the lower bound dropped that contribution entirely. The paper shows both were loose. The direct variance from the head initialisation is damped exponentially during burn-in, but fourth-moment energy scattered early into slow spectral modes survives into the averaging window.",
  "Under a spectral feedback condition the authors obtain matching upper and lower bounds, and prove the condition holds in two regimes: any spectrum with a horizon-dependent step size fixed in advance, and polynomially decaying spectra \\(\\lambda_i \\asymp i^{-a}\\) with \\(a > 1\\) under a single horizon-free step size. Low-dimensional constructions show an exponential-versus-polynomial gap in the earlier lower bound, and that fourth-moment assumptions alone cannot fix the asymptotic decay rate."
 ],
 "published": "2026-11-10",
 "authors": "Zhao et al.",
 "arxiv": "2611.13383",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "Matching upper and lower bounds on the excess risk of constant-step tail-averaged SGD in high-dimensional linear regression, explicit in the covariance spectrum H and the initial error.",
 "image": "/assets/og/2026-11-12-daily-settling-the-burn-in-gap-sharp-risk-bounds-for-tail-averaged-sgd-in-li.png"
}
---
