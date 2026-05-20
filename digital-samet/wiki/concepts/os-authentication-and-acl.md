# OS Authentication and Access Control Lists (ACL)

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #authentication #acl #identities

## Overview
Identification and authentication are the initial steps for the OS to determine which security domain is requesting access to a resource.

## Identities in the OS
The OS tracks several key identifiers:
- **UID (User ID):** Identifies the human user on whose behalf a process is running.
- **GID (Group ID):** Identifies the group memberships of the user (e.g., student, admin).
- **PID (Process ID):** A unique identifier for every running execution unit.
- **Binary Ownership:** Tracks which user owns the executing binary file, which might differ from the user running it.

## Authentication Methods
To determine a UID, the OS must authenticate the user:
- **Something you know:** Passwords, PINs.
- **Something you have:** Smartcards, hardware tokens (e.g., TPM-backed).
- **Something you are:** Biometric data like fingerprints or face recognition.
- **Multi-Factor Authentication (MFA):** Combining different factors to significantly increase security.

## Access Control Lists (ACL)
Conceptually, an ACL is a table specifying for each object (file, data block) which users/groups have which access rights.
- **UNIX Example:** A small set of permission bits for **Read (r)**, **Write (w)**, and **Execute (x)**, grouped by Owner, Group, and Others.
- **Hierarchical Access:** Access controls are often hierarchical (e.g., directory-level vs. file-level).
- **Fine-grained Control:** Modern OSs support more granular ACLs allowing detailed rules for multiple users and groups.

## Security Guarantees
- **Authentication Integrity:** Ensuring that a UID cannot be forged.
- **Mediation:** The OS must guarantee that every file or memory access is checked against the relevant ACL or permission model.

## Related Concepts
- [[access-control-models]]
- [[os-security-domains]]
- [[os-security-principles]]
