# Adversarial TTP Foundations

- **Source:** [[mitre-attack-2026]], [[ka-adversarial-behaviours]]
- **Tags:** #ttp #adversary #tactics #mitre

## Overview
**TTP (Tactics, Techniques, and Procedures)** is the fundamental methodology for describing adversarial behavior. It moves security analysis from "indicators" (like IP addresses or hashes) to "behaviors," which are harder for attackers to change.

## The Hierarchy
1. **Tactics (The "Why"):** The adversary's tactical objective. Examples include Initial Access, Persistence, and Exfiltration.
2. **Techniques (The "How"):** The specific method used to achieve a tactic. For example, "Phishing" is a technique for the "Initial Access" tactic.
3. **Procedures (The "Specifics"):** The exact implementation or toolset used by a specific threat actor (e.g., APT28 using a specific macro-enabled Word document).

## Value in Defense
Mapping behaviors to TTPs allows defenders to:
- Identify gaps in detection.
- Perform behavioral threat hunting.
- Communicate risk in a standardized language across the industry.

## Related Concepts
- [[adversary-characterization]]
- [[modern-threat-landscape]]
- [[defense-evasion-vs-stealth]]
