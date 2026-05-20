# Side-Channel Formal Analysis

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #side-channel #leakage #entropy

## Overview
Formal analysis of side-channels aims to detect and quantify unintended information leaks (timing, power consumption, etc.) from hardware or software.

## Theoretical Basis
- **Non-interference:** A property stating that secret inputs do not affect observable outputs. If non-interference holds, there are no side-channels.
- **Quantitative Leakage:** Since full non-interference is often impossible (e.g., login success/failure leaks 1 bit), formal methods measure the *amount* of leakage using **Information Theory**.

## Metrics
- **Entropy (Shannon/Min-entropy):** Measuring the adversary's uncertainty about the secret.
- **Adaptive Adversaries:** Models that consider attackers who choose their inputs based on previous observations.

## Tools and Techniques
- **Abstract Interpretation:** Used by tools like **Cache Audit** to track possible cache states and quantify timing leaks from cache hits/misses.
- **Constant-time Generation:** Using formal models to ensure all execution paths take the same time (e.g., ensuring branches are independent of secret data).
- **Taint Tracking:** Propagating secret labels to identify instructions that branch or access memory based on those secrets.

## Limitations
Current formal models often lack the micro-architectural detail to capture leaks from **speculative execution** (Spectre) or **out-of-order execution** (Meltdown) in a generalized way.

## Related Concepts
- [[hyperproperties-and-trace-properties]]
- [[hardware-security-vulnerabilities]]
- [[hardware-formal-verification]]
