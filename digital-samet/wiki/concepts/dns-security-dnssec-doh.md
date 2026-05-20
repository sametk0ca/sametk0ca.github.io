# DNS Security (DNSSEC, DoH, and DoT)

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #dns #protocols #privacy

## Overview
The Domain Name System (DNS) was originally unauthenticated and unencrypted, leading to threats like cache poisoning and eavesdropping.

## 1. DNSSEC (DNS Security Extensions)
Provides **Integrity** and **Authenticity** for DNS records.
- **Mechanism:** Authoritative name servers sign DNS records using digital signatures.
- **Verification:** Clients verify the signatures using a chain of trust leading up to the root name servers.
- **Limitation:** Does NOT provide confidentiality (queries are still in the clear).

## 2. Confidentiality Protocols
To prevent eavesdropping and metadata analysis by ISPs or on-path attackers:
- **DoT (DNS over TLS):** DNS queries are sent over a dedicated TLS-encrypted port (853).
- **DoH (DNS over HTTPS):** DNS queries are tunneled within standard HTTPS traffic (port 443).
    - **Controversy:** DoH can bypass local network security controls and centralizes traffic toward a few providers (e.g., Google, Cloudflare).
- **ODoH (Oblivious DoH):** Adds a proxy between the client and resolver so that no single entity knows both the client's IP and the queried domain.

## 3. DNS Attacks
- **Cache Poisoning:** Injecting bogus records into a resolver's cache to divert users.
- **NXDOMAIN Attack:** A DDoS attack where spoofed clients query non-existent subdomains, forcing resolvers to flood authoritative servers.
- **Amplification DDoS:** Exploiting the fact that a small DNS query can trigger a significantly larger response to overwhelm a victim's IP.

## 4. DNS Filtering
Resolvers can use blocklists to prevent users from reaching known phishing or malware Command & Control (C2) domains.

## Related Concepts
- [[web-pki-and-https]]
- [[digital-signatures-applied]]
- [[network-attacker-models]]
