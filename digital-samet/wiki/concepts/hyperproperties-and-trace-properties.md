# Hyperproperties and Trace Properties

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #properties #semantics

## Overview
In formal methods, security requirements are specified as mathematical properties. A critical distinction exists between properties of individual executions and properties of sets of executions.

## 1. Trace Properties
A trace property is a statement about individual system executions (traces).
- **Definition:** A set of traces. A system satisfies the property if every possible execution of the system is in that set.
- **Security Examples:** 
    - **Authentication:** "For every trace where Bob accepts a message from Alice, Alice must have actually sent it."
    - **Safety:** "No trace ever reaches an error state (e.g., buffer overflow)."

## 2. Hyperproperties
A hyperproperty is a statement about the relationship *between* different executions of a system.
- **Definition:** A property of *sets* of traces.
- **Security Significance:** Many core security concepts like confidentiality and anonymity are hyperproperties because they involve comparing what an attacker sees in one execution versus another.
- **Examples:**
    - **Non-interference:** "For any two executions that differ only in secret inputs, the publicly observable outputs must be identical." (Comparing two traces).
    - **Observational Equivalence:** The attacker cannot distinguish between two different system configurations.

## Why the Distinction Matters?
- **Tooling:** Traditional model checkers (like SPIN) are designed for trace properties. Verifying hyperproperties often requires specialized tools or techniques (like **Self-Composition**, where two copies of the system are analyzed in parallel).
- **Refinement:** A system that satisfies a trace property will still satisfy it after refinement (making it more deterministic). However, refinement can break hyperproperties (e.g., removing non-determinism might leak secrets via timing).

## Related Concepts
- [[formal-methods-foundations]]
- [[adversary-modeling-in-formal-methods]]
- [[information-theoretic-security]]
