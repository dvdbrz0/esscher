---
{
 "layout": "story",
 "title": "OpenAI posts a proof that matrix multiplication has exponent 9/4",
 "kind": "story",
 "section": "Must-read · Mathematics · AI",
 "edition": "daily",
 "edition_url": "/2026/11/25/daily/",
 "date": "2026-11-25 05:00:00 +0300",
 "summary": "An unnamed internal OpenAI model produced a manuscript claiming the matching lower bound to its October result, which would fix the exponent at exactly \\(\\omega = 9/4\\) over every field. Part of the proof is checked in Lean, but no human referee has yet reviewed it.",
 "body": [
  "OpenAI added nine manuscripts to its public mathematics repository on 24 November, all produced by an unnamed internal model. The most consequential, titled “The matrix multiplication exponent is nine fourths”, claims that multiplying two \\(n \\times n\\) matrices needs at least \\(\\lceil n^{9/4}/2 \\rceil\\) nonscalar multiplication or division gates for every \\(n \\ge 2\\), even when additions are free. Bilinear algorithms of the kind Strassen introduced in 1969 would need at least \\(\\lceil n^{9/4} \\rceil\\) products. In October the same model had posted an upper bound of \\(9/4\\) over the complex numbers, which human authors, including Amanov, van den Berg and Zuiddam, then extended to every field. Together the two results would give \\(\\omega = 9/4\\) exactly, ruling out the long-held hope that \\(\\omega = 2\\).",
  "The lower bound rests on a companion paper that treats the cost of a tensor as a distance between sites in Euclidean space; the paper also states that the geometric border rank of the matrix multiplication tensor is at least \\(n^{9/4}\\). The same framework underlies a claimed proof of the sunflower conjecture for a fixed number of petals and claimed separations of Valiant’s classes VF, VBP, VP and VNP. Before this release the best concrete rank lower bounds were of order \\(n^2\\).",
  "The caveats are substantial. OpenAI describes the collection as raw research data rather than finished papers, and it withdrew three manuscripts in October after a sign error. The Lean formalisation covers division-free circuits computing formal polynomial identities, a narrower setting than the paper’s main theorem. The result changes no practical computation: hardware multiplies matrices with the schoolbook method or a level or two of Strassen’s trick."
 ],
 "why": "If it survives checking, a question open since 1969 is settled, and every algorithm whose running time is stated in terms of \\(\\omega\\) gets a definite exponent.",
 "links": [
  {
   "label": "OpenAI: the matrix multiplication paper",
   "url": "https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf"
  },
  {
   "label": "OpenAI: the release notes for 24 November",
   "url": "https://github.com/openai/math/blob/main/history.md"
  },
  {
   "label": "OpenAI: scope of the Lean formalisation",
   "url": "https://github.com/openai/math/blob/main/lean/docs/379.md"
  },
  {
   "label": "OfficeChai: what the paper claims",
   "url": "https://officechai.com/ai/openai-says-it-has-pinned-down-the-exact-speed-limit-for-matrix-multiplication-9-4/"
  }
 ],
 "status": "Not yet peer reviewed",
 "math": true,
 "summary_plain": "An unnamed internal OpenAI model produced a manuscript claiming the matching lower bound to its October result, which would fix the exponent at exactly ω = 9/4 over every field. Part of the proof is checked in Lean, but no human referee has yet reviewed it.",
 "image": "/assets/og/2026-11-25-daily-openai-posts-a-proof-that-matrix-multiplication-has-exponent-9-4.png"
}
---
