---
{
 "layout": "story",
 "title": "LLMs Don’t Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/08/weekly/",
 "date": "2026-11-08 08:00:00 +0300",
 "summary": "A benchmark of 2,226 dated US facts shows that frontier models understate what they know: GPT-5 answers 76% of controlled facts correctly but claims to know 38%. Backtests inside a model’s training window cannot be certified free of leakage by self-report, instruction or a stated cutoff.",
 "body": [
  "A backtest of a language model means something only if the model did not already know the outcome. Practitioners usually trust the vendor’s stated cutoff, ask the model what it knows, or tell it to answer as of a past date. The authors test all three with FinDendro, 2,226 dated facts from 1999 to 2026 covering monthly macroeconomic series, month-end stock prices and Federal Reserve decisions, with controls that keep chance accuracy near 0.27.",
  "Self-reports understate knowledge for most frontier models. GPT-5 answers 61% of the facts it says it does not know. Claims of knowledge persist up to seven quarters beyond the measured boundary, and a declared date removes most claims of prior knowledge while leaving accuracy unchanged. The authors propose choosing backtest periods by measured factual knowledge instead."
 ],
 "published": "2026-11-04",
 "authors": "Qian et al.",
 "arxiv": "2611.06808",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-08-weekly-llms-dont-know-what-they-know-benchmarking-temporal-self-knowledge-for.png"
}
---
