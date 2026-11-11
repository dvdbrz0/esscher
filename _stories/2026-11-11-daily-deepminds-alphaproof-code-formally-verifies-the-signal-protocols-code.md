---
{
 "layout": "story",
 "title": "DeepMind’s AlphaProof Code formally verifies the Signal protocol’s code",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/11/daily/",
 "date": "2026-11-11 05:00:00 +0300",
 "summary": "Google DeepMind said a team of AI agents proved key security properties of the compiled code behind the Signal protocol in four weeks, with human experts writing and reviewing the specifications.",
 "body": [
  "AlphaProof Code splits formal verification in two. Human experts work with language models to turn Signal’s security goals into formal specifications, each one reviewed by a person. Agents running on Gemini Carbon then write the proofs, which came to more than six million lines of Lean, and flag the parts that need a human look, about 1% of the code according to DeepMind.",
  "The proofs cover the implementation rather than only the design, including protection of messages before and after a device is temporarily compromised. DeepMind said it is the first time the implementation of a widely deployed protocol of this kind has been formally verified by any method. As a check, the team reintroduced two real, long-fixed bugs into an isolated copy of the code, and in both cases the system produced a machine-checked proof that the buggy version was insecure.",
  "The work did not cover the whole Signal app, and Google did not disclose its cost, Wired reported. The specification and proofs are being released."
 ],
 "why": "Machine-checked proofs about production code, at this scale, move formal verification from a research exercise towards a practical security tool.",
 "sources": [
  {
   "name": "Google DeepMind",
   "url": "https://deepmind.google/blog/introducing-alphaproof-code/"
  },
  {
   "name": "Wired",
   "url": "https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/"
  }
 ],
 "published": "2026-11-10",
 "topics": [
  "Agents",
  "Mathematics",
  "AI safety"
 ],
 "image": "/assets/og/2026-11-11-daily-deepminds-alphaproof-code-formally-verifies-the-signal-protocols-code.png"
}
---
