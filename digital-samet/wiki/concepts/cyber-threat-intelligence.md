---
concept: Cyber-Threat Intelligence (CTI)
source: [[ka-security-operations-and-incident-management]]
tags: [concept, cti, sharing, isac, cert, cybok]
---

# Concept: Cyber-Threat Intelligence (CTI)

## Overview
CTI is the collection and analysis of information about current and potential attacks to inform security decisions. It provides the "Knowledge" component of the MAPE-K loop.

## 1. Sources of Intelligence
- **Open Source Intelligence (OSINT)**: Publicly available data from forums, news, and research.
- **Commercial Feeds**: Specialized data provided by security companies.
- **Trusted Organizations**: 
    - **CERT (Computer Emergency Response Team)**: National or organizational entities for incident handling.
    - **ISAC (Information Sharing and Analysis Center)**: Sector-specific entities (e.g., Financial ISAC) for sharing threat data between peers.

## 2. Information Sharing
Exchanging information about breaches helps organizations protect themselves proactively.
- **Indicators of Compromise (IoC)**: Technical artifacts (IPs, hashes, domain names) that suggest a system is compromised.
- **Standards**: 
    - **STIX/TAXII**: Languages and protocols for exchanging CTI.
    - **IODEF (RFC 7970)**: Format for sharing incident information.

## 3. Situational Awareness
Understanding attackers' motivations and tactics (TTPs - Tactics, Techniques, and Procedures) to predict future moves rather than just reacting to individual alerts.

## 4. Legal & Regulatory Context
Regulatory bodies often mandate information sharing for critical infrastructure operators to ensure national security and business continuity.

## References
- [[ka-security-operations-and-incident-management]]
- [[adversarial-modeling-frameworks]]
- [[siem-and-alert-management]]
