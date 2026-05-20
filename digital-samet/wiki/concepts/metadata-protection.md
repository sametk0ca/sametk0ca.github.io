---
concept: Metadata Protection
source: [[ka-privacy-and-online-rights]]
tags: [concept, privacy, metadata, tor, mix-networks, cybok]
---

# Concept: Metadata Protection

## Overview
Metadata (data about data) can be more revealing than the actual content. It includes information like:
- **Identity**: Who is communicating?
- **Relationship**: Who is talking to whom?
- **Traffic Patterns**: When, how often, and for how long?
- **Location**: Where is the communication originating?

## Privacy Goals in Metadata
1. **Anonymity**: The state of being not identifiable within a set of subjects (the **anonymity set**).
2. **Unlinkability**: Two or more items (e.g., messages, actions) cannot be linked to the same user.
3. **Undetectability**: An adversary cannot even distinguish whether an item of interest exists or not.

## Communication Privacy Technologies
### 1. The Onion Router (Tor)
- **Mechanism**: Data is wrapped in multiple layers of encryption (like an onion). It passes through three nodes (Entry, Middle, Exit). Each node only knows its immediate predecessor and successor.
- **Protection**: Hides the relationship between the sender and the destination.
- **Limitations**: Vulnerable to global timing analysis (if an adversary sees both entry and exit points).

### 2. Mix Networks
- **Mechanism**: Messages are collected in a "mix," batched, reordered, and sometimes delayed before being sent to the next hop.
- **Protection**: Stronger than Tor against timing analysis but introduces higher latency. Ideal for non-real-time applications like email.

### 3. VPNs (Virtual Private Networks)
- **Protection**: Encrypts traffic to a single point (the VPN provider). 
- **Caveat**: The VPN provider becomes a single point of failure/trust. They see all your traffic destination patterns.

## Location Privacy
- **Dummy Locations**: Sending fake locations along with the real one.
- **Spatial Cloaking**: Sending a region (bounding box) instead of a precise point.

## References
- [[ka-privacy-and-online-rights]]
- [[privacy-as-confidentiality]]
