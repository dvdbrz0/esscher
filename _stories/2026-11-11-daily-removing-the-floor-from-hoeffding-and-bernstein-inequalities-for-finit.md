---
{
 "layout": "story",
 "title": "Removing the floor from Hoeffding and Bernstein inequalities for finite-population U-statistics",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/11/daily/",
 "date": "2026-11-11 05:00:00 +0300",
 "summary": "For a U-statistic of order \\(k\\) on a sample of size \\(n\\) drawn without replacement, Hoeffding, Bennett and Bernstein bounds hold with effective sample size \\(n/k\\) instead of \\(\\lfloor n/k \\rfloor\\).",
 "body": [
  "Take a uniformly random \\(n\\)-element subset \\(C\\) of a finite population \\(D\\) of size \\(N\\) and form the complete U-statistic \\(U_C\\) of order \\(k\\) from a bounded kernel. Classical concentration bounds for \\(U_C\\) go through Hoeffding’s blocking argument and so only see \\(\\lfloor n/k \\rfloor\\) independent blocks.",
  "The authors prove a product inequality for the uniform distribution on \\(n\\)-subsets and deduce a comparison of moment generating functions:\n\\[ \\log \\mathbb{E}\\, e^{\\theta (U_C - \\mathbb{E} U_C)} \\le \\frac{n}{k} \\log \\mathbb{E}\\, e^{\\frac{k\\theta}{n}(Y - \\mathbb{E} Y)}, \\]\nwhere \\(Y\\) is the kernel evaluated at one uniformly random \\(k\\)-subset. The standard Chernoff route then gives Hoeffding, Bennett and Bernstein inequalities with \\(n/k\\) in the exponent.",
  "The gain is small when \\(n \\gg k\\) but approaches a factor of two in the exponent when \\(k\\) is close to \\(n\\), a regime that matters for sampling-without-replacement estimators in learning theory."
 ],
 "published": "2026-11-07",
 "authors": "Ai et al.",
 "arxiv": "2611.10551",
 "tag": "Probability",
 "topics": [
  "Probability",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "For a U-statistic of order k on a sample of size n drawn without replacement, Hoeffding, Bennett and Bernstein bounds hold with effective sample size n/k instead of ⌊n/k⌋.",
 "image": "/assets/og/2026-11-11-daily-removing-the-floor-from-hoeffding-and-bernstein-inequalities-for-finit.png"
}
---
