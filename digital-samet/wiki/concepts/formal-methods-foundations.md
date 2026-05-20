# Formal Methods Foundations

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #mathematics #logic

## Overview
Formal methods are a discipline focused on foundations, methods, and tools based on mathematics and logic for the rigorous development and reasoning about computer systems.

## Core Requirements for Formal Analysis
To formally reason about a system, three elements must be precisely specified:
1. **The System:** Represented at an appropriate level of abstraction (e.g., protocol logic, architectural design, or source code).
2. **The Environment:** Specifically, the **Adversary Model** that captures the capabilities of potential attackers.
3. **The Properties:** Precise statements of what the system should satisfy (e.g., "The secret key is never leaked").

## Levels of Abstraction
- **High-Level Design:** Focuses on logic and protocols (e.g., verifying that a cryptographic protocol is inherently secure).
- **Implementation (Code):** Focuses on finding software bugs (e.g., buffer overflows, race conditions) or proving full functional correctness.
- **Hardware/Low-Level:** Reasoning about physical side channels or micro-architectural isolation.

## Formal Verification vs. Finding Bugs
- **Verification:** Establishing a mathematical proof that a system satisfies a property for *all* possible executions and attacker actions.
- **Bug Finding (Falsification):** Using formal tools to find specific counter-examples (violations) of a security property.

## Related Concepts
- [[adversary-modeling-in-formal-methods]]
- [[hyperproperties-and-trace-properties]]
- [[distributed-systems-fundamental-concepts]]
