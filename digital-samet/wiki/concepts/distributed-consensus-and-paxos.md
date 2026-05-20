# Distributed Consensus and Paxos

- **Source:** [[ka-distributed-systems]]
- **Tags:** #distributed-systems #consensus #paxos #raft

## Overview
Consensus is the fundamental problem of reaching agreement among a set of distributed processes on a single value, even in the presence of failures.

## Properties of Consensus
For a consensus protocol to be correct, it must satisfy three properties:
1. **Agreement:** Every honest process must agree on the same value.
2. **Validity:** The value agreed upon must have been proposed by an honest process.
3. **Termination:** Every honest process eventually reaches a decision.

## Paxos Protocol
Paxos is a widely used protocol for reaching consensus in asynchronous systems where nodes may crash but do not exhibit malicious (Byzantine) behavior.
- **Phases:**
    1. **Prepare/Promise:** A proposer asks the majority if they can propose a value.
    2. **Accept/Accepted:** If the majority promises, the proposer sends the value for acceptance.
- **Outcome:** Once a majority accepts, the value is "chosen" and becomes the consensus.
- **Robustness:** As long as a majority of nodes are alive, the system can make progress.

## RAFT Protocol
RAFT was developed as a more understandable alternative to Paxos, providing the same safety guarantees.
- **Leader Election:** RAFT uses a strong leader model where one node is elected to manage the replicated log.
- **Log Replication:** The leader accepts client requests and replicates them across the cluster.

## FLP Impossibility
The **FLP Impossibility** result states that in a fully asynchronous system with even a single process failure, it is impossible to guarantee that a deterministic consensus protocol will always terminate. Modern protocols (like Paxos) circumvent this by using timeouts or partial synchrony assumptions.

## Related Concepts
- [[byzantine-fault-tolerance]]
- [[distributed-consistency-models]]
- [[cap-theorem]]
