# Cryptographic Implementation Security

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #implementation #side-channel #fault-attacks

## Overview
Secure algorithms can still be vulnerable if their implementation leaks information through physical or protocol-level side channels.

## Side-Channel Attacks
Attacks based on information gained from the physical implementation of a cryptosystem.
- **Timing Attacks:** Measuring the time an algorithm takes to process different inputs.
    - **Mitigation:** **Constant-time programming** (ensuring all execution paths take the same time).
- **Power Analysis:** Measuring power consumption during computation (e.g., Simple Power Analysis - SPA, Differential Power Analysis - DPA).
    - **Mitigation:** **Masking** (using secret-sharing to randomize intermediate values).
- **EM Radiation / Sound:** Exploiting electromagnetic emissions or acoustic signatures from the CPU.
- **Remote Side Channels:** Measuring response time differences from a server over a network.

## Fault Attacks
Injecting faults into a cryptographic device to induce errors that reveal secret information.
- **Methods:** Voltage glitches, clock manipulation, laser pulses.
- **Mitigation:** Redundancy, self-checking logic, and input validation.

## Performance and Hardware Support
Modern CPUs provide specialized instructions to improve cryptographic performance and security:
- **AES-NI:** Intel/AMD instructions for fast and side-channel resistant AES.
- **CLMUL:** Instruction for carry-less multiplication (used in GCM mode).
- **Low-level implementation:** Often written in tuned assembly to ensure both speed and constant-time execution.

## Related Concepts
- [[symmetric-primitives]] (AES)
- [[block-cipher-modes]] (GCM)
- [[digital-signatures]] (ECDSA brittle nonces)
