# Cryptographic Agility and Opinionated Systems

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #design #standards

## Overview
Protocols and systems must decide how much flexibility they allow in choosing cryptographic algorithms. This represents a trade-off between interoperability and security simplicity.

## 1. Cryptographic Agility
The ability of a system to easily switch from one algorithm to another (e.g., from RSA to ECC, or from SHA-1 to SHA-256).
- **Motivation:** Essential for responding to cryptanalytic breakthroughs or adopting more efficient technologies.
- **Mechanism:** Often implemented via "Cipher Suite Negotiation" where the client and server agree on a mutually supported set of algorithms.
- **Risks:** 
    - **Complexity:** Agility adds code paths, increasing the chance of bugs.
    - **Downgrade Attacks:** An active attacker may force the parties to choose the weakest algorithm both support (e.g., Logjam, FREAK).

## 2. Cryptographically Opinionated Systems
Systems that hard-code a single, carefully selected set of algorithms and do not support negotiation.
- **Example:** **WireGuard** (VPN protocol) uses a single set of primitives (ChaCha20-Poly1305, Curve25519, BLAKE2s).
- **Benefits:** 
    - **Simplicity:** Much smaller codebase and attack surface.
    - **Security:** Eliminates downgrade attacks entirely.
- **Risks:** If one of the chosen primitives is broken, the entire system must be updated and redeployed.

## 3. The Middle Way
Modern standards like **TLS 1.3** attempt a middle ground: support agility but strictly limit the allowed cipher suites to only those that are currently considered highly secure, removing legacy and broken options (like RC4 or CBC with padding).

## Related Concepts
- [[applied-cryptography-themes]]
- [[network-security-basics]]
- [[post-quantum-cryptography]]
