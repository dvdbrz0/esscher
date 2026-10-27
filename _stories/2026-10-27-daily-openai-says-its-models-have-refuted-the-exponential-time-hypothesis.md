---
{
 "layout": "story",
 "title": "OpenAI says its models have refuted the Exponential Time Hypothesis",
 "kind": "story",
 "section": "Must-read · Mathematics · AI",
 "edition": "daily",
 "edition_url": "/2026/10/27/daily/",
 "date": "2026-10-27 05:00:00 +0300",
 "summary": "A machine-written paper gives a deterministic algorithm that counts the satisfying assignments of any k-CNF formula in subexponential time and polynomial space. A Lean formalisation of a slightly weaker bound is public, and the original proposers of the hypothesis will lead the review.",
 "body": [
  "The Exponential Time Hypothesis, proposed by Russell Impagliazzo, Ramamohan Paturi and Francis Zane, says that deciding 3-SAT on \\(n\\) variables needs time \\(2^{\\Omega(n)}\\) in the worst case. It has been the assumption behind hundreds of conditional hardness results in graph algorithms, computational biology, databases and geometry. On 26 October OpenAI published a paper, dated 17 October and revised on 25 October, that claims to refute it.",
  "The main theorem gives, for each fixed \\(k \\ge 2\\), a deterministic algorithm that computes the number of satisfying assignments of a \\(k\\)-CNF with \\(n\\) variables and \\(m\\) clauses in \\((n+m)^{O_k(1)}\\, 2^{O_k(n \\log\\log n/\\sqrt{\\log n})}\\) bit operations and polynomial space. For sparse formulas with \\(m \\le Dn\\) the exponent improves to \\(O(n/\\sqrt{\\log n})\\). The method reduces counting for \\(k\\)-SAT to counting common zeros of sparse polynomial equations, built from low-degree replacement forms and shared linear summaries. A corollary uses Hoeffding’s inequality and a union bound over all \\(2^n\\) assignments to give subexponential approximation schemes for Max-\\(k\\)-SAT.",
  "OpenAI says the model wrote the disproof on 16 October and that it was formalised in Lean the next day. The public formalisation proves the weaker bound \\(2^{O_k(n(\\log\\log n)^2/\\sqrt{\\log n})}\\). Impagliazzo and Paturi of UC San Diego and Ryan Williams of MIT will lead a group to verify and explain the result, and asked that all raw data be made public. The paper notes that bounds of the form \\(2^{o(n)}\\) do not carry over to every NP problem under general polynomial-time reductions."
 ],
 "why": "If it stands, a large body of conditional lower bounds in algorithms loses its foundation, and the claim arrives with a machine-checked proof.",
 "links": [
  {
   "label": "OpenAI: the announcement",
   "url": "https://openai.com/index/building-scientific-understanding-with-academic-communities/"
  },
  {
   "label": "The paper (PDF)",
   "url": "https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf"
  },
  {
   "label": "Scope of the Lean formalisation",
   "url": "https://github.com/openai/math/blob/main/lean/docs/378.md"
  }
 ],
 "published": "2026-10-26",
 "status": "Not yet independently reviewed",
 "topics": [
  "Mathematics",
  "Reasoning and inference",
  "AI industry"
 ],
 "math": true,
 "image": "/assets/og/2026-10-27-daily-openai-says-its-models-have-refuted-the-exponential-time-hypothesis.png"
}
---
