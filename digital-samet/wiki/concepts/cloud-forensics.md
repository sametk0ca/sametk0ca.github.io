# Cloud Forensics

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #cloud #saas

## Overview
Cloud forensics addresses the disruptive challenges and new opportunities of the cloud computing model (SaaS, PaaS, IaaS).

## Canonical Service Models
- **Infrastructure as a Service (IaaS):** Focus on virtual machine snapshots and network logs.
- **Platform as a Service (PaaS):** Middle layer where responsibility is shared between client and provider.
- **Software as a Service (SaaS):** Heavy lifting on the server side, client performs user interaction.

## Key Transitions
- **Logical Acquisition:** Inapplicable to the cloud. APIs are the norm for data acquisition.
- **Cloud as Authoritative Source:** Local replicas (e.g., cloud drives) are transient and of uncertain provenance.
- **Pervasive Logging:** Cloud applications are highly logged for debugging and monitoring.
- **Distributed Computations:** Code and data are downloaded on demand, breaking traditional device-centric tools.

## Challenges: SaaS Forensics
- **Partial Replication:** No guarantee a client has a complete copy of the cloud drive content.
- **Revision Acquisition:** Version history is stored in the cloud, and missing from local caches.
- **Cloud-native Artifacts:** Digital artifacts (e.g., Google Docs) with no local file representation (links only).

## Analysis Targets
- **Cloud APIs:** The primary interface for data acquisition.
- **Cloud-native Artifacts:** Internal data structures (e.g., editing logs in Google Docs).
- **Service Provider Interaction:** Legal and technical paths to obtain data from CSPs.

## Related Concepts
- [[data-acquisition-methods]]
- [[application-forensics]]
- [[legal-risk-management]]
