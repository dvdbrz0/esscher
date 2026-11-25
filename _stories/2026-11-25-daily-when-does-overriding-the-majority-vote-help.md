---
{
 "layout": "story",
 "title": "When Does Overriding the Majority Vote Help?",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/25/daily/",
 "date": "2026-11-25 05:00:00 +0300",
 "summary": "On 150 competition-maths questions, extra reasoning by the same model rarely changes a 16-sample majority vote, while executed programs fix more errors than they introduce at every agreement threshold tested.",
 "body": [
  "Majority voting over sampled answers is a standard way to spend test-time compute. The paper asks when an override, replacing the voted answer with one produced by further reasoning, code execution or a different model, does more good than harm. It starts from a vote over 16 responses from each of three open reasoning models on 150 competition-mathematics questions.",
  "When the vote is wrong, the correct answer is often missing from the original responses altogether, which caps what any reselection can achieve. Same-model reasoning seldom overrides; executed programs correct more errors than they introduce at every threshold; cross-model overrides help some weaker baselines but do not beat the stronger model alone. Requiring stricter agreement makes overrides rarer without reliably making them more accurate."
 ],
 "published": "2026-11-23",
 "authors": "Ma and Zhang",
 "arxiv": "2611.31165",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-25-daily-when-does-overriding-the-majority-vote-help.png"
}
---
