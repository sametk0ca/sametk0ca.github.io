---
concept: Botnets and Advanced Persistent Threats (APTs)
source: [[ka-malware-and-attack-technologies]]
tags: [concept, malware, botnet, apt, cybok]
---

# Concept: Botnets and Advanced Persistent Threats (APTs)

## 1. Botnets
A **Botnet** is a network of compromised computers (**bots**) under the control of a single attacker (**botmaster**).

### Command and Control (C2)
- **Centralized**: Bots connect to a central server (IRC, HTTP) to receive commands. Single point of failure.
- **Decentralized (P2P)**: Bots communicate with each other to pass commands. Harder to take down.
- **Agility Techniques**:
    - **DGA (Domain Generation Algorithms)**: Automatically generating thousands of potential C2 domains daily.
    - **Fast-Flux DNS**: Rapidly changing the IP addresses associated with a C2 domain using a pool of compromised hosts.

### Botnet Activities
- **DDoS Attacks**: Using combined bandwidth to overwhelm targets.
- **Spam/Phishing**: Sending massive volumes of malicious emails.
- **Click Fraud**: Generating fake ad clicks for revenue.
- **Cryptojacking**: Using bot resources to mine cryptocurrency.

## 2. Advanced Persistent Threats (APTs)
APTs are targeted, highly sophisticated attacks typically conducted by nation-states or organized groups.

### Key Characteristics
- **Persistence**: Goal is to stay undetected for long periods (years).
- **Lateral Movement**: Moving from an initial compromised host to higher-value targets within the same network.
- **Exfiltration**: Stealing sensitive data (IP, military secrets) in small, "low and slow" batches to avoid detection.
- **Custom Malware**: Often uses zero-day exploits and unique, non-signature-based malware.

### Detection Challenges
- APTs often use **"Living off the Land"** techniques—using legitimate system tools (PowerShell, WMI) rather than obvious malicious binaries.

## References
- [[ka-malware-and-attack-technologies]]
- [[cyber-kill-chain]]
- [[malware-evasion-techniques]]
