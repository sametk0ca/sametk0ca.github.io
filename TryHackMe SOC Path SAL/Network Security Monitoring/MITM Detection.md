
A Man-in-the-Middle (MITM) attack is a cyberattack where an attacker secretly i==ntercepts and potentially alters communication between two parties, such as a user and a service, without their knowledge.== The attacker may eavesdrop to steal sensitive data like credentials and credit card info or inject malicious content. These attacks can target any organization or individual, especially where encryption or authentication is weak.

![[Pasted image 20251215125356.png]]

## How MITM Attacks Work

MITM attacks generally involve two main steps:

- **Interception**: The attacker inserts themselves into a communication stream, often by exploiting weaknesses in network protocols or by using techniques like ARP, DNS, or IP spoofing.
- **Manipulation/Decryption**: The attacker tries to access or modify the communication, decrypting encoded data or injecting harmful content, such as altered website responses or fake login forms.

## Common Types of MITM Attacks

- Packet sniffing: Capturing unencrypted data packets exchanged over a network, often on open Wi-Fi.
- Session hijacking: Stealing and using session tokens to impersonate users.
- SSL stripping: Downgrading HTTPS connections to insecure HTTP to steal or alter data transferred.
- DNS spoofing: Redirecting legitimate website traffic to fraudulent domains by manipulating DNS responses.
- IP spoofing: Crafting malicious IP packets that appear to come from trusted systems.
- Rogue Wi-Fi access point: Creating fake networks to intercept user traffic.


# ARP PROTOCOL

ARP (Address Resolution Protocol) maps IP addresses to MAC addresses in a local network. When a device wants to send data to another IP, it first asks: "Who has this IP?” The correct device replies with its MAC address.

## ARP Spoofing

In ARP spoofing, an attacker sends fake ARP replies to trick devices into associating the attacker’s MAC address with a legitimate IP, usually the default gateway. This allows the attacker to intercept, modify, or redirect traffic. 

ARP has **no authentication**. Any device can send unsolicited `is-at` messages. An attacker exploits this vulnerability by sending fake ARP replies to victims and gateways:

## Indicators of the Attack

We can look for the following key indicators while investigating the logs or network traffic for a potential Man-in-the-Middle attack using ARP spoofing.

- **Duplicate MAC-to-IP Mappings**: Multiple MAC addresses claiming the same IP address. Indicates impersonation.
- **Unsolicited ARP Replies**: High number of ARP replies without matching requests ("gratuitous ARP").
- **Abnormal ARP Traffic Volume:** A Large number of ARP packets in short intervals.
- **Unusual Traffic Routing**: Traffic rerouted through the attacker’s MAC.
- **Gateway Redirection Patterns:** Multiple destination MACs for the same gateway IP.
- **ARP Probe / Reply Loops**: Many ARP requests with `Who has 192.168.1.x? Tell 192.168.1.y` patterns.

# DNS SPOOFING

**DNS Spoofing** (or DNS Cache Poisoning) is when an attacker corrupts this system. They give your computer the wrong "phone number" for a website you're trying to visit.

This is a powerful technique for launching a **Man-in-the-Middle (MITM)** attack. Here's how it works:

1. **The Victim** tries to visit their bank at `my-real-bank.com`.
2. **The Attacker**, who is already on the local network (perhaps via ARP spoofing), intercepts the victim's DNS query.
3. **The Spoof:** The attacker quickly sends a **fake DNS response** to the victim. This fake response says, `my-real-bank.com` is at my IP address: `ATTACKER_IP`.
4. **The Interception:** The victim's computer trusts this fake response and saves it in its DNS cache. When the victim tries to connect to their bank, they unknowingly connect directly to the attacker's server, which might host a perfect replica of the real banking site.

The attacker is now `in the middle`, capturing everything the victim types, including their username and password.

![[Pasted image 20251215134248.png]]

## Indicators of the Attack

We can look for the following key indicators while investigating the logs or network traffic for a potential Man-in-the-Middle attack using DNS spoofing.

- **Multiple DNS responses for the same query**: A legitimate resolver and a forged responder reply to the same query. This is the single most reliable indicator.
- **DNS response from an unexpected source**: A DNS reply arrives from an IP address **that does not match any configured resolver** (like 8.8.8.8 or your DNS server).
- **Suspiciously short TTL (Time-To-Live) values**: Attackers use very low TTLs (1 - 30s) to keep poisoned entries short-lived and reassert control.
- **Unsolicited DNS responses**: A DNS reply appears without a corresponding DNS request from the victim.


# SSL STRIPPING (SSL DOWNGRADE)

SSL stripping is a man-in-the-middle technique in which an attacker intercepts and modifies traffic to remove or prevent TLS encryption between a client and a server. This causes the client to communicate over HTTP instead of HTTPS. The attacker retains a secure (HTTPS) session with the server while relaying plain HTTP to the victim, enabling eavesdropping and credential capture.

## How It Works

1. **The victim initiates an HTTPS request** to a website.
2. **The attacker intercepts the request** using ARP spoofing or a rogue access point.
3. **The attacker connects to the website over HTTPS** but relays the response to the victim through HTTP.
4. **The victim unknowingly interacts over HTTP**, exposing sensitive data in plaintext.

## Indicators of SSL stripping

- **Initial Request vs. Response:** The user's initial request may be for `HTTPS` (port 443), but the subsequent packets immediately shift to unencrypted `HTTP` (port 80) for the same domain.
- **Redirects/Link Rewriting**: Monitoring for redirects (HTTP Status Codes 301, 302) that persistently direct an HTTPS request to an HTTP resource.
- **Certificate Errors**: Although the attacker usually tries to hide this, the initial **TLS/SSL Handshake** may fail or display a self-signed certificate if the attacker uses a more direct proxying technique.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
