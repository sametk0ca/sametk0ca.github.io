# Byzantine Fault Tolerance (BFT)

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #consensus #bft #byzantine

## Overview
Byzantine Fault Tolerance (BFT) is the property of a distributed system to reach consensus even when some nodes fail arbitrarily or act maliciously (sending different valid messages to different recipients).

## The Byzantine Generals Problem
Proposed by Lamport, this problem illustrates the difficulty of reaching agreement when nodes (generals) can lie or fail to communicate.

## Core Requirements
- **Node Count:** To tolerate $f$ Byzantine failures, a system typically requires at least $3f + 1$ total nodes.
- **Quorums:** Decisions are made by reaching a quorum of honest nodes (usually $2f + 1$).

## PBFT (Practical Byzantine Fault Tolerance)
The first widely used BFT protocol for high-performance systems.
- **Three Phases:** Pre-prepare, Prepare, and Commit.
- **View Change:** If the leader is found to be faulty, a new leader is elected through a view change protocol.

## Security Implications
BFT is critical for:
- **Intrusion Tolerance:** Systems that remain secure even if some parts are compromised.
- **Blockchains:** Reaching agreement on transactions in a trustless environment.
- **Critical Infrastructure:** SCADA and aerospace systems where a single malicious command could be catastrophic.

## Limitations
- **Complexity:** High message overhead ($O(n^2)$) compared to crash-tolerant protocols.
- **Synchrony:** Standard BFT often requires synchronous communication rounds to guarantee termination (related to FLP impossibility).

## Related Concepts
- [[distributed-consensus-and-paxos]]
- [[merkle-trees-and-blockchains]]
- [[cap-theorem]]
