---
{
 "layout": "story",
 "title": "Fine-Tuning an Order-Flow Foundation Model for Sub-Second Forecasting",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/13/daily/",
 "date": "2026-11-13 05:00:00 +0300",
 "summary": "A 300m-parameter generative model pretrained on Level-3 crypto order flow and then fine-tuned beats gradient boosting at sub-second microprice forecasts and transfers to unseen assets.",
 "body": [
  "The author pretrains an autoregressive generative model of 300m parameters on Level-3 order-flow data from two crypto exchanges, Bitstamp and Bitfinex, and then fine-tunes it to predict the microprice return and its realised volatility. Earlier work had pretrained such models but, the paper says, none had fine-tuned one for downstream tasks.",
  "The fine-tuned model beats classical baselines, including gradient boosting on handcrafted features, at predicting microprice returns over sub-second horizons, and its predictive ability transfers zero-shot to assets it was not fine-tuned on. The predicted moves are smaller than the bid-ask spread plus fees, so the applications are in execution and market making rather than directional trading."
 ],
 "published": "2026-11-10",
 "authors": "Shabashev",
 "arxiv": "2611.14117",
 "tag": "Market microstructure",
 "topics": [
  "Market microstructure",
  "Quantitative finance"
 ],
 "image": "/assets/og/2026-11-13-daily-fine-tuning-an-order-flow-foundation-model-for-sub-second-forecasting.png"
}
---
