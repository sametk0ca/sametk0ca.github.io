# Network Attacker Models

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #adversary #modeling

## Overview
Understanding the capabilities and position of an attacker is vital for defining the security guarantees of a network protocol or architecture.

## 1. Dolev-Yao Model
The "worst-case" formal model used in protocol research.
- **Capabilities:** The attacker has complete control over the network. They can read any message, prevent delivery, duplicate messages, and synthesize new messages (if they have the keys).
- **Limitation:** Assumes cryptography is perfect (cannot be broken without the key).

## 2. On-path vs. Off-path
- **On-path (Person-in-the-Middle - PITM):** The attacker is located directly on the communication path (e.g., a rogue router). They can eavesdrop and manipulate traffic in real-time.
- **Off-path:** The attacker cannot see or directly manipulate the traffic between two parties. They rely on **Spoofing** (e.g., TCP reset attacks or IP spoofing for DoS) to interfere with the connection.

## 3. Passive vs. Active
- **Passive (Eavesdropper):** Can observe traffic but not alter it. They perform **Traffic Analysis** to infer sensitive information even from encrypted streams (e.g., identifying visited websites via packet patterns).
- **Active:** Can modify, inject, or delete packets.

## 4. Position and Scale
- **Insider vs. Outsider:** Insider attackers are within the trusted domain (e.g., a malicious employee or a compromised IoT device on a LAN).
- **Botnets:** Aggregated power of thousands of devices used for large-scale DDoS.
- **Rogue ISP / AS:** Can correlate traffic patterns across large segments of the Internet and hijack global routes.

## Related Concepts
- [[adversary-modeling-in-formal-methods]]
- [[sybil-and-eclipse-attacks]]
- [[side-channel-formal-analysis]]
