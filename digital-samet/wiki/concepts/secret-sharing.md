# Secret Sharing

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #secret-sharing #shirley

## Overview
Secret sharing schemes allow a secret to be distributed among a set of parties such that only a given subset (qualified set) can reconstruct the secret, while unqualified sets learn nothing.

## Threshold Secret Sharing
A threshold structure (or $(t, n)$ scheme) allows any subset of $t+1$ parties to reconstruct the secret, while any subset of $t$ parties learns nothing. $t$ is the "threshold".

### 1. Shamir's Secret Sharing Scheme
Based on polynomial interpolation over a finite field $F_p$:
- **Dealing:** Select a random polynomial $f(X)$ of degree $t$ where the constant coefficient is the secret $s$ ($f(0) = s$).
- **Shares:** Share $s_i = f(i) \pmod p$ is given to party $i$.
- **Reconstruction:** Using Lagrange interpolation with $t+1$ shares to recover $f(X)$ and thus $s$.
- **Error Correction:**
    - If $t < n/2$, it can detect invalid shares ($Q2$ structure).
    - If $t < n/3$, it can correct invalid shares ($Q3$ structure).

### 2. Replicated Secret Sharing
A popular scheme for any monotone access structure. It represents the access formula as a boolean formula and replaces AND with addition (+) and OR with a new secret.

## Adversary Structures ($Q_i$)
- **Qi Structure:** No set of $i$ unqualified sets can have the full set of players as their union.
- **Importance:** Crucial for Secure Multi-Party Computation (MPC).
    - $Q2$ ($t < n/2$) enables error detection.
    - $Q3$ ($t < n/3$) enables error correction.

## Related Concepts
- [[information-theoretic-security]]
- [[cryptographic-security-models]]
- [[multi-party-computation]]
