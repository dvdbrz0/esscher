---
{
 "layout": "story",
 "title": "Anthropic rewrites its Messages API in Rust with Claude, using production as the check",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "Claude wrote the first version of the API’s core request path in about a week; the hard part was verification, solved by comparing the new service against the live Python one on production traffic.",
 "body": [
  "Anthropic said it has moved its Messages API, the main way customers and its own apps reach Claude, from Python to Rust. API traffic grew roughly 1,800 times between early 2024 and autumn 2026, and Python’s per-object overhead had become costly. An earlier partial rewrite of output parsing in Rust cut CPU use by 8–10%.",
  "Claude wrote a first version of the core request path in about a week. Establishing parity was harder: the Python service kept changing, model replies are nondeterministic, and engineers could not read customer requests. The company turned the production API into a verifier, running the Rust version on live traffic, locating differences and dispatching agents to fix them.",
  "The new service uses about 70% less CPU per request and cuts median time to first token by about 20%, and the migration was done without taking the service offline."
 ],
 "why": "It is a worked example of agents taking on a live system once a reliable verifier exists.",
 "sources": [
  {
   "name": "Anthropic",
   "url": "https://www.anthropic.com/research/migrating-api-to-rust"
  }
 ],
 "published": "2026-11-25",
 "topics": [
  "Agents",
  "AI industry"
 ],
 "image": "/assets/og/2026-11-26-daily-anthropic-rewrites-its-messages-api-in-rust-with-claude-using-producti.png"
}
---
