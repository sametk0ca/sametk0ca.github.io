# Hardware Root of Trust (RoT)

- **Source:** [[ka-hardware-security]]
- **Tags:** #hardware-security #trust #rot #tpm #hsm

## Overview
A Hardware Root of Trust (RoT) is a component at the lowest level of a system's architecture that is inherently trusted. It provides the foundation for all security operations, as its own trustworthiness cannot be verified by the layers above it.

## 1. Defining Trust
- **Anderson's Definition:** A component on which a designer relies but whose trustworthiness cannot be explicitly verified.
- **TCG Definition:** An entity that always behaves in the expected manner for the intended purpose.

## 2. Core Functions of an RoT
- **Measurement (RTM):** Calculating hashes of other components (e.g., bootloader, OS) to create an integrity record.
- **Storage (RTS):** Providing secure memory for cryptographic keys and configuration data (PCRs).
- **Reporting (RTR):** Cryptographically signing and presenting the state of the system to other parties (Attestation).

## 3. Real-world Implementations

### HSM (Hardware Security Module)
High-performance, tamper-resistant devices used in data centers. They handle large-scale key generation and encryption, often protected by physical chassis that erase keys if opened.

### Secure Element (SE) / Smart Card
A single-chip computer designed for portability and extreme physical security. Used in SIM cards, credit cards, and specialized mobile chips (e.g., Apple's Secure Enclave).

### TPM (Trusted Platform Module)
A standard for a dedicated micro-controller on a PC motherboard.
- **TPM 2.0:** The modern standard supporting diverse cryptographic algorithms and broader device classes (IoT, Mobile).
- **Usage:** Protecting BitLocker keys, verifying boot integrity, and supporting biometric login (Windows Hello).

## 4. Hierarchy of Trust
The hardware RoT is at the bottom of the "Chain of Trust." It verifies the firmware, which verifies the OS loader, which verifies the kernel, and so on. If the hardware RoT is compromised (e.g., via a Hardware Trojan), the entire chain is broken.

## Related Concepts
- [[secure-and-measured-boot]]
- [[tee-and-enclave-architectures]]
- [[physically-unclonable-functions-puf]]
