# OS Security Principles

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #security-principles #tcb

## Overview
Fundamental design principles guide the creation of secure operating systems, focusing on minimizing the attack surface and establishing a trusted foundation.

## Saltzer and Schroeder's Principles
Established in the 1970s, these are the cornerstone of OS security design:
- **Economy of Mechanism:** Keep the system as simple and small as possible to minimize bugs and vulnerabilities.
- **Fail-safe Defaults:** Deny access by default; only explicitly permit authorized access.
- **Complete Mediation:** Every access to every protected object must be checked by the security mechanism.
- **Open Design:** Security must not depend on the secrecy of the mechanism (avoid "security by obscurity").
- **Separation of Privilege:** Where possible, require multiple conditions to grant access to a sensitive resource.
- **Least Privilege:** Every process should operate using the minimum set of privileges necessary for its task.
- **Least Common Mechanism:** Minimize mechanisms shared between users/domains to prevent unintended communication channels.
- **Psychological Acceptability:** Security mechanisms must be easy to use and not hinder legitimate workflows.

## Trusted Computing Base (TCB)
The TCB is the set of all hardware, software, and firmware components that are critical to the system's security.
- **Goal:** Minimize the size of the TCB (e.g., through a microkernel design) to make it easier to audit, verify, and secure.
- **Vulnerability:** If any part of the TCB is compromised, the entire system's security is void.

## Modern Principles
- **Intentional Use:** Requiring explicit intent for privileged actions.
- **Minimal Trusted Code:** A modern phrasing of Economy of Mechanism focusing specifically on code volume.

## Related Concepts
- [[os-design-paradigms]]
- [[access-control-models]]
- [[cia-triad]]
