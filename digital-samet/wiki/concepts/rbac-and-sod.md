# Role-Based Access Control (RBAC) and Separation of Duties (SoD)

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #access-control #rbac #sod

## Overview
Role-Based Access Control (RBAC) is an elegant paradigm that decouples users from permissions by introducing "Roles" as an intermediate layer. This reflects organization-level structures where permissions are tied to job functions rather than individuals.

## 1. RBAC Model (NIST Standard)
- **Users to Roles:** Users are assigned to one or more roles.
- **Roles to Permissions:** Roles are granted permissions to perform operations.
- **Core variants:**
    - **Flat RBAC:** Basic user-role and role-permission mapping.
    - **Hierarchical RBAC:** Roles can inherit permissions from other roles (e.g., 'Senior Engineer' inherits from 'Engineer').
    - **Constrained RBAC:** Implements **Separation of Duties**.

## 2. Separation of Duties (SoD)
The principle that no single individual should have enough authority to complete a critical business process without oversight.
- **Static SoD:** Rules enforced during user-role assignment (e.g., a user cannot be assigned to both 'Purchasing' and 'Auditing' roles).
- **Dynamic SoD:** Rules enforced during session activation (e.g., a user can have both roles but cannot activate them simultaneously in the same transaction).

## 3. Benefits and Challenges
- **Pros:** Scalable management; aligned with business logic; easy user-role review.
- **Cons:** High initial effort to define role structures (role mining); "Role Explosion" (too many specific roles created over time).

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[access-control-matrix-and-policies]]
- [[abac-and-ucon]]
