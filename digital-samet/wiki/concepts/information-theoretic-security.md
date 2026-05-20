# Information-Theoretic Security

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #security-levels #unbounded-adversary

## Overview
Information-theoretic security (or unconditional security) provides protection against adversaries with unbounded computing power. Unlike computational security, it does not depend on mathematical hard problems (e.g., Factoring).

## Key Primitives

### 1. One-Time Pad (OTP)
The most famous example, providing security even against unbounded adversaries:
- **Operation:** $c = m \oplus k$, where $k$ is a random key the same length as the message $m$.
- **Security:** Achieves IND-PASS (Indistinguishability under passive attack) security.
- **Constraints:**
    - Key must be as long as the message.
    - Key must be used only once (hence "one-time").
    - Key must be truly random and secret.
- **Limitation:** Does not provide IND-CPA security because it is deterministic.

### 2. Secret Sharing
Allows a secret to be distributed among parties such that only specified subsets (access structures) can reconstruct it:
- **Access Structure:** Sets of parties qualified to reconstruct the secret.
- **Adversary Structure:** Sets of parties unqualified to learn anything about the secret.
- **Monotonicity:** If set A can reconstruct, any superset of A can also reconstruct.

## Applications
- Secure communication for extreme confidentiality.
- Foundation for secure multi-party computation (MPC).
- Quantum Key Distribution (QKD) aiming for this level of security.

## Related Concepts
- [[secret-sharing]]
- [[cryptographic-security-models]]
- [[symmetric-primitives]]
