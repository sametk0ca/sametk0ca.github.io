# KEM-DEM Paradigm (Hybrid Encryption)

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #hybrid-encryption #public-key #symmetric-encryption

## Overview
Asymmetric encryption (like RSA) is computationally expensive and restricted in the size of the data it can encrypt. Hybrid encryption solves this by using public-key cryptography to securely transmit a symmetric key, which is then used for bulk data encryption.

## 1. The Components

### KEM (Key Encapsulation Mechanism)
A public-key mechanism that "encapsulates" a symmetric key.
- **Input:** Recipient's public key.
- **Output:** A random symmetric key ($k$) and a ciphertext ($C_k$) that encapsulates it.
- **Goal:** Securely transport the key.

### DEM (Data Encapsulation Mechanism)
A symmetric mechanism that uses the transported key.
- **Input:** The symmetric key ($k$) and the plaintext ($M$).
- **Output:** A ciphertext ($C_m$).
- **Goal:** Efficient bulk encryption.

## 2. Benefits of the Paradigm
- **Efficiency:** The expensive public-key operation is only performed once per session or message.
- **Flexibility:** The DEM can encrypt data of arbitrary length.
- **Modular Security:** If the KEM is IND-CCA secure and the DEM is AE-secure, the resulting hybrid scheme is IND-CCA secure.

## 3. Real-world Examples
- **RSA-KEM:** A simpler and more robust way to use RSA than older padding-based encryption (RSA-OAEP).
- **ECIES:** The Elliptic Curve Integrated Encryption Scheme is inherently a KEM-DEM construction.
- **TLS Handshake:** Modern TLS uses a Diffie-Hellman exchange (functioning like a KEM) to establish session keys for AES-GCM (the DEM).

## Related Concepts
- [[asymmetric-encryption-schemes]]
- [[authenticated-encryption-ae-details]]
- [[digital-signatures-applied]]
