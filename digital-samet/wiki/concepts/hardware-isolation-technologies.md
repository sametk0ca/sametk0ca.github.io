# Hardware Isolation Technologies

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #hardware #isolation #tee #iommu

## Overview
Beyond standard CPU ring protections and paging, modern hardware provides specialized technologies to isolate peripheral devices and extremely sensitive code.

## 1. IOMMU (Input-Output Memory Management Unit)
Standard MMUs protect the CPU from processes. The **IOMMU** protects the system from devices.
- **Function:** Maps device-visible virtual addresses to physical addresses for Direct Memory Access (DMA).
- **Security Goal:** Prevents malicious or buggy peripheral devices (e.g., PCIe cards, Thunderbolt devices) from reading or overwriting arbitrary RAM.
- **Virtualized Use:** Allows a hypervisor to safely assign a physical device directly to a specific Virtual Machine (VM).

## 2. Trusted Execution Environments (TEE) / Enclaves
Hardware-level isolation that protects code and data even from a compromised OS kernel or hypervisor.
- **Intel SGX (Software Guard Extensions):** Allows an application to create an "enclave"—a protected region of memory. Enclave memory is encrypted while in RAM and only decrypted inside the CPU.
- **ARM TrustZone:** Divides the processor into two worlds: **Normal World** (Rich OS) and **Secure World** (Trusted OS/Apps). A hardware bus bit determines the world, ensuring the Normal World cannot access Secure World resources.

## 3. TPM (Trusted Platform Module)
A dedicated micro-controller designed to secure hardware through integrated cryptographic keys.
- **Root of Trust:** Provides "sealed" storage for encryption keys and measurements of the boot process (Attestation).

## 4. Hardware Side-Channel Mitigations
Modern hardware includes features to mitigate attacks like Spectre/Meltdown:
- **KPTI (Kernel Page Table Isolation):** Hardware/software synergy to hide kernel mappings from user-space.
- **Serialization Instructions:** (e.g., `LFENCE`) used to prevent speculative execution across security boundaries.

## Related Concepts
- [[os-security-domains]]
- [[memory-protection-mechanisms]]
- [[hardware-security-vulnerabilities]]
