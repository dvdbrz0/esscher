---
{
 "layout": "story",
 "title": "Why the Riemann hypothesis is a statement about counting primes",
 "kind": "explainer",
 "section": "The maths behind the news",
 "edition": "weekly",
 "edition_url": "/2026/11/22/weekly/",
 "date": "2026-11-22 08:00:00 +0300",
 "summary": "The hypothesis now certified in Lean says that the zeros of \\(\\zeta\\) lie on one line. Through the explicit formula, that is the same as saying the primes up to \\(x\\) are counted by \\(x\\) with an error of about \\(\\sqrt{x}\\), the smallest error possible.",
 "body": [
  "The proof released on 20 November is a Lean library that no one has yet read as mathematics. What it proves is classical and can be stated precisely. For \\(\\mathrm{Re}\\, s > 1\\) the Riemann zeta function is \\(\\zeta(s) = \\sum_{n \\ge 1} n^{-s} = \\prod_p (1 - p^{-s})^{-1}\\), the product running over primes. It extends to a meromorphic function on \\(\\mathbb{C}\\) with a single simple pole at \\(s = 1\\). It vanishes at \\(-2, -4, -6, \\dots\\), and every other zero \\(\\rho = \\beta + i\\gamma\\) lies in the strip \\(0 < \\beta < 1\\). The hypothesis is that every such zero has \\(\\beta = 1/2\\). This is the form checked in Lean, with Mathlib’s own definition of \\(\\zeta\\).",
  "The link to primes runs through a weighted count. Let \\(\\Lambda(n) = \\log p\\) when \\(n = p^k\\) is a prime power and \\(\\Lambda(n) = 0\\) otherwise, and let \\(\\psi(x) = \\sum_{n \\le x} \\Lambda(n)\\). The prime number theorem says \\(\\psi(x) \\sim x\\). Von Mangoldt’s explicit formula of 1895 says how far \\(\\psi\\) is from \\(x\\). For \\(x > 1\\) not a prime power,",
  "\\[ \\psi(x) = x - \\sum_{\\rho} \\frac{x^{\\rho}}{\\rho} - \\log(2\\pi) - \\tfrac{1}{2}\\log\\left(1 - x^{-2}\\right), \\] where \\(\\rho\\) runs over the zeros in the strip and the sum is taken over \\(|\\gamma| < T\\) with \\(T \\to \\infty\\). Each zero adds an oscillating term of size \\(|x^{\\rho}/\\rho| = x^{\\beta}/|\\rho|\\), so the real parts of the zeros set the size of the error in counting primes.",
  "This makes the hypothesis equivalent to a bound on that error. If every zero has \\(\\beta \\le \\Theta\\), the truncated explicit formula gives \\(\\psi(x) = x + O(x^{\\Theta} \\log^2 x)\\). Conversely, if \\(\\psi(x) = x + O(x^{\\theta})\\) for some \\(\\theta < 1\\), then the identity \\(-\\zeta'(s)/\\zeta(s) = s \\int_1^{\\infty} \\psi(x)\\, x^{-s-1}\\, dx\\) shows that \\(-\\zeta'/\\zeta\\) minus its pole term is analytic for \\(\\mathrm{Re}\\, s > \\theta\\), so \\(\\zeta\\) has no zeros there. The Riemann hypothesis is therefore the statement that \\(\\psi(x) = x + O(x^{1/2 + \\varepsilon})\\) for every \\(\\varepsilon > 0\\). The exponent \\(1/2\\) cannot be lowered, because zeros on the line do exist.",
  "Schoenfeld made the bound explicit in 1976. Assuming the hypothesis, \\[ |\\psi(x) - x| < \\frac{1}{8\\pi} \\sqrt{x} \\log^2 x \\quad (x \\ge 73.2), \\qquad |\\pi(x) - \\mathrm{li}(x)| < \\frac{1}{8\\pi} \\sqrt{x} \\log x \\quad (x \\ge 2657), \\] where \\(\\pi(x)\\) counts primes up to \\(x\\) and \\(\\mathrm{li}(x)\\) is the logarithmic integral \\(\\int_0^x dt/\\log t\\), taken as a principal value. At \\(x = 10^{12}\\) the second bound is about \\(1.1 \\times 10^{6}\\), against \\(\\mathrm{li}(x)\\) of order \\(10^{10}\\). Until now such statements were conditional, and many theorems carried the hypothesis as an assumption.",
  "The library also proves the generalised hypothesis for every Dirichlet L-function \\(L(s, \\chi) = \\sum_{n} \\chi(n) n^{-s}\\), where \\(\\chi\\) is a character modulo \\(q\\). Orthogonality of characters writes the count of primes \\(p \\equiv a \\pmod q\\) as an average of the corresponding sums over the \\(\\chi\\), and the same argument gives, for \\(a\\) coprime to \\(q\\), \\(\\pi(x; q, a) = \\mathrm{li}(x)/\\varphi(q) + O(x^{1/2+\\varepsilon})\\). One consequence is computational: in 1976 Gary Miller showed that this hypothesis makes the Miller-Rabin primality test deterministic in polynomial time, by bounding the smallest witness to compositeness.",
  "None of this says how the new proof works. Alpöge’s note describes an argument descended from Stepanov’s proof of the analogue over function fields, with multiplicity replaced by chains of theta lifts, and Terence Tao wrote that early analysis suggests it uses the full strength of the modern Langlands programme. Those are descriptions by the people involved. What the Lean check settles is the statement itself, with every consequence above now unconditional for \\(\\zeta\\) and Dirichlet L-functions."
 ],
 "sources": [
  {
   "name": "Andrew Sutherland, MIT: verification files",
   "url": "https://math.mit.edu/~drew/grh/"
  },
  {
   "name": "Wikipedia: Riemann hypothesis (Schoenfeld’s bounds)",
   "url": "https://en.wikipedia.org/wiki/Riemann_hypothesis"
  },
  {
   "name": "Wikipedia: Chebyshev function (explicit formula)",
   "url": "https://en.wikipedia.org/wiki/Chebyshev_function"
  },
  {
   "name": "Wikipedia: Generalized Riemann hypothesis",
   "url": "https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis"
  },
  {
   "name": "Levent Alpöge: announcement (PDF)",
   "url": "https://alpo.ge/remark.pdf"
  },
  {
   "name": "Terence Tao: What’s new",
   "url": "https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/"
  }
 ],
 "topics": [
  "Mathematics"
 ],
 "math": true,
 "summary_plain": "The hypothesis now certified in Lean says that the zeros of ζ lie on one line. Through the explicit formula, that is the same as saying the primes up to x are counted by x with an error of about √x, the smallest error possible.",
 "image": "/assets/og/2026-11-22-weekly-why-the-riemann-hypothesis-is-a-statement-about-counting-primes.png"
}
---
