---
{
 "layout": "story",
 "title": "Can diffusion models generate market data?",
 "kind": "story",
 "section": "Markets",
 "edition": "daily",
 "edition_url": "/2026/10/11/daily/",
 "date": "2026-10-11 05:00:00 +0300",
 "summary": "Jane Street finds flow matching stable where earlier diffusion training failed, but multi-step rollouts still drift.",
 "body": [
  "In a post on its technical blog, Jane Street describes an attempt to generate synthetic order-book data with a causal transformer. A categorical head predicts the type of the next event, and a diffusion head predicts its price and timing.",
  "Training with flow matching was stable where a standard denoising diffusion setup blew up, but rollouts over many steps still drift away from realistic behaviour. The post is a clear account of why data that mixes discrete events with continuous values resists generative modelling."
 ],
 "sources": [
  {
   "name": "Jane Street blog",
   "url": "https://blog.janestreet.com/can-you-use-autoregressive-diffusion-to-generate-market-data/"
  }
 ],
 "topics": [
  "Quantitative finance",
  "Market microstructure"
 ],
 "image": "/assets/og/2026-10-11-daily-can-diffusion-models-generate-market-data.png"
}
---
