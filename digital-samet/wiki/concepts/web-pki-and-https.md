# Web PKI and HTTPS

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #cryptography #pki #https

## Overview
HTTPS (HTTP over TLS) is the standard for secure communication on the web, providing authentication, confidentiality, and integrity. It relies on the Web Public-Key Infrastructure (PKI).

## 1. How HTTPS Works
- **Encapsulation:** HTTP traffic is wrapped inside a TLS session.
- **Protected Elements:** URLs, HTTP headers (including cookies), and the message body are encrypted.
- **Visible Metadata:** IP addresses, port numbers, and (usually) the Server Name Indication (SNI) remain visible to eavesdroppers.

## 2. The Web PKI
- **Certificate Authorities (CAs):** Trusted third parties that sign X.509 certificates to bind a domain name to a public key.
- **Trust Stores:** Browsers and OSs come with pre-installed lists of hundreds of trusted root CAs.
- **Detection of Fraud:** **Certificate Transparency (CT)** provides a public, verifiable log of all issued certificates, making it easier to detect rogue CAs or fraudulent issuance.

## 3. Advanced Protections
- **HSTS (HTTP Strict Transport Security):** An HTTP header that tells the browser to *only* interact with the domain via HTTPS for a specified period, preventing protocol downgrade attacks.
- **Mixed Content:** Occurs when an HTTPS page loads resources (scripts, CSS) over plain HTTP. Modern browsers block "active" mixed content (scripts) to maintain the security context.

## 4. Visual Indicators
Browsers use padlock icons and color-coding to indicate security status. However, mobile apps often lack these visual cues, requiring users to trust the developer's implementation.

## Related Concepts
- [[asymmetric-encryption-schemes]] (PKI)
- [[network-security-basics]] (TLS)
- [[web-content-isolation-sop-csp]]
