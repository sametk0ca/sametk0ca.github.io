+++
title = "WiFi Standartları (802.11) | WiFi Standards (802.11)"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
+++

WiFi, yerel alan ağlarında kablosuz veri iletimi için kullanılan temel teknolojidir. Siber güvenlik uzmanı için WiFi, saldırı yüzeyinin en geniş olduğu alanlardan biridir.

### 1. Standartlar ve Hızlar
- **802.11 b/g/n/ac/ax:** Her yeni nesil daha yüksek hız ve daha geniş frekans (2.4GHz / 5GHz / 6GHz) sunar. 
- **Güvenlik Notu:** Daha eski standartlar (b/g), saldırganların trafiği yakalamasını kolaylaştıracak daha zayıf modülasyonlar kullanabilir.

### 2. Şifreleme Protokolleri (Kritik)
- **WEP:** Zayıf RC4 algoritması nedeniyle dakikalar içinde kırılabilir. Asla kullanılmamalıdır.
- **WPA / WPA2 (TKIP/AES):** WPA2-AES (CCMP) uzun süre standart kalmıştır. Ancak **KRACK** gibi zafiyetler, WPA2 trafiğinin şifresinin çözülebileceğini göstermiştir.
- **WPA3:** En güncel standarttır. **SAE (Simultaneous Authentication of Equals)** protokolü ile "offline sözlük saldırılarına" (handshake kırma) karşı koruma sağlar.

### 3. Zayıf Noktalar
- **WPS (Wi-Fi Protected Setup):** Bir butonla bağlanmayı sağlayan bu özellik, 8 haneli PIN kodu üzerinden kaba kuvvet saldırısı ile kırılabilir.
- **Evil Twin (Kötü İkiz):** Saldırganın meşru ağla aynı isimde (SSID) bir ağ kurarak kullanıcıları kendi cihazına bağlaması saldırısıdır.

---

## English Version

WiFi is the basic technology used for wireless data transmission in local area networks. For the cybersecurity professional, WiFi is one of the areas with the largest attack surface.

### 1. Standards and Speeds
- **802.11 b/g/n/ac/ax:** Each new generation offers higher speed and wider frequency (2.4GHz / 5GHz / 6GHz). 
- **Security Note:** Older standards (b/g) may use weaker modulations, making it easier for attackers to intercept traffic.

### 2. Encryption Protocols (Critical)
- **WEP:** Can be cracked in minutes due to weak RC4 algorithm. It should never be used.
- **WPA / WPA2 (TKIP/AES):** WPA2-AES (CCMP) has remained the standard for a long time. However, vulnerabilities such as **KRACK** have shown that WPA2 traffic can be decrypted.
- **WPA3:** It is the most current standard. It provides protection against "offline dictionary attacks" (handshake breaking) with the **SAE (Simultaneous Authentication of Equals)** protocol.

### 3. Weak Points
- **WPS (Wi-Fi Protected Setup):** This feature, which allows connection with a button, can be broken with a brute force attack via the 8-digit PIN code.
- **Evil Twin:** It is an attack in which the attacker connects users to his own device by establishing a network with the same name (SSID) as the legitimate network.
