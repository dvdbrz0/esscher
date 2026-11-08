---
{
 "layout": "story",
 "title": "Why a Sharpe ratio near 3 can fall to 0.26 on a holdout",
 "kind": "explainer",
 "section": "The maths behind the news",
 "edition": "weekly",
 "edition_url": "/2026/11/08/weekly/",
 "date": "2026-11-08 08:00:00 +0300",
 "summary": "An agentic research loop for trading found a rule with net Sharpe ratios near 3 in discovery and validation that fell to 0.26 on its one holdout test. The mathematics of choosing the best of many noisy estimates explains why the holdout is the number to trust.",
 "body": [
  "Henry Zhang’s paper on a bounded research loop for quantitative finance, posted on 4 November, reports one result in detail. In its 13th run on zero-days-to-expiry options on QQQ, the language model proposed a rule that sold near-the-money put credit spreads on Mondays and Tuesdays. Its net Sharpe ratio was 2.94 over 221 discovery trades and 3.34 over 43 validation trades. On 72 holdout trades, opened once, it was 0.26, and expectancy fell by about 90%. The question is how an honest calculation can produce 3.34 for a rule with little or no edge.",
  "Start with the noise in one estimate. Let returns \\(r_1, \\dots, r_n\\) be independent with mean \\(\\mu\\) and standard deviation \\(\\sigma\\), so the true Sharpe ratio is \\(s = \\mu/\\sigma\\), and let \\(\\hat s = \\bar r / \\hat\\sigma\\) be the sample ratio. Lo (2002) showed that, if the returns are also normally distributed,",
  "\\[ \\sqrt{n}\\,(\\hat s - s) \\xrightarrow{\\;d\\;} \\mathcal{N}\\!\\left(0,\\; 1 + \\tfrac{s^2}{2}\\right). \\] For a rule with little edge the standard error of \\(\\hat s\\) is therefore close to \\(1/\\sqrt{n}\\): about 0.15 per trade for 43 trades and about 0.12 for 72. Converting a per-trade ratio to an annual one multiplies the estimate and its standard error by the same constant, so comparisons measured in standard errors do not depend on that convention.",
  "Now add selection. Suppose a loop evaluates \\(N\\) rules with no edge, and let \\(Z_1, \\dots, Z_N\\) be their estimates divided by the standard error, each standard normal but not necessarily independent. For any \\(\\lambda > 0\\), Jensen’s inequality and a sum of moment generating functions give \\(e^{\\lambda \\mathbb{E}[\\max_i Z_i]} \\le \\mathbb{E}[e^{\\lambda \\max_i Z_i}] \\le \\sum_i \\mathbb{E}[e^{\\lambda Z_i}] = N e^{\\lambda^2/2}\\). Taking logarithms and choosing \\(\\lambda = \\sqrt{2 \\ln N}\\) yields",
  "\\[ \\mathbb{E}\\Big[\\max_{i \\le N} Z_i\\Big] \\le \\sqrt{2 \\ln N}. \\] For independent estimates the bound is sharp to first order as \\(N\\) grows. With \\(N = 100\\) it equals about 3.03, and the exact expected maximum of 100 independent standard normals is about 2.51. The best of a hundred useless rules thus looks, on average, like a rule two and a half standard errors above zero. Every stage that is used to choose, validation included, carries this upward bias, often called the winner’s curse.",
  "The holdout breaks the bias. It is read once, after the rule is fixed, on data that played no part in the choice, so if returns in that window are independent of earlier ones its estimate carries no selection bias for the chosen rule. Two caveats apply. A real fall can also come from a change of regime, which one holdout cannot separate from noise. And Lo’s formula assumes normal returns: for returns with skewness \\(\\gamma_3\\) and kurtosis \\(\\gamma_4\\) the asymptotic variance of \\(\\hat s\\) becomes \\(1 - \\gamma_3 s + \\tfrac{\\gamma_4 - 1}{4} s^2\\), which is larger for a positive Sharpe ratio when returns are negatively skewed, as they typically are for a strategy that collects option premium and occasionally takes a large loss.",
  "The deflated Sharpe ratio of Bailey and López de Prado (2014) combines both corrections: it compares the observed ratio with the expected maximum under \\(N\\) trials, using the non-normal standard error. It needs \\(N\\), which is why Zhang’s loop refuses duplicate proposals and logs every trial in an append-only ledger. The same week, the OLIVIA paper by Dehkordi et al. reported that no pre-registered strategy built on language-model readings of news survived costs and a deflated Sharpe ratio."
 ],
 "sources": [
  {
   "name": "Zhang, Hard to Fool (arXiv)",
   "url": "https://arxiv.org/abs/2611.06607"
  },
  {
   "name": "Lo, The Statistics of Sharpe Ratios (Financial Analysts Journal, 2002)",
   "url": "https://doi.org/10.2469/faj.v58.n4.2453"
  },
  {
   "name": "Bailey and López de Prado, The Deflated Sharpe Ratio (Journal of Portfolio Management, 2014)",
   "url": "https://doi.org/10.3905/jpm.2014.40.5.094"
  },
  {
   "name": "Dehkordi et al., Thinking Fast, Trading Late (arXiv)",
   "url": "https://arxiv.org/abs/2611.03985"
  }
 ],
 "topics": [
  "Quantitative finance",
  "Probability",
  "Mathematics"
 ],
 "math": true,
 "image": "/assets/og/2026-11-08-weekly-why-a-sharpe-ratio-near-3-can-fall-to-0-26-on-a-holdout.png"
}
---
