---
concept: SIEM and Alert Management
source: [[ka-security-operations-and-incident-management]]
tags: [concept, soim, siem, alerts, soc, cybok]
---

# Concept: SIEM and Alert Management

## 1. SIEM (Security Information and Event Management)
SIEM platforms centralize data from distributed sensors to provide a global view of the security posture. They bridge the *Analyze* and *Plan* stages of the MAPE-K loop.

## 2. The Alert Pipeline
1. **Aggregation**: Collecting alerts from heterogeneous sensors (IDS, Firewalls, Logs).
2. **Normalization**: Converting different formats into a common schema (e.g., IDMEF or Syslog-based).
3. **Correlation**: Linking multiple alerts from different sources to identify a single complex **Incident**.
4. **Prioritization**: Scoring incidents based on severity, asset value, and likelihood.

## 3. Operational Processes
- **Triage**: Analysts review the SIEM console to separate "noise" from actionable incidents.
- **Escalation**: Passing complex or confirmed incidents to specialized senior analysts.
- **Reporting**: Analyzing SOC performance and improving detection rules over time.

## 4. SIEM Contributions to Analysis
Because sensors only see local data, SIEMs can detect distributed attacks:
- **Vertical Correlation**: Linking events across layers (e.g., a web alert followed by a database query).
- **Horizontal Correlation**: Linking events across multiple hosts (e.g., a slow scan targeting an entire subnet).

## 5. Deployment Challenges
- **Volume**: Modern systems generate billions of events daily.
- **Tuning**: SIEMs require constant rule adjustment to minimize false positives while maintaining coverage.
- **Dynamics**: Cloud and ephemeral environments make static correlation rules difficult to maintain.

## References
- [[ka-security-operations-and-incident-management]]
- [[soim-fundamental-concepts]]
- [[detection-and-analysis-algorithms]]
