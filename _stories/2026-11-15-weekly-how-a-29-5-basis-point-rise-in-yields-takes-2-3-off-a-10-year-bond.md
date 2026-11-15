---
{
 "layout": "story",
 "title": "How a 29.5 basis point rise in yields takes 2.3% off a 10-year bond",
 "kind": "explainer",
 "section": "The maths behind the news",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "The 10-year Treasury yield rose from 4.859% to 5.154% this week. For a bond priced at par at the start, a modified duration of \\(D \\approx 7.85\\) gives a loss of 2.31% to first order, and convexity brings it to 2.28%, the exact repricing.",
 "body": [
  "The 10-year Treasury yield closed at 4.859% on 6 November and at 5.154% on 13 November, a rise of 29.5 basis points after inflation data came in above forecasts. A higher yield means a lower price for bonds already issued. How much lower follows from a short calculation that rests only on discounting.",
  "Take a bond with maturity \\(T\\) years, an annual coupon rate \\(c\\) paid in two halves, and face value 1. Discounting each cash flow at the semi-annually compounded yield \\(y\\) gives its price \\[ P(y) = \\sum_{k=1}^{2T} \\frac{c/2}{(1+y/2)^{k}} + \\frac{1}{(1+y/2)^{2T}}. \\] Every term is a decreasing, convex function of \\(y\\), so the price is too. When \\(c = y\\) the sum equals 1 and the bond trades at par.",
  "The modified duration \\(D = -P'(y)/P(y)\\) is the relative fall in price per unit rise in yield. It equals the Macaulay duration, the present-value-weighted average time of the cash flows, divided by \\(1 + y/2\\). For a bond at par, differentiating the geometric sum gives the closed form \\[ D = \\frac{1}{y}\\left(1 - (1+y/2)^{-2T}\\right). \\] With \\(y = 0.04859\\) and \\(T = 10\\), \\((1+y/2)^{-20} \\approx 0.6187\\), so \\(D \\approx 7.85\\) years, and the Macaulay duration is about 8.04 years.",
  "Expanding the price to second order around the starting yield gives \\[ \\frac{\\Delta P}{P} \\approx -D\\,\\Delta y + \\tfrac{1}{2}\\,C\\,(\\Delta y)^2, \\qquad C = \\frac{P''(y)}{P(y)}, \\] where \\(C\\) is the convexity. With \\(\\Delta y = 0.00295\\) the first term is \\(-7.85 \\times 0.00295 \\approx -2.31\\%\\). The convexity of this bond is about 74.3, so the second term adds \\(\\tfrac{1}{2} \\times 74.3 \\times 0.00295^2 \\approx 0.03\\%\\), for an estimate of \\(-2.28\\%\\). Repricing the bond exactly at 5.154% gives 97.72 per 100 of face value, the same loss to two decimals.",
  "The calculation assumes a bond priced at par at 4.859% with exactly ten years left, and a single yield that moves by the same amount for every cash flow. It ignores the week of accrued coupon, about \\(4.859\\%/52 \\approx 0.09\\%\\), and the slight shortening of maturity, both of which offset a little of the loss. Duration is a local measure: the error of the linear rule is of order \\((\\Delta y)^2\\), and because the price is convex the true loss is smaller than the linear estimate when yields rise and the true gain larger when they fall.",
  "Duration grows with maturity. At the same yield of 4.859%, a 30-year bond at par has \\(D = (1 - 1.024295^{-60})/0.04859 \\approx 15.7\\), so the same move would cost it about 4.6% to first order, twice the loss on the 10-year. For the 10-year itself, the week’s 2.28% fall is close to half a year of its coupon income."
 ],
 "sources": [
  {
   "name": "Yahoo Finance: US 10-year Treasury yield",
   "url": "https://finance.yahoo.com/quote/%5ETNX/"
  },
  {
   "name": "FRED: 10-year Treasury constant maturity rate",
   "url": "https://fred.stlouisfed.org/series/DGS10"
  }
 ],
 "topics": [
  "Markets",
  "Mathematics"
 ],
 "math": true,
 "summary_plain": "The 10-year Treasury yield rose from 4.859% to 5.154% this week. For a bond priced at par at the start, a modified duration of D ≈ 7.85 gives a loss of 2.31% to first order, and convexity brings it to 2.28%, the exact repricing.",
 "image": "/assets/og/2026-11-15-weekly-how-a-29-5-basis-point-rise-in-yields-takes-2-3-off-a-10-year-bond.png"
}
---
