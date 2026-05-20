# Accountability and Logging

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #accountability #logging #audit

## Overview
Accountability is the security goal that ensures actions of an entity can be traced uniquely to that entity. It is a critical component for non-repudiation, deterrence, and incident response.

## Technical Pillars

### 1. Audit Policies
System administrators define which events are security-relevant and should be recorded.
- **Common Events:** Successful/failed logins, privilege escalation, access to sensitive objects, configuration changes.
- **Equation:** Effective Audit = Clear Policy + Reliable Collection.

### 2. Evidence Preservation (Tamper Resistance)
Protecting collected logs is essential because attackers often try to delete their tracks.
- **Physical Measures:** Printing logs to paper, using WORM (Write-Once, Read-Many) optical media.
- **Cryptographic Measures:** Storing logs in a **Hash Chain** where every entry includes the hash of the previous one. This makes deletions or modifications detectable.
- **Distributed Logs:** Using a blockchain or a set of independent nodes to maintain a consistent and unalterable audit trail.

### 3. Evidence Analysis
Automated tools are required to handle high log volumes.
- **Signature Detection:** Matching logs against known attack patterns.
- **Anomaly Detection:** Using machine learning to find deviations from baseline behavior.
- **Visualization:** Helping human analysts spot trends or critical spikes.

## Conflict with Privacy
Excessive logging can violate privacy laws (e.g., monitoring employee web usage).
- **Technical Mitigation:** Logging only metadata (e.g., internal IP + port) rather than full destinations, allowing for attribution only when a specific external incident is reported.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[soim-fundamental-concepts]] (Incident management)
- [[merkle-trees-and-blockchains]]
