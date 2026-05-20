# Oblivious Transfer (OT)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #advanced-protocols #oblivious-transfer

## Overview
Oblivious Transfer (OT) is a fundamental cryptographic primitive between a **Sender** and a **Receiver** that enables selective but private data access.

## Types of OT

### 1-out-of-2 OT
The basic form of the protocol:
- **Sender:** Has two messages $m_0$ and $m_1$.
- **Receiver:** Has a selection bit $b \in \{0, 1\}$.
- **Security Goals:**
    - **Receiver Privacy:** The Sender learns nothing about the selection bit $b$.
    - **Sender Privacy:** The Receiver learns only the selected message $m_b$, and gains no information about the other message $m_{1-b}$.

### n-out-of-m OT
Extensions of the basic protocol where the Receiver can choose $n$ messages from a set of $m$.

## Implementations
OT can be implemented using mathematical hard problems (e.g., Diffie-Hellman in elliptic curve groups).

## Applications
OT is a critical building block for many advanced cryptographic protocols:
- **Secure Multi-Party Computation (MPC):** Used to evaluate functions on private data.
- **Garbled Circuits:** Fundamental component for the evaluation of a circuit on two private inputs.
- **Private Information Retrieval (PIR):** Retrieving data from a server without the server knowing which data was requested.

## Related Concepts
- [[multi-party-computation]]
- [[zero-knowledge-proofs]]
- [[cryptographic-primitives]]
