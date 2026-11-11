---
{
 "layout": "story",
 "title": "OpenAI describes Control Room, a system to halt research workloads in 35 seconds",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/11/daily/",
 "date": "2026-11-11 05:00:00 +0300",
 "summary": "OpenAI said it has deployed a central service across its research infrastructure that can stop a training run, evaluation or data job from receiving further model outputs within 35 seconds of a decision to intervene.",
 "body": [
  "Every research workload that runs agentic inference must be tied to an approved safety case and must obtain a job identifier from Control Room. The identifier travels with each request to the inference engines, which check with the service before generating output. When a human or an automated monitor flags a job, its authorisation is revoked and output stops.",
  "The design fails closed: if the central service becomes unavailable, inference requests are blocked. Placing the control at the inference layer rather than in research code means a change to a training script cannot switch it off. OpenAI said its external model-serving systems are more centralised and already have ways to take down deployments.",
  "The system is internal and is not offered to customers."
 ],
 "why": "It is a concrete mechanism for stopping a misbehaving model during research, the stage at which labs say the risk is now greatest.",
 "sources": [
  {
   "name": "OpenAI",
   "url": "https://openai.com/index/control-room/"
  },
  {
   "name": "Interesting Engineering",
   "url": "https://interestingengineering.com/ai-robotics/openai-control-room-35-second-model-shutdown"
  }
 ],
 "topics": [
  "AI safety",
  "Agents"
 ],
 "image": "/assets/og/2026-11-11-daily-openai-describes-control-room-a-system-to-halt-research-workloads-in-3.png"
}
---
