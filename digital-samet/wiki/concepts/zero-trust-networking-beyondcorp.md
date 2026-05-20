# Zero Trust Networking and BeyondCorp

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #zero-trust #architecture #access-control

## Overview
Zero Trust is a security paradigm shift that abandons the idea of a trusted "internal" network. It operates on the principle of "Never Trust, Always Verify."

## 1. The Core Philosophy
In traditional networking, a firewall protects the perimeter. Once inside, devices are largely trusted. Zero Trust assumes the network is always hostile.
- **Micro-perimeters:** Security is applied to each individual resource or request, not just the network edge.
- **Identity-centric:** Access decisions are based on the identity of the user and the device, rather than the network location (IP address).

## 2. BeyondCorp (Google's Implementation)
BeyondCorp is a real-world zero-trust architecture developed by Google.
- **Key Components:**
    - **Single Sign-On (SSO):** Centralized user authentication.
    - **Access Proxy:** All applications are exposed via an external-facing proxy that terminates TLS and checks authorization.
    - **Device Inventory:** Real-time database of managed devices and their security posture (e.g., OS version, patch level).
    - **Trust Engine:** Evaluates the risk of a request based on user, device, and context (e.g., location, time).

## 3. Benefits
- **BYOD Support:** Securely integrates unmanaged or personal devices.
- **Work-from-Anywhere:** Eliminates the need for traditional VPNs while providing better security.
- **Lateral Movement Prevention:** Compromising one device does not grant automatic access to other internal resources.

## 4. Transition Challenges
- **Legacy Systems:** Many older applications do not support modern authentication protocols (OIDC, SAML).
- **Inventory Complexity:** Requires a perfect understanding of all users, devices, and services in the organization.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[oauth-and-oidc-security]]
- [[os-protection-rings]]
