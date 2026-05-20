# Software Security Foundations

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #vulnerabilities #lifecycle

## Overview
Software security focuses on the identification, mitigation, and prevention of implementation-level vulnerabilities throughout the software development lifecycle (SDLC).

## Core Objectives
- **Prevention:** Avoiding the introduction of bugs through secure coding practices and language choice.
- **Detection:** Finding existing vulnerabilities via static and dynamic analysis.
- **Mitigation:** Limiting the impact of exploits using platform-level defenses (e.g., ASLR, DEP).

## Taxonomy of Vulnerabilities
Vulnerabilities are often categorized by the underlying programming error:
- **Memory Errors:** Buffer overflows, use-after-free (common in C/C++).
- **Injection Attacks:** SQL injection, Cross-Site Scripting (XSS).
- **Concurrency Issues:** Race conditions, time-of-check to time-of-use (TOCTOU).
- **Logic Flaws:** Insecure defaults, broken access control.

## Trusted Computing Base (TCB) in Software
The software security of an application depends on its TCB, which includes the operating system, compilers, libraries, and any external services it calls.

## Related Concepts
- [[os-hardening-techniques]]
- [[static-and-dynamic-analysis-formal]]
- [[software-security-models]]
