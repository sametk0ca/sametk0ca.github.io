---
title: DNS Leak
tags: ["Privacy", "Networking", "VPN", "DNS"]
source: "Web Search"
date: 2026-05-12
---

# DNS Leak

A **DNS leak** is a privacy vulnerability where DNS queries are sent outside of an encrypted VPN tunnel, typically to the user's Internet Service Provider (ISP). This exposes the user's browsing history despite the use of a VPN.

## Technical Mechanism

When a VPN is active, all traffic, including DNS requests, should be routed through the VPN's encrypted tunnel to the VPN provider's DNS servers. A leak occurs when the operating system or an application bypasses these settings and uses the default network interface's DNS (usually the ISP's).

### Common Causes
- **IPv6 Mismatch**: Many VPNs only handle IPv4. If the OS attempts an IPv6 DNS lookup, it may go through the ISP's IPv6-enabled DNS.
- **Windows Features**:
    - **Smart Multi-Homed Name Resolution (SMHNR)**: Introduced in Windows 8, it sends requests to all interfaces and accepts the fastest response.
    - **Teredo**: A tunneling protocol for IPv6 that can bypass VPN rules.
- **Transparent DNS Proxies**: ISPs may intercept DNS traffic on port 53 and redirect it to their own servers.
- **VPN Misconfiguration**: Failure of the VPN client to properly update system DNS settings or handle connection drops.

## Prevention & Mitigation
- **Leak Protection**: Use VPN clients with built-in DNS leak protection and kill switches.
- **Disable IPv6**: Manually disabling IPv6 on the host OS to prevent protocol-mismatch leaks.
- **DNS-over-HTTPS/TLS (DoH/DoT)**: Encrypting DNS traffic independently of the VPN.
- **Firewall Rules**: Configuring the firewall to only allow outgoing traffic through the VPN interface (TUN/TAP).

## Verification Tools
- [dnsleaktest.com](https://www.dnsleaktest.com)
- [ipleak.net](https://ipleak.net)

---
*Related: [[VPN]], [[DNS]]*
