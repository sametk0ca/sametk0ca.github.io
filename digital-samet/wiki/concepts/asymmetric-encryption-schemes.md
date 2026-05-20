# Asymmetric Encryption Schemes

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #public-key #encryption

## Overview
Asymmetric encryption (public-key encryption) uses a pair of keys: a public key for encryption ($pk$) and a secret key for decryption ($sk$).

## KEM-DEM Paradigm (Hybrid Encryption)
Since asymmetric encryption is slower than symmetric encryption, the standard approach is to use a hybrid method:
- **KEM (Key Encapsulation Mechanism):** A public-key method to securely transmit a short random key ($k$).
- **DEM (Data Encryption Mechanism):** An efficient symmetric encryption scheme using the key ($k$) to encrypt the actual message ($m$).
- **Goal:** Provides the security of asymmetric encryption with the performance of symmetric encryption.

## Standard Schemes

### 1. RSA
Based on the difficulty of factoring a large modulus $N = pq$.
- **RSA-OAEP (Optimal Asymmetric Encryption Padding):** The modern standard for RSA encryption, providing IND-CCA security using random oracles.
- **RSA-KEM:** A simpler KEM where a random element $r$ is encrypted ($r^e \pmod N$) and the session key is $k = H(r)$.
- **Security:** Requires large keys (e.g., 2048 or 3072 bits) to maintain security.

### 2. Elliptic Curve Cryptography (ECC)
Based on the discrete logarithm problem in elliptic curve groups.
- **ECIES (Elliptic Curve Integrated Encryption Scheme):** A hybrid encryption standard using ECC.
- **Benefit:** Offers the same security level as RSA but with significantly smaller keys (e.g., 256-bit ECC vs 3072-bit RSA). This reduces bandwidth and improves performance.

## Security Goal
The "gold standard" for public-key encryption is **IND-CCA** (Indistinguishability under Chosen Ciphertext Attack).

## Related Concepts
- [[cryptographic-primitives]] (Hard problems)
- [[cryptographic-security-models]]
- [[digital-signatures]]
- [[post-quantum-cryptography]]
