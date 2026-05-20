# Multi-Party Computation (MPC)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #advanced-protocols #mpc #privacy

## Overview
Secure Multi-Party Computation (MPC) allows a set of parties to jointly compute a function $f(x_1, \dots, x_n)$ over their private inputs $x_i$, without revealing anything other than the result.

## Adversary Models
- **Corruption Type:**
    - **Static:** The set of corrupt parties is fixed before the protocol starts.
    - **Adaptive:** The adversary can choose which parties to corrupt during execution.
- **Security Level:**
    - **Passive (Semi-honest):** Parties follow the protocol but try to learn extra information from their views.
    - **Active (Malicious):** Parties can arbitrarily deviate from the protocol.
- **Robustness:**
    - **Robust MPC:** Honest parties receive the correct output even if some parties cheat.
    - **MPC with Abort:** If cheating is detected, the protocol terminates without giving output to anyone.

## Key Approaches

### 1. Information-Theoretic (Secret Sharing)
Based on distributing shares of inputs (e.g., Shamir's scheme).
- **Passive Security:** Possible if $t < n/2$ (majority honest).
- **Active Security:** Possible if $t < n/3$.

### 2. Computational (Garbled Circuits)
Used for two-party computation (2PC).
- **Yao's Garbled Circuits:** A "Creator" encrypts a boolean circuit gate-by-gate, and an "Evaluator" computes it using keys obtained via **Oblivious Transfer**.

## Implementation Phases
Modern MPC often uses a two-phase approach:
1. **Offline Phase:** Precomputes function-independent data (using expensive public-key cryptography).
2. **Online Phase:** Performs the actual computation quickly using function-dependent data and cheap information-theoretic primitives.

## Related Concepts
- [[oblivious-transfer]]
- [[secret-sharing]]
- [[information-theoretic-security]]
