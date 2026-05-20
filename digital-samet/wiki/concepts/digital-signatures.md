# Digital Signatures

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #public-key #signatures #non-repudiation

## Overview
A digital signature is a mathematical scheme for demonstrating the authenticity of digital messages or documents. It provides authentication, integrity, and **non-repudiation** (the signer cannot deny the signature).

## Key Characteristics
- **Public/Private Keys:** The signer uses their secret key ($sk$) to generate a signature ($\sigma$), while the verifier uses the signer's public key ($pk$) to verify it.
- **Verification:** Testing the signature against the message and the public key.
- **Goal:** Adherence to **UF-CMA** (Unforgeability under Chosen Message Attack).

## Standard Schemes

### 1. RSA
RSA signatures are based on the RSA primitive.
- **RSA-PSS (Probabilistic Signature Scheme):** The modern, standard method for signing with RSA. It uses random oracles and probabilistic padding to provide high security.
- **PKCS#1 v1.5:** An older, deterministic signature standard with no formal proof of security. RSA-PSS is generally preferred.

### 2. Elliptic Curve DSA (ECDSA)
The elliptic curve variant of the Digital Signature Algorithm (DSA).
- **Benefit:** Much shorter signatures and keys than RSA for the same security level.

## Related Concepts
- **Digital Certificate:** A signed statement by a **Certificate Authority (CA)** that binds an entity to its public key. This is a foundational element of the **Public-Key Infrastructure (PKI)**.

## Related Concepts
- [[asymmetric-encryption-schemes]]
- [[message-authentication-codes]]
- [[cryptographic-security-models]]
