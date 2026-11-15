---
{
 "layout": "story",
 "title": "Chollet says scale multiplies generalisation rather than replacing it",
 "kind": "story",
 "section": "The debates",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "Francois Chollet, creator of Keras, answered Richard Sutton by arguing that more data and compute multiply the generalisation power of a method, so they cannot rescue a weak one. Yann LeCun separated joint-embedding from joint-embedding predictive architectures and defended the second against critics who point to weaker benchmarks.",
 "body": [
  "Chollet’s point is about ordering. Inefficient methods can look adequate when investment is enormous, but a method that generalises better gains more from each additional unit of scale, so in his view it will eventually overtake. The argument is a claim about the shape of scaling curves, not a reported measurement.",
  "LeCun traced the loss functions of joint-embedding methods to siamese networks, Barlow Twins, VICReg and DINO, and argued that adding a predictor helps when a task is asymmetric, as in predicting the future state of a world model. Critics replied that many papers with JEPA in the title report weaker results than tuned systems such as DINO or V-JEPA. LeCun answered that research on a method and the engineering that later makes it competitive are different stages. The two threads agree that architecture still matters and disagree on how much of it can be learned from scale alone."
 ],
 "sources": [
  {
   "name": "Francois Chollet on X",
   "url": "https://x.com/fchollet/status/2119201339020648849"
  },
  {
   "name": "Yann LeCun on X",
   "url": "https://x.com/ylecun/status/2119522855515824428"
  },
  {
   "name": "Discussion on X: LeCun",
   "url": "https://x.com/ylecun/status/2119143953081799011"
  }
 ],
 "topics": [
  "Learning theory",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-15-weekly-chollet-says-scale-multiplies-generalisation-rather-than-replacing-it.png"
}
---
