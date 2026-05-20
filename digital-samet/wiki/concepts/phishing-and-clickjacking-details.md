# Phishing and Clickjacking

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #attacks #phishing #clickjacking

## Overview
Phishing and Clickjacking are attacks that exploit human psychology and user interface weaknesses rather than purely technical software bugs.

## 1. Phishing
Fraudulent attempts to steal sensitive information by masquerading as a trustworthy entity.
- **Deception Techniques:**
    - **URL Obfuscation:** Using misspelled domains or complex subdomains (e.g., `paypal.security.com`).
    - **IDN Homograph Attack:** Using characters from different scripts that look identical (e.g., Cyrillic 'a' vs. Latin 'a').
    - **Address Bar Manipulation:** Using JavaScript to hide or fake the true URL.
- **Drive-by-downloads:** A specific type of phishing where visiting a malicious site triggers an automated malware download.

## 2. Clickjacking (UI Redress Attack)
An attacker tricks a user into clicking something different from what the user perceives.
- **Mechanism:** Using transparent or opaque `iFrames` to overlay a malicious button on top of a legitimate website element.
- **Consequence:** The user unknowingly triggers a state-changing action (e.g., deleting an account, granting camera permissions) on a trusted site while logged in.
- **Defense:**
    - **X-FRAME-OPTIONS:** A server-side header (values: `DENY` or `SAMEORIGIN`) that prevents the site from being rendered inside an iFrame.
    - **FrameBusting:** JavaScript code that forces the page to be the top-level window.

## Related Concepts
- [[user-authentication-factors]]
- [[web-origin-security-policies]]
- [[aaa-fundamental-concepts]]
