# OAuth 2.0 and OpenID Connect Security

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #authentication #authorization #oauth #oidc

## Overview
OAuth 2.0 and OpenID Connect (OIDC) are modern, JSON/HTTP-based protocols for sharing authorization and identity across web and mobile applications.

## 1. OAuth 2.0 (The Authorization Layer)
Allows a **Resource Owner** (User) to grant a **Client Application** access to their resources on a **Resource Server** without sharing their password.
- **Grant Types:** Authorization Code, Implicit (obsolete), Client Credentials, Device Code.
- **Key Artifacts:** 
    - **Access Token:** An opaque string (or JWT) representing the authorization.
    - **Redirect URI:** The address where the authorization server sends the user after approval. Must be strictly validated to prevent data theft.
    - **State Parameter:** A unique nonce used to prevent CSRF attacks and ensure the response matches the request.

## 2. OpenID Connect (The Identity Layer)
Built on top of OAuth 2.0 to add **Authentication**.
- **Role:** Turns the OAuth Authorization Server into an **OpenID Provider (OP)**.
- **Key Artifact:**
    - **ID Token:** A signed JSON Web Token (JWT) containing user info (Issuer, Subject, Audience, Expiry, Nonce).
- **Relying Party (RP):** The application that consumes the ID Token to log the user in.

## 3. Core Differences
| Feature | OAuth 2.0 | OpenID Connect |
| :--- | :--- | :--- |
| **Primary Goal** | Authorisation (Access to data) | Authentication (Identity) |
| **Token** | Access Token | ID Token (JWT) |
| **Question** | "Is this app allowed to do X?" | "Who is this user?" |

## 4. Common Vulnerabilities
- **Redirect URI Manipulation:** Attacker gets the authorization code sent to their own server.
- **State Omission:** Leads to Cross-Site Request Forgery (CSRF).
- **Token Leakage:** Via referrer headers or browser history.

## Related Concepts
- [[federated-identity-protocols]]
- [[web-origin-security-policies]]
- [[aaa-fundamental-concepts]]
