---
title: "Week 28 - 06/07 - 12/07"
date: 2026-07-12
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Ghostcommit, Yapay Zeka Ajanlarını Aldatmak ve Sırları Çalmak İçin Görüntülere Prompt Injection Gizliyor](https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/)
**Kategori:** `AI Security` | **Kaynak:** `BleepingComputer`

Araştırmacılar, 'Ghostcommit' adını verdikleri yöntemle PNG dosyalarının içine gizlenmiş prompt injection saldırılarının yapay zeka tabanlı kod inceleme araçlarını atlattığını gösterdi. Saldırı, yapay zeka kodlama ajanını depoların .env dosyalarını okumaya ve hassas bilgileri sızdırmaya ikna edebilmektedir. Bu durum, CI/CD süreçlerindeki yapay zeka entegrasyonlarının yeni nesil tedarik zinciri saldırılarına karşı ne kadar savunmasız olduğunu ortaya koymaktadır.

### 2. [RedHook Android Zararlı Yazılımı Kablosuz ADB ile Kabuk Erişimi Sağlıyor](https://www.bleepingcomputer.com/news/security/redhook-android-malware-now-uses-wireless-adb-for-shell-access/)
**Kategori:** `Malware` | **Kaynak:** `BleepingComputer`

RedHook Android zararlı yazılımının yeni bir sürümü, bir bilgisayar bağlantısına ihtiyaç duymadan kabuk seviyesinde yetkiler elde etmek için Android Kablosuz Hata Ayıklama (Wireless ADB) mekanizmasını istismar etmektedir. Bu yenilikçi yöntem sayesinde zararlı yazılım, standart uygulama izinlerini aşarak cihaz üzerinde yüksek yetkili komutlar çalıştırabilmektedir.

### 3. [Yeni ATM Kripto Yazılım Açıkları: Jackpot mu, Fiyasko mu?](https://www.darkreading.com/vulnerabilities-threats/atm-crypto-software-bugs-jackpot-bust)
**Kategori:** `Vulnerability` | **Kaynak:** `Dark Reading`

Microsoft BitLocker güvenlik sarmalayıcısındaki kritik zafiyetler, finansal kuruluşları ve ATM'leri ciddi bir ele geçirilme riskiyle karşı karşıya bırakmaktadır. Bu kriptografik açıklar, saldırganların güvenlik önlemlerini aşarak doğrudan ATM sistemlerine veya kurumsal ağlara yetkisiz erişim sağlamasına olanak tanıyabilir.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Ghostcommit hides prompt injection in images to fool AI agents, steal secrets](https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/)
**Category:** `AI Security` | **Source:** `BleepingComputer`

Researchers demonstrated 'Ghostcommit,' a technique that hides prompt injection payloads inside PNG images to bypass AI code reviewers like CodeRabbit and Bugbot, which fail to scan image files. The hidden payload then manipulates AI coding agents into reading .env files and exfiltrating repository secrets. This represents a significant shift in supply chain attacks targeting AI-integrated development workflows.

### 2. [RedHook Android malware now uses Wireless ADB for shell access](https://www.bleepingcomputer.com/news/security/redhook-android-malware-now-uses-wireless-adb-for-shell-access/)
**Category:** `Malware` | **Source:** `BleepingComputer`

A new variant of the RedHook Android malware abuses the Android Wireless Debugging (Wireless ADB) mechanism to gain shell-level privileges without requiring a physical USB connection to a computer. This novel technique allows the malware to bypass standard application permission boundaries and execute high-privilege commands directly on the compromised device.

### 3. [Fresh ATM Crypto Software Bugs: Jackpot or Bust?](https://www.darkreading.com/vulnerabilities-threats/atm-crypto-software-bugs-jackpot-bust)
**Category:** `Vulnerability` | **Source:** `Dark Reading`

Critical vulnerabilities discovered in a Microsoft BitLocker security wrapper put financial organizations and ATM hardware at risk of compromise. These cryptographic software flaws could allow attackers to bypass security layers and gain unauthorized access to underlying ATM systems or corporate networks.

