---
concept: SOAR and Incident Response
source: [[ka-security-operations-and-incident-management]]
tags: [concept, soim, soar, response, mitigation, cybok]
---

# Concept: SOAR and Incident Response

## 1. SOAR (Security Orchestration, Automation and Response)
SOAR platforms represent the evolution of SIEM, focusing on the *Execute* part of the MAPE-K loop. They aim to automate the response to threats and manage the lifecycle of an incident.

## 2. Automated Mitigation
- **Intrusion Prevention Systems (IPS)**: Acting as gateways to block or alter malicious data streams in real-time.
- **Virtual Patching**: Modifying packet payloads to neutralize exploits without breaking the connection.
- **DDoS Mitigation**: Automated load management, traffic redirection, and blacklisting (e.g., using TCP Syn cookies or BGP Flowspec).

## 3. Incident Management & Ticketing
Most responses are still partially manual due to the risk of disrupting business operations.
- **Change Control**: SOC analysts push requests to IT teams via ticketing systems to ensure stable configurations (Site Reliability Engineering).
- **Escalation Path**: Clearly defined responsibilities for triaging, diagnosing, and authorizing countermeasures.

## 4. Impact and Risk Assessment
Before deploying a countermeasure (like blocking an account or machine), analysts must assess:
- **Asset Level Impact**: What hardware/software is affected?
- **Business Level Impact**: Which business services will go offline? (e.g., blocking a database might be worse than the attack itself).
- **Attack Graphs**: Modeling potential paths an attacker might take to prioritize defenses.

## 5. Economic Trade-off
Cybersecurity is an economic balance between the cost of protection, the acceptable risk, and cyber-insurance.

## References
- [[ka-security-operations-and-incident-management]]
- [[siem-and-alert-management]]
- [[soim-fundamental-concepts]]
