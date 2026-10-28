---
{
 "layout": "story",
 "title": "Low-degree polynomials lower bounds for clustering in small dimension",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/28/daily/",
 "date": "2026-10-28 05:00:00 +0300",
 "summary": "Low-degree polynomials need about \\(K^2 d^{3/2}\\) observations to cluster a mixture of \\(K\\) groups in \\(\\mathbb{R}^d\\) at polylogarithmic separation when \\(K\\) is much larger than \\(d\\).",
 "body": [
  "The paper studies clustering \\(n\\) observations from a mixture of \\(K\\) isotropic distributions in \\(\\mathbb{R}^d\\) when \\(K\\) is much larger than \\(d\\). Tensor methods recover the partition at polylogarithmic separation but need a large, non-explicit polynomial number of samples in \\(dK\\), while earlier low-degree lower bounds only required \\(n\\) to exceed \\(dK^2\\).",
  "The authors build a mixture of \\(2K\\) product Bernoulli distributions on \\(\\{0,1\\}^d\\), with \\(K = (d+1)^m\\) and centres taken from a dual BCH code, so that the moment tensors match those of the uniform distribution on \\(\\{-1,1\\}^d\\) up to order \\(2m+1\\). For fixed \\(m\\) they show that low-degree polynomials fail when \\(\\Delta^2 \\ll (K^2 d^{3/2}/n)^{1/(2m+2)} \\wedge \\sqrt{d}\\), up to polylogarithmic factors, so polylogarithmic separation needs \\(n \\gtrsim K^2 d^{3/2}\\). A Gaussianisation argument carries the hardness to Gaussian mixtures. The proof counts solutions of polynomial systems over the finite field \\(\\mathbb{F}_{d+1}\\)."
 ],
 "published": "2026-10-27",
 "authors": "Carpentier and Verzelen",
 "arxiv": "2610.37272",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Probability"
 ],
 "math": true,
 "summary_plain": "Low-degree polynomials need about K²d^(3/2) observations to cluster a mixture of K groups in ℝᵈ at polylogarithmic separation when K is much larger than d.",
 "image": "/assets/og/2026-10-28-daily-low-degree-polynomials-lower-bounds-for-clustering-in-small-dimension.png"
}
---
