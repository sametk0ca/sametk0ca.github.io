# Sybil and Eclipse Attacks

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #p2p #attacks #identity

## Overview
Sybil and Eclipse attacks exploit the decentralized nature of P2P systems, where nodes rely on a limited, local view of the network to make decisions.

## 1. Sybil Attack
The Sybil attack occurs when a single adversary controls multiple fake identities (Sybils) to gain a disproportionate influence over the network.
- **Goal:** Outvote honest nodes in a consensus protocol, manipulate reputation systems, or subvert routing.
- **Impact:** Compromises **Integrity** and **Availability**.
- **Mitigation:**
    - **Centralized Certification:** Requiring a trusted third party to verify identities.
    - **Resource Hardening:** Requiring proof-of-work or proof-of-stake to create an identity.
    - **Social Graph Analysis:** Identifying Sybil clusters based on their limited number of connections to the honest part of the graph.

## 2. Eclipse Attack
An Eclipse attack is a more targeted attack where an adversary colludes to surround a specific victim node with malicious peers.
- **Mechanism:** The attacker corrupts the victim's routing table (P-DS) so that all of its outgoing and incoming connections are through malicious nodes.
- **Goal:** Provide the victim with a false view of the network state (e.g., hiding transactions in a blockchain or isolating a node for censorship).
- **Impact:** Compromises **Confidentiality**, **Integrity**, and **Availability**.
- **Mitigation:**
    - **Deterministic Identity Allocation:** Preventing nodes from choosing their own network IDs.
    - **Diverse Peer Selection:** Forcing nodes to connect to peers in different IP ranges or network segments.
    - **Lookup Verification:** Comparing results from multiple disjoint paths in a DHT.

## Relationship
Sybil attacks are often a precursor to Eclipse attacks. An adversary uses Sybil identities to fill the routing slots of many honest nodes, eventually "eclipsing" them.

## Related Concepts
- [[p2p-architectures]]
- [[p2p-routing-security]]
- [[distributed-systems-fundamental-concepts]]
