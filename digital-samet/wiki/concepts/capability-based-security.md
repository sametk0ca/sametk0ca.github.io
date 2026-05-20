# Capability-based Security

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #access-control #capabilities #pola

## Overview
Capability-based security is an access control paradigm where access to an object is granted by possession of an unforgeable token (a "capability") rather than by checking a centralized list (ACL) based on user identity.

## What is a Capability?
A capability is a "token, ticket, or key" that includes:
1. A unique identifier for a specific object (resource).
2. A set of permitted access rights (e.g., read, write, execute).

## Key Principles

### 1. Principle of Intentional Use
Access control should be explicit. A process must intentionally use a specific capability to access a resource, rather than relying on its "ambient authority" (the general power of the user who started it).

### 2. Avoiding the Confused Deputy Problem
In ACL systems, a privileged service (the deputy) might be tricked by a less-privileged process into using its authority to perform an unauthorized action. Capability systems prevent this because the process must pass the specific capability required for the action to the deputy.

### 3. Delegation
Capabilities are easily delegatable. A process can pass a subset of its rights to another process simply by sending it a capability.

## Implementation Challenges
- **Revocation:** It is difficult to revoke a capability once it has been shared, as the system may not track all holders of that capability.
- **Forgeries:** Capabilities must be protected from tampering, either by storing them in the kernel (e.g., as file descriptors) or using cryptographic protection.

## Examples
- **Research/Historical:** Multics, Hydra, Amoeba.
- **Modern:** seL4 (formally verified microkernel), Capsicum (FreeBSD), CHERI (hardware-enforced capabilities).

## Related Concepts
- [[access-control-models]] (ACL comparison)
- [[os-security-principles]] (POLA)
- [[os-security-domains]]
