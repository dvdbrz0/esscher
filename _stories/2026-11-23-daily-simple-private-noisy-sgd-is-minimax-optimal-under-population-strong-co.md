---
{
 "layout": "story",
 "title": "Simple Private Noisy SGD is Minimax-Optimal under Population Strong Convexity",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/23/daily/",
 "date": "2026-11-23 05:00:00 +0300",
 "summary": "A single pass of differentially private Noisy SGD with a fixed step-size schedule attains the minimax rate for strongly convex generalised linear models, including private logistic regression, without extra logarithmic factors.",
 "body": [
  "Plain stochastic gradient descent is known to be minimax-optimal for many regression problems, such as convex generalised linear models. Whether its simplest differentially private counterpart, Noisy SGD, enjoys the same guarantee on strongly convex losses had been open.",
  "The authors bound the parameter estimation error of one pass of Noisy SGD, with constant batch sizes and a fixed step-size schedule, for smooth, strongly convex Lipschitz losses on a compact convex domain under Rényi differential privacy. For strongly convex generalised linear models the bound matches minimax lower bounds they derive with the score attack framework.",
  "The result gives the first minimax-optimal rate for Noisy SGD in private logistic regression, removing the poly-logarithmic terms in earlier analyses. The proof uses standard convex analysis and holds both in expectation and with high probability."
 ],
 "published": "2026-11-19",
 "authors": "Roth and Avella Medina",
 "arxiv": "2611.26515",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory"
 ],
 "image": "/assets/og/2026-11-23-daily-simple-private-noisy-sgd-is-minimax-optimal-under-population-strong-co.png"
}
---
