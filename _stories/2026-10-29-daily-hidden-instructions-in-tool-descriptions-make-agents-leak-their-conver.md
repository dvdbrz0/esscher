---
{
 "layout": "story",
 "title": "Hidden instructions in tool descriptions make agents leak their conversations",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/29/daily/",
 "date": "2026-10-29 05:00:00 +0300",
 "summary": "A paper shows that instructions hidden in Model Context Protocol tool descriptions can make agents finish a task and then send the conversation to an attacker’s logging tool, succeeding in 62.64–100% of tested cases.",
 "body": [
  "Agents built on large language models reach external tools through the Model Context Protocol (MCP), which describes each tool in natural language. Hu et al. study an attack they call Log-To-Leak, in which a poisoned description tells the agent to make one extra call after its last legitimate one, to a logging tool controlled by the attacker. The payload carries the user’s query, the server’s name and response, and the agent’s answer.",
  "Across 18 pairs of models and MCP servers with valid tool execution, the attack succeeded 62.64–100% of the time and logged the targeted content accurately in 76.55–95.64% of successful cases. In 16 of the pairs, completion of the user’s real task changed by at most 6.63 percentage points, so the leak is hard to notice from the output.",
  "Three defences the authors tested left success rates above 55% on the GitHub server with GPT-4o, and an instruction detector flagged 85.53% of benign descriptions. The authors argue that secondary tool calls should require authorisation by the host application."
 ],
 "why": "Task success is no evidence that an agent behaved, which matters as agents gain access to company data through shared tool servers.",
 "sources": [
  {
   "name": "arXiv",
   "url": "https://arxiv.org/abs/2610.36108"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/rohanpaul_ai/status/2115585031901257874"
  }
 ],
 "published": "2026-10-26",
 "topics": [
  "Agents",
  "AI safety"
 ],
 "image": "/assets/og/2026-10-29-daily-hidden-instructions-in-tool-descriptions-make-agents-leak-their-conver.png"
}
---
