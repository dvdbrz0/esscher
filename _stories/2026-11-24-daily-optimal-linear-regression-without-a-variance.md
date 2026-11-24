---
{
 "layout": "story",
 "title": "Optimal Linear Regression Without a Variance",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/24/daily/",
 "date": "2026-11-24 05:00:00 +0300",
 "summary": "A residual-pruning reduction turns any sub-Gaussian-rate regression method into one that is minimax optimal when the noise has only a finite \\(\\alpha\\)-moment for an unknown \\(\\alpha \\in (1, 2)\\).",
 "body": [
  "Heavy-tailed regression usually assumes at least a finite noise variance. The authors drop it: the noise has only a finite conditional \\(\\alpha\\)-moment \\(\\nu\\) for some unknown \\(\\alpha \\in (1, 2)\\), and covariates may have only a few finite moments.",
  "Their black-box reduction prunes large empirical residuals and needs no knowledge of \\(\\alpha\\), \\(\\nu\\), the covariance or the design moment. With fourth-moment covariates and enough samples, it gives with probability at least \\(1 - \\delta\\) the bound \\[ \\|\\hat\\theta - \\theta^*\\|_\\Sigma \\lesssim_\\alpha \\nu^{1/\\alpha} \\Big( \\frac{d + \\log(1/\\delta)}{n} \\Big)^{(\\alpha - 1)/\\alpha}, \\] and a matching minimax lower bound shows the rate cannot be improved. The reduction is efficient whenever the subroutine is, and an analogous result holds for mean estimation."
 ],
 "published": "2026-11-20",
 "authors": "Tajdini et al.",
 "arxiv": "2611.27983",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Probability"
 ],
 "math": true,
 "summary_plain": "A residual-pruning reduction turns any sub-Gaussian-rate regression method into one that is minimax optimal when the noise has only a finite α-moment for an unknown α ∈ (1, 2).",
 "image": "/assets/og/2026-11-24-daily-optimal-linear-regression-without-a-variance.png"
}
---
