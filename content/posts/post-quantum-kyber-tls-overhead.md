---
title: "Post-Quantum Handshake Overhead | Post-Kuantum TLS ve Kyber768 Maliyeti"
date: 2026-07-20
description: "Real-world engineering challenges, packet fragmentation, and latency overhead of deploying Kyber768 in TLS 1.3. / TLS 1.3 protokolünde Kyber768 kullanımının gerçek dünya ağ maliyetleri ve paket parçalanması."
draft: false
tags: ["Post-Quantum", "Cryptography", "TLS 1.3", "Networking", "Kyber768"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/xiaohei-post-quantum-kyber-tls-overhead-1.jpg"
    alt: "Post-Quantum Kyber TLS Overhead Illustration"
    relative: false
related:
  - "[[concepts/post-quantum-cryptography|Post-Quantum Cryptography (PQC)]]"
---

## 🇹🇷 Türkçe (TR)

### Giriş: Kuantum Sonrası Şifrelemenin Ağ Katmanındaki Gerçekliği

Kuantum bilgisayarların Shor algoritması ile mevcut RSA ve ECC (Elliptic Curve Cryptography) açık anahtarlı şifreleme yöntemlerini kırma potansiyeli, siber güvenlik dünyasını **Post-Quantum Cryptography (PQC)** standartlarına geçmeye zorlamıştır. NIST tarafından ML-KEM (FIPS 203) adıyla standartlaştırılan Kyber algoritması, Cloudflare, Google Chrome ve AWS gibi devler tarafından TLS 1.3 protokolüne **X25519Kyber768** hibrit anahtar değişim mekanizması olarak entegre edilmiştir. (Standartlaşmadan sonra bu grup, aynı boyutlarla **X25519MLKEM768** adına geçmiştir.)

Ancak teorik matematiksel güvenlik sağlayan bu geçiş, ağ mühendisliği tarafında ciddi ve öngörülmeyen problemler doğurmuştur: **Büyük Anahtar Boyutları ve Ağ Paketi Parçalanması (Packet Fragmentation)**.

![İllüstrasyon](/img/xiaohei-post-quantum-kyber-tls-overhead-1.jpg)

### Kyber768 ve TLS 1.3 Handshake Sancıları

Klasik TLS 1.3 el sıkışmasında (Handshake) kullanılan Elliptic Curve X25519 anahtar değişiminde, istemcinin gönderdiği public key sadece **32 bayt** büyüklüğündedir. Bu küçük veri miktarı, ilk TCP SYN/ACK paketlerinin hemen ardından gelen tek bir `ClientHello` IP paketine kolayca sığar.

Ancak kafes tabanlı (Lattice-based) bir algoritma olan Kyber768 devreye girdiğinde durum radikal şekilde değişir:

* **X25519 Public Key:** 32 bayt
* **Kyber768 Public Key:** 1.184 bayt
* **X25519Kyber768 Hibrit Anahtar Payı:** 32 + 1.184 = 1.216 bayt (sunucunun yanıtındaki Kyber768 şifreli metni de 1.088 bayttır)
* **Toplam `ClientHello`:** diğer uzantılarla birlikte genellikle ~1,5 KB'ı aşar

#### Paket Parçalanması (MTU & TCP MSS Exceeded)

Standart bir Ethernet ağında Maksimum İletim Birimi (MTU) **1.500 bayt** ile sınırlıdır. TLS başlıkları, IP başlıkları ve Kyber public key verisi birleştiğinde, `ClientHello` mesajı tek bir TCP segmentine sığmaz ve **iki ayrı TCP segmentine bölünür**.

### Gerçek Dünya Performans Maliyetleri ve Ağ Zafiyetleri

1. **Middlebox & Legacy Firewall Drop Riski:** Eski nesil güvenlik duvarları (Firewall) ve WAF cihazları, parçalanmış veya alışılagelmişin dışında büyük `ClientHello` paketlerini şüpheli trafik olarak değerlendirip sessizce düşürebilir (packet drop). Bu durum bazı ağlarda TLS bağlantısının tamamen zaman aşımına (timeout) uğramasına neden olur.
2. **Ekstra RTT (Round-Trip Time) Gecikmesi:** Paketlerden biri kaybolduğunda TCP yeniden iletimi (retransmission) ve zaman aşımı devreye girer. Ortalama etki küçük olsa da, kayıplı ağlarda (özellikle mobilde) ilk bayta kadar geçen süre (TTFB) belirgin şekilde uzayabilir.
3. **QUIC ve Amplification Sınırları:** UDP tabanlı QUIC ve HTTP/3'te sunucu, doğrulanmamış bir istemciye aldığının en fazla 3 katı kadar veri gönderebilir. Büyük post-kuantum mesajları bu sınırı zorlayarak ek gidiş-dönüş gerektirebilir; sunucu tarafında yansıtma (amplification) saldırılarına karşı dikkatli doğrulama şarttır.

---

## 🇬🇧 English (EN)

### Introduction: The Network Layer Reality of Post-Quantum Cryptography

The threat of quantum computers leveraging Shor’s algorithm to compromise modern RSA and Elliptic Curve Cryptography (ECC) has accelerated the deployment of **Post-Quantum Cryptography (PQC)**. The National Institute of Standards and Technology (NIST) standardized Kyber as ML-KEM (FIPS 203), and major infrastructure providers (such as Cloudflare, Google, and AWS) deploy hybrid key exchanges—combining classical X25519 with lattice-based Kyber768 (**X25519Kyber768**) within TLS 1.3. (After standardization, this group moved to the name **X25519MLKEM768** with the same sizes.)

While hybrid PQC protects against "harvest now, decrypt later" adversary campaigns, its real-world implementation exposes severe network protocol challenges: **Public Key Bloat and IP Packet Fragmentation**.

### Kyber768 and TLS 1.3 Handshake Bottlenecks

In conventional TLS 1.3 handshakes, the client shares an ECDH public key payload of merely **32 bytes**. This compact size fits effortlessly inside a single IP packet alongside standard TCP and TLS headers within the initial `ClientHello` record.

Transitioning to lattice-based cryptography fundamentally alters payload dynamics:

* **X25519 Public Key:** 32 bytes
* **Kyber768 Public Key:** 1,184 bytes
* **X25519Kyber768 Hybrid Key Share:** 32 + 1,184 = 1,216 bytes (the Kyber768 ciphertext in the server's reply is 1,088 bytes)
* **Total `ClientHello`:** typically exceeds ~1.5 KB once the other extensions are included

#### Packet Fragmentation Across MTU Boundaries

Standard Ethernet networks enforce a Maximum Transmission Unit (MTU) limit of **1,500 bytes**. When combined with outer IPv4/IPv6 headers, TCP options, and TLS record framing, a Kyber-enabled `ClientHello` exceeds the typical Maximum Segment Size (MSS), forcing the TCP stack to split the handshake initiation across **two distinct segments**.

### Engineering Impact: Middlebox Failures and Latency Overhead

1. **Middlebox & Legacy Firewall Packet Drops:** Outdated Network Address Translation (NAT) devices, legacy Firewalls, and Deep Packet Inspection (DPI) middleboxes often assume a `ClientHello` must reside within a single TCP segment. Multichunk TLS handshake records frequently trigger anomalies, leading to silent connection drops and TLS timeouts.
2. **Increased Round-Trip Latency (RTT):** Loss of one of the segments triggers TCP retransmission and timeouts. The average impact is small, but on lossy networks (especially mobile), Time-To-First-Byte (TTFB) can grow noticeably.
3. **QUIC and Amplification Limits:** Over QUIC/HTTP3, a server may send at most three times the data it has received to an unvalidated client. Large post-quantum messages can hit this limit and require an extra round trip, and servers need precise validation to prevent UDP amplification reflection attacks.
