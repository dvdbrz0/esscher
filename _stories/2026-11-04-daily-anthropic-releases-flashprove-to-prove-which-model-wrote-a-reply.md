---
{
 "layout": "story",
 "title": "Anthropic releases FlashProve to prove which model wrote a reply",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "The open-source system uses a zero-knowledge succinct argument so that a provider can commit to a model and prove each response came from it without revealing the weights.",
 "body": [
  "Anthropic published FlashProve on 2 November with authors from EPFL, MIT, StarkWare and Succinct. It targets provable inference: a user with little computing power and no sight of the weights checks that a reply came from the promised model, and not from a cheaper one swapped in by a router.",
  "For Llama 4 Maverick, a 400bn-parameter model, a single H100 generates proofs at about 110 tokens a second, with a proof of about 19MB per 1,024-token request. That is 70 to 95 times the GPU time of running the model on vLLM, for 4-bit quantised weights. Anthropic says prior open-source systems are orders of magnitude slower.",
  "The code, Lean proofs and documentation are released under the Apache 2.0 licence. The company says Claude produced the improvements and that the Lean statements exist because such decisions are hard to evaluate. It describes the work as intermediate progress. TechCrunch notes that labs would have to publish a fingerprint of each model."
 ],
 "why": "Independent evaluators and regulators cannot currently confirm which model they are testing.",
 "sources": [
  {
   "name": "Anthropic",
   "url": "https://www.anthropic.com/research/provable-inference"
  },
  {
   "name": "TechCrunch",
   "url": "https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/StarkWareLtd/status/2117637978990268906"
  }
 ],
 "published": "2026-11-02",
 "topics": [
  "AI safety",
  "Mathematics"
 ],
 "image": "/assets/og/2026-11-04-daily-anthropic-releases-flashprove-to-prove-which-model-wrote-a-reply.png"
}
---
