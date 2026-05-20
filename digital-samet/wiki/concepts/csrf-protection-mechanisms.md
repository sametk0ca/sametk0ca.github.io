# Cross-Site Request Forgery (CSRF) Protection

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #attacks #csrf

## Overview
CSRF misleads a victim into submitting a malicious HTTP request to a remote server. The request is executed with the victim's identity and session privileges (e.g., cookies).

## Why It Works
Browsers automatically include ambient authority artifacts (session cookies, basic auth credentials) in requests to a domain, even if the request was triggered by a third-party script or form.

## Common Misconceptions
- **"Secret" Cookies:** Do not help, as they are sent automatically by the browser.
- **HTTPS:** Does not help, as it secures the transport but does not validate the *intent* of the request.
- **POST Requests:** Are insufficient, as attackers can use auto-submitting HTML forms.

## Effective Defenses

### 1. Anti-CSRF Tokens (Synchronizer Tokens)
The most common defense.
- **Mechanism:** The server generates a unique, unpredictable token for the user session and embeds it in every state-changing form or request header.
- **Verification:** The server rejects any request that lacks a valid token. Since an attacker cannot read the token (due to the **Same-Origin Policy**), they cannot forge the request.

### 2. SameSite Cookie Attribute
A modern browser feature that controls when cookies are sent with cross-site requests.
- **SameSite=Strict:** Cookies are only sent for first-party requests.
- **SameSite=Lax:** Cookies are only sent for top-level navigation (GET requests).

### 3. Custom Request Headers
Requiring a custom header (e.g., `X-Requested-With`) for sensitive actions. Since cross-origin scripts cannot set custom headers without a **CORS** preflight, this prevents forgery.

## Related Concepts
- [[web-origin-security-policies]] (SOP, CORS)
- [[aaa-fundamental-concepts]]
- [[injection-vulnerabilities]]
