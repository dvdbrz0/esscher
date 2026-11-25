---
{
 "layout": "story",
 "title": "Silver rate is sharp for gradient descent",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/25/daily/",
 "date": "2026-11-25 05:00:00 +0300",
 "summary": "For any predetermined stepsize schedule, gradient descent on smooth convex functions cannot beat the rate \\(n^{-p}\\) with \\(p = \\log_2(1+\\sqrt{2}) \\approx 1.2716\\), up to an absolute constant.",
 "body": [
  "Recent work showed that gradient descent with carefully chosen long stepsizes, the silver schedules, reaches an accuracy of order \\(n^{-p}\\) after \\(n\\) steps on \\(L\\)-smooth convex functions, with \\(p = \\log_2(1+\\sqrt{2}) \\approx 1.2716\\), beating the classical \\(1/n\\). Earlier lower bounds matched this exponent only up to subpolynomial losses.",
  "The paper removes those losses. For every \\(L > 0\\), every \\(n\\) and every real stepsize schedule \\(h \\in \\mathbb{R}^n\\), it constructs a convex \\(L\\)-smooth function with \\((f(x_n) - f(x_\\star))/(L\\|x_0 - x_\\star\\|^2) \\ge c\\,n^{-p}\\) for an absolute constant \\(c > 0\\). The minimax rate of fixed-schedule gradient descent is therefore settled up to a constant factor."
 ],
 "published": "2026-11-23",
 "authors": "Jeong and Hong",
 "arxiv": "2611.30100",
 "tag": "Optimization",
 "topics": [
  "Optimization"
 ],
 "math": true,
 "summary_plain": "For any predetermined stepsize schedule, gradient descent on smooth convex functions cannot beat the rate n⁻ᵖ with p = log ₂(1+√2) ≈ 1.2716, up to an absolute constant.",
 "image": "/assets/og/2026-11-25-daily-silver-rate-is-sharp-for-gradient-descent.png"
}
---
