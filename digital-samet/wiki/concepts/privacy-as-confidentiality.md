---
concept: Privacy as Confidentiality
source: [[ka-privacy-and-online-rights]]
tags: [concept, privacy, confidentiality, encryption, cybok]
---

# Concept: Privacy as Confidentiality

## Overview
This paradigm focuses on hiding information from adversaries. It is divided into "Hard Privacy" (cryptographic guarantees) and "Soft Privacy" (obfuscation and inference control).

## 1. Data Confidentiality (Hard Privacy)
Uses advanced cryptography to protect data in transit and during processing.

### A. Protecting Data in Transit (E2EE)
- **End-to-End Encryption (E2EE)**: Ensures confidentiality between origin and destination. Intermediaries cannot access content.
- **Protocols**: TLS, PGP, and the **Signal Protocol** (used by Signal, WhatsApp, etc.).
- **Properties**: Forward secrecy (compromise of today's keys doesn't reveal yesterday's messages) and deniability (OTR protocol).

### B. Protecting Data During Processing
- **Outsourcing**: Computing on encrypted data without decrypting it.
    - **Homomorphic Encryption**: Allows operations on ciphertexts. High computational cost.
    - **Private Information Retrieval (PIR)**: Querying a database without revealing which record is accessed.
- **Collaborative Computation**: Multi-Party Computation (MPC) allows parties to compute a function over their combined inputs while keeping those inputs private.
- **Zero-Knowledge Proofs (ZKP)**: Proving that an input is valid without revealing the input itself.

### C. Private Authentication & Payments
- **Anonymous Credentials (ABCs)**: Proving possession of attributes (e.g., "I am over 18") without revealing identity. Provides **unlinkability**.
- **Private Payments**: Systems like **Zerocash** use ZK-SNARKs to prove funds exist and transactions are valid without revealing amounts or participants.

## 2. Obfuscation & Inference Control (Soft Privacy)
Relaxes strict confidentiality to limit the information an adversary can infer.
- **Anonymization**: Removing direct identifiers. (Note: Often insufficient against re-identification attacks).
- **k-anonymity**: Ensuring each individual is indistinguishable from at least $k-1$ others in a dataset.
- **Differential Privacy**: Adding noise to data so that the presence or absence of an individual's record does not significantly change the result of a query.

## 3. Metadata Protection
Metadata (e.g., who you talk to, when, for how long) can be more revealing than content.
- **Tor (The Onion Router)**: Layers of encryption to hide the path of a packet.
- **Mix Networks**: Batching and reordering packets to prevent timing analysis.

## References
- [[ka-privacy-and-online-rights]]
- [[privacy-paradigms]]
- [[cryptography|KA: Cryptography]]
