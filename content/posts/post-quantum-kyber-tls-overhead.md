---
title: "Post-Quantum Handshake Overhead | Post-Kuantum TLS ve Kyber768 Maliyeti"
date: 2026-07-20
description: "Real-world engineering challenges, packet fragmentation, and latency overhead of deploying Kyber768 in TLS 1.3. / TLS 1.3 protokolünde Kyber768 kullanımının gerçek dünya ağ maliyetleri ve paket parçalanması."
tags: ["Post-Quantum", "Cryptography", "TLS 1.3", "Networking", "Kyber768"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/xiaohei-post-quantum-kyber-tls-overhead-1.jpg"
    alt: "Post-Quantum Kyber TLS Overhead Illustration"
    relative: false
---

## 🇹🇷 Türkçe (TR)

### Giriş: Kuantum Sonrası Şifrelemenin Ağ Katmanındaki Gerçekliği

Kuantum bilgisayarların Shor algoritması ile mevcut RSA ve ECC (Elliptic Curve Cryptography) açık anahtarlı şifreleme yöntemlerini kırma potansiyeli, siber güvenlik dünyasını **Post-Quantum Cryptography (PQC)** standartlarına geçmeye zorlamıştır. NIST tarafından standartlaştırılan ML-KEM (Kyber768) algoritması, Cloudflare, Google Chrome ve AWS gibi devler tarafından TLS 1.3 protokolüne **X25519Kyber768** hibrit anahtar değişim mekanizması olarak entegre edilmiştir.

Ancak teorik matematiksel güvenlik sağlayan bu geçiş, ağ mühendisliği tarafında ciddi ve öngörülmeyen problemler doğurmuştur: **Büyük Anahtar Boyutları ve Ağ Paketi Parçalanması (Packet Fragmentation)**.

![İllüstrasyon / Illustration](/img/xiaohei-post-quantum-kyber-tls-overhead-1.jpg)

---

### Kyber768 ve TLS 1.3 Handshake Sancıları

Klasik TLS 1.3 el sıkışmasında (Handshake) kullanılan Elliptic Curve X25519 anahtar değişiminde, istemcinin gönderdiği public key sadece **32 bayt** büyüklüğündedir. Bu küçük veri miktarı, ilk TCP SYN/ACK paketlerinin hemen ardından gelen tek bir `ClientHello` IP paketine kolayca sığar.

Ancak kafes tabanlı (Lattice-based) bir algoritma olan Kyber768 devreye girdiğinde durum radikal şekilde değişir:

* **X25519 Public Key:** 32 bayt
* **Kyber768 Public Key:** 1.184 bayt
* **X25519Kyber768 Hybrid ClientHello:** ~1.250 - 1.500 bayt

#### Paket Parçalanması (MTU & TCP MSS Exceeded)
Standart bir Ethernet ağında Maksimum İletim Birimi (MTU) **1.500 bayt** ile sınırlıdır. TLS başlıkları, IP başlıkları ve Kyber public key verisi birleştiğinde, `ClientHello` mesajı 1.500 bayt sınırını aşarak **iki ayrı TCP segmentine parçalanır (fragmentation)**.

---

### Gerçek Dünya Performans Maliyetleri ve Ağ Zafiyetleri

1. **Middlebox & Legacy Firewall Drop Riski:** Eski nesil güvenlik duvarları (Firewall) ve WAF cihazları, parçalanmış veya alışılagelmişin dışında büyük `ClientHello` paketlerini şüpheli trafik olarak değerlendirip sessizce düşürebilir (packet drop). Bu durum bazı ağlarda TLS bağlantısının tamamen zaman aşımına (timeout) uğramasına neden olur.
2. **Ekstra RTT (Round-Trip Time) Gecikmesi:** Paket parçalandığında ve kayıplar yaşandığında, TCP retransmission ve ek RTT süreleri devreye girer. Bu durum web sitelerinin açılış süresini (TTFB) 50ms ile 300ms arasında geciktirebilir.
3. **Amplification DoS Riskleri:** Büyük paket boyutları, UDP tabanlı QUIC ve HTTP/3 protokollerinde saldırganların yansıtma (amplification) DoS saldırıları yapma riskini artırır.

---
---

## 🇬🇧 English (EN)

### Introduction: The Network Layer Reality of Post-Quantum Cryptography

The threat of quantum computers leveraging Shor’s algorithm to compromise modern RSA and Elliptic Curve Cryptography (ECC) has accelerated the deployment of **Post-Quantum Cryptography (PQC)**. The National Institute of Standards and Technology (NIST) standardized ML-KEM (Kyber), prompting major infrastructure providers (such as Cloudflare, Google, and AWS) to deploy hybrid key exchanges—combining classical X25519 with lattice-based Kyber768 (**X25519Kyber768**) within TLS 1.3.

While hybrid PQC guarantees resistance against "harvest now, decrypt later" adversary campaigns, its real-world implementation exposes severe network protocol challenges: **Public Key Bloat and IP Packet Fragmentation**.

---

### Kyber768 and TLS 1.3 Handshake Bottlenecks

In conventional TLS 1.3 handshakes, the client shares an ECDH public key payload of merely **32 bytes**. This compact size fits effortlessly inside a single IP packet alongside standard TCP and TLS headers within the initial `ClientHello` record.

Transitioning to lattice-based cryptography fundamentally alters payload dynamics:

* **X25519 Public Key:** 32 bytes
* **Kyber768 Public Key:** 1,184 bytes
* **X25519Kyber768 Hybrid ClientHello Payload:** ~1,250 to 1,560 bytes

#### Packet Fragmentation Across MTU Boundaries
Standard Ethernet networks enforce a Maximum Transmission Unit (MTU) limit of **1,500 bytes**. When combined with outer IPv4/IPv6 headers, TCP options, and TLS record framing, a Kyber-enabled `ClientHello` exceeds the typical Maximum Segment Size (MSS), forcing the TCP stack to split the handshake initiation across **two distinct packets**.

---

### Engineering Impact: Middlebox Failures and Latency Overhead

1. **Middlebox & Legacy Firewall Packet Drops:** Outdated Network Address Translation (NAT) devices, legacy Firewalls, and Deep Packet Inspection (DPI) middleboxes often assume a `ClientHello` must reside within a single TCP segment. Multichunk TLS handshake records frequently trigger anomalies, leading to silent connection drops and TLS timeouts.
2. **Increased Round-Trip Latency (RTT):** Loss of a single fragmented segment requires TCP retransmission timeouts (RTO), increasing Time-To-First-Byte (TTFB) latencies by 50ms to 300ms on high-loss mobile networks.
3. **UDP & QUIC Amplification Risks:** Over QUIC/HTTP3, large ClientHello messages challenge initial congestion window limits, requiring precise server-side validation to prevent UDP amplification reflection attacks.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / Post Quantum Cryptography]]*
