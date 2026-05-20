# AAA Fundamental Concepts

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #access-control #identity

## Overview
Authentication, Authorisation, and Accountability (AAA) are the three pillars of managing access and behavior in information systems.

## 1. Access Control Equation
Access Control = Authentication + Authorisation

## 2. Core Entities

### Principal
The active entity in an access request that holds rights. 
- **Examples:** A user (in IBAC), a role (in RBAC), or a specific program (e.g., an Android app).

### Subject
The active entity (usually a process) that makes requests during system execution. 
- **Relation:** A subject *speaks for* a principal when the system associates it unforgeably.
- **Lifetime:** Subjects (processes) usually have much shorter lifetimes than principals (user accounts).

### Object
The passive entity being accessed (e.g., a file, a database record, a hardware device).

## 3. Operations and Rights
- **Access Operations:** The actions that can be performed (e.g., Read, Write, Execute).
- **Access Rights (Permissions/Privileges):** The specific authorization granted to a principal to perform an operation on an object.

## 4. Reference Monitor
A core system component that:
- Mediates all access requests.
- Consults the security policy.
- Decides whether to **Permit** or **Deny**.
- May impose **Obligations** (additional actions like logging).

## Related Concepts
- [[access-control-matrix-and-policies]]
- [[soim-fundamental-concepts]] (Incident management)
- [[digital-forensics-definitions]] (Accountability)
