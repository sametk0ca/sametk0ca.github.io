---
title: "Bellek Adli Bilişimi: RAM Analizi ve Olay Müdahale Teknikleri"
date: 2026-04-11
draft: true
tags: ["Forensics", "DFIR", "Malware Analysis", "CyBOK"]
categories: ["Digital Forensics"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:800/1*A1B2C3D4E5F6G7H8I9.png"
    alt: "Memory Forensics"
    relative: false
---

![](https://miro.medium.com/v2/resize:fit:800/1*A1B2C3D4E5F6G7H8I9.png)

Modern siber saldırılar, geleneksel disk tabanlı adli bilişim (forensics) yöntemlerini atlatmak için giderek daha karmaşık hale gelmektedir. "Fileless" (dosyasız) zararlı yazılımlar ve doğrudan bellekte (RAM) çalışan kodlar, adli bilişim uzmanlarını **Bellek Adli Bilişimi (Memory Forensics)** tekniklerine yöneltmektedir. Bu disiplin, sistemin çalışma zamanındaki (run-time) durumunu analiz ederek, diskte iz bırakmayan saldırı kanıtlarını ortaya çıkarmayı amaçlar.

### Teknik Mekanizmalar ve Veri Yapıları

Bellek analizi, CyBOK "Digital Forensics" bilgi alanı altında incelenen, işletim sistemi çekirdek yapılarına (kernel structures) derinlemesine hakimiyet gerektiren bir süreçtir:

1. **Bellek Edinimi (Memory Acquisition):** Fiziksel belleğin (RAM) tam bir kopyasının (memory dump) alınması işlemidir. LiME, DumpIt veya WinPmem gibi araçlar kullanılır. "Order of Volatility" (Uçuculuk Sırası) prensibi uyarınca, bellek her zaman en öncelikli veri kaynağıdır.
2. **Anlamsal Boşluk (Semantic Gap):** Ham bit yığınlarından anlamlı işletim sistemi verilerinin (süreçler, ağ bağlantıları, şifreleme anahtarları) elde edilmesi sürecidir. Volatility Framework ve Rekall gibi araçlar, "Profile" ve "Symbol" dosyaları aracılığıyla bu boşluğu kapatır.
3. **Adres Çevrimi (Address Translation):** Sanal bellek adreslerinin fiziksel adreslere dönüştürülmesi için sayfa tablolarının (Page Tables) ve Directory Table Base (DTB) değerlerinin analiz edilmesidir. Bu, gizlenmiş (unlinked) süreçlerin tespitinde kritik rol oynar.

### Standartlar ve Olay Müdahale

NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident Response) standardı, bellek analizinin olay müdahale süreçlerine nasıl entegre edileceğine dair kapsamlı bir rehber sunar. Bellek analizi sayesinde; saldırganın C2 sunucusuyla kurduğu aktif soket bağlantıları, enjekte edilmiş kod parçaları (Code Injection) ve canlı oturumlardan elde edilen temizlenmemiş şifreler tespit edilebilir.

---

### Main Memory Forensics: RAM Analysis and Incident Response Techniques

Modern cyberattacks are becoming increasingly sophisticated to bypass traditional disk-based forensics. Fileless malware and code executing directly in memory (RAM) drive forensic experts toward **Memory Forensics**. This discipline aims to extract evidence of attacks that leave no trace on the disk by analyzing the run-time state of the system.

### Technical Mechanisms and Data Structures

Memory analysis is a process studied under the CyBOK "Digital Forensics" knowledge area, requiring deep knowledge of operating system kernel structures:

1. **Memory Acquisition:** The process of capturing a full copy (memory dump) of the physical RAM. Tools such as LiME, DumpIt, or WinPmem are utilized. According to the "Order of Volatility" principle, memory is always the highest-priority data source.
2. **Semantic Gap:** The process of deriving meaningful operating system data (processes, network connections, encryption keys) from raw bitstreams. Tools like the Volatility Framework and Rekall bridge this gap through "Profile" and "Symbol" files.
3. **Address Translation:** Analyzing Page Tables and Directory Table Base (DTB) values to translate virtual memory addresses into physical addresses. This plays a critical role in detecting hidden (unlinked) processes.

### Standards and Incident Response

The NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident Response) standard provides a comprehensive guide on integrating memory analysis into incident response workflows. Through memory forensics, active socket connections to an adversary's C2 server, injected code snippets, and uncleared passwords from live sessions can be identified.
