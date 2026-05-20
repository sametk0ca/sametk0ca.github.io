# P2P Architectures

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #p2p #overlay

## Overview
Peer-to-Peer (P2P) systems are decentralized distributed systems where nodes (peers) act as both clients and servers. They are characterized by scalability, resilience to node failure, and resource sharing at the edge of the network.

## Taxonomy of P2P Protocols

### 1. Unstructured P2P
- **Discovery:** Uses non-deterministic search algorithms like flooding, random walks, or expanding ring searches.
- **Addressing:** No fixed relationship between a resource and the node that hosts it.
- **Pros:** Extremely resilient to high "churn" (peers frequently joining/leaving); easy to implement.
- **Cons:** Search efficiency decreases as the network grows; no guarantee of finding rare resources.
- **Examples:** Gnutella (early), Freenet.

### 2. Structured P2P
- **Discovery:** Uses a **Distributed Hash Table (DHT)** to map resource keys to specific nodes.
- **Addressing:** Deterministic routing based on a distance function (e.g., XOR distance in Kademlia).
- **Pros:** Guaranteed discovery of existing resources; efficient $O(\log n)$ lookup time.
- **Cons:** High maintenance overhead to maintain the graph structure during churn.
- **Examples:** Chord, Kademlia (used in BitTorrent DHT, Ethereum).

### 3. Hybrid and Hierarchical P2P
- **Hybrid:** Combines centralized components (like Napster's central index) with decentralized data transfer.
- **Hierarchical:** Introduces **Super-peers** (nodes with high bandwidth/stability) that index a subset of the network, acting as a coordination layer for standard peers.
- **Examples:** KaZaA, modern BitTorrent (DHT + Trackers).

## Functional Elements
- **P2P Operations (P-OP):** Discovery, query, routing, and data transfer.
- **P2P Data Structures (P-DS):** Routing tables (finger tables), neighbor lists, and local indexes.

## Related Concepts
- [[sybil-and-eclipse-attacks]]
- [[p2p-routing-security]]
- [[distributed-systems-fundamental-concepts]]
