# Hardware Formal Verification

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #hardware #microprocessor #assurance

## Overview
Hardware verification uses formal logic to prove that a circuit design (at the register transfer level or lower) behaves correctly and meets security requirements.

## Abstraction Levels
- **HDL (Hardware Description Languages):** Verilog, VHDL. Designs are translated into models for analysis.
- **Microcode:** The low-level instructions that implement processor logic.
- **Transistor Level:** The most detailed physical model.

## Verification Techniques
- **Equivalence Checking:** Proving that two versions of a design (e.g., an optimized vs. an original one) are functionally identical. Uses **Binary Decision Diagrams (BDDs)**.
- **Model Checking:** Verifying temporal properties of sequential circuits.
- **Interactive Theorem Proving:** Used for full-scale microprocessors (e.g., **ACL2**). Establishing invariants for complex mechanisms like out-of-order execution and branch prediction.

## High Assurance Standards
- **Common Criteria (CC):** Higher Evaluation Assurance Levels (EAL 6/7) mandate formal verification.
- **Case Study:** The **AAMP7G** Microprocessor used the ACL2 theorem prover to verify its microcode for a separation microkernel, ensuring space partitioning.

## Security Focus
- **Isolation:** Ensuring that a bug in one component cannot bypass the protection rings.
- **Integrity of the Boot Process:** Verifying the initial hardware state.

## Related Concepts
- [[side-channel-formal-analysis]]
- [[secure-and-measured-boot]]
- [[hardware-isolation-technologies]]
