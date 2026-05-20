# OS Security Domains and Isolation

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #security-domains #isolation

## Overview
A security domain (or isolation domain) is an entity that the operating system or hypervisor protects from other entities. Isolation is the core principle for maintaining the confidentiality, integrity, and availability of system resources.

## Key Security Domains
- **Processes:** User-space programs isolated from each other.
- **Kernel:** The most privileged software component, protected from user processes.
- **Hypervisor:** The software that manages and isolates multiple virtual machines.
- **Virtual Machines (VMs):** Isolated environments running an entire operating system.
- **Trusted Execution Environments (TEEs):** Hardware-protected enclaves (e.g., Intel SGX) isolated even from the kernel.

## Shared Resources and Isolation Challenges
Isolation is achieved by managing shared resources:
- **CPU Time:** Managed through scheduling to prevent resource hogging (DoS).
- **Memory:** Managed through address space mappings (MMU/Paging) to prevent unauthorized access.
- **Disk/Files:** Managed through file systems and access controls.

### Side Channels
Despite coarse-grained isolation (e.g., memory paging), security domains often share low-level micro-architectural resources:
- **Caches:** Can leak information about a victim's code execution patterns.
- **TLBs (Translation Lookaside Buffers):** Shared between domains, providing another timing side channel.
- **Memory Deduplication:** A software-level side channel where an OS shares identical memory pages across domains, allowing one domain to detect the presence of data in another.

## Security Principles
- **Principle of Least Common Mechanism:** Every mechanism shared between security domains can become a communication channel that leaks sensitive data.

## Related Concepts
- [[os-design-paradigms]]
- [[hardware-security-vulnerabilities]]
- [[cia-triad]]
