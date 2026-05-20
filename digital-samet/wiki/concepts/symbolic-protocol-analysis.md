# Symbolic Protocol Analysis

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #protocols #dolev-yao #tamarin

## Overview
Symbolic analysis models cryptographic protocols by treating messages as terms in a term algebra and cryptography as idealized functions.

## The Dolev-Yao Adversary
The standard model for symbolic analysis:
- **Capabilities:** The attacker is an active network controller who can intercept, block, and inject any message.
- **Assumptions:** Cryptography is "perfect"—the attacker cannot decrypt without the key, find collisions, or perform cryptanalysis unless specified by algebraic rules (e.g., Diffie-Hellman properties).

## Key Formalisms
- **Transition Systems:** Protocols are modeled as state machines with an unbounded number of concurrent sessions.
- **Multiset Rewriting:** Used by tools like Tamarin to manage complex state transitions and persistent data.
- **Applied Pi Calculus:** A process calculus used by ProVerif to model interacting agents and channels.

## Properties Analyzed
- **Secrecy:** The adversary never learns a sensitive term (e.g., a session key).
- **Authentication:** Ensuring that Bob only accepts a session if Alice actually initiated it (Correspondence properties).
- **Observational Equivalence:** Used for privacy properties (Anonymity, Unlinkability).

## State-of-the-Art Tools
- **ProVerif:** Automated, uses Horn clause resolution. Scales well for many protocols but uses abstractions that can lead to false attacks.
- **Tamarin:** Supports stateful protocols and custom algebraic theories (DH, XOR). Can be interactive for complex proofs.
- **Isabelle/HOL:** Used for inductive proofs of protocols like TLS 1.3.

## Related Concepts
- [[adversary-modeling-in-formal-methods]]
- [[hyperproperties-and-trace-properties]]
- [[cryptographic-security-models]]
