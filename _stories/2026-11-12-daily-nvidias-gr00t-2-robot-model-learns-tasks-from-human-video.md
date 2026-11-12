---
{
 "layout": "story",
 "title": "Nvidia’s GR00T 2 robot model learns tasks from human video",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/12/daily/",
 "date": "2026-11-12 05:00:00 +0300",
 "summary": "Nvidia’s GEAR lab introduced GR00T 2, a world-action model that predicts future video and robot actions together; on 50 unseen tasks it succeeds 40% of the time zero-shot and 95% after five demonstrations.",
 "body": [
  "GR00T 2 is a single diffusion transformer that denoises future camera frames and a chunk of robot actions at the same time, with small heads that translate the plan into motor commands for each robot body. Predicting how the scene should change is what lets it learn physical interaction from people: the pretraining mix holds 402,730 hours of egocentric human video, 10,184 hours of handheld-gripper demonstrations and 23,500 hours of robot teleoperation. In Nvidia’s ablation, raising the share of human video from none to all of it lifted real-robot task progress on 72 tasks from 50% to 70%.",
  "On 50 tasks the target robot had never practised, the model succeeded 40% of the time zero-shot. Five demonstrations per task, under three minutes of robot data, and a 30-minute fine-tune on one consumer graphics card raised that to 95%. A smaller variant, GR00T 2 Turbo, runs on the Unitree G1 humanoid’s own computer at 124 milliseconds per prediction.",
  "Jim Fan, who leads the lab, announced the model on X. Nvidia has released 100,000 hours of the human video on Hugging Face; the code and weights are due in December. The results are Nvidia’s own and have not been independently replicated."
 ],
 "why": "If human video transfers to robots at this rate, the scarcity of robot training data becomes a smaller constraint.",
 "sources": [
  {
   "name": "Nvidia GEAR lab",
   "url": "https://research.nvidia.com/labs/gear/gr00t-2/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/DrJimFan/status/2120186653448810948"
  }
 ],
 "topics": [
  "AI industry",
  "Agents"
 ],
 "image": "/assets/og/2026-11-12-daily-nvidias-gr00t-2-robot-model-learns-tasks-from-human-video.png"
}
---
