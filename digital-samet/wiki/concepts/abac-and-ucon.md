# Attribute-Based Access Control (ABAC) and Usage Control (UCON)

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #access-control #abac #ucon

## Overview
As IT systems evolved, access control moved from simple identity checks to more flexible systems that consider the context and dynamic characteristics of the request.

## 1. Attribute-Based Access Control (ABAC)
Authorisation is determined by evaluating logical rules against attributes associated with:
- **Subject:** (e.g., job title, security clearance, group membership).
- **Object:** (e.g., sensitivity level, file type, owner).
- **Requested Operation:** (e.g., read, delete).
- **Environment:** (e.g., current time, location/IP address, device health).

## 2. Usage Control (UCON)
UCON extends traditional access control by including three main pillars throughout the access lifecycle (before, during, and after):
- **Authorisations:** Traditional attribute checks.
- **Obligations:** Actions the user or system *must* perform (e.g., clicking "I Agree", logging the event).
- **Conditions:** Environmental constraints (e.g., office hours only).

### Dynamic Nature
UCON allows for **Mutable Attributes**: attributes that change as a result of the access (e.g., decrementing a "free trial" counter after reading an article).

## 3. Comparison
- **RBAC:** Rigid, function-based, easier to audit for large sets of users.
- **ABAC:** Flexible, context-aware, requires complex rule management (XACML).
- **UCON:** Comprehensive, lifecycle-oriented, suitable for modern services like pay-per-view or subscription models.

## Related Concepts
- [[rbac-and-sod]]
- [[aaa-fundamental-concepts]]
- [[web-origin-security-policies]]
