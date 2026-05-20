# OS Hardening Techniques

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #hardening #exploit-mitigation #aslr #cfi

## Overview
OS hardening involves applying various defensive layers to mitigate the impact of software and hardware vulnerabilities that cannot be easily fixed.

## Core Mitigation Strategies

### 1. Information Hiding
- **ASLR (Address Space Layout Randomization):** Randomizes the base addresses of code, stack, and heap.
- **KASLR (Kernel ASLR):** Randomizes the location of the kernel code in memory to prevent attackers from finding exploit targets.

### 2. Control-Flow Restrictions
- **CFI (Control-Flow Integrity):** Ensures that the program execution follows a legitimate, static control-flow graph (e.g., return instructions only go back to call sites).
- **Hardware Support:** Features like **Intel CET (Shadow Stacks)** and **ARM Pointer Authentication (PAC)** help enforce CFI with low overhead.

### 3. Memory Partitioning
- **W⊕X (Write XOR Execute):** Ensures that a memory page can be either writable or executable, but never both. This prevents code injection attacks. Known as **DEP (Data Execution Prevention)** in Windows and **NX/XD** in CPUs.
- **SMEP (Supervisor Mode Execution Protection):** Prevents the kernel from executing code in user-space pages.
- **SMAP (Supervisor Mode Access Protection):** Prevents the kernel from reading/writing user-space data without explicit authorization.

### 4. Kernel Isolation
- **KPTI (Kernel Page Table Isolation):** Mitigates side-channel attacks like **Meltdown** by maintaining separate page table mappings for user-space and the kernel, preventing speculative leaks.

## Anomaly Detection
Detecting suspicious patterns of execution or resource usage that deviate from normal system behavior.

## Related Concepts
- [[hardware-security-vulnerabilities]]
- [[memory-protection-mechanisms]]
- [[os-protection-rings]]
