---
{
 "layout": "story",
 "title": "Gradient Descent Achieves 𝒪(ε⁻⁷ᐟ⁴) Convergence",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "A deterministic stepsize rule lets plain gradient descent find an \\(\\varepsilon\\)-stationary point in \\(O(\\varepsilon^{-7/4})\\) gradient evaluations for functions with Lipschitz gradient and Hessian.",
 "body": [
  "With a fixed stepsize, gradient descent on a nonconvex function with \\(L\\)-Lipschitz gradient decreases the objective by order \\(\\varepsilon^2/L\\) per step. The authors propose a deterministic rule that groups \\(O(m)\\) updates whose stepsizes sum to order \\(m^2/L\\), and prove a weighted descent inequality for every prefix of such a sequence on quadratics.",
  "On general objectives with \\(\\rho\\)-Lipschitz Hessian they control the error caused by Hessian variation, which dictates \\(m \\asymp (L^2/(\\rho\\varepsilon))^{1/4}\\). The result is an \\(O(\\varepsilon^{-7/4})\\) bound on gradient evaluations to reach an \\(\\varepsilon\\)-stationary point, which the authors say matches the optimal gradient-complexity guarantee, obtained with no momentum, only the choice of steps."
 ],
 "published": "2026-11-24",
 "authors": "He and Jiang",
 "arxiv": "2611.31917",
 "tag": "Optimization",
 "topics": [
  "Optimization"
 ],
 "math": true,
 "summary_plain": "A deterministic stepsize rule lets plain gradient descent find an ε-stationary point in O(ε^(−7/4)) gradient evaluations for functions with Lipschitz gradient and Hessian.",
 "image": "/assets/og/2026-11-26-daily-gradient-descent-achieves-o-74-convergence.png"
}
---
