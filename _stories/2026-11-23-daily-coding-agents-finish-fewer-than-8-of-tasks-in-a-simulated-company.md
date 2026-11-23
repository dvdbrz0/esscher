---
{
 "layout": "story",
 "title": "Coding agents finish fewer than 8% of tasks in a simulated company",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/23/daily/",
 "date": "2026-11-23 05:00:00 +0300",
 "summary": "SWE-CoWork places agents inside a software organisation with 26 simulated colleagues; the two leading models pass about 63% of the target tests but fully deliver fewer than 8% of 101 assignments.",
 "body": [
  "Coding agents now score near the ceiling of standard benchmarks such as SWE-bench, which hand the model a self-contained issue. SWE-CoWork, a benchmark released on arXiv by a team of 26 authors, tests something closer to real employment: each of its 101 assignments, drawn from 101 real repositories in 11 programming languages, starts from a brief handoff inside a simulated engineering organisation with 26 colleagues who each hold part of the requirements.",
  "Eleven models were evaluated. The two best satisfied roughly 63% of the fail-to-pass tests but completed fewer than 8% of assignments in full. Giving the agents complete requirements up front raised the test pass rate by about 16 percentage points for Seed Evolving and GPT-6 Astra, yet left the share of fully completed assignments unchanged.",
  "The authors trace failures through the whole delivery process. Claude Opus 5.5 sent 93% of its first questions to the right colleague but gathered only 64% of the requirements those colleagues held; deferred questions were not followed up, and 31% of requirements the agents reported as done failed their tests. The study was covered by The Decoder on 22 November."
 ],
 "why": "It separates writing correct code from delivering a finished task, the gap that matters for autonomous software work.",
 "sources": [
  {
   "name": "arXiv: SWE-CoWork",
   "url": "https://arxiv.org/abs/2611.20218"
  },
  {
   "name": "The Decoder",
   "url": "https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/"
  }
 ],
 "published": "2026-11-15",
 "topics": [
  "Agents",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-23-daily-coding-agents-finish-fewer-than-8-of-tasks-in-a-simulated-company.png"
}
---
