# Adversary Modeling in Formal Methods

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #adversary #modeling

## Overview
Security is only meaningful relative to an adversary model. In formal methods, this involves specifying the capabilities and behaviors of the attacker as part of the formal environment.

## Importance of Explicit Models
A system might be secure against a remote network attacker but vulnerable to an attacker with physical access or the ability to observe side channels. Formal proofs must state exactly which class of attackers they cover.

## Common Adversary Classes
- **Dolev-Yao Adversary:** The standard model for protocol analysis. The attacker controls the network (can intercept, delete, and inject messages) but cannot break cryptographic primitives (e.g., cannot decrypt without the key).
- **Passive vs. Active:**
    - **Passive:** Can only eavesdrop on communications (eavesdropping).
    - **Active:** Can modify messages, impersonate parties, and initiate sessions.
- **Hardware/Physical Adversary:** Can observe power consumption, timing, or use laser pulses to flip bits.
- **Micro-architectural Adversary:** Can exploit shared CPU resources (e.g., caches) to leak data (Spectre/Meltdown).

## Formalizing the Adversary
In formal tools, the adversary is typically modeled as:
- **A set of deduction rules:** Defining what new information an attacker can derive from known data.
- **A process:** A separate parallel process that interacts with the honest participants of the system.

## Related Concepts
- [[formal-methods-foundations]]
- [[cryptographic-security-models]]
- [[hardware-security-vulnerabilities]]
