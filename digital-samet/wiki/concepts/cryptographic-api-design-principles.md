# Cryptographic API Design Principles

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #engineering #usability #api

## Overview
Developers often misuse cryptographic libraries, leading to insecure systems. Designing "misuse-resistant" APIs is critical for reducing these errors.

## The Ten Principles (Green & Smith)
1. **Abstraction:** Integrate crypto into standard APIs; hide the complexity from the developer where possible.
2. **Powerful but Simple:** Ensure the API satisfies all functional requirements (not just security) so developers don't write their own crypto.
3. **Low Barrier to Entry:** Design APIs that are easy to learn without advanced cryptographic expertise.
4. **Intuitive Paradigm:** Don't break the developer's mental model of how an API should work.
5. **Self-Documenting:** APIs should be usable even without reading extensive documentation.
6. **Hard to Misuse:** Incorrect usage should result in immediate, visible errors (e.g., compile-time errors or clear exceptions).
7. **Safe Defaults:** Provide unambiguous and secure default settings (e.g., using AES-GCM instead of ECB).
8. **Explicit Testing Modes:** Provide a safe way to test during development without hacking the security mechanisms (which might accidentally remain in production).
9. **Readable and Maintainable:** Code using the API should be easy to audit. Key parameters (like iteration counts) should be handled internally.
10. **Assisted Interaction:** The API should help handle end-user interactions (like error messages) correctly.

## Practical Impact
Good API design moves the responsibility of security from the application developer to the library author, who is typically more expert in the field.

## Related Concepts
- [[applied-cryptography-themes]]
- [[software-security-foundations]]
- [[human-factors-basics]]
