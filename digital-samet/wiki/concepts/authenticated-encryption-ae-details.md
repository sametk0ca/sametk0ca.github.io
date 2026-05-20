# Authenticated Encryption (AE)

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #symmetric-encryption #aead #integrity

## Overview
Authenticated Encryption (AE) is a symmetric cryptographic scheme that simultaneously provides confidentiality and integrity for plaintext data. In modern applied cryptography, AE is considered the correct tool for almost all symmetric encryption needs.

## 1. AE Security Model
A secure AE scheme must satisfy two properties:
- **IND-CPA (Confidentiality):** An adversary cannot distinguish which of two plaintexts was encrypted.
- **INT-CTXT (Integrity of Ciphertexts):** An adversary cannot create a new ciphertext that decrypts to a valid message.
- **Result:** Together, these imply **IND-CCA** security, the gold standard for encryption.

## 2. Nonce-based AE
Most practical AE schemes require a **Nonce** (Number used once).
- **Responsibility:** The application must ensure that the same (Key, Nonce) pair is *never* used to encrypt two different messages.
- **Reuse Impact:** For many schemes (like AES-GCM), nonce reuse leads to total loss of integrity and partial loss of confidentiality.
- **Misuse Resistance:** Some schemes (e.g., **AES-GCM-SIV**) are designed to fail more gracefully if nonces are reused.

## 3. AEAD (Authenticated Encryption with Associated Data)
An extension where additional data (the Associated Data) is integrity-protected but not encrypted.
- **Example:** A network packet where the header (IP addresses) must be in the clear for routing but needs to be tamper-proof, while the payload is both secret and tamper-proof.

## 4. Generic Constructions
AE can be built by combining an encryption scheme and a MAC:
- **Encrypt-then-MAC (EtM):** The most robust approach. (Encrypt $M$ to get $C$, then MAC $C$). Used in TLS 1.3.
- **MAC-then-Encrypt (MtE):** Historically used in SSL/TLS but led to many vulnerabilities (e.g., Lucky Thirteen).
- **Encrypt-and-MAC (E&M):** Used in SSH. Can leak information if the MAC is deterministic.

## Standard AEAD Schemes
- **AES-GCM:** Widely used (90% of web traffic). Hardware accelerated on Intel/AMD.
- **ChaCha20-Poly1305:** Fast in software, used in mobile apps and WireGuard.

## Related Concepts
- [[symmetric-primitives]]
- [[block-cipher-modes]]
- [[message-authentication-codes]]
