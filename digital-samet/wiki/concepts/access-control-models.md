# Access Control Models

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #access-control #mac #dac #rbac

## Overview
Access control models define the rules and mechanisms for who (subject) can perform what action on what object. These are system-wide policies enforced by the operating system kernel.

## Main Access Control Models

### 1. Mandatory Access Control (MAC)
The system enforces a centralized, system-wide policy that users cannot change.
- **Bell-LaPadula Model:** Focuses on confidentiality.
    - **No Read Up:** A subject cannot read an object with a higher classification level.
    - **No Write Down:** A subject cannot write data to an object with a lower classification level (to prevent leakage).
- **Biba Model:** Focuses on integrity.
    - **No Read Down:** A subject cannot read an object with a lower integrity level.
    - **No Write Up:** A subject cannot write data to an object with a higher integrity level (to prevent corruption).
- **Usage:** Security-hardened operating systems (e.g., SELinux, AppArmor).

### 2. Discretionary Access Control (DAC)
The owner of an object has discretionary power over who can access it.
- **Mechanism:** Owners can use commands (e.g., `chmod` in UNIX) to grant read, write, or execute permissions to others.
- **Vulnerability:** Once access is granted, it is hard to control the further flow of information (e.g., a process can copy the data and share it again).

### 3. Role-Based Access Control (RBAC)
Access is granted based on predefined roles (e.g., student, admin, faculty) rather than specific users.
- **Benefit:** Simplifies management by assigning permissions to jobs or functions.
- **Flexibility:** Can be used to implement both MAC and DAC policies.

## Implementation Primitives
- **Access Control Lists (ACLs):** Tables mapping users/roles to objects and their permissions.
- **Capabilities:** Unforgeable tokens that grant the holder specific access rights to a resource.

## Related Concepts
- [[os-security-principles]]
- [[os-authentication-and-acl]]
- [[cia-triad]]
