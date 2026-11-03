---
{
 "layout": "story",
 "title": "Variance-adaptive Chernoff bounds: nonasymptotically valid, asymptotically sharp confidence sets for unbounded means",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/03/daily/",
 "date": "2026-11-03 05:00:00 +0300",
 "summary": "Closed-form, nonasymptotically valid intervals for sub-Gaussian means under martingale dependence match the Gaussian width \\(\\sigma z_{1-\\alpha/2}/\\sqrt{n}\\) to first order, adapting to the true standard deviation.",
 "body": [
  "Given \\(n\\) observations with conditional mean \\(\\mu\\) and a known sub-Gaussian proxy \\(s\\), the usual Chernoff interval has half-width \\(s\\sqrt{2\\log(2/\\alpha)/n}\\). It ignores the actual standard deviation \\(\\sigma \\le s\\) and misses the Gaussian quantile.",
  "Ramdas and Martinez-Taboada build two supermartingales, one with an empirical quadratic variance and a cubic correction, the other a continuation supermartingale. The first gives an empirical-Bernstein bound for unbounded data and the second an empirical Berry-Esseen bound. Their interval agrees almost surely to first order with \\(\\bar X_n \\pm \\sigma z_{1-\\alpha/2}/\\sqrt{n}\\) at every iid law with \\(\\sigma > 0\\).",
  "The same constructions give a time-uniform confidence sequence with half-width \\(\\sigma\\sqrt{2\\log\\log n/n}\\), multivariate ellipsoids and heavy-tailed extensions. The authors conclude that any more than two moments suffice for fully data-dependent, asymptotically efficient, nonasymptotic confidence sets."
 ],
 "published": "2026-10-30",
 "authors": "Ramdas and Martinez-Taboada",
 "arxiv": "2610.42058",
 "tag": "Probability",
 "topics": [
  "Probability"
 ],
 "math": true,
 "summary_plain": "Closed-form, nonasymptotically valid intervals for sub-Gaussian means under martingale dependence match the Gaussian width σz_(1−α/2)/√n to first order, adapting to the true standard deviation.",
 "image": "/assets/og/2026-11-03-daily-variance-adaptive-chernoff-bounds-nonasymptotically-valid-asymptotical.png"
}
---
