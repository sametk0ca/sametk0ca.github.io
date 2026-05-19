+++
title = "WiFi Standartları (802.11)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Hardware"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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