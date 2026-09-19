---
title: "Fuzzy Hashing"
date: 2026-01-04
description: "Fuzzy hashing measures how similar two files are rather than whether they are identical, which helps spot malware variants. / Fuzzy hashing, dosyaların aynı olup olmadığını değil ne kadar benzediğini ölçer; zararlı yazılım varyantlarını yakalamaya yarar."
draft: false
tags: ["Blue Team", "Malware Analysis"]
categories: ["Writeups"]
related:
  - "[[Hashing_Algoritmalari|Hashing Algoritmaları (MD5, SHA-1, SHA-256)]]"
---

## 🇹🇷 Türkçe (TR)

### Giriş

Siber güvenlik dünyasında saldırganların sürekli geliştirdiği zararlı yazılımlar, savunma tarafında da yeni yöntemlerin ortaya çıkmasına neden oluyor. Klasik hash algoritmaları (MD5, SHA1, SHA256) dosyaların bütünlüğünü doğrulamak için çok güçlüdür. Ancak dosyada tek bir bit bile değişse tamamen farklı bir hash değeri üretirler. Bu durum, özellikle zararlı yazılımların ufak değişikliklerle tekrar dolaşıma sokulmasında, savunma tarafının işini zorlaştırır. İşte tam da bu noktada **fuzzy hashing** devreye girer.

### Fuzzy Hashing Nedir?

Fuzzy hashing (bulanık hashleme), dosyaların birebir aynı olup olmadığını değil, **ne kadar benzer** olduklarını ölçen bir tekniktir. Normal hash’ler sadece “aynı” veya “farklı” cevabını verirken, fuzzy hashing bir **benzerlik skoru** üretir. Örneğin, iki dosyanın %82 benzer olduğunu söyleyebilir.

### Nasıl Çalışır?

Yöntem algoritmaya göre değişir. Örneğin ssdeep, dosyayı içeriğe göre belirlenen parçalara ayırıp her parçanın özetini çıkarır; TLSH ise bayt dizilerinin istatistiksel dağılımından bir özet üretir. Sonunda iki dosyanın özeti karşılaştırılır ve bir benzerlik skoru hesaplanır.  
En bilinen fuzzy hashing algoritmaları:

- **ssdeep** (Context-Triggered Piecewise Hashing): 0-100 arası benzerlik skoru verir.
- **sdhash**
- **TLSH (Trend Micro Locality Sensitive Hash)**: bir mesafe değeri verir; değer ne kadar küçükse dosyalar o kadar benzerdir.

### Kullanım Alanları

- **Zararlı yazılım analizi:** Zararlı yazılımın farklı varyantlarını tespit etmek.
- **Olay Müdahalesi / Adli Analiz:** Şüpheli bir dosyanın daha önce görülen bir zararlı ile bağlantılı olup olmadığını anlamak.
- **Tehdit Avcılığı:** Ağda veya sistemde zararlı dosyaların değiştirilmiş sürümlerini bulmak.

### Örnek Senaryo

Bir saldırgan, bir zararlı yazılımı farklılaştırmak için sadece dosya içindeki bir string’i değiştirir. Normal hash’ler bu yeni dosyayı tamamen farklı gösterir. Ancak fuzzy hashing, iki dosyanın büyük oranda benzer olduğunu gösterir. Bu sayede analist, saldırganın aynı aileye ait zararlıyı tekrar kullanmaya çalıştığını fark eder.

### Sonuç

Fuzzy hashing, günümüzün dinamik tehdit ortamında sadece “dosyalar aynı mı?” sorusuna değil, “bu dosya daha önce gördüğüm bir zararlının türevi mi?” sorusuna da cevap verir. Bu yaklaşım, SOC analistlerinin ve siber güvenlik araştırmacılarının sık kullandığı tekniklerden biridir.

---

## 🇬🇧 English (EN)

### Introduction

In the cybersecurity landscape, attackers constantly create new variants of malware. Traditional hashing algorithms (MD5, SHA1, SHA256) are great for verifying file integrity, but even a single-bit change results in a completely different hash value. This makes it difficult for defenders when malware is slightly modified and redistributed. That’s where **fuzzy hashing** comes into play.

### What is Fuzzy Hashing?

Fuzzy hashing is a technique that measures **how similar** two files are, instead of checking whether they are identical. While traditional hashes only say “same” or “different,” fuzzy hashing produces a **similarity score**. For example, it may say two files are 82% similar.

### How Does It Work?

The method varies by algorithm. For example, ssdeep splits a file into content-defined pieces and hashes each piece, while TLSH builds a digest from the statistical distribution of byte sequences. The digests of two files are then compared to produce a similarity score.  
Some well-known fuzzy hashing algorithms include:

- **ssdeep** (Context-Triggered Piecewise Hashing): returns a 0-100 similarity score.
- **sdhash**
- **TLSH (Trend Micro Locality Sensitive Hash)**: returns a distance value; the smaller it is, the more similar the files.

### Use Cases

- **Malware Analysis:** Identify different variants of the same malware family.
- **Incident Response / Digital Forensics:** Check whether a suspicious file is related to previously known malware.
- **Threat Hunting:** Detect modified versions of malicious files within a network or system.

### Example Scenario

An attacker modifies a malware sample by changing just a string within the code. Traditional hashes show the new file as completely different. However, fuzzy hashing detects that the two files are largely similar, allowing analysts to identify that the attacker is reusing a known malware family.

### Conclusion

Fuzzy hashing provides defenders with the ability to not only answer “Are these files identical?” but also “Is this file a variant of something I’ve seen before?” This makes it a commonly used technique for SOC analysts and cybersecurity researchers dealing with today’s evolving threats.
