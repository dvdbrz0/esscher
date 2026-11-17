---
{
 "layout": "story",
 "title": "Local Stochastic Volatility Iterations",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/17/daily/",
 "date": "2026-11-17 05:00:00 +0300",
 "summary": "A fixed-point iteration calibrates the leverage function of a local stochastic volatility model, fitting S&P 500 implied volatilities within a few basis points after five iterations.",
 "body": [
  "Local stochastic volatility models need a leverage function chosen so that the model reproduces market implied volatilities. Each iteration of the proposed method simulates the model with the current leverage and estimates the conditional expectation of the variance given the spot with a single regression in time and state, using a quasi-likelihood loss for positive responses.",
  "Recalibrating to S&P 500 options on the day of an interest rate announcement, with a two-factor Bergomi model calibrated four weeks earlier, leverage functions with 63 and 143 coefficients reproduced the fitted surface within a few basis points after five iterations. A few regularised Gauss–Newton steps then put 87% and 95% of liquid quotes inside their bid-ask spreads."
 ],
 "published": "2026-11-13",
 "authors": "Bayer et al.",
 "arxiv": "2611.18214",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance"
 ],
 "image": "/assets/og/2026-11-17-daily-local-stochastic-volatility-iterations.png"
}
---
