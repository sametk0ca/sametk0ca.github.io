# Cryptographic Security Models

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #security-models #provable-security

## Overview
Modern cryptography relies on "Provable Security," a methodology for defining and understanding the security of cryptographic constructions through formal models and mathematical proofs.

## Methodology
The design process follows three main steps:
1. **Define Syntax:** Specify the algorithms (KeyGen, Enc/Dec, MAC/Verify) and their input/output behaviors.
2. **Specify Security Goals & Capabilities:** Define the adversary's objective and their available resources (oracles).
3. **Formal Security Proof:** Prove that breaking the scheme implies solving a known "hard problem" (e.g., Factoring).

## Security Goals
Common goals include:
- **IND (Indistinguishability):** The primary goal for modern encryption. An adversary cannot distinguish which of two chosen plaintexts was encrypted.
- **UF (Universal Forgery):** The primary goal for signatures and MACs. An adversary cannot create a valid message-signature/tag pair.
- **OW (One-Wayness):** A basic goal where an adversary cannot recover the plaintext from a ciphertext.

## Adversary Capabilities (Oracles)
Adversaries are categorized by the information or access they possess:
- **PASS (Passive Attack):** The adversary only observes communications.
- **CPA (Chosen Plaintext Attack):** The adversary can obtain ciphertexts for arbitrary plaintexts of their choice.
- **CCA (Chosen Ciphertext Attack):** The adversary can obtain decryptions of arbitrary ciphertexts (excluding the challenge ciphertext).
- **CMA (Chosen Message Attack):** The adversary can obtain signatures/MAC tags for arbitrary messages.

## Security Game
A security definition is framed as a "game" between a challenger and an adversary. The adversary "wins" if they achieve their goal with an "advantage" (probability higher than random guessing). A scheme is considered secure if this advantage is negligible for all polynomial-time adversaries.

## Related Concepts
- [[cryptographic-primitives]]
- [[cia-triad]]
- [[post-quantum-cryptography]]
