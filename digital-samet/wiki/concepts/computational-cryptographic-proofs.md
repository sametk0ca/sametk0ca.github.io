# Computational Cryptographic Proofs

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #cryptography #game-based #simulation

## Overview
Unlike symbolic models that treat cryptography as perfect black boxes, computational models treat messages as bit strings and adversaries as probabilistic polynomial-time (PPT) Turing machines.

## Key Paradigms

### 1. Game-based Proofs
Proofs are structured as a sequence of "games" between an adversary and a challenger.
- **Initial Game:** Represents the security goal (e.g., Indistinguishability under CCA).
- **Game Hopping:** Small, mathematically justified transformations that preserve or slightly alter the adversary's advantage.
- **Final Game:** A state where the adversary's advantage is zero or easily bounded by a hard problem.
- **Tools:** **CryptoVerif** (automated process algebraic approach) and **EasyCrypt** (interactive tactic-based approach with SMT support).

### 2. Simulation-based Security
Security is defined by comparing a "Real" system with an "Ideal" system (Ideal Functionality).
- **Universal Composability (UC):** A framework ensuring that if a protocol is secure in isolation, it remains secure when used as a component in a larger distributed system.
- **Mechanism:** A "Simulator" must prove that any attack on the real system can be emulated in the ideal system, making them indistinguishable to an environment.

### 3. Computational Soundness
Bridging the gap between symbolic and computational models. Results that prove if a property holds in the simple symbolic world, it also holds (with high probability) in the complex computational world.

## Tools
- **CertiCrypt/CryptHol:** Foundational approaches implemented in Coq/Isabelle that formalize probabilistic program semantics.
- **EasyCrypt:** Combines relational Hoare logic with SMT solvers for game-based proofs.

## Related Concepts
- [[cryptographic-security-models]]
- [[symbolic-protocol-analysis]]
- [[formal-methods-foundations]]
