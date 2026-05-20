# Double Ratchet Algorithm

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #secure-messaging #keys #ratcheting

## Overview
The Double Ratchet algorithm is used by end-to-end encrypted messaging services (like Signal and WhatsApp) to provide secure communication between two parties in an asynchronous environment.

## 1. Key Objectives
- **Forward Secrecy:** Protecting past messages if keys are compromised in the future.
- **Post-Compromise Security:** Recovering security after keys were compromised in the past.
- **Asynchronicity:** Working even when both parties are never online at the same time.

## 2. The Two Ratchets

### Diffie-Hellman (DH) Ratchet
- **Mechanism:** Every time a party sends a new message, they include a fresh DH public key. When they receive a reply, they perform a DH exchange to update the "root key."
- **Benefit:** Provides **Post-Compromise Security**. If an attacker learns all keys but the parties perform a new DH exchange that the attacker cannot intercept, the attacker is locked out.

### Symmetric Key (KDF) Ratchet
- **Mechanism:** For every message sent or received between DH updates, the "chaining key" is passed through a KDF to produce a message key and a new chaining key.
- **Benefit:** Provides **Forward Secrecy**. Once a message key is used and deleted, it cannot be recovered even if the current chaining key is compromised.

## 3. Composition
The "Double Ratchet" name comes from the combination of these two techniques.
- The DH Ratchet provides new entropy for the root of the symmetric key chains.
- The Symmetric Ratchet ensures each individual message has a unique, short-lived key.

## 4. Implementation Details
- **Encryption:** Signal typically uses AES-256 in CBC mode with HMAC-SHA256 (Encrypt-then-MAC) for individual messages.
- **Synchronicity:** Caches of recent chaining keys are used to handle out-of-order or lost messages.

## Related Concepts
- [[forward-and-post-compromise-security]]
- [[key-agreement-protocols]]
- [[federated-identity-protocols]]
