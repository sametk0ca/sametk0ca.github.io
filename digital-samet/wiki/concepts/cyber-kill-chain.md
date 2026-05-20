---
concept: The Cyber Kill Chain Model
source: [[ka-malware-and-attack-technologies]]
tags: [concept, malware, attack, kill-chain, cybok]
---

# Concept: The Cyber Kill Chain Model

## Overview
Developed by Lockheed Martin, the Cyber Kill Chain represents the stages of a cyberattack. Understanding these steps allows defenders to identify and stop attacks at various points in the lifecycle.

## Stages of the Kill Chain
1. **Reconnaissance**: Harvesting information (email addresses, vulnerable services) about the target.
2. **Weaponization**: Coupling an exploit with a backdoor into a deliverable payload (e.g., a malicious PDF or Office document).
3. **Delivery**: Sending the weaponized payload to the victim (via email, web download, USB, etc.).
4. **Exploitation**: The payload executes on the victim's system, triggering a vulnerability (e.g., buffer overflow).
5. **Installation**: Installing additional malware or backdoors to maintain persistence.
6. **Command & Control (C2)**: Establishing a channel for the attacker to remotely manage the compromised system.
7. **Actions on Objectives**: Achieving the final goal (e.g., data exfiltration, service disruption, ransomware encryption).

## Defense Strategies
- **Confidentiality Attacks**: Prevent data theft through encryption and access control.
- **Integrity Attacks**: Use file integrity monitoring and digital signatures to prevent falsified information.
- **Availability Attacks**: Implement DDoS mitigation and robust backup/recovery systems (especially for ransomware).

## Advanced Persistent Threats (APTs)
Unlike noisy botnets, APTs are "low and slow." They move laterally within an organization, cover their tracks, and stay persistent for long periods to achieve specific, high-value objectives.

## References
- [[ka-malware-and-attack-technologies]]
- [[malware-taxonomy]]
- [[botnets-and-apts]]
