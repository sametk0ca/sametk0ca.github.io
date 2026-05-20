# Post-Quantum Cryptography (PQC)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #quantum-computing #lattices

## Overview
Post-Quantum Cryptography (PQC) aims to develop cryptographic systems that are secure against both quantum and classical computers. It is a proactive response to **Shor's algorithm**, which could easily break current RSA and ECC primitives.

## The Quantum Threat
Quantum computers can solve certain mathematical problems exponentially faster than classical computers:
- **Shor's Algorithm:** Efficiently solves the factoring and discrete logarithm problems, rendering current public-key cryptography insecure.
- **Grover's Algorithm:** Provides a quadratic speedup for unstructured searches, effectively halving the security of symmetric keys (e.g., AES-128 becomes AES-64).

## Prominent PQC Approaches

### 1. Lattice-based Cryptography
The most prominent class of PQC schemes. They are based on hard problems in high-dimensional lattices:
- **Hard Problems:** Shortest Vector Problem (SVP), Closest Vector Problem (CVP), and Learning With Errors (LWE).
- **Benefits:** Generally fast, smaller keys/signatures compared to other PQC classes, and very versatile.

### 2. Isogeny-based Cryptography
Based on finding mappings (isogenies) between elliptic curves.
- **Benefit:** Very small keys.
- **Challenge:** Computationally more expensive than lattice-based schemes.

### 3. Code-based Cryptography
Based on the difficulty of decoding a linear error-correcting code (e.g., McEliece cryptosystem).
- **Benefit:** Well-studied and believed to be very secure.
- **Challenge:** Very large public keys.

### 4. Multivariate Cryptography
Based on solving systems of multivariate quadratic equations over finite fields.

## Standardization: The NIST Era (2024-2026)
As of **April 2026**, the **National Institute of Standards and Technology (NIST)** has moved into the implementation and expansion phase:

### 1. Finalized Standards (2024)
- **FIPS 203 (ML-KEM):** Based on Kyber.
- **FIPS 204 (ML-DSA):** Based on Dilithium.
- **FIPS 205 (SLH-DSA):** Based on SPHINCS+.

### 2. New Developments (2025-2026)
- **HQC (Hamming Quasi-Cyclic):** Selected as the 5th PQC algorithm in 2025 for additional variety in code-based cryptography. Draft standards expected by late 2026.
- **Deprecation Roadmap:** NIST has set a clear timeline. Legacy algorithms like **RSA-2048** and **ECDSA P-256** are set for deprecation by **2030** and will be disallowed by **2035**.

## Transition Strategy (2026 Perspective)
Organizations are now in the "Inventory and Discovery" phase, identifying all quantum-vulnerable systems in preparation for the 2030 deadline.

## Related Concepts
- [[cryptographic-primitives]]
- [[asymmetric-encryption-schemes]]
- [[digital-signatures]]
- [[nist-pqc-2024]]
- [[cyber-forecast-2026]]


