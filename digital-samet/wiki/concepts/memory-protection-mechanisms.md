# Memory Protection Mechanisms

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #memory #isolation #paging

## Overview
Memory protection ensures that a security domain (e.g., a process) cannot access memory assigned to another domain without explicit authorization.

## Core Mechanisms

### 1. Virtual Address Spaces
The OS gives each process the illusion of its own private memory range (from 0 to a maximum address). This abstraction prevents processes from naming and thus accessing each other's memory directly.

### 2. Paging and the MMU
Modern processors use **Paging** to map virtual addresses to physical RAM.
- **MMU (Memory Management Unit):** Hardware that performs the translation.
- **Page Tables:** Hierarchical data structures (managed by the OS) that define the mappings.
- **Protection Bits:** Each entry in a page table has flags (e.g., R/W, Supervisor bit) that the hardware checks on every access.
- **Context Switch:** The OS changes the pointer to the top-level page table (e.g., CR3 register) during a context switch to isolate the new process.

### 3. Segmentation (Historical)
Assigns variable-length segments to processes with specific permissions. While crucial in Multics and x86-32, it is largely obsolete in modern 64-bit architectures, replaced by paging.

## Memory Safety Features
Modern hardware adds extensions to prevent memory errors:
- **Bounds Checking (e.g., Intel MPX):** Prevents array pointer overflows.
- **Memory Tagging (e.g., ARM MTE):** Colors memory regions and pointers with tags; access is granted only if tags match.
- **Memory Protection Keys (MPK):** Provides rapid, user-space controlled permission changes for sets of pages.

## Related Concepts
- [[hardware-isolation-technologies]] (IOMMU, TEE)
- [[os-security-domains]]
- [[hardware-security-vulnerabilities]]
