---
concept: SOIM Data Sources
source: [[ka-security-operations-and-incident-management]]
tags: [concept, soim, monitoring, logging, network, host, cybok]
---

# Concept: SOIM Data Sources

## Overview
Detection relies on collecting activity traces (event streams) from various layers of the ICT infrastructure. These traces are the input for sensors that generate alerts.

## 1. Network Traffic Data
- **Packet Capture (pcap)**: Full recording of network traffic. Essential for forensics but storage-intensive. Requires interfaces in "promiscuous mode."
- **Network Aggregates (Netflow/IPFix)**: Synthetic views of traffic (source, destination, volume) without payload. Efficient for identifying patterns but may miss details if sampled.
- **Infrastructure Info**: DNS (naming) and BGP (routing) logs. DNS is often used for botnet Command & Control (C2) and DDoS amplification.

## 2. Host and System Logs
- **System/Kernel Logs**: Monitor internal OS operations, privileged user activity, and system calls. Fine granularity but hard to analyze at scale.
- **Endpoint Protection**: Modern antivirus/EDR engines that intercept activity close to the hardware.
- **Application Logs**: Document activity within specific software (e.g., web server logs like Apache's CLF). Closer to the "business logic" but generated after the event.

## 3. Standardized Infrastructure: Syslog
Syslog (RFC 5424) is the de-facto standard for centralizing logs.
- **Format**: Includes Timestamp, Hostname, Process Name, Priority (Severity 0-7), PID, and the ASCII Message.
- **Facility**: Categorizes logs (e.g., auth, mail, kernel).
- **Transport**: Typically uses UDP/514 for speed and resilience, though TCP/TLS is used for reliability and security.

## 4. Rich Documents
Files like PDF, Office docs, and Flash are data sources for malware detection, as they often contain malicious macros or JavaScript.

## References
- [[ka-security-operations-and-incident-management]]
- [[soim-fundamental-concepts]]
- [[malware-taxonomy]]
