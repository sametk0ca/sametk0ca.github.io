# Cross-Site Scripting (XSS) Types and Defenses

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #attacks #xss #javascript

## Overview
XSS is an injection vulnerability where an attacker injects malicious client-side scripts (usually JavaScript) into a web page viewed by other users.

## 1. Main Types

### Stored XSS (Persistent / Type-I)
The malicious script is permanently stored on the target server (e.g., in a database, comment field, or user profile).
- **Execution:** Every user who visits the affected page executes the script.

### Reflected XSS (Non-persistent / Type-II)
The script is "reflected" off the web server to the victim's browser.
- **Delivery:** Usually via a malicious link (e.g., in a search parameter or error message).
- **Execution:** The server includes the script from the URL in its response.

### DOM-based XSS
The vulnerability exists entirely in the client-side code.
- **Mechanism:** The script is executed when the web application's client-side code writes untrusted data to the Document Object Model (DOM) in an unsafe way.

## 2. Core Defenses

### Output Encoding
Converting data into a safe format before rendering it in the browser.
- **Context matters:** Data must be encoded differently depending on whether it's placed in an HTML tag, an attribute, or a JavaScript variable.

### Input Sanitization
Removing or neutralizing dangerous parts of input (e.g., stripping `<script>` tags). **Whitelist approaches** (allowing only known good characters) are much safer than blacklists.

### Content Security Policy (CSP)
Providing a high-level policy that restricts which scripts can run, disabling inline scripts and restricting allowed domains.

## Related Concepts
- [[injection-vulnerabilities]]
- [[web-content-isolation-sop-csp]]
- [[web-origin-security-policies]]
