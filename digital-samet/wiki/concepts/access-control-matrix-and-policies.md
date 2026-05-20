# Access Control Matrix and Policies

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #access-control #matrix #acl #capabilities

## Overview
Automated security policies are collections of rules that specify the access rights a principal has on an object. The Access Control Matrix is the conceptual foundation for representing these rules.

## 1. Access Control Matrix
A theoretical table where:
- **Rows:** Represent Principals.
- **Columns:** Represent Objects.
- **Cells:** Contain the Access Rights.

## 2. Implementation Strategies

### Access Control Lists (ACL)
Storing the matrix by **columns**. 
- Each object maintains a list of principals and their rights.
- **Pros:** Easy to see who can access a specific file; efficient for sharing.
- **Examples:** Windows NTFS permissions, POSIX ACLs.

### Capabilities
Storing the matrix by **rows**.
- Each principal holds a collection of unforgeable tokens (keys) representing their rights.
- **Pros:** Easy to delegate rights; avoids the **Confused Deputy** problem.
- **Examples:** Android app permissions, seL4 capabilities.

## 3. High-level Policy Models

### IBAC (Identity-Based Access Control)
Rules refer directly to specific user identities. (e.g., "Alice can read file.txt").

### RBAC (Role-Based Access Control)
Rules refer to job functions (Roles).
- **Process:** Users $\to$ Roles $\to$ Rights.
- **Benefit:** Simplifies management in large organizations.

### ABAC (Attribute-Based Access Control)
Rules refer to labels or generic characteristics (Attributes).
- **Example:** "Users in the Engineering department can access internal servers during working hours."

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[os-design-paradigms]]
- [[capability-based-security]]
