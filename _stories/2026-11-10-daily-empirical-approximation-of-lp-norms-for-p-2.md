---
{
 "layout": "story",
 "title": "Empirical approximation of Lₚ norms for p ∈ (2, ∞)",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/10/daily/",
 "date": "2026-11-10 05:00:00 +0300",
 "summary": "For an \\(N\\)-dimensional subspace with a Nikol’skii-type condition, order \\(N \\log N\\) independent samples approximate every \\(L_p\\) norm in it to within \\(1 \\pm \\varepsilon\\), with exponentially small failure probability.",
 "body": [
  "The question is how many random points are needed so that empirical averages of \\(|f|^p\\) approximate \\(\\|f\\|_{L_p(\\mu)}^p\\) uniformly over a whole subspace \\(X\\) of dimension \\(N\\), for \\(p > 2\\). The authors assume \\(\\|f\\|_\\infty \\le (KN)^{1/p} \\|f\\|_{L_p(\\mu)}\\) for all \\(f \\in X\\).",
  "They show that \\(m \\ge C(p) K N (\\varepsilon^{-p} + \\varepsilon^{-2} \\log_2(2N))\\) independent samples from \\(\\mu\\) give \\[ (1-\\varepsilon)\\|f\\|_{L_p(\\mu)}^p \\le \\frac{1}{m}\\sum_{j=1}^m |f(\\xi^j)|^p \\le (1+\\varepsilon)\\|f\\|_{L_p(\\mu)}^p \\] for every \\(f \\in X\\), with probability at least \\(1 - \\exp(-c(p) m \\varepsilon^2 / (KN))\\). For fixed \\(K\\), \\(p\\) and \\(\\varepsilon\\), the order \\(N \\log N\\) is optimal for independent sampling. The result follows from a more general empirical moment estimate over unit balls of \\(p\\)-convex norms, a uniform concentration statement of the kind used in sampling discretisation and random matrix theory."
 ],
 "published": "2026-11-06",
 "authors": "Dai et al.",
 "arxiv": "2611.08896",
 "tag": "Probability",
 "topics": [
  "Probability",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "For an N-dimensional subspace with a Nikol’skii-type condition, order Nlog N independent samples approximate every Lₚ norm in it to within 1±ε, with exponentially small failure probability.",
 "image": "/assets/og/2026-11-10-daily-empirical-approximation-of-lp-norms-for-p-2.png"
}
---
