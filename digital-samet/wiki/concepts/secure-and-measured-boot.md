# Secure and Measured Boot

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #boot #integrity #tpm #uefi

## Overview
Ensuring the integrity of the operating system starts at the boot process. Secure and measured boot mechanisms establish a "Chain of Trust" from the hardware up to the OS.

## Core Concepts

### 1. Root of Trust
A hardware or firmware component that is inherently trusted (e.g., Apple T2 chip, Google Titan, or a hardware-integrated TPM).

### 2. Secure Boot (UEFI)
Ensures that only authorized software can run during the boot process.
- **Verification:** The firmware checks digital signatures of the bootloader, and the bootloader checks the signature of the OS kernel.
- **Goal:** Prevents malicious **Bootkits** from gaining control before the OS starts.

### 3. Measured Boot
Instead of stopping unauthorized code (like Secure Boot), Measured Boot records what code was executed.
- **TPM (Trusted Platform Module):** A cryptographic module that maintains **PCRs (Platform Configuration Registers)**.
- **Extending PCRs:** As each stage of the boot process executes, it "measures" (hashes) the next stage and sends the hash to the TPM to extend a PCR ($PCR_{new} = Hash(PCR_{old} \| Hash_{new\_code})$).
- **Integrity History:** The PCRs contain a unique hash chain representing the entire sequence of software loaded since power-on.

### 4. Remote Attestation
A process where a third party (e.g., a server) requests the PCR values from a machine to verify that it is running a known, trusted version of the BIOS, bootloader, and kernel.

## Related Concepts
- [[os-hardening-techniques]]
- [[hardware-isolation-technologies]] (TPM)
- [[trust-services]] (Digital signatures)
