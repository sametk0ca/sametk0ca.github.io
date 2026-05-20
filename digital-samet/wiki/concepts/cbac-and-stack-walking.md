# Code-Based Access Control (CBAC) and Stack Walking

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #access-control #cbac #software-security

## Overview
Code-Based Access Control (CBAC) shifts the principal of access control from the *User* to the *Executable Code* itself.

## 1. Principles
- **Granting Rights:** Permissions are assigned to binaries based on their **Origin** (domain, signer), **Identity** (cryptographic hash), or other properties.
- **Scenario:** Even if a user has admin rights, a non-trusted script should not be allowed to perform sensitive operations like deleting system files.

## 2. The Confused Deputy Problem
A situation where a low-privileged process tricks a high-privileged process (the "Deputy") into performing an unauthorized action on its behalf.

## 3. Stack Walking
The standard defense mechanism in CBAC (used in Java and .NET).
- **Mechanism:** When a sensitive resource is accessed, the security runtime "walks back" through the execution stack to check the permissions of *every* caller.
- **Check:** Access is granted only if ALL callers in the chain have the required permission.
- **Assert/Override:** A privileged function can "Assert" its rights to stop the stack walk if it is performing a known safe operation on behalf of an untrusted caller.

## 4. Usage
- **Java Security Model:** Uses Permissions and Policy files.
- **.NET Architecture:** Uses Evidence and Code Groups.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[software-security-models]]
- [[capability-based-security]]
