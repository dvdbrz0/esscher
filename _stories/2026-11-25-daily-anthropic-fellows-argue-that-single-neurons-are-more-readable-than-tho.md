---
{
 "layout": "story",
 "title": "Anthropic Fellows argue that single neurons are more readable than thought",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/25/daily/",
 "date": "2026-11-25 05:00:00 +0300",
 "summary": "Two posts from the Anthropic Fellows programme report that, judged by what they write to the model’s output, neurons rarely mix unrelated concepts and keep a stable meaning across layers.",
 "body": [
  "Interpretability research moved away from individual neurons for three reasons: neurons fire on unrelated inputs, representations seem to change from layer to layer, and facts appear spread over many neurons. Jasmine Shone and Lisa Dunlap revisit these objections by reading each neuron’s output vector, the direction it adds to the residual stream, rather than only the inputs that make it fire, and test their readings by switching neurons off or moving their outputs to other layers.",
  "In their samples, a neuron added two unrelated concepts at once in about 1% of cases or fewer. A neuron’s output kept roughly the same meaning across most layers. Changing a fact usually required altering many neurons, but those neurons generally represented concepts related to the fact, so recall was distributed yet still readable. A second post applies the method to detecting harmful text, steering behaviour and auditing hidden behaviours in fine-tuned models without extra training."
 ],
 "sources": [
  {
   "name": "Anthropic Alignment Science blog, part 1",
   "url": "https://alignment.anthropic.com/2026/neuron-basis-theory/"
  },
  {
   "name": "Anthropic Alignment Science blog, part 2",
   "url": "https://alignment.anthropic.com/2026/neuron-basis-applications/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/AnthropicAI/status/2125365268381929637"
  }
 ],
 "published": "2026-11-23",
 "topics": [
  "AI safety",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-25-daily-anthropic-fellows-argue-that-single-neurons-are-more-readable-than-tho.png"
}
---
