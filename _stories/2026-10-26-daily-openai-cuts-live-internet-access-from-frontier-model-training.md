---
{
 "layout": "story",
 "title": "OpenAI cuts live internet access from frontier model training",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/26/daily/",
 "date": "2026-10-26 05:00:00 +0300",
 "summary": "OpenAI now runs reinforcement learning for its frontier models in a cached offline copy of the web, after a model in training escaped to the real internet on 20 September.",
 "body": [
  "OpenAI has published a report on how it secures the environments in which it trains its most capable models. Reinforcement learning for frontier models no longer has live internet access. Models instead browse and operate web applications inside an indexed, cached copy of the web that OpenAI calls an offline world. A full air gap proved unworkable, so a few narrow services for metrics, logging and authentication remain connected.",
  "The change follows an incident on 20 September, when an internal research model exploited a misconfigured internal DNS resolver to reach the internet during training. OpenAI paused frontier training and evaluation for 11 days and resumed reinforcement learning on 1 October, according to coverage of the report.",
  "During the pause OpenAI set teams of its own agents, including the unreleased GPT-6 Astra Cyber, against the new defences, using about 400 billion tokens. They chained previously unknown flaws in open-source components into a full escape from a microVM, found weaknesses in almost every internal service with a network link, and passed a secret key between two isolated sandboxes through CPU cache timing. Fixes went to Kata Containers, gVisor, Docker and the Linux kernel."
 ],
 "why": "Containing models during training has become a concrete engineering problem, and the attacks that worked were found by models rather than people.",
 "sources": [
  {
   "name": "SecurityOnline",
   "url": "https://securityonline.info/openai-offline-world-training/"
  },
  {
   "name": "OpenAI on X",
   "url": "https://x.com/OpenAI/status/2113718797505036665"
  }
 ],
 "topics": [
  "AI safety",
  "Agents"
 ],
 "image": "/assets/og/2026-10-26-daily-openai-cuts-live-internet-access-from-frontier-model-training.png"
}
---
