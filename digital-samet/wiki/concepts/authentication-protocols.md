# Authentication Protocols

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #authentication #protocols

## Overview
Authentication protocols are interactive procedures where a **Prover** convinces a **Verifier** of their identity and that they are "online" (to prevent replay attacks).

## Protocol Types

### 1. Encryption-based Protocols
- **Mechanism:** The Verifier encrypts a random nonce $N$ using the Prover's public key (or a shared symmetric key). The Prover decrypts $N$ and returns it.
- **Requirement:** Encryption must be **IND-CCA** secure to protect against active attacks.
- **Goal:** Assures the Prover holds the private/secret key.

### 2. Message Authentication-based Protocols
- **Mechanism:** The Verifier sends a random nonce $N$ in the clear. The Prover signs $N$ (or produces a MAC tag) and returns it.
- **Requirement:** Signatures must be **UF-CMA** secure.
- **Goal:** Assures the Prover has the secret/signing key.

### 3. Zero-Knowledge-based Protocols
- **Mechanism:** Using a $\Sigma$-protocol (Sigma protocol) consisting of three flows: **Commitment**, **Challenge**, and **Response**.
- **Example:** The Schnorr identification protocol, which proves knowledge of a discrete logarithm without revealing the secret itself.
- **Advantage:** No long-term secrets are directly used in calculations, and no information about the secret is leaked.

## Replay Prevention
All modern authentication protocols use a **nonce** (number used once) or a timestamp to ensure the Prover is responding to a fresh challenge, thus preventing replay attacks.

## Related Concepts
- [[zero-knowledge-proofs]]
- [[message-authentication-codes]]
- [[digital-signatures]]
