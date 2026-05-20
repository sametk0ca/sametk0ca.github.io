# Network Intrusion Detection and Prevention (IDS/IPS)

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #detection #ids #ips #monitoring

## Overview
Intrusion Detection Systems (IDS) monitor network traffic for suspicious activity, while Intrusion Prevention Systems (IPS) actively block detected threats.

## 1. Detection Methods

### Signature-based Detection
Matches traffic against a database of known malicious patterns (signatures).
- **Pros:** High accuracy for known threats; low false positive rate.
- **Cons:** Ineffective against new (zero-day) attacks; requires constant signature updates.
- **Example:** Snort rules matching specific byte sequences in a payload.

### Anomaly-based Detection
Builds a model of "normal" network behavior and alerts on deviations.
- **Pros:** Can detect zero-day attacks and unusual patterns.
- **Cons:** High false positive rate (legitimate changes in behavior look like attacks); difficult to build a clean baseline.
- **Mechanism:** Using statistical features (bandwidth, ports, arrival rates) or machine learning.

## 2. Scope of Deployment
- **HIDS (Host-based):** Runs on individual systems (e.g., antivirus monitoring network calls).
- **NIDS (Network-based):** Strategically placed sensors monitoring traffic for an entire segment.

## 3. Analysis Techniques
- **DPI (Deep Packet Inspection):** Examining the application-layer payload (e.g., matching SQL commands in HTTP traffic).
- **Flow Monitoring:** Analyzing traffic statistics (e.g., NetFlow, IPFIX) without inspecting payloads. Good for large-scale anomaly detection and forensics.

## 4. Challenges
- **Encrypted Traffic:** Traditional IDS/IPS cannot inspect payloads of TLS sessions unless they act as a proxy (TLS termination).
- **Operational Load:** "Alert fatigue" caused by too many false positives.

## Related Concepts
- [[accountability-and-logging]]
- [[soim-fundamental-concepts]] (Incident management)
- [[fuzz-testing-techniques]]
