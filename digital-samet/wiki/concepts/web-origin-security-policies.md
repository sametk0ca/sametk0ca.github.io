# Web Origin Security Policies (SOP, CSP, CORS)

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #web-security #sop #csp #cors

## Overview
Web applications are the primary principals in web-based access control. Security is managed by the browser using policies based on the "Origin" of the script or resource.

## 1. Same-Origin Policy (SOP)
The cornerstone of web security. A script from one origin is generally restricted from reading or modifying data from another origin.
- **Origin Definition:** A combination of **Protocol**, **Host Name**, and **Port**.
- **Scope:** Controls access to the DOM, local storage, and XMLHttpRequest targets.

## 2. Content Security Policy (CSP)
A mechanism for web servers to specify which scripts are authorized to execute in their context, primarily to mitigate **Cross-Site Scripting (XSS)**.
- **Mechanism:** The server sends an HTTP header (`Content-Security-Policy`) listing trusted sources.
- **Nonces:** Modern CSP uses unpredictable, single-use nonces to authorize specific inline scripts.

## 3. Cross-Origin Resource Sharing (CORS)
An explicit mechanism to allow exceptions to the SOP for sharing resources across origins.
- **Preflight Request:** The browser sends an `OPTIONS` request to check if the cross-origin target permits the access.
- **Headers:** Uses headers like `Access-Control-Allow-Origin` and `Access-Control-Allow-Methods`.

## 4. Sender Policy Framework (SPF)
Origin-based access control applied to email.
- **Goal:** Prevents spoofing of the sending domain.
- **Mechanism:** DNS records list authorized IP addresses allowed to send mail for a domain.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[abac-and-ucon]]
- [[web-mobile-security-basics]]
