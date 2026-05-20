---
concept: SOIM Fundamental Concepts
source: [[ka-security-operations-and-incident-management]]
tags: [concept, soim, mape-k, soc, cybok]
---

# Concept: SOIM Fundamental Concepts

## Overview
SOIM is built on the principle that technical and economic constraints make 100% protection impossible. Detection and reaction are necessary complements to protection.

## The MAPE-K Loop
Applied to security, this autonomic computing loop consists of five stages:
1. **Monitor**: Collecting data from the ICT infrastructure (network, hosts, applications).
2. **Analyze**: Determining if the collected data contains evidence of an attack.
3. **Plan**: Deciding on the appropriate response to a detected threat.
4. **Execute**: Implementing the mitigation or recovery actions.
5. **Knowledge**: A stable base of intelligence (signatures, configurations, CTI) that informs all other stages.

## Evolution of SOIM Tools
- **Intrusion Detection Systems (IDS)**: Initially focused on the *Monitor* and *Analyze* stages.
- **Intrusion Prevention Systems (IPS/IDPS)**: Evolved IDS that can automatically *Execute* simple blocks.
- **SIEM (Security Information and Event Management)**: Focuses on *Plan* and *Analyze* at a global level, managing massive alert volumes.
- **SOAR (Security Orchestration, Automation and Response)**: The newest layer, focusing on the *Plan* and *Execute* stages through high-level automation and external intelligence.

## Security Operations Center (SOC)
The centralized organizational unit (tech + humans) responsible for SOIM. SOCs use SIEM/SOAR platforms to assess impact and deploy mitigations following established processes.

## Architecture Principles
- **Sensors**: Distributed throughout the network (DMZs, internal segments) and on hosts.
- **Attachment**: Sensors often have a "stealth" attachment for monitoring and a "regular" attachment for reporting alerts to the SIEM over a protected management network.
- **Zones**: Using DMZs to terminate external communications and increase scrutiny.

## References
- [[ka-security-operations-and-incident-management]]
- [[siem-and-alert-management]]
- [[soar-and-incident-response]]
