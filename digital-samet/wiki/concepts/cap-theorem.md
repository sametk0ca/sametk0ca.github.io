# CAP Theorem

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #consistency #availability #partition-tolerance

## Overview
The CAP theorem (also known as Brewer's theorem) states that a distributed data store can simultaneously provide at most two out of the following three guarantees:

1. **Consistency (C):** Every read receives the most recent write or an error.
2. **Availability (A):** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
3. **Partition Tolerance (P):** The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

## The Choice
In the event of a network partition (P), a system must choose between:
- **CP (Consistency/Partition Tolerance):** Cancel the operation and decrease availability but ensure data consistency.
- **AP (Availability/Partition Tolerance):** Proceed with the operation and provide availability but risk inconsistency.

*Note: CA systems (Consistency/Availability without Partition Tolerance) are effectively impossible in large-scale distributed systems because network partitions are inevitable.*

## Security Significance
- **Integrity Attacks:** Attackers may induce network partitions to force a system into an AP state where they can exploit eventual consistency to perform double-spending or other fraudulent activities.
- **Availability Attacks:** Inducing partitions to force a CP system into a state of total unavailability.

## Related Concepts
- [[distributed-consistency-models]]
- [[distributed-consensus-and-paxos]]
- [[p2p-architectures]]
