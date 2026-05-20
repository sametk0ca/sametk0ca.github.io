# Forward and Post-Compromise Security

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #keys #security-properties

## Overview
Forward and Post-compromise security are properties that define how a system behaves when long-term secrets or session keys are compromised by an adversary.

## 1. Forward Secrecy (Perfect Forward Secrecy)
A property of key agreement protocols ensuring that a compromise of a party's long-term private keys (e.g., a server's signing key) does *not* compromise the security of past session keys.
- **Mechanism:** Using **Ephemeral Diffie-Hellman** exchanges. Since the session keys are derived from temporary values that are deleted after the session, an attacker who later obtains the long-term key cannot recover those past sessions from intercepted traffic.
- **Importance:** Protects against retrospective decryption by state actors or other powerful entities who record traffic.

## 2. Post-Compromise Security (Backward Security)
Ensures that even if an adversary temporary compromises a system (e.g., learning all current state and keys), the system can eventually heal itself and establish new secure communications that the adversary cannot read.
- **Mechanism:** Frequent key updates or "ratcheting" (as in the Signal Protocol). If the adversary is passive for a period, the parties can exchange new entropy to arrive at a state the adversary no longer knows.

## 3. Comparison
| Property | Focus | Scenario |
| :--- | :--- | :--- |
| **Forward Secrecy** | Past sessions | Long-term key theft in the future. |
| **Post-Compromise Security** | Future sessions | Temporary system intrusion in the past. |

## 4. Cryptographic Brittle Systems
Traditional PKE-based key transport (e.g., using RSA to encrypt a session key) does *not* provide forward secrecy. If the RSA private key is stolen, all past intercepted master keys (and thus session keys) can be recovered.

## Related Concepts
- [[key-agreement-protocols]]
- [[double-ratchet-algorithm]]
- [[key-lifecycle-management]]
