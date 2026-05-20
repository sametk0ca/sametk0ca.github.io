# Cryptographic Primitives (Hard Problems)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #primitives #hard-problems

## Overview
Cryptographic primitives are the basic building blocks from which all cryptographic schemes and protocols are constructed. They are typically based on mathematical problems believed to be computationally difficult.

## Complexity Theoretic Primitives
Keyed complexity theoretic definitions of functions:
- **PRF (Pseudo-Random Function):** A function that is indistinguishable from a uniform random function by a polynomial-time adversary.
- **PRP (Pseudo-Random Permutation):** A function indistinguishable from a randomly chosen permutation (e.g., Block Ciphers like AES).

## Mathematical Hard Problems

### Classical Primitives
These are the foundation for current public-key cryptography but are vulnerable to large-scale quantum computers:
- **Factoring:** The problem of decomposing a large integer into its prime components (e.g., $N = p \cdot q$ in RSA).
- **RSA Inversion Problem:** Finding $x$ such that $x^e \equiv y \pmod N$ (given $y, e, N$).
- **Discrete Logarithm Problem (DLP):** Inverting the function $x \to g^x$ in a finite field or group.
- **Diffie-Hellman Problem (DHP/DDH):** Distinguishing triples of the form $(g^x, g^y, g^z)$ from $(g^x, g^y, g^{xy})$.

### Post-Quantum Primitives
Mathematical problems believed to be hard even for quantum computers:
- **SVP (Shortest Vector Problem):** Finding the shortest non-zero vector in a high-dimensional lattice.
- **CVP (Closest Vector Problem):** Determining the closest lattice vector to a non-lattice vector.
- **Lattice Reduction:** The best-known class of algorithms (e.g., LLL) for solving these problems.

## Provable Security
A security proof demonstrates that an adversary who can break a cryptographic scheme can also solve the underlying hard problem.

## Related Concepts
- [[cryptographic-security-models]]
- [[post-quantum-cryptography]]
- [[cia-triad]]
