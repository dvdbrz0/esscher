---
{
 "layout": "story",
 "title": "Non-asymptotic analysis of SGLD with discontinuous stochastic gradients: a new route to portfolio CVaR minimization",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "For regularised conditional value at risk, stochastic gradient Langevin dynamics converges in Wasserstein-2 distance at rate \\(\\mathcal{O}(\\lambda^{1/4})\\) in the step size, with excess risk linear in the number of assets.",
 "body": [
  "Conditional value at risk has a positive-part loss, and with a softmax portfolio parametrisation the stochastic gradients can be discontinuous. Existing guarantees for non-convex Langevin methods then often depend exponentially on dimension.",
  "The authors use the geometry of the objective to establish linear growth, convexity at infinity and one-sided Lipschitz conditions, without density assumptions on asset losses and with constants independent of the number of assets. They prove a Wasserstein-2 bound with rate \\(\\mathcal{O}(\\lambda^{1/4})\\) for step size \\(\\lambda\\), a finite-time excess risk guarantee, and an excess risk bound linear in the number of assets. Experiments on simulated Gaussian portfolios show the predicted dependence on dimension."
 ],
 "published": "2026-10-31",
 "authors": "Ding et al.",
 "arxiv": "2611.00578",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance",
  "Optimization"
 ],
 "math": true,
 "summary_plain": "For regularised conditional value at risk, stochastic gradient Langevin dynamics converges in Wasserstein-2 distance at rate O(λ^(1/4)) in the step size, with excess risk linear in the number of assets.",
 "image": "/assets/og/2026-11-04-daily-non-asymptotic-analysis-of-sgld-with-discontinuous-stochastic-gradient.png"
}
---
