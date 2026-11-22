---
{
 "layout": "story",
 "title": "LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/22/weekly/",
 "date": "2026-11-22 08:00:00 +0300",
 "summary": "In 91 backtest runs of six models over a rally, a bear market and a crash, no trading agent produced significant alpha. Market and style exposure explained a median 78% of returns, and the agents’ picks did no better than random stocks from the same sector.",
 "body": [
  "The benchmark, rta-bench-1, releases each headline only after its minute of publication and checks every run for look-ahead, two common leaks in earlier backtests. It then splits each return into factor exposure and alpha. Two runs of the same model that differed only in the random seed ended 5.2 points apart on average, which shows how little a single run says about skill.",
  "The agents bought the stocks with the most positive news, yet earned as much when the headlines were removed. They did follow instructions: one cash rule in the prompt cut a GPT-based agent’s share in stocks by 30.3 points in all six pairs. The author’s advice is that builders supply the edge themselves and report exposures alongside alpha."
 ],
 "published": "2026-11-14",
 "authors": "Jackson Wang",
 "arxiv": "2611.19530",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance",
  "Agents"
 ],
 "image": "/assets/og/2026-11-22-weekly-llm-trading-agents-earn-beta-not-alpha-a-look-ahead-free-benchmark.png"
}
---
