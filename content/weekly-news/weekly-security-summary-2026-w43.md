---
title: "Week 43 - 19/10 - 25/10"
date: 2026-10-25
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [BlackX UEFI Bootkit'i Secure Boot'u Geçmek İçin Baton Drop Zafiyetini İstismar Ediyor](https://www.bleepingcomputer.com/news/security/blackx-uefi-bootkit-exploits-baton-drop-flaw-to-bypass-secure-boot/)
**Kategori:** `Malware` | **Kaynak:** `BleepingComputer`

Yeni tespit edilen BlackX UEFI bootkit'i, Secure Boot mekanizmasını devre dışı bırakmak için Baton Drop zafiyetini kullanmaktadır. Siber casusluk operasyonlarında kullanılan bu gelişmiş zararlı yazılım, işletim sistemi yüklenmeden önce çalışarak güvenlik çözümlerinin sürücülerini engellemekte ve sistemde alt seviye kalıcılık sağlamaktadır.

### 2. [Yaygın PHP Zafiyeti Birçok Web Sitesinde Kesintilere Yol Açabilir](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
**Kategori:** `Vulnerability` | **Kaynak:** `Krebs on Security`

Web sitelerinin yaklaşık %70'ini etkileyen kritik PHP zafiyetleri, saldırganların hedef sunucularda uzaktan kod yürütmesine (RCE) ve tam kontrol elde etmesine imkan tanımaktadır. Aktif olarak istismar edildiği bildirilen bu zafiyet için sistem yöneticilerinin acilen yama güncellemelerini uygulaması gerekmektedir.

### 3. [AWS MCP Python Sandbox Yalıtımının Aşılması](https://www.reddit.com/r/netsec/comments/1xevj5i/breaking_the_aws_mcp_python_sandbox/)
**Kategori:** `Sandbox Escape` | **Kaynak:** `r/netsec`

Siber güvenlik araştırmacıları, AWS MCP Python Sandbox yapısındaki yalıtım sınırlarını ihlal ederek kısıtlı ortamdan kaçış (sandbox escape) sağlayan teknik bir zafiyet yayınladı. Çalışma, bulut tabanlı kod çalıştırma sandbox'larının ve konteyner izolasyon mekanizmalarının güvenlik zafiyetlerini teknik detaylarıyla göstermektedir.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [BlackX UEFI bootkit exploits Baton Drop flaw to bypass Secure Boot](https://www.bleepingcomputer.com/news/security/blackx-uefi-bootkit-exploits-baton-drop-flaw-to-bypass-secure-boot/)
**Category:** `Malware` | **Source:** `BleepingComputer`

The newly discovered BlackX UEFI bootkit exploits the Baton Drop flaw to bypass Secure Boot verification. Deployed in targeted cyber espionage campaigns, this bootkit loads before the operating system to interfere with security solution drivers and establish deep system persistence.

### 2. [Widespread PHP Flaw May Cause Many Site Outages Today](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
**Category:** `Vulnerability` | **Source:** `Krebs on Security`

Critical PHP vulnerabilities affecting nearly 70 percent of websites allow attackers to achieve remote code execution (RCE) and full server compromise. With working exploits actively circulating, security administrators are urged to apply emergency patches immediately.

### 3. [Breaking the AWS MCP Python Sandbox](https://www.reddit.com/r/netsec/comments/1xevj5i/breaking_the_aws_mcp_python_sandbox/)
**Category:** `Sandbox Escape` | **Source:** `r/netsec`

Security researchers published a technical breakdown demonstrating a sandbox escape vulnerability within the AWS MCP Python Sandbox environment. The research highlights core isolation bypass techniques and implementation flaws in cloud-hosted execution sandboxes.

