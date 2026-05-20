# Key Agreement Protocols

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #keys #protocols

## Overview
A key agreement protocol allows two or more parties to agree on a secret key to be used for subsequent secure communications.

## Security Requirements
- **Indistinguishability:** The derived key must be indistinguishable from a random string for an adversary.
- **Mutual Authentication:** Assurance for each party that only the intended peer has the key.
- **Mutual/Implicit Key Confirmation:** Assurance that both parties have received the *same* secret key.

## Advanced Security Properties

### 1. Forward Secrecy
The compromise of a party's long-term secret in the future does *not* compromise the security of past session keys derived using this protocol. This ensures that past conversations remain secure even if keys are later stolen.

### 2. Unknown Key Share Security
Prevents a scenario where Alice believes she is sharing a key with Bob, while Bob believes he is sharing a key with Charlie (an attacker). This is critical in preventing "man-in-the-middle" attacks.

## Common Protocol Variants

### 1. Key Transport
A party generates a random key and encrypts it using the other's public key (e.g., traditional RSA-based TLS 1.2).
- **Drawback:** Usually lacks forward secrecy.

### 2. Diffie-Hellman (DH) Key Agreement
Parties exchange public parameters ($g^a, g^b$) to arrive at a shared secret ($g^{ab}$).
- **Benefit:** Offers **Forward Secrecy**.
- **Requirement:** Must be signed or used within an authenticated structure to prevent man-in-the-middle attacks.
- **STS (Station-to-Station) Protocol:** An authenticated version of DH that uses encryption and signatures on the entire transcript to provide mutual authentication and prevent unknown key share attacks.

## Usage in Modern Systems
- **TLS 1.3:** The current web standard which *only* supports forward-secure key exchange (Diffie-Hellman variants).

## Related Concepts
- [[cryptographic-primitives]] (Diffie-Hellman)
- [[asymmetric-encryption-schemes]]
- [[authentication-protocols]]
