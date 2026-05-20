# Wireless Security (WPA3 and OWE)

- **Source:** [[ka-network-security]]
- **Tags:** #network-security #wireless #wpa3 #owe #encryption

## Overview
Wireless networks are inherently prone to eavesdropping due to the broadcast nature of the medium. Security has evolved from the broken WEP/WPA standards to the modern WPA3.

## 1. WPA2 (Legacy Standard)
- **Mechanism:** Uses AES-CCMP for encryption.
- **Weakness:** The 4-way handshake is vulnerable to offline dictionary attacks (KRACK attack) and lacks **Forward Secrecy**.

## 2. WPA3 (Modern Standard)
Introduced in 2018 to address the deficiencies of WPA2.
- **SAE (Simultaneous Authentication of Equals):** Replaces the PSK handshake with the **Dragonfly Key Exchange**.
    - **Benefit:** Resistant to offline dictionary attacks and provides **Forward Secrecy**.
- **WPA3-Personal:** Uses 128-bit encryption.
- **WPA3-Enterprise:** Uses 192-bit encryption for higher assurance environments.

## 3. OWE (Opportunistic Wireless Encryption)
Designed for public "Open" hotspots (e.g., at airports) where no password is used.
- **Problem:** Traditional open networks send all traffic in the clear.
- **Solution:** OWE performs a Diffie-Hellman key exchange during the initial connection to provide unauthenticated encryption.
- **Benefit:** Protects against passive eavesdropping without requiring user-provided credentials.

## 4. WPA3-SAE vs. OWE
- **SAE:** Authenticated encryption (requires a password). Protects against active and passive attacks.
- **OWE:** Unauthenticated encryption (no password). Protects only against passive eavesdropping.

## Related Concepts
- [[key-agreement-protocols]] (Diffie-Hellman)
- [[forward-and-post-compromise-security]]
- [[network-attacker-models]]
