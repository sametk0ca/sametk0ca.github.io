# Defense Evasion vs. Stealth (v19 Split)

- **Source:** [[mitre-attack-2026]]
- **Tags:** #mitre #v19 #defense-evasion #stealth #sabotage

## Overview
In April 2026, MITRE officially split the "Defense Evasion" tactic into two distinct categories: **Stealth** and **Impair Defenses**. This reflects a major shift in how security operations (SOC) must respond to different types of adversary activity.

## 1. Stealth (The Passive Approach)
Stealth techniques are designed to avoid detection by blending into the environment. The adversary's goal is to remain hidden for as long as possible.
- **Techniques:** Obfuscation, Steganography, Living-off-the-Land (using legitimate system tools), and Data Encapsulation.
- **Defensive Focus:** Anomaly detection, behavioral baselining, and high-fidelity logging.

## 2. Impair Defenses (The Active Approach)
These techniques involve the active sabotage of security controls. The adversary is no longer trying to hide; they are trying to break the lock.
- **Techniques:** Disabling antivirus (AV), killing EDR agents, wiping event logs, and tampering with security policies.
- **Defensive Focus:** System hardening, tamper-resistance (e.g., protected processes), and alerting on security tool failures.

## Rationale for the Split
The split allows organizations to differentiate between "unauthorized noise" (Stealth) and "direct attack on security infrastructure" (Impair Defenses), prioritizing the latter as critical system-integrity events.

## Related Concepts
- [[adversarial-ttp-foundations]]
- [[malware-evasion-techniques]]
- [[soim-fundamental-concepts]]
