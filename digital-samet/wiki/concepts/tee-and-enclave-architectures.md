# TEE and Enclave Architectures

- **Source:** [[ka-hardware-security]]
- **Tags:** #hardware-security #isolation #tee #enclave

## Overview
Trusted Execution Environments (TEEs) and Enclaves provide hardware-enforced isolation for sensitive code and data, protecting them even from privileged software like the operating system kernel or hypervisor.

## 1. Core Principles
- **Separation:** Creating a distinct environment (the "Secure World" or "Enclave") that is logically and physically separated from the "Normal World" (Rich OS).
- **Attestation:** Providing a way for the hardware to prove to an external party that a specific piece of code is running inside a legitimate TEE.
- **Sealed Storage:** Allowing the TEE to store data that only it can decrypt, tied to the identity of the code and the state of the hardware.

## 2. Prominent Architectures

### ARM TrustZone
Divides the entire processor, memory, and peripherals into two worlds via a hardware bus bit (the NS bit).
- **Mechanism:** A "Monitor Mode" handles the secure transition between worlds.
- **Limitation:** A single compromise in the Secure World compromises all trusted applications within it.

### Intel SGX (Software Guard Extensions)
Allows applications to define private regions of memory called **Enclaves**.
- **Mechanism:** Enclave memory is encrypted while in DRAM and decrypted only inside the CPU. The CPU enforces access checks on every memory reference.
- **Benefit:** Provides fine-grained isolation for specific modules within a larger application.

### RISC-V Keystone
An open-source TEE framework for the RISC-V architecture, utilizing Physical Memory Protection (PMP) and a small trusted security monitor.

## 3. Vulnerabilities: The Micro-architectural Gap
While TEEs provide logical isolation, they often share micro-architectural resources (caches, branch predictors) with the Normal World.
- **Threat:** Speculative execution attacks (Spectre, Meltdown, Foreshadow) can bypass TEE boundaries by measuring side-effects in shared caches.

## Related Concepts
- [[os-protection-rings]]
- [[hardware-isolation-technologies]]
- [[hardware-security-vulnerabilities]]
