---
{
 "layout": "story",
 "title": "Generalization Bounds via Vector-Valued Lₚ Correlation Vα",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/23/daily/",
 "date": "2026-10-23 05:00:00 +0300",
 "summary": "A family of dependence measures \\(V_\\alpha\\) that interpolates between total-variation and \\(\\chi^2\\)-type generalisation bounds, and stays finite for heavy-tailed losses when \\(\\alpha > 2\\).",
 "body": [
  "Information-theoretic generalisation bounds measure how much a randomised algorithm’s output depends on its training data, typically through mutual information or total variation, which behave differently in high dimensions. Hamaneh, Mojahedian and Yassaee study a one-parameter family \\(V_\\alpha\\) of vector-valued \\(L_p\\) correlations whose bounds run from total variation at \\(\\alpha = 1\\) to variance and \\(\\chi^2\\) behaviour at \\(\\alpha = 2\\).",
  "For \\(\\alpha > 2\\) the conjugate loss moment falls below two, so the bounds remain finite even when the loss variance is infinite. At \\(\\alpha = 2\\) the bound reads as the spread of the output density across datasets, \\(\\int \\sqrt{\\mathrm{Var}_S[p(w \\mid S)]}\\,dw\\). The whole family is invariant under smooth reparameterisations, and an adaptive density stability condition gives explicit rates for Gibbs posteriors under bounded losses."
 ],
 "published": "2026-10-21",
 "authors": "Hamaneh et al.",
 "arxiv": "2610.29425",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Probability"
 ],
 "math": true,
 "summary_plain": "A family of dependence measures V_α that interpolates between total-variation and χ²-type generalisation bounds, and stays finite for heavy-tailed losses when α > 2.",
 "image": "/assets/og/2026-10-23-daily-generalization-bounds-via-vector-valued-lp-correlation-v.png"
}
---
