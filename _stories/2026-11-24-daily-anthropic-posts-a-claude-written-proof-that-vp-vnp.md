---
{
 "layout": "story",
 "title": "Anthropic posts a Claude-written proof that VP ≠ VNP",
 "kind": "story",
 "section": "Must-read · Mathematics · AI",
 "edition": "daily",
 "edition_url": "/2026/11/24/daily/",
 "date": "2026-11-24 05:00:00 +0300",
 "summary": "A 70-page paper and about 73,000 lines of Lean claim to settle Leslie Valiant’s 1979 question in algebraic complexity. Lean accepts the proofs, but no human mathematician has checked them.",
 "body": [
  "Anthropic added a folder called vp-vnp to its public formal-math repository on 23 November, without a press release. The paper lists ‘Claude, Anthropic’ as its only author, and its README says the result was found by an internal research Claude model. It claims a lower bound of the form \\(m^{c(\\log m)^{1/3}}\\), for some fixed \\(c > 0\\), on the size of any arithmetic circuit computing the \\(m \\times m\\) permanent, over every field of characteristic other than 2, and the same bound over every field for the Hamiltonian cycle polynomial. A bound that grows faster than any polynomial separates VP, the polynomial families computable by circuits of polynomial size, from VNP, which contains the permanent.",
  "The best general lower bound previously known was of order \\(m^2 \\log m\\), going back to Strassen and to Baur and Strassen. The paper says its argument also covers circuits that only approximate the permanent, which yields the separation that geometric complexity theory set as its target, and that it uses neither representation theory nor orbit closures. Lance Fortnow, a complexity theorist, wrote on X that it would be a huge result if correct. The claim says nothing about Boolean circuits or about P and NP.",
  "The Lean code is checked by Lean’s kernel and again by an independently written checker. The README names the gap that remains: a short file defines circuits, the permanent, VP and VNP and states the theorems, and no machine checks that it says what is claimed. The paper adds that only AI readers judged whether the statements mean what is intended."
 ],
 "why": "If it holds, it is the first superpolynomial lower bound for the permanent in general arithmetic circuits, found and formalised by a model.",
 "links": [
  {
   "label": "Anthropic: vp-vnp folder in the formal-math repository",
   "url": "https://github.com/anthropics/formal-math/tree/main/vp-vnp"
  },
  {
   "label": "MACCUS: account of the paper and the Lean code",
   "url": "https://maccus.fr/en/vp-vs-vnp-claude/"
  },
  {
   "label": "Discussion on X: Lance Fortnow",
   "url": "https://x.com/fortnow/status/2125005191577502168"
  }
 ],
 "published": "2026-11-23",
 "status": "Not yet checked by human mathematicians",
 "topics": [
  "Mathematics",
  "Large language models"
 ],
 "math": true,
 "image": "/assets/og/2026-11-24-daily-anthropic-posts-a-claude-written-proof-that-vp-vnp.png"
}
---
