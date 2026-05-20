# Memory Management Vulnerabilities

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #memory #vulnerabilities #buffer-overflow

## Overview
Memory management vulnerabilities arise in memory-unsafe languages (like C and C++) when a program violates the implicit contract for correctly allocating, accessing, and deallocating memory.

## Main Categories

### 1. Spatial Vulnerabilities
Accessing memory outside the intended contiguous range.
- **Buffer Overflow:** Writing beyond the end of an array (e.g., on the stack or heap).
- **Out-of-bounds Read:** Reading past the end of an array (e.g., Heartbleed).

### 2. Temporal Vulnerabilities
Accessing memory based on its state over time.
- **Use-after-free:** Dereferencing a pointer to memory that has already been deallocated.
- **Double Free:** Deallocating the same memory block twice, often leading to heap corruption.
- **Dangling Pointer:** A pointer that still points to a memory location after the object it was pointing to has been deleted.

## Attack Techniques
- **Code Corruption:** Modifying existing compiled code.
- **Control-Flow Hijack:** Overwriting a return address or function pointer to divert execution to:
    - **Shellcode:** Attacker-injected code (Direct code injection).
    - **ROP (Return-Oriented Programming):** Existing code fragments (gadgets) linked together (Code-reuse attack).
- **Data-only Attack:** Modifying critical variables (e.g., `is_admin`) without changing control flow.
- **Information Leak:** Reading sensitive data (keys, pointers) from memory.

## Prevention and Mitigation
- **Prevention:** Using memory-safe languages (Rust, Java), or smart pointers in C++.
- **Detection:** AddressSanitizer (ASan), static analysis.
- **Mitigation:** Stack canaries, NX (No-Execute), ASLR, and Control-Flow Integrity (CFI).

## Related Concepts
- [[os-hardening-techniques]]
- [[software-security-foundations]]
- [[capability-based-security]]
