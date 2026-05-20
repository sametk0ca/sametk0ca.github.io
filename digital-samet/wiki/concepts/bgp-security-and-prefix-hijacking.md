# BGP Security and Prefix Hijacking

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #bgp #routing #internet

## Overview
The Border Gateway Protocol (BGP) is the "glue" of the Internet, allowing Autonomous Systems (ASs) to exchange routing information. Historically, BGP lacks inherent authentication, making the global routing table vulnerable.

## 1. BGP Prefix Hijacking
A malicious or misconfigured router announces an IP prefix that it does not own.
- **Goal:** Divert traffic intended for another network through the attacker's network.
- **Impact:** Eavesdropping (PITM), censorship (dropping traffic), or overloading an AS (DoS).
- **Sub-type (Route Leak):** Propagating routing information beyond its intended scope, violating peering agreements.

## 2. RPKI (Resource Public Key Infrastructure)
The primary modern defense for **Origin Validation**.
- **Mechanism:** Regional Internet Registries (RIRs) issue **ROAs (Route Origin Authorizations)** that bind an IP prefix to a specific authorized AS.
- **Enforcement:** Routers perform **ROV (Route Origin Validation)** to discard BGP announcements that contradict ROA data.

## 3. BGPsec
An extension to BGP designed for **Path Validation**.
- **Mechanism:** Routers sign their BGP updates, creating a cryptographic trace of the AS path.
- **Challenge:** High computational overhead and requires universal adoption to be fully effective. Deployment is currently very low.

## 4. ASPA (Autonomous System Provider Authorization)
A newer initiative to strengthen trust in the AS path by allowing ASs to cryptographically declare their authorized providers, helping detect "valley-free" routing violations.

## Related Concepts
- [[network-attacker-models]]
- [[distributed-consensus-and-paxos]]
- [[public-key-infrastructure]]
