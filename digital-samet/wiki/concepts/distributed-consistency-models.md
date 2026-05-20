# Distributed Consistency Models

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #consistency #replication

## Overview
Consistency models define the rules for the order in which updates to data are seen by different nodes in a distributed system.

## Strong Consistency Models
High coordination, lower availability (prioritizes accuracy).
- **Strict Consistency:** Any read on a data item returns the value of the most recent write. (Difficult to achieve in practice due to network latency).
- **Linearisability:** A stronger version of strict consistency that ensures operations appear instantaneous and follow real-time order.
- **Sequential Consistency:** All processes see the same order of operations, and that order is consistent with the order in which they were issued by each individual process.

## Weak Consistency Models
Low coordination, higher availability (prioritizes responsiveness).
- **Eventual Consistency:** If no new updates are made to a data item, eventually all reads will return the last updated value. Used in large-scale web systems (DNS, Amazon Dynamo).
- **Causal Consistency:** Only operations that are causally related must be seen in the same order by all processes. Unrelated (concurrent) operations may be seen in different orders.
- **Client-Centric Consistency:** Ensures that a single client sees a consistent view of the data, even if different clients see different views (e.g., Read-Your-Writes).

## Trade-offs
Strong consistency requires frequent synchronization (locking), which increases latency and reduces availability in the event of network partitions.

## Related Concepts
- [[cap-theorem]]
- [[distributed-consensus-and-paxos]]
- [[p2p-architectures]]
