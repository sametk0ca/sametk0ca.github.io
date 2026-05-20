# OS Design Paradigms and Security

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #architecture #design-paradigms

## Overview
The architectural design of an operating system significantly impacts its security, reliability, and isolation. Different paradigms make distinct trade-offs between performance and security.

## Main OS Architectures

### 1. Monolithic Kernel
Most common in general-purpose systems (e.g., Linux, Windows).
- **Design:** Most OS services (drivers, networking, file systems) run in a single, large, privileged security domain (the kernel).
- **Security Implications:**
    - **Pros:** High performance due to fast inter-component communication (function calls/shared memory).
    - **Cons:** Any vulnerability in any component (e.g., a buggy driver) can compromise the entire system.
- **Modern Refinements:** Implementing non-critical drivers or file systems in user space (e.g., FUSE, UMDF) to limit the impact of crashes or exploits.

### 2. Microkernel / Multi-Server Architecture
Designed for extreme reliability and security (e.g., MINIX 3, seL4).
- **Design:** The kernel provides only minimal primitives (IPC, scheduling, low-level memory management). Other services run as isolated, unprivileged processes (servers).
- **Security Implications:**
    - **Pros:** A compromise of one component (e.g., the network server) does not automatically compromise others or the kernel.
    - **Cons:** Performance overhead due to the requirement for inter-process communication (IPC) for every OS operation.

### 3. Library Operating System (LibraryOS) / Unikernels
Gaining popularity in virtualized/cloud environments (e.g., MirageOS, OSv).
- **Design:** OS functionality is provided as a library and directly linked with the application into a single address space (security domain).
- **Security Implications:**
    - **Pros:** Minimal attack surface as only the required OS features are included. The OS is part of the application's trusted computing base, reducing the risk of side channels between the OS and the app.
    - **Cons:** No internal isolation between the application and the OS; any exploit in the app has full control of the OS functions.

## Design Principles
- **Separation of Duty:** Breaking the OS into smaller components to prevent one failure from leading to a total compromise.
- **Attack Surface Reduction:** Minimizing the amount of reachable code an adversary can target.

## Related Concepts
- [[os-security-domains]]
- [[os-hardening-techniques]]
- [[software-security-models]]
