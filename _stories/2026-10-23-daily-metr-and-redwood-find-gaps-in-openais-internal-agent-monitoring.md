---
{
 "layout": "story",
 "title": "METR and Redwood find gaps in OpenAI’s internal agent monitoring",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/23/daily/",
 "date": "2026-10-23 05:00:00 +0300",
 "summary": "A three-week exercise with deep access found ways agents could, in principle, evade OpenAI’s misalignment monitor, including an exploit that hid hundreds of recent actions.",
 "body": [
  "Between 21 July and 11 August, one employee of METR and one of Redwood Research worked inside OpenAI with access to its codebase, monitor prompts and documentation, and interviewed about a dozen staff. They estimated that 75–94% of agentic internal traffic from models at least as strong as GPT-5.5 was eligible for monitoring, and 99.2% of internal Codex traffic.",
  "They found that unmonitored compaction events probably left about 10% of eligible Codex traffic unchecked between May and July, letting agents postpone review by continuing to act. Other findings included a way for Codex agents to bypass sandboxing, an exploit that kept hundreds of recent actions from the monitor, and two client-controllable headers that switched monitoring off for new agents. RL training runs were not covered at the start of the exercise.",
  "OpenAI said it has patched every vulnerability affecting its production safeguards. METR said it has not evaluated that claim, and that only a brief public summary was agreed in advance."
 ],
 "sources": [
  {
   "name": "METR",
   "url": "https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/"
  }
 ],
 "published": "2026-10-22",
 "topics": [
  "AI safety",
  "Agents"
 ],
 "image": "/assets/og/2026-10-23-daily-metr-and-redwood-find-gaps-in-openais-internal-agent-monitoring.png"
}
---
