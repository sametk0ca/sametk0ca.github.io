# Digital Signatures in Practice

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #signatures #ecc #rsa

## Overview
While the theoretical goal of digital signatures is unforgeability, the practical application focuses on implementation robustness and efficiency.

## 1. Evolution of Schemes

### RSA-PSS (Probabilistic Signature Scheme)
- **Status:** The modern standard for RSA-based signatures.
- **Benefit:** Comes with a formal security proof and is more robust than the older PKCS#1 v1.5 padding.

### ECDSA (Elliptic Curve Digital Signature Algorithm)
- **Status:** Widely used in mobile devices and blockchains (e.g., Bitcoin, Ethereum).
- **Major Pitfall:** Brittle nonces. If the same random nonce ($k$) is used to sign two different messages, the private key can be trivially recovered.
- **Side-Channel Risk:** Even partial leakage of the nonce bits can lead to key recovery.

### EdDSA (Edwards-curve Digital Signature Algorithm)
- **Status:** Newer standard (e.g., **Ed25519**).
- **Key Feature:** **Deterministic Signing**. It derives the nonce from a hash of the message and the private key, completely eliminating the "nonce reuse" vulnerability.
- **Benefit:** Generally faster and more secure against certain side-channel attacks than ECDSA.

## 2. Certificates and PKI
Digital signatures only prove that a key signed a message. To know *who* owns the key, we use **Digital Certificates**.
- **Certificate Authority (CA):** A trusted third party that signs a binding between a user's identity and their public key.
- **Revocation:** The difficult process of informing everyone that a certificate is no longer valid (using CRLs or OCSP).

## 3. Duplicate Signature Key Selection (DSKS)
A subtle attack where an adversary can find an alternative key pair that validates an existing signature on a specific message. This can be critical in complex protocols that assume a signature uniquely identifies the signer.

## Related Concepts
- [[digital-signatures]]
- [[web-pki-and-https]]
- [[attribute-based-encryption]]
