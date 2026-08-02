---
title: "Week 31 - 27/07 - 02/08"
date: 2026-08-02
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Rails, RCE Potansiyeli Barındıran Kritik Active Storage Zafiyetini Yamaladı](https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/)
**Kategori:** `Vulnerability` | **Kaynak:** `BleepingComputer`

Active Storage bileşenindeki kritik bir güvenlik açığı, kimlik doğrulaması yapılmamış saldırganların Rails uygulamalarından rastgele dosyaları okumasına ve uzaktan kod yürütme (RCE) yetkisi elde etmesine olanak tanımaktadır. Bu zafiyet, dosya yükleme ve işleme mekanizmalarını hedef alarak uygulama sunucularının tamamen ele geçirilmesine yol açabilir.

### 2. [Microsoft, Rekor Sayıda 570 Güvenlik Açığını Yamaladı](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)
**Kategori:** `Vulnerability` | **Kaynak:** `Krebs on Security`

Microsoft, Windows işletim sistemleri ve ilişkili yazılımlarında bulunan ve önceki ayların rekorlarını neredeyse üçe katlayan rekor düzeyde 570 güvenlik açığını kapatan güncellemeler yayınladı. Bu devasa yama paketi, kritik sistem bileşenlerini hedef alan uzaktan kod yürütme, yetki yükseltme ve bilgi ifşası zafiyetlerini gidermektedir.

### 3. [LG, Akıllı TV Uygulamalarından Konut Tipi Proxy (Residential Proxy) Kullanımını Yasaklıyor](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/)
**Kategori:** `IoT Security` | **Kaynak:** `Krebs on Security`

LG Electronics, akıllı TV'leri sürekli aktif çalışan konut tipi proxy düğümlerine (residential proxy node) dönüştüren tüm uygulamaları askıya alacağını duyurdu. Yapılan araştırmalar, LG uygulama mağazasındaki oyun ve uygulamaların %42'sinden fazlasının, kullanıcıların internet bağlantılarını gizlice üçüncü taraflara kiralayan proxy SDK'ları barındırdığını ortaya koymuştur.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Rails patches critical Active Storage flaw with RCE potential](https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/)
**Category:** `Vulnerability` | **Source:** `BleepingComputer`

A critical vulnerability in the Active Storage framework allows unauthenticated attackers to read arbitrary files from Rails applications, potentially escalating to remote code execution (RCE). This flaw targets file upload and processing mechanisms, posing a severe risk of full application server compromise.

### 2. [Microsoft Patches a Record 570 Security Flaws](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)
**Category:** `Vulnerability` | **Source:** `Krebs on Security`

Microsoft released software updates patching a record-breaking 570 security vulnerabilities across Windows operating systems and associated software, nearly tripling previous monthly records. This massive patch release addresses highly critical flaws, including remote code execution, privilege escalation, and information disclosure vulnerabilities.

### 3. [LG to Ban Residential Proxies from Smart TV Apps](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/)
**Category:** `IoT Security` | **Source:** `Krebs on Security`

LG Electronics announced plans to suspend smart TV apps that secretly transform televisions into always-on residential proxy nodes. The decision follows research revealing that over 42 percent of available games and applications contained embedded SDKs that silently rented out users' internet bandwidth to third parties.

