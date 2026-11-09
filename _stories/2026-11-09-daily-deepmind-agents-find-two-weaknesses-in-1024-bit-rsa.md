---
{
 "layout": "story",
 "title": "DeepMind agents find two weaknesses in 1024-bit RSA",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/09/daily/",
 "date": "2026-11-09 05:00:00 +0300",
 "summary": "Google DeepMind said human-guided AI agents weakened padded signatures and batch factoring for legacy 1024-bit RSA; 2048-bit keys are unaffected, and some of the gains are theoretical estimates.",
 "body": [
  "Google DeepMind said on 6 November that AI agents, guided by researchers including Nadia Heninger and Emmanuel Thomé, uncovered two weaknesses in legacy 1024-bit RSA. The first concerns signature padding: once an attacker controls about half of the signed block, padding adds little protection. In a sandboxed reproduction against an earlier benchmark key, the agents used 3.5 times less CPU time than the original result.",
  "The second concerns factoring many keys of the same length at once. The agents found a batch algorithm with better asymptotic complexity than earlier ones, cutting the average cost of each additional 1024-bit key by about 30 times. For short signed fingerprints, DeepMind estimates a further algorithm improves on the best known method by about 1,600 times, a figure that is theoretical.",
  "The company stressed that the results apply only to retired 1024-bit systems and that 2048-bit RSA is not affected."
 ],
 "sources": [
  {
   "name": "OfficeChai",
   "url": "https://officechai.com/ai/google-deepmind-says-it-has-used-ai-agents-to-break-legacy-rsa-1024-encryption-faster-than-anyone-thought-possible/"
  },
  {
   "name": "RuntimeWire",
   "url": "https://runtimewire.com/article/google-deepmind-ai-agents-1024-bit-rsa-weaknesses"
  }
 ],
 "published": "2026-11-06",
 "topics": [
  "Agents",
  "Mathematics"
 ],
 "image": "/assets/og/2026-11-09-daily-deepmind-agents-find-two-weaknesses-in-1024-bit-rsa.png"
}
---
