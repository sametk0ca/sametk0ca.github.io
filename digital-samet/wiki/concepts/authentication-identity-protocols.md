# Concept: Authentication and Identity Protocols

- **Source:** [[ka-aaa]]
- **Tags:** #authentication #identity #protocols #kerberos #oauth #oidc #fido2

## Overview
Authentication protocols are the mechanisms by which a principal (user, device, or service) proves its identity to a verifier. Modern identity protocols extend this to provide federated identity and single sign-on (SSO) across different security domains.

## 1. Classical Network Authentication

### Kerberos
A ticket-based symmetric-key protocol designed for trusted local networks.
- **Key Distribution Center (KDC):** Composed of an Authentication Service (AS) and a Ticket Granting Service (TGS).
- **Mechanism:** The user proves identity to the AS, receives a Ticket Granting Ticket (TGT), and then uses the TGT to request Service Tickets (ST) from the TGS.
- **Strength:** Mutual authentication and prevention of password transmission over the wire.

## 2. Web-Based Federation Protocols

### SAML (Security Assertion Markup Language)
An XML-based standard for exchanging authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP).
- **Use Case:** Enterprise SSO.
- **Pros:** Mature and widely supported in legacy corporate environments.

### OAuth 2.0
An authorization framework that allows a third-party application to obtain limited access to an HTTP service.
- **Roles:** Resource Owner, Client, Resource Server, and Authorization Server.
- **Tokens:** Access Tokens and Refresh Tokens.

### OpenID Connect (OIDC)
An identity layer built on top of the OAuth 2.0 protocol. It allows clients to verify the identity of the end-user based on the authentication performed by an Authorization Server.
- **ID Token:** A JSON Web Token (JWT) containing user profile information.

## 3. Modern Strong Authentication

### FIDO2 and WebAuthn
A set of standards for passwordless, multi-factor authentication using public-key cryptography.
- **WebAuthn:** A browser-based API for creating and challenging public-key credentials.
- **CTAP (Client to Authenticator Protocol):** Allows external authenticators (e.g., YubiKey, smartphone) to talk to the browser.
- **Security:** Resistant to phishing, as the credential is bound to the origin (domain).

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[user-authentication-factors]]
- [[federated-identity-protocols]]
