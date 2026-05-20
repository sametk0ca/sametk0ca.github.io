# Software Defined Networking (SDN) Security

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #sdn #nfv #virtualization

## Overview
SDN decouples the network control plane (deciding where traffic goes) from the data plane (forwarding packets). This architecture enables centralized management but introduces new attack vectors.

## 1. Security Opportunities
- **Dynamic Mitigation:** The central controller can instantly reprogram switches to drop malicious flows (e.g., during a DDoS).
- **Automated Quarantine:** Infected hosts can be automatically moved to a "walled garden" segment via software.
- **Micro-segmentation:** Easily creating isolated network partitions for different tenants or applications.

## 2. Security Threats

### Centralized Controller Vulnerability
The controller is a single point of failure and a high-value target.
- **Impact:** If the controller is compromised, the attacker has full control over the entire network topology and traffic.
- **DoS:** Flooding the controller with requests for new flows can exhaust its resources.

### Control Plane Communication
The interface between the controller and the switches (e.g., OpenFlow) must be secured (usually via TLS) to prevent spoofing or unauthorized command injection.

### Timing Side-Channels
Attackers can measure the time it takes for a switch to process a packet.
- **Mechanism:** If a packet takes longer, it likely triggered a new flow request to the controller. This can reveal information about internal communication patterns (e.g., whether a host recently accessed a specific service).

## 3. Network Functions Virtualization (NFV)
NFV replaces dedicated hardware (middleboxes) with software-based **Virtual Network Functions (VNFs)**.
- **Threat:** Compromising the underlying hypervisor can expose all VNFs running on the platform.
- **Benefit:** Allows for "security-as-a-service" where firewalls and IDSs can be rapidly deployed and scaled.

## Related Concepts
- [[os-design-paradigms]] (Virtualization)
- [[side-channel-formal-analysis]]
- [[network-intrusion-detection-ids-ips]]
