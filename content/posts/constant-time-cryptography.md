---
title: "Constant-Time Cryptography"
date: 2026-06-23
description: "Why mathematical encryption can fail on physical hardware and how constant-time code prevents timing attacks. / Matematiksel şifrelemenin fiziksel donanımda nasıl zayıfladığı ve sabit zamanlı kodun zamanlama saldırılarını nasıl önlediği."
draft: false
tags: ["Constant-Time", "Cryptography", "Side-Channel", "Cybersecurity", "Authentication"]
categories: ["Security"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/cover-1501139083538-0139883ac326.jpg"
    alt: "Hourglass symbolizing time and security"
    relative: false
related:
  - "[[concepts/constant-time-cryptography|Constant-Time Cryptography]]"
---

## 🇹🇷 Türkçe (TR)

### 1. Giriş: Kağıt Üzerindeki Kriptografi vs. Silikon Vadisi Gerçekleri

Kriptografi denildiğinde aklımıza genellikle kırılamaz matematiksel algoritmalar, devasa asal sayılar ve karmaşık şifreleme denklemleri gelir. Matematiksel olarak AES-256 veya RSA gibi algoritmaları kırmak, evrenin ömründen daha uzun sürebilir. Ancak bu algoritmalar kağıt üzerinde mükemmel olsalar da çalışmak için fiziksel bir donanıma (CPU, RAM, önbellek) ihtiyaç duyarlar. 

İşte siber güvenlik dünyasının en büyüleyici alanlarından biri burada başlar: **Yan Kanal Saldırıları (Side-Channel Attacks)**. Saldırganlar şifreleme matematiğini çözmek yerine, donanımın çalışırken sızdırdığı fiziksel ipuçlarını toplarlar. Bu ipuçlarının en yaygını ve yakalanması en kolay olanı **işlem süreleridir**. Bilgisayarın bir şifreyi doğrulamak için harcadığı nanosaniyelik zaman farklarını ölçerek şifreleme anahtarlarını çalma yöntemine **Zamanlama Saldırısı (Timing Attack)**, bunu engelleme felsefesine ise **Sabit Zamanlı Kriptografi (Constant-Time Cryptography)** denir.

### 2. Zamanlama Saldırıları Nasıl Çalışır? (Klasik `memcmp` Hatası)

Bir sunucuya giriş yapmak için şifrenizi gönderdiğinizi veya bir API isteğinin doğruluğunu kontrol etmek için bir doğrulama kodu (MAC tag) gönderdiğinizi düşünün. Sunucu, girdiğiniz kod ile hafızasındaki doğru kodu karşılaştırırken genellikle standart bir karşılaştırma fonksiyonu (C dilindeki `memcmp` veya birçok dildeki `==` operatörü) kullanır.

Klasik karşılaştırma algoritmaları hız için optimize edilmiştir: **İlk uyuşmayan karakteri buldukları anda taramayı durdurur ve hata dönerler.**

*   Doğru şifrenin `SECURITY` olduğunu varsayalım.
*   Saldırgan `AXXXXXXX` gönderir. Sistem 1. karaktere bakar ('S' ile 'A'). Eşleşme yok. Anında hata döner. İşlem süresi: **1.0 μs** (mikrosaniye).
*   Saldırgan `SXXXXXXX` gönderir. Sistem 1. karaktere bakar. Eşleşti! 2. karaktere geçer ('E' ile 'X'). Eşleşme yok. Hata döner. İşlem süresi: **1.2 μs**.

Saldırgan, ağ gecikmelerini (jitter) filtreleyen istatistiksel analizler kullanarak bu farkı ölçebilir. Yukarıdaki süreler yalnızca gösterim amaçlıdır; gerçekte fark nanosaniyeler düzeyindedir ve binlerce ölçümün istatistiksel olarak birleştirilmesini gerektirir. Bayt bayt deneme yaparak, tüm kombinasyonları denemek yerine her bayt için en fazla 256 denemede doğru değeri bulabilir.

### 3. Karşılaştırma Akışı

Aşağıdaki diyagramda, standart karşılaştırma ile sabit zamanlı karşılaştırma arasındaki fark gösterilmektedir:

![Diyagram](/img/mermaid-constant-time-cryptography-1-a2982506.svg)

### 4. Sabit Zamanlı Kriptografi Prensipleri

Sabit Zamanlı Kriptografi yazmak sezgisel değildir ve modern derleyici (compiler) optimizasyonlarıyla savaşmayı gerektirir. Temel kurallar şunlardır:

1.  **Gizli Veriye Bağlı Dallanma Yasağı (No Secret-Branching):** Gizli bir verinin (anahtar, şifre) değerine göre çalışan hiçbir `if`, `else`, `while` bloğu olamaz. Çünkü işlemcinin dallanma tahmincisi (branch predictor) bu durumdan etkilenir ve süre değişir.
2.  **Gizli Veriye Bağlı Bellek Erişimi Yasağı (No Secret-Indexed Memory):** Gizli veriler, dizilerde indeks olarak kullanılamaz (örn: `S-Box[secret_key]`). Farklı indeksler işlemci önbelleğinde (L1/L2 cache) hit veya miss durumuna yol açarak bellek okuma sürelerini değiştirir.
3.  **Bit Düzeyinde Mantıksal İşlemler (Bitwise Logic):** Koşullu ifadeler yerine bit düzeyinde maskeleme işlemleri yapılır. Örneğin, bir koşul doğruysa `a`, yanlışsa `b` seçmek için `if` yerine `r = (mask & a) | (~mask & b)` gibi bir yapı kurulur (koşul doğruysa `mask` tüm bitleri 1, yanlışsa 0 olur).

### 5. Pratikte Ne Yapmalı?

Sabit zamanlı kodu kendiniz yazmak yerine, bunu zaten yapan kütüphane fonksiyonlarını kullanın. Gizli değerleri (MAC, token, parola özeti) karşılaştırırken `==` veya `memcmp` yerine şunlar tercih edilmelidir: Python'da `hmac.compare_digest`, Go'da `crypto/subtle.ConstantTimeCompare`, Node.js'te `crypto.timingSafeEqual`, OpenSSL'de `CRYPTO_memcmp`.

---

## 🇬🇧 English (EN)

### 1. Introduction: Cryptography on Paper vs. Silicon Reality

When we think of cryptography, we often picture unbreakable mathematical algorithms, massive prime numbers, and complex encryption equations. Mathematically, cracking algorithms like AES-256 or RSA could take longer than the age of the universe. However, while these algorithms are mathematically perfect on paper, they require physical hardware (CPU, RAM, cache) to execute.

This is where one of the most fascinating fields of cybersecurity begins: **Side-Channel Attacks**. Instead of attempting to break the mathematical security of the cipher, attackers collect physical clues leaked by the hardware during execution. The most common and easily measured of these clues is **execution time**. The methodology of stealing cryptographic keys by measuring nanosecond variations in validation processes is called a **Timing Attack**, and the defensive implementation standard is known as **Constant-Time Cryptography**.

### 2. How Timing Attacks Work: The Classic `memcmp` Flaw

Imagine logging into a server or sending an authentication token (MAC tag) to verify an API request. The server compares your input with the expected value in memory, often using a standard comparison function (such as `memcmp` in C or the `==` operator in many high-level languages).

Standard comparison algorithms are optimized for speed: **they terminate and return a mismatch as soon as they encounter the first incorrect byte.**

*   Suppose the correct password is `SECURITY`.
*   An attacker sends `AXXXXXXX`. The system checks the first character ('S' vs 'A'). No match. It immediately aborts and returns an error. Time taken: **1.0 μs** (microseconds).
*   An attacker sends `SXXXXXXX`. The system checks the first character. Match! It proceeds to check the second character ('E' vs 'X'). No match. It aborts and returns an error. Time taken: **1.2 μs**.

By performing statistical analysis to filter out network latency (jitter), an attacker can measure this difference. Through byte-by-byte validation (brute-forcing), they can guess the correct value in at most 256 attempts per byte, rather than testing every combination. The timings above are for illustration only: in reality the difference is on the order of nanoseconds and takes many thousands of measurements to extract statistically.

### 3. Comparison Workflow

The diagram below contrasts standard comparison with constant-time comparison:

![Diagram](/img/mermaid-constant-time-cryptography-2-73ab9594.svg)

### 4. Principles of Constant-Time Cryptography

Writing constant-time code is highly non-intuitive and requires fighting modern compiler optimizations. The main rules include:

1.  **No Secret-Dependent Branching:** You cannot use `if`, `else`, or `while` statements whose conditions depend on secret data (such as keys or plaintexts). Otherwise, CPU branch predictors will alter execution times.
2.  **No Secret-Indexed Memory Access:** Secrets must not be used as array indices (e.g., `S-Box[secret_key]`). Accessing varying memory addresses causes cache hits or misses in the CPU cache (L1/L2), altering retrieval times.
3.  **Use Bitwise Operations:** Conditional checks are replaced with bitwise logic. For example, selecting `a` if a condition is met and `b` otherwise is achieved with `r = (mask & a) | (~mask & b)` instead of an `if` block (`mask` is all ones when the condition is true and all zeros otherwise).

### 5. In Practice

Rather than writing constant-time code yourself, use library functions that already do it. When comparing secrets (MACs, tokens, password hashes), prefer these over `==` or `memcmp`: `hmac.compare_digest` in Python, `crypto/subtle.ConstantTimeCompare` in Go, `crypto.timingSafeEqual` in Node.js, and `CRYPTO_memcmp` in OpenSSL.
