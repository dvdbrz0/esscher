---
{
 "layout": "story",
 "title": "Google’s Cogentic proves that integers can be factored in time L[1/3] unconditionally",
 "kind": "story",
 "section": "Must-read · Mathematics · AI",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "Google researchers posted six papers produced by an agentic system built on Gemini 4 from a single prompt, led by a factoring algorithm with expected running time \\(L_N[1/3, 105]\\) that relies on no unproven hypotheses. The constant is far too large for the result to threaten deployed cryptography.",
 "body": [
  "On 25 November Google researchers added six papers to a public GitHub directory of work produced by Cogentic, an agentic framework for mathematical discovery that uses Gemini 4 as its base model. According to the papers, there was no human involvement beyond the initial prompt asking for a full proof. The headline result is a zero-error Las Vegas algorithm that completely factors every integer \\(N \\ge 2\\) in worst-case expected time \\(L_N[1/3, 105]\\), where \\(L_x[\\alpha, c] = \\exp\\big(c (\\ln x)^{\\alpha} (\\ln\\ln x)^{1-\\alpha}\\big)\\), with every prime factor certified by the Agrawal–Kayal–Saxena test.",
  "The previous best rigorous bound was \\(L_N[1/2, 1]\\), proved by Lenstra and Pomerance in 1992. The general number field sieve reaches exponent \\(1/3\\) with constant \\((64/9)^{1/3} \\approx 1.92\\), but only under unproven heuristics. The new paper matches the exponent without those assumptions, at the price of a constant of 105. Companion papers claim discrete logarithms in finite fields of fixed characteristic in time \\((p^n)^{o(\\log n)}\\), deterministic factoring in time \\(\\exp(3 (\\ln N)^{3/4})\\) and progress past the square-root barrier for the log-rank conjecture.",
  "Claims on social media that the papers break RSA or elliptic-curve signatures are not supported by the texts: they make the heuristic exponent rigorous rather than faster in practice. None of the results has yet been independently checked."
 ],
 "why": "Rigorous factoring bounds had stood still for more than 30 years, and the result arrives in a week of machine-produced proofs of long-open problems.",
 "links": [
  {
   "label": "Google Research: Cogentic papers",
   "url": "https://github.com/google-research/google-research/tree/master/cogentic_research_papers"
  },
  {
   "label": "The factoring paper (PDF)",
   "url": "https://github.com/google-research/google-research/blob/master/cogentic_research_papers/integer_factorization/paper.pdf"
  },
  {
   "label": "Discussion on X",
   "url": "https://x.com/P3b7_/status/2125717404374475179"
  }
 ],
 "status": "Not yet independently reviewed",
 "math": true,
 "summary_plain": "Google researchers posted six papers produced by an agentic system built on Gemini 4 from a single prompt, led by a factoring algorithm with expected running time L_N[1/3, 105] that relies on no unproven hypotheses. The constant is far too large for the result to threaten deployed cryptography.",
 "image": "/assets/og/2026-11-26-daily-googles-cogentic-proves-that-integers-can-be-factored-in-time-l-1-3-un.png"
}
---
