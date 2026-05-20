# Key Lifecycle Management

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #keys #governance

## Overview
A cryptographic key is not a static object but has a lifecycle from its initial generation to its final destruction. Effective key management must address every stage of this cycle.

## Stages of the Lifecycle

### 1. Generation
Keys must be generated using high-entropy, cryptographically secure random bit sources (TRNG/PRNG). Weak randomness is a common cause of total system failure.

### 2. Distribution / Transportation
Moving keys from the point of generation to the point of use. 
- **Methods:** Physical couriers, manual entry (for low-value), or encrypted transport using Key Encryption Keys (KEKs).

### 3. Storage
Protecting keys at rest.
- **Software:** Using OS access controls and process isolation.
- **Hardware (Best Practice):** Using **HSMs (Hardware Security Modules)**, **TPMs**, or **Smartcards**. These devices ensure keys never leave the hardware in plaintext.

### 4. Usage
Applying the key to data. Usage should be limited by:
- **Assurance of Purpose:** A key should only be used for one specific algorithm/task (e.g., signing only, never also for encryption).
- **Usage Limits:** Cryptographic analysis determines how much data a single key can safely encrypt before it must be replaced.

### 5. Refreshing / Updating
Regularly replacing keys to limit the impact of a potential compromise and to adhere to security bounds.

### 6. Revocation
Invalidating a key before its scheduled expiry if it is suspected of being compromised. This is one of the most difficult stages to manage in large-scale systems.

### 7. Archival
Storing keys for long periods to allow for the decryption of historical data. Requires its own management layer.

### 8. Destruction
Ensuring the key is unrecoverable at the end of its life. Involves physically destroying hardware or using "zeroization" (overwriting the memory locations).

## Related Concepts
- [[key-derivation-functions]]
- [[forward-and-post-compromise-security]]
- [[hardware-isolation-technologies]]
