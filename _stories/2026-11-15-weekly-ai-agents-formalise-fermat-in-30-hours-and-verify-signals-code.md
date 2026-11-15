---
{
 "layout": "story",
 "title": "AI agents formalise Fermat in 30 hours and verify Signal’s code",
 "kind": "story",
 "section": "What mattered",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "Anthropic said 1,000 agents running Claude Fable 5.2 completed a Lean formalisation of Fermat’s Last Theorem in 30 hours, against 11 days for its first attempt. Google DeepMind’s AlphaProof Code verified security properties of the Signal protocol’s implementation in four weeks.",
 "body": [
  "Anthropic released Claude Fable 5.2 and Claude Mythos 5.2, one underlying model with different safeguards, on 9 November at $8 per million input tokens and $40 per million output tokens. In its Fermat run the new model needed a third as many action tokens as the first formalisation, which had relied on a purpose-built harness and human guidance, and produced a proof seven times shorter. With the same 1,000-agent setup, Opus 5.5 completed 26% of the work in 18 hours. The company reports a single run per model.",
  "The first formalisation, published in September, was already checked by Lean against its three standard axioms, with the statement matched to the one in Mathlib. The new result is therefore about cost and autonomy rather than about a new proof.",
  "DeepMind’s work, reported by Wired on 10 November, takes the same approach to software. Agents produced proofs that key cryptographic guarantees of the Signal protocol hold, with people reviewing the work at key stages. On older versions with known, long-fixed flaws, the system correctly failed to prove them secure. The analysis covered the protocol rather than the whole Signal app, and Google did not disclose its cost."
 ],
 "why": "Machine-checked proof is turning from a research exercise into something labs can run at scale, on mathematics and on code.",
 "sources": [
  {
   "name": "Anthropic: Claude Fable 5.2 and Mythos 5.2",
   "url": "https://www.anthropic.com/claude-fable-and-mythos-5-2"
  },
  {
   "name": "Anthropic: formalising Fermat’s Last Theorem",
   "url": "https://www.anthropic.com/research/formalizing-fermats-last-theorem"
  },
  {
   "name": "Wired: AlphaProof Code and Signal",
   "url": "https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/"
  }
 ],
 "published": "2026-11-09",
 "topics": [
  "Agents",
  "Mathematics",
  "AI industry"
 ],
 "image": "/assets/og/2026-11-15-weekly-ai-agents-formalise-fermat-in-30-hours-and-verify-signals-code.png"
}
---
