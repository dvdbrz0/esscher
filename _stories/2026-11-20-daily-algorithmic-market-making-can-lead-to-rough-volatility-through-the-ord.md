---
{
 "layout": "story",
 "title": "Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/20/daily/",
 "date": "2026-11-20 05:00:00 +0300",
 "summary": "Market makers who adjust their quotes by a stochastic-gradient rule over different lookback horizons generate order flow with power-law memory, which by standard scaling arguments produces rough volatility.",
 "body": [
  "Rough volatility models, in which volatility paths are rougher than Brownian motion, fit market data well, and theory links them to order flow that is close to instability with power-law memory. It has been less clear how algorithmic market making would produce such order flow.",
  "The paper models each market maker as a desk that moves its quote distances from the mid price towards targets set by an unknown oracle, updating whenever new information arrives over its own lookback horizon. Across desks this is stochastic gradient descent with information-driven noise. In the continuum limit the volume of the order book follows the Dean-Kawasaki stochastic partial differential equation, and the spread of horizons gives power-law memory in the order flow. The author tests the predictions on simulated agents and on six months of Binance perpetual futures data with about 790 million orders."
 ],
 "published": "2026-11-18",
 "authors": "Ramachandran",
 "arxiv": "2611.24028",
 "tag": "Market microstructure",
 "topics": [
  "Market microstructure",
  "Quantitative finance"
 ],
 "image": "/assets/og/2026-11-20-daily-algorithmic-market-making-can-lead-to-rough-volatility-through-the-ord.png"
}
---
