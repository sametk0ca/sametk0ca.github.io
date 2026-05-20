# P2P Routing Security

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #p2p #routing #security

## Overview
In a P2P overlay, nodes are responsible for forwarding messages and lookup requests for each other. Routing security ensures that messages reach their intended destination correctly and that the routing infrastructure cannot be subverted.

## Routing Attacks

### 1. Routing Table Poisoning (Index Poisoning)
An attacker injects false information into the routing tables (P-DS) of other nodes.
- **Example:** A node claims to be the "responsible peer" for a specific key in a DHT to intercept all queries for that key.

### 2. Message Dropping and Delays
Malicious nodes participate in the routing process but drop or significantly delay messages to disrupt the overlay's performance.

### 3. Attraction and Repulsion
- **Attraction:** Malicious nodes make themselves appear highly desirable (e.g., by claiming high bandwidth) to attract more traffic for interception.
- **Repulsion:** Malicious nodes make honest nodes appear unreachable or slow to force traffic through the attacker's nodes.

## Mitigation Approaches

### 1. Redundant Routing (Disjoint Paths)
Instead of following a single path to a destination, a node sends the same request through multiple, geographically or topologically disjoint paths. If the results differ, the node can detect a compromise.

### 2. Cryptographic Routing Updates
Requiring nodes to sign their routing table updates. This prevents simple spoofing but is difficult to implement in fully decentralized systems without a shared Public Key Infrastructure (PKI).

### 3. Active Probing and Monitoring
Peers periodically "ping" their neighbors to verify liveness and correctness. In structured P2P, nodes can perform "lookup verification" by asking multiple neighbors for the same key.

### 4. Bounding Node IDs
Preventing nodes from choosing their own IDs (e.g., by deriving the ID from a hash of the IP address and a nonce) makes it much harder for an attacker to target a specific range of the DHT.

## Related Concepts
- [[sybil-and-eclipse-attacks]]
- [[p2p-architectures]]
- [[distributed-systems-fundamental-concepts]]
