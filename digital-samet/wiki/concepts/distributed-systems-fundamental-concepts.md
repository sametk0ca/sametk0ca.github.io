# Distributed Systems Fundamental Concepts

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #architecture #coordination

## Overview
A distributed system is a collection of independent computers that appears to its users as a single coherent system. It aims to provide geo-proximate access, high availability, and aggregate computational power.

## Core Characteristics
- **Resource Orchestration:** Transparently managing dispersed resources so users don't see the underlying complexity.
- **Middleware:** A layer of software between applications and the OS that facilitates communication and coordination (e.g., RPC, Publish-Subscribe).
- **Concurrency:** Multiple tasks executing simultaneously across different nodes.
- **No Global Clock:** Nodes must synchronize through message passing rather than a shared clock.
- **Independent Failures:** A fault in one node does not necessarily bring down the entire system.

## Communication Models
- **Message Passing:** Direct exchange of data between nodes.
- **Remote Procedure Call (RPC):** Executing a function on a remote node as if it were local.
- **Publish-Subscribe:** Decoupling producers and consumers through event-based messaging.

## Coordination and Consistency
To provide a "virtually centralized" view, distributed systems must handle:
- **Ordering:** Ensuring events are processed in a logical or causal sequence.
- **Consensus:** Reaching agreement among nodes on a single data value or state.
- **Replication:** Keeping multiple copies of data consistent across nodes to ensure availability.

## Related Concepts
- [[p2p-systems-security]]
- [[os-security-domains]]
- [[network-security-basics]]
