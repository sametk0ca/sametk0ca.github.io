---
title: "Post-Quantum Cryptography"
date: 2026-05-19
description: "Why quantum computers threaten RSA and ECC, the main PQC families, and NIST's FIPS 203/204/205 standards. / Kuantum bilgisayarların RSA ve ECC'yi neden tehdit ettiği, temel PQC aileleri ve NIST'in FIPS 203/204/205 standartları."
draft: false
tags: ["Cryptography", "Quantum Computing", "NIST", "CyBOK"]
categories: ["Security Future"]
related:
  - "[[concepts/post-quantum-cryptography|Post-Quantum Cryptography (PQC)]]"
  - "[[nist-pqc-2024|NIST PQC Standards (2024)]]"
  - "[[cryptographic-primitives|Cryptographic Primitives (Hard Problems)]]"
  - "[[post-quantum-kyber-tls-overhead|Post-Quantum Handshake Overhead]]"
---

## 🇹🇷 Türkçe (TR)

Kuantum bilgisayarların gelişimi, günümüzde dijital güvenliğin temelini oluşturan asimetrik şifreleme yöntemleri (RSA, ECC) için varoluşsal bir tehdit oluşturmaktadır. Shor Algoritması'nın kuantum işlemciler üzerinde çalışması, klasik bilgisayarlar için pratikte çözülemez kabul edilen tamsayı çarpanlarına ayırma (factoring) ve ayrık logaritma (discrete log) problemlerini, yeterince büyük bir kuantum bilgisayarda polinom zamanda çözebilir. Simetrik şifreleme ve hash fonksiyonları ise Grover algoritmasından daha az etkilenir; anahtar boyutunu büyütmek (örneğin AES-256) yeterlidir. **Post-Kuantum Kriptografi (PQC)**, kuantum bilgisayarların saldırılarına karşı dirençli matematiksel temellere dayanan yeni nesil kriptografik sistemleri temsil eder.

### Matematiksel Temeller ve Algoritmalar

CyBOK "Cryptography" bilgi alanı kapsamında incelenen PQC, farklı matematiksel zorluklara dayanan birkaç temel sınıfa ayrılır:

1. **Kafes Temelli Kriptografi (Lattice-based Cryptography):** En güçlü adaydır. Çok yüksek boyutlu matematiksel kafes yapılarındaki "Shortest Vector Problem" (SVP) ve "Learning With Errors" (LWE) gibi zorluklara dayanır.
2. **Kod Temelli Kriptografi (Code-based Cryptography):** McEliece kripto sistemi gibi, hata düzeltme kodlarının çözülmesinin zorluğuna dayanır.
3. **Çok Değişkenli Kriptografi (Multivariate Cryptography):** Çok değişkenli ikinci dereceden denklem sistemlerinin çözülmesinin zorluğunu kullanır.
4. **Karma Temelli Kriptografi (Hash-based Cryptography):** Dijital imzalar için kullanılır ve yalnızca güvenli özet (hash) fonksiyonlarına dayanır.

### NIST Standardizasyon Süreci ve FIPS Standartları

NIST (National Institute of Standards and Technology), 2016 yılında başlattığı global yarışma sonucunda PQC standartlarını belirlemiştir. Bu süreçte öne çıkan algoritmalar şunlardır:

* **FIPS 203 (ML-KEM):** Eskiden Kyber olarak bilinen kafes temelli anahtar kapsülleme mekanizması.
* **FIPS 204 (ML-DSA):** Eskiden Dilithium olarak bilinen kafes temelli dijital imza algoritması.
* **FIPS 205 (SLH-DSA):** SPHINCS+ tabanlı, vatansız (stateless) karma temelli imza şeması.

NIST ayrıca 2025'te kod temelli HQC algoritmasını yedek bir anahtar kapsülleme mekanizması olarak seçmiştir.

Pratikte geçiş genellikle **hibrit** yapılır: klasik ve post-kuantum algoritmalar birlikte kullanılır (örneğin TLS'te X25519 + ML-KEM). Böylece yeni algoritmada bir zayıflık çıksa bile klasik algoritmanın güvencesi korunur.

Kritik veriler için "Harvest Now, Decrypt Later" (Bugün Çal, Yarın Kır) riskine karşı, PQC geçiş süreçlerinin bugünden planlanması bir zorunluluktur.

---

## 🇬🇧 English (EN)

### Post-Quantum Cryptography: New Standards Against the Quantum Threat

The advancement of quantum computers poses an existential threat to asymmetric encryption methods (RSA, ECC) that form the foundation of today's digital security. The execution of Shor's Algorithm on quantum processors can solve integer factoring and discrete log problems—considered practically unsolvable for classical computers—in polynomial time on a sufficiently large quantum computer. Symmetric encryption and hash functions are affected much less by Grover's algorithm; larger key sizes (for example AES-256) are enough. **Post-Quantum Cryptography (PQC)** represents next-generation cryptographic systems based on mathematical foundations resistant to attacks from quantum computers.

### Mathematical Foundations and Algorithms

PQC, as studied within the CyBOK "Cryptography" knowledge area, is divided into several fundamental classes based on different mathematical hard problems:

1. **Lattice-based Cryptography:** The most prominent candidate. It relies on problems such as the "Shortest Vector Problem" (SVP) and "Learning With Errors" (LWE) within high-dimensional mathematical lattice structures.
2. **Code-based Cryptography:** Based on the difficulty of decoding error-correcting codes, such as the McEliece cryptosystem.
3. **Multivariate Cryptography:** Utilizes the hardness of solving systems of multivariate quadratic equations.
4. **Hash-based Cryptography:** Primarily used for digital signatures, relying solely on secure hash functions.

### NIST Standardization Process and FIPS Standards

NIST (National Institute of Standards and Technology) has determined PQC standards following a global competition initiated in 2016. The prominent algorithms in this process include:

* **FIPS 203 (ML-KEM):** A lattice-based key encapsulation mechanism, formerly known as Kyber.
* **FIPS 204 (ML-DSA):** A lattice-based digital signature algorithm, formerly known as Dilithium.
* **FIPS 205 (SLH-DSA):** A stateless hash-based signature scheme based on SPHINCS+.

In 2025, NIST also selected the code-based HQC algorithm as a backup key encapsulation mechanism.

In practice, the transition is usually **hybrid**: classical and post-quantum algorithms are used together (for example X25519 + ML-KEM in TLS). This way, even if a weakness is found in the new algorithm, the guarantees of the classical one remain.

Against the risk of "Harvest Now, Decrypt Later," it is imperative to plan the transition to PQC today for critical data protection.
