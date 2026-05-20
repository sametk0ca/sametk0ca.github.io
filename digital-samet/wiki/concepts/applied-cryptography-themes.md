# Applied Cryptography Themes

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #engineering #philosophy

## Overview
Applied cryptography is not just about mathematical proofs; it's about the robust integration of cryptographic primitives into complex systems. Several high-level themes define the field.

## 1. The Implementation Gap
Vulnerabilities rarely arise from mathematical breaks in standardized algorithms (like AES). Instead, they occur in the gaps:
- **Theory vs. Practice:** Assumptions in proofs (e.g., random oracles) might not hold in reality.
- **Design vs. Implementation:** Cryptographic libraries might have bugs or leak information via side-channels.
- **Library vs. Use:** Developers who are not crypto-experts often misuse library APIs.

## 2. Brittleness
Cryptography is inherently brittle. A single bit difference in a key or a small flaw in a padding scheme (e.g., PKCS#1 v1.5) can lead to a complete security failure. Unlike other engineering disciplines, cryptographic systems rarely "fail gracefully."

## 3. Data States (The Triumvirate)
Cryptography is applied differently depending on the state of the data:
- **Data in Transit:** Secure communication protocols (e.g., TLS, IPsec). Mature and standardized.
- **Data at Rest:** Secure storage (e.g., full disk encryption). Closely related to data in transit (communication across time).
- **Data under Computation:** Privacy-preserving techniques (e.g., MPC, Homomorphic Encryption). Emergent and computationally expensive.

## 4. The Political Dimension (The Crypto Wars)
Cryptography is a "dual-use" technology. It protects human rights and privacy but can also be used by malicious actors. This lead to ongoing conflicts between governments (desiring "exceptional access" or backdoors) and the technical community (emphasizing that backdoors weaken security for everyone).

## Related Concepts
- [[cryptographic-implementation-security]]
- [[cryptographic-agility-and-opinionated-systems]]
- [[multi-party-computation]]
