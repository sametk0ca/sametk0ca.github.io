# Symmetric Primitives

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #symmetric-encryption #hash-functions

## Overview
Symmetric primitives use a single secret key for both encryption and decryption (or generation and verification). The three basic primitives are block ciphers, stream ciphers, and hash functions.

## 1. Block Ciphers
Functions $f: K \times \{0,1\}^b \to \{0,1\}^b$, where $b$ is the block size.
- **Security Assumption:** Acts as a Pseudo-Random Permutation (PRP) for a fixed key.
- **Architectures:**
    - **Feistel Network:** Non-injective S-boxes can be used while maintaining overall invertibility (e.g., DES).
    - **Substitution-Permutation Network (SPN):** Rounds of key addition, permutation, and bijective S-boxes (e.g., AES).
- **Standards:**
    - **DES:** 56-bit key (obsolete).
    - **2DES/3DES:** Uses double or triple DES keys (secure but slow).
    - **AES:** 128-, 192-, or 256-bit key with 128-bit block size. Modern standard with hardware support.

## 2. Stream Ciphers
Produce arbitrary length output bits.
- **Security Assumption:** Acts as a Pseudo-Random Function (PRF) indistinguishable from a random function.
- **Usage:** Counter Mode of block ciphers is commonly used as a stream cipher.
- **Examples:** eStream competition results (e.g., ChaCha20).

## 3. Hash Functions
Map unbounded input domains to fixed-size outputs.
- **Security Properties:**
    - **One-wayness:** Infeasible to invert.
    - **Collision Resistance:** Infeasible to find two inputs with the same output.
    - **Second Preimage Resistance:** Infeasible to find a new input for a given input-output pair.
- **Architectures:**
    - **Merkle-Damgård:** Compression-based iterative construction (e.g., SHA-1, SHA-2). Vulnerable to length extension attacks.
    - **Sponge Construction:** Absorb and squeeze phases using a permutation (e.g., SHA-3/Keccak). Prevents length extension.

## Related Concepts
- [[block-cipher-modes]]
- [[cryptographic-primitives]]
- [[cryptographic-security-models]]
