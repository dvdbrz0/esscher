---
{
 "layout": "story",
 "title": "GPT-6 Astra edits a small model’s weights and lifts its maths score",
 "kind": "story",
 "section": "Must-read · AI",
 "edition": "daily",
 "edition_url": "/2026/11/03/daily/",
 "date": "2026-11-03 05:00:00 +0300",
 "summary": "Four MIT researchers report that a frontier model can read and rewrite neural network weights without gradients or training. Critics call the claim overstated.",
 "body": [
  "Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab of MIT CSAIL published results on 2 November under the name weight-space programming. GPT-6 Astra, given raw weights as text, named the game each of four small policy networks had been trained on, and identified the shapes learned by small diffusion models without running them. With no data, loss or tools, it wrote MinAtar game networks in one reply that beat networks trained by PPO for 100 million steps.",
  "The largest test used Qwen3.5-0.8B, a model its own card warns is prone to thinking loops. Given a Python session over the weights and 50 forward passes on practice problems, Astra traced the loops to one direction written by layers 15 and 19 and subtracted it from 131,072 weights, or 0.016% of the total. MATH-500 rose from 7.9% to 48.1%, GSM8K from 13.8% to 67.1% and IFEval from 21.0% to 62.3%. With 10 or 25 passes the loops barely went away, and on Gemma 3 270M, a model that does not loop, scores hardly moved, from 6.8% to at most 7.7%.",
  "Sean Goedecke argued that the results are overstated, that a competent researcher could do the same, and that the Qwen edit resembles existing steering techniques. The authors have released their logs and the edited model, and Ahsen Khaliq at Hugging Face rebuilt it from those logs and re-ran its evaluation. The work is a blog post and has not been peer reviewed."
 ],
 "why": "A cheap, targeted fix for a known failure in an open model is testable now, and the larger claim about optimisation will stand or fall on replication at scale.",
 "links": [
  {
   "label": "Takehi et al.: Sparks of Weight-Space Programming",
   "url": "https://rikiyat.github.io/blog/weight-space-programming/"
  },
  {
   "label": "Discussion on X",
   "url": "https://x.com/rikiyatakehi/status/2117313742891327994"
  },
  {
   "label": "VentureBeat: the coverage",
   "url": "https://venturebeat.com/technology/like-gene-editing-for-neural-networks-mit-researchers-used-gpt-6-astra-to-edit-qwens-open-weights-directly-boosting-math-performance"
  },
  {
   "label": "daily.dev: summary of Goedecke’s critique",
   "url": "https://daily.dev/posts/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights-yrkwtj9xo"
  }
 ],
 "published": "2026-11-02",
 "status": "Not peer reviewed",
 "topics": [
  "Large language models",
  "Optimization"
 ],
 "image": "/assets/og/2026-11-03-daily-gpt-6-astra-edits-a-small-models-weights-and-lifts-its-maths-score.png"
}
---
