# Block Cipher Modes of Operation

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #symmetric-encryption #modes

## Overview
A block cipher alone is not an encryption algorithm. To encrypt messages of arbitrary length, a block cipher must be used within a "mode of operation."

## Traditional Modes

### 1. CBC (Cipher Block Chaining)
Each block of plaintext is XORed with the previous ciphertext block before being encrypted.
- **Initial Vector (IV):** A random value is XORed with the first plaintext block to ensure uniqueness.
- **Dependency:** Ciphertext blocks depend on all preceding plaintext blocks.
- **Drawback:** Encryption is sequential and cannot be parallelized.

### 2. ECB (Electronic Codebook)
Each block is encrypted independently with the same key.
- **Vulnerability:** Identical plaintext blocks result in identical ciphertext blocks, leaking structural information. **Rarely used and generally considered insecure.**

### 3. OFB/CFB (Output/Cipher Feedback)
Older modes used for stream-like encryption, largely replaced by CTR.

## Modern Modes

### 1. CTR (Counter Mode)
Turns a block cipher into a stream cipher.
- **Operation:** A counter (IV/Nonce + Counter value) is encrypted, and the result is XORed with the plaintext.
- **Benefit:** Highly parallelizable for both encryption and decryption. Allows random access to ciphertext.

### 2. GCM (Galois/Counter Mode)
An "Authenticated Encryption with Associated Data" (AEAD) mode.
- **Security:** Provides both confidentiality (CTR) and integrity/authentication (Galois field multiplication).
- **Efficiency:** Parallelizable and widely used in modern protocols (e.g., TLS 1.3).

## Usage Note
Always prefer authenticated encryption modes (like GCM) over simple encryption modes (like CBC or CTR) to protect against active attackers who might modify the ciphertext.

## Related Concepts
- [[symmetric-primitives]]
- [[cryptographic-security-models]]
- [[cia-triad]]
