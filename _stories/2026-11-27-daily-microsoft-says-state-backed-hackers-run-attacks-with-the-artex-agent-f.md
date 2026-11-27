---
{
 "layout": "story",
 "title": "Microsoft says state-backed hackers run attacks with the ARTEX agent framework",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/27/daily/",
 "date": "2026-11-27 05:00:00 +0300",
 "summary": "Microsoft Threat Intelligence said groups from China and North Korea, including Salt Typhoon, now use ARTEX, a multi-agent framework that runs existing attack tools with little human oversight.",
 "body": [
  "ARTEX was released as an AI penetration-testing framework in July and has spread since, according to a Microsoft analysis summarised by The Decoder. Microsoft names Salt Typhoon, Crystal Typhoon, Onyx Sleet and Storm-0940 among the state-backed groups using it, alongside financially motivated criminals. The source code was published on GitHub in July and deleted in October, but copies still circulate.",
  "The framework does not invent new techniques. A goal model splits the attacker’s instruction into subgoals, a planning agent assigns short tasks from a knowledge graph of discovered systems, and worker agents run tools such as Nmap, Sqlmap and Metasploit. Any language model can be connected, and the framework switches models or API keys automatically when one fails. In one case an agent took five minutes to go from credentials exposed on GitHub to data in Azure Key Vault. Microsoft recommends deception, such as decoy systems and fake signals of success, to make agents stop."
 ],
 "sources": [
  {
   "name": "The Decoder",
   "url": "https://the-decoder.com/microsoft-details-how-state-backed-hackers-use-the-artex-ai-framework-to-automate-cyberattacks/"
  }
 ],
 "published": "2026-11-26",
 "topics": [
  "Agents",
  "AI safety"
 ],
 "image": "/assets/og/2026-11-27-daily-microsoft-says-state-backed-hackers-run-attacks-with-the-artex-agent-f.png"
}
---
