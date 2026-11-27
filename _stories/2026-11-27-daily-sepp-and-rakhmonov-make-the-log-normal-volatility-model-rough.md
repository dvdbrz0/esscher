---
{
 "layout": "story",
 "title": "Sepp and Rakhmonov make the log-normal volatility model rough",
 "kind": "story",
 "section": "Markets",
 "edition": "daily",
 "edition_url": "/2026/11/27/daily/",
 "date": "2026-11-27 05:00:00 +0300",
 "summary": "Adding memory to the Karasinski–Sepp log-normal volatility model keeps a unique solution, bounded variance and, when \\(\\kappa_2 \\ge \\beta\\), the martingale property, but loses fast option pricing.",
 "body": [
  "In a new paper with Parviz Rakhmonov, Artur Sepp adds memory, governed by a Hurst exponent \\(H < 1/2\\), to the log-normal stochastic volatility model in which shocks are proportional to the level of volatility and mean reversion strengthens quadratically as volatility rises. The authors prove that the rough model has a unique solution, that volatility cannot become negative, and that any positive quadratic mean reversion keeps the variance bounded for every degree of roughness.",
  "The price remains a martingale when the quadratic mean-reversion coefficient \\(\\kappa_2\\) is at least the volatility beta \\(\\beta\\), even when rallies lift volatility, as in bitcoin and ether options. Fast transform pricing does not carry over, so options are priced by Monte Carlo. Fitted to the same bitcoin option quotes, the rough version gives a daily standard deviation of log-volatility changes of 36% against 21% for the classical one, while over 30 days the figures are 84% and 85%. Sepp notes that the fitted parameters also differ, so the comparison does not isolate the effect of memory."
 ],
 "sources": [
  {
   "name": "Artur Sepp",
   "url": "https://artursepp.com/2026/11/26/what-survives-when-a-log-normal-volatility-model-is-made-rough/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/ArturSepp/status/2126139068165816384"
  }
 ],
 "published": "2026-11-26",
 "topics": [
  "Quantitative finance",
  "Probability"
 ],
 "math": true,
 "summary_plain": "Adding memory to the Karasinski–Sepp log-normal volatility model keeps a unique solution, bounded variance and, when κ₂ ≥ β, the martingale property, but loses fast option pricing.",
 "image": "/assets/og/2026-11-27-daily-sepp-and-rakhmonov-make-the-log-normal-volatility-model-rough.png"
}
---
