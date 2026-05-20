# Kernel and Software Verification Case Studies

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #sel4 #compcert #high-assurance

## Overview
Applying formal methods to large-scale, real-world software is a monumental task. These case studies represent the pinnacle of high-assurance engineering.

## 1. seL4 Microkernel
The first general-purpose OS kernel to be fully verified.
- **Scope:** 8,700 lines of C and 600 lines of assembly.
- **Proof:** Done in Isabelle/HOL using **Refinement**.
    - **Abstract Spec:** Describes what the kernel does (syscalls, faults).
    - **Executable Spec:** A functional representation of the kernel.
    - **C Implementation:** The actual source code.
- **Guarantee:** The implementation strictly follows the abstract specification (functional correctness). It was later extended to prove **Non-interference** (information flow).
- **Effort:** Approximately 20 person-years.

## 2. CompCert
A formally verified compiler for the C programming language.
- **Proof:** Developed in Coq.
- **Guarantee:** **Semantic Preservation**—the assembly code produced by the compiler has exactly the same behavior as the source C program.
- **Significance:** Standard compilers (GCC, LLVM) often have bugs that can introduce vulnerabilities. CompCert eliminates the compiler as a source of mis-compilation bugs.

## 3. Verve OS
A high-assurance operating system built using type-safe languages.
- **Approach:** Written in a safe dialect of C#, compiled to **Typed Assembly Language (TAL)**.
- **Proof:** Uses the **Boogie** Hoare verifier and **Z3** solver to mechanically verify type and memory safety for all instructions.

## 4. DeepSpec Project
A large-scale effort to build a "Full-stack" verified system.
- **Goal:** Link proofs across the entire stack (Hardware $\to$ OS $\to$ Crypto $\to$ App).
- **Toolchain:** Uses the **Verified Software Toolchain (VST)** for C program verification in Coq.

## Related Concepts
- [[formal-methods-foundations]]
- [[os-design-paradigms]]
- [[hardware-formal-verification]]
