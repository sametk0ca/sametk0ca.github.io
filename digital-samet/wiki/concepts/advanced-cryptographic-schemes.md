# Advanced Cryptographic Schemes

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #advanced-primitives #anonymity #homomorphic-encryption

## Overview
Beyond standard encryption and signatures, modern cryptography includes advanced schemes with special properties like anonymity, unlinkability, and processing on encrypted data.

## Anonymity Schemes

### 1. Group Signatures
Allows a group member to sign on behalf of the group anonymously.
- **Opener:** A trusted entity who can revoke anonymity to identify a dishonest signer.
- **Usage:** Direct Anonymous Attestation (DAA) in hardware security modules.

### 2. Ring Signatures
Allows a signer to sign a message such that it is from a "ring" of public keys.
- **Difference:** No group manager or "opener" exists. Complete anonymity within the ring.
- **Usage:** Privacy-focused cryptocurrencies (e.g., Monero).

### 3. Blind Signatures
Allows a user to get a message signed by a signer without the signer knowing the message content.
- **Usage:** Electronic voting and digital cash systems.

## Processing Schemes

### 1. Identity-Based Encryption (IBE)
Uses a string (like an email address) as a public key.
- **Key Generation Centre (KGC):** A third party that generates private keys for users.
- **Escrow:** The KGC inherently has the power to decrypt all messages.

### 2. Homomorphic Encryption (HE)
Allows computations to be performed on ciphertexts such that the decrypted result matches the result of operations on the plaintexts.
- **Linearly Homomorphic:** Supports only additions (e.g., Paillier encryption).
- **Fully Homomorphic Encryption (FHE):** Supports both addition and multiplication (any function). Currently computationally expensive.
- **Somewhat Homomorphic Encryption (SHE):** Supports operations of limited complexity/depth.

## Related Concepts
- [[multi-party-computation]]
- [[digital-signatures]]
- [[asymmetric-encryption-schemes]]
