# Constant-Time Cryptography

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #implementation #side-channel #timing-attacks

## Overview
Constant-time cryptography is a programming paradigm aimed at eliminating timing side-channels by ensuring that the execution time of a cryptographic operation is independent of the sensitive data (keys or plaintexts) being processed.

## 1. The Threat: Timing Side-Channels
If an algorithm's execution time varies based on secret data, an adversary can measure these variations to recover the secret.
- **Example:** A simple `memcmp` for checking a MAC tag returns as soon as it finds a mismatching byte. An attacker can use this to guess the tag byte-by-byte.

## 2. Core Principles
To achieve constant-time execution, programmers must avoid:
- **Secret-dependent Branching:** No `if`, `while`, or `for` loops whose conditions depend on secret data.
- **Secret-dependent Memory Access:** Avoiding table lookups (like S-boxes) or array indexing based on secret data, as these can trigger different cache hits/misses.
- **Variable-time Instructions:** Avoiding CPU instructions whose execution time depends on operands (e.g., some forms of division or shifts on older CPUs).

## 3. Techniques
- **Bitwise Operations:** Using logical bitwise operations (AND, OR, XOR, NOT) to implement conditional logic without branching.
- **Blinding:** Masking internal values with random numbers to decorrelate them from observable physical characteristics.
- **Masking:** Using secret sharing to split secrets into multiple random parts throughout the computation.

## 4. Challenges
- **Complexity:** Writing constant-time code is difficult and non-intuitive.
- **Compiler Interference:** Modern compilers may optimize away constant-time protections (e.g., turning a constant-time bitwise swap back into a conditional branch).
- **Hard-to-Fix Algorithms:** Some algorithms (like traditional AES with S-box tables) are inherently difficult to implement in constant-time on general-purpose CPUs without hardware support (e.g., AES-NI).

## Related Concepts
- [[cryptographic-implementation-security]]
- [[side-channel-formal-analysis]]
- [[hardware-isolation-technologies]]
