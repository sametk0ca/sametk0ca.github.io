# Federated Identity Protocols

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #authentication #kerberos #saml #oidc

## Overview
Federated identity allows identities and authorizations to be shared across different organizational boundaries, enabling **Single Sign-On (SSO)**.

## 1. Kerberos
A symmetric-key protocol used for local and cross-domain authentication.
- **Trusted Third Party:** Key Distribution Center (KDC), which includes the Authentication Server (KAS) and Ticket Granting Server (TGS).
- **Mechanism:** Users log in once to get a **Ticket Granting Ticket (TGT)**. They use the TGT to request specific service tickets without re-entering their password.
- **Focus:** Authentication and key establishment.

## 2. SAML (Security Assertion Markup Language)
An XML-based meta-protocol for web-based federated SSO.
- **Parties:** 
    - **Identity Provider (IdP):** Authenticates the user and issues assertions.
    - **Service Provider (SP):** Consumes assertions to grant access.
- **Profiles:**
    - **POST Profile:** Assertion is sent via the user's browser.
    - **Artifact Profile:** A handle (artifact) is sent via the browser, and the SP pulls the actual assertion directly from the IdP.
- **Security:** Must include SP-ID and Request-ID to prevent impersonation attacks (reuse of assertions across different SPs).

## 3. OAuth 2.0 and OpenID Connect (OIDC)
Modern HTTP-based protocols.
- **OAuth 2.0:** Primarily an **Authorization** protocol. It provides **Access Tokens** to allow a third-party app to access a user's resources.
- **OpenID Connect (OIDC):** An identity layer on top of OAuth 2.0. It adds an **ID Token** to provide **Authentication** (info about who the user is).
- **Benefit:** JSON-based, more lightweight and mobile-friendly than SAML.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[user-authentication-factors]]
- [[web-origin-security-policies]]
