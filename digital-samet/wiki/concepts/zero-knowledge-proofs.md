# Zero-Knowledge Proofs (ZKP)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #advanced-protocols #zero-knowledge

## Overview
A Zero-Knowledge Proof is an interactive or non-interactive protocol where a **Prover** demonstrates to a **Verifier** that a statement is true without revealing the secret (witness) that makes it true.

## Core Properties
For a protocol to be zero-knowledge, it must satisfy three conditions:
1. **Completeness:** If the statement is true, an honest Prover can convince an honest Verifier.
2. **Soundness:** If the statement is false, a cheating Prover cannot convince the Verifier (with high probability).
3. **Zero-Knowledge:** The Verifier learns *nothing* other than the fact that the statement is true. This is formally proven using a **Simulator**.

## Proof of Knowledge
A stronger form where the protocol proves that the Prover actually *possesses* the witness. This is demonstrated if a Verifier with "rewinding" capability can extract the witness from the Prover.

## Protocol Structures

### 1. $\Sigma$-Protocols (Sigma Protocols)
A common three-flow interactive structure:
- **Commitment:** Prover sends a value.
- **Challenge:** Verifier sends a random challenge.
- **Response:** Prover sends a response based on the challenge and witness.
- **Example:** Schnorr identification protocol.

### 2. SNARKs (Succinct Non-interactive ARguments of Knowledge)
Modern, non-interactive proofs that are very short and fast to verify.
- **Usage:** Blockchains (e.g., Zcash) for private transactions and scaling.

### 3. Fiat-Shamir Transform
A methodology to convert any interactive $\Sigma$-protocol into a **non-interactive digital signature scheme** by using a hash function to generate the "challenge" instead of a Verifier.

## Related Concepts
- [[authentication-protocols]]
- [[digital-signatures]]
- [[oblivious-transfer]]
