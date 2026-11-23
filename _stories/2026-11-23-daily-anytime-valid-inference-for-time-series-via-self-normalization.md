---
{
 "layout": "story",
 "title": "Anytime-valid inference for time series via self-normalization",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/23/daily/",
 "date": "2026-11-23 05:00:00 +0300",
 "summary": "Builds asymptotic confidence sequences for parameters of weakly dependent stationary time series, including quantiles and expected shortfall, without estimating the long-run variance.",
 "body": [
  "Confidence sequences give intervals that hold simultaneously at every time, so a sequential analysis can be stopped whenever the data warrant. Under serial dependence they usually require an estimate of the long-run variance, which is hard to obtain for nonlinear parameters.",
  "The paper replaces that estimate with self-normalisation. After a burn-in of length \\(m\\), intervals are released sequentially and their simultaneous coverage over all later times tends to \\(1-\\alpha\\) as \\(m \\to \\infty\\). The theory covers quantiles, expectiles, expected shortfall and autoregressive coefficients.",
  "Two self-normalisers are proposed: a forward construction that uses only the history of estimates and costs almost nothing to update, and a three-block construction that gives narrower sequences and is compatible with the optimal law-of-the-iterated-logarithm width. The authors also apply the method to Markov chain Monte Carlo output."
 ],
 "published": "2026-11-19",
 "authors": "Kutta and Shao",
 "arxiv": "2611.26536",
 "tag": "Probability",
 "topics": [
  "Probability",
  "Quantitative finance"
 ],
 "math": true,
 "image": "/assets/og/2026-11-23-daily-anytime-valid-inference-for-time-series-via-self-normalization.png"
}
---
