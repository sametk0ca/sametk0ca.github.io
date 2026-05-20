# Web Content Isolation (SOP and CSP)

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #isolation #sop #csp

## Overview
Content isolation ensures that code and data from one website cannot interfere with or access data from another website in the user's browser.

## 1. Same-Origin Policy (SOP)
The fundamental security model of the web. It restricts how a document or script loaded from one "Origin" can interact with a resource from another origin.
- **Origin:** The triple of **(Protocol, DNS Name, Port)**.
- **Rules:**
    - Scripts can only access the DOM of documents from the same origin.
    - `XMLHttpRequest` can only be sent to the source origin (by default).
    - Cookies are strictly scoped to the origin that set them.
- **Weakness:** Relies on DNS names; vulnerable if an attacker can manipulate DNS mapping.

## 2. Content Security Policy (CSP)
A defense-in-depth mechanism that allows web servers to inform the browser about trusted sources of content.
- **Primary Goal:** Mitigating **Cross-Site Scripting (XSS)** and data injection attacks.
- **Mechanism:** An HTTP response header (`Content-Security-Policy`) that defines a whitelist of authorized domains for scripts, styles, images, etc.
- **Example:** `script-src 'self' https://trusted.com` tells the browser only to execute scripts from its own origin and the trusted domain.

## 3. Site Isolation
A modern browser architectural feature where websites are rendered in separate operating system processes.
- **Goal:** Providing a second line of defense if the software enforcing the SOP is compromised.
- **Benefit:** Protects against side-channel attacks (like Spectre) that could otherwise leak cross-site data within a single browser process.

## Related Concepts
- [[web-origin-security-policies]]
- [[injection-vulnerabilities]]
- [[os-security-domains]]
