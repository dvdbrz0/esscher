---
{
 "layout": "story",
 "title": "Anthropic says Claude independently refuted the Exponential Time Hypothesis",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/29/daily/",
 "date": "2026-10-29 05:00:00 +0300",
 "summary": "Anthropic published a paper credited to Claude giving a deterministic algorithm for 3-SAT in time \\(2^{o(n)}\\), a result that would refute the Exponential Time Hypothesis, hours after OpenAI made the same claim.",
 "body": [
  "Anthropic published a paper, with the author listed as Claude, that describes a deterministic algorithm that solves 3-SAT and its counting version #3-SAT in time \\(2^{o(n)}\\) for \\(n\\) variables. If correct, this refutes the Exponential Time Hypothesis of Impagliazzo, Paturi and Zane and therefore also the Strong Exponential Time Hypothesis. OpenAI had announced a similar result from one of its internal models hours earlier, and Anthropic’s paper cites it.",
  "According to Anthropic researcher Levent Alpoge, an internal Claude research model found the core algorithm on 16 October using 14 million output tokens, without human input. The proof is formalised in Lean 4 in 1,050 modules built on Mathlib, and was checked by Lean’s kernel and by an independent checker, nanoda. The paper states that the Lean development was written and reviewed by AI models and that no person is known to have checked it.",
  "The result is asymptotic. By the paper’s own estimate, the bound beats brute-force search on a typical formula only when the number of variables exceeds about \\(10^{10000}\\), and it says nothing about solving formulas in practice. A literature search reported in the paper found more than 800 papers whose results rely on the hypothesis or a variant."
 ],
 "why": "Two labs claiming the same refutation independently makes human review of the formal statements the decisive next step.",
 "sources": [
  {
   "name": "OfficeChai",
   "url": "https://officechai.com/ai/anthropic-says-claude-too-independently-disproved-exponential-time-hypothesis-on-the-same-day-as-openai/"
  }
 ],
 "published": "2026-10-27",
 "topics": [
  "Mathematics",
  "Reasoning and inference",
  "AI industry"
 ],
 "math": true,
 "summary_plain": "Anthropic published a paper credited to Claude giving a deterministic algorithm for 3-SAT in time 2ᵒ⁽ⁿ⁾, a result that would refute the Exponential Time Hypothesis, hours after OpenAI made the same claim.",
 "image": "/assets/og/2026-10-29-daily-anthropic-says-claude-independently-refuted-the-exponential-time-hypot.png"
}
---
