# Software Security Mitigation Techniques

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #mitigation #aslr #dep #cfi

## Overview
Mitigation techniques aim to limit the impact of vulnerabilities that cannot be prevented or detected during development. They are typically implemented in the execution infrastructure (OS, CPU).

## Core Mechanisms

### 1. Address Space Layout Randomization (ASLR)
Randomizes the base addresses of key memory segments (stack, heap, code).
- **Goal:** Makes it difficult for an attacker to predict the location of target code or data (e.g., gadgets for ROP).
- **Effectiveness:** Depends on the amount of entropy (randomness) provided by the OS.

### 2. Data Execution Prevention (DEP / NX / W⊕X)
Ensures that a memory page can be either writable or executable, but not both.
- **Goal:** Prevents "Shellcode" (direct code injection) where an attacker writes code to a buffer and then jumps to it.
- **Counter-measure:** Attackers bypass DEP using **Code-Reuse Attacks** (like ROP).

### 3. Control-Flow Integrity (CFI)
Monitors the execution flow of a program to ensure it follows a predefined, legitimate control-flow graph.
- **Goal:** Detects and stops code-reuse attacks by ensuring returns only go to call sites and indirect jumps only go to valid function entries.
- **Hardware Support:** Intel CET (Control-Flow Enforcement Technology) and ARM PAC (Pointer Authentication Code).

### 4. Stack Canaries (Cookies)
Small random values placed on the stack before the return address.
- **Mechanism:** The kernel checks if the canary has been modified before the function returns. If it has (indicating a buffer overflow), the program is terminated.

## Isolation Techniques
- **Sandboxing:** Running software in a restricted environment with limited resource access (e.g., Chrome renderer process).
- **Compartmentalization:** Dividing an application into smaller pieces, each with the minimum privileges required (Principle of Least Privilege).

## Related Concepts
- [[os-hardening-techniques]]
- [[memory-management-vulnerabilities]]
- [[capability-based-security]]
