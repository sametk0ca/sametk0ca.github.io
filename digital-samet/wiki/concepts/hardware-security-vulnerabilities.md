# Hardware Security Vulnerabilities

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #hardware #vulnerabilities #side-channels

## Overview
Modern operating systems face threats from vulnerabilities at the hardware-software interface. These vulnerabilities are often inherent to the performance-oriented design of modern CPUs and DRAM.

## Micro-Architectural Attacks
These attacks exploit the underlying implementation (micro-architecture) of a processor, bypassing traditional software-level security domains.

### 1. Speculative Execution Attacks
CPUs speculatively execute instructions before knowing if they should be executed (e.g., branch prediction).
- **Spectre:** Traces of squashed speculative execution are left in micro-architectural state (caches), allowing data extraction across security domains.
- **Meltdown:** Allows a user process to read kernel memory directly by exploiting race conditions during speculative execution (especially on certain Intel CPUs).
- **Foreshadow:** Exploits speculative access to the L1 cache when memory pages are marked as not present.
- **RIDL (Rogue In-Flight Data Load):** Exploits temporary micro-architectural buffers (fill buffers, store buffers) that leak data from other domains regardless of page tables.

### 2. DRAM Vulnerabilities
- **Rowhammer:** A bit-flipping attack in DRAM. Rapidly accessing one row of memory (hammering) causes electrical interference that can flip bits in adjacent rows, even if they belong to different security domains. This can be used to corrupt kernel data or page tables.

## Operating System Mitigations
OS designers must implement complex workarounds for these hardware flaws:
- **KPTI (Kernel Page Table Isolation):** Mitigating Meltdown by maintaining separate page tables for user-space and kernel.
- **Cache Flushing:** Clearing micro-architectural buffers during context switches.
- **Serialization:** Using special instructions (e.g., LFENCE) to stop speculative execution across certain branches.
- **Disabling Features:** Turning off insecure optimizations like memory deduplication or hyper-threading (SMT) where necessary.

## Related Concepts
- [[os-security-domains]]
- [[os-hardening-techniques]]
- [[cryptographic-implementation-security]]
