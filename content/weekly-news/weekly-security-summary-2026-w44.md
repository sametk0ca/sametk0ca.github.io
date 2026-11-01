---
title: "Week 44 - 26/10 - 01/11"
date: 2026-11-01
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Mirage2FA, AiTM Vekili Aracılığıyla ÇMF'ye Rağmen 4.561 M365 Oturum Çerezini Çaldı (CVE-2026-69836 CVSS 10.0)](https://www.reddit.com/r/netsec/comments/1xkzjb0/mirage2fa_stole_4561_m365_session_cookies_despite/)
**Kategori:** `Vulnerability / Authentication Bypass` | **Kaynak:** `r/netsec`

Mirage2FA adlı Ortadaki Saldırgan (AiTM) vekil sunucu saldırısı, Çok Faktörlü Kimlik Doğrulamayı (MFA) baypas ederek 4.561 Microsoft 365 oturum çerezini çaldı. CVSS 10.0 olarak değerlendirilen CVE-2026-69836 zafiyetine karşı tespit kuralları ile Windows Hello for Business (WHfB) ve Cloud Kerberos Trust sıkılaştırma rehberleri yayınlandı.

### 2. [Yaygın PHP Zafiyeti Bugün Birçok Sitenin Kesintiye Uğramasına Neden Olabilir](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
**Kategori:** `Vulnerability / RCE` | **Kaynak:** `Krebs on Security`

Dünya genelindeki web sitelerinin yaklaşık yüzde 70'ini etkileyen iki kritik PHP zafiyeti, saldırganların hedef sunucularda uzaktan kod çalıştırarak (RCE) tam kontrol sağlamasına imkan tanıyor. Çalışan istismar kodlarının dolaşımda olması nedeniyle güncellenmeyen sistemlerde kitlesel erişim kesintileri ve sunucu ihlalleri bekleniyor.

### 3. [FBI, 6,3 Milyar Dolarlık Binance Kripto Soygununu Kuzey Koreli Hackerlara Bağladı](https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/)
**Kategori:** `Cyber Crime / APT` | **Kaynak:** `BleepingComputer`

FBI, Binance kripto para borsasından gerçekleştirilen ve tarihe geçen 6,3 milyar dolarlık devasa hırsızlığın arkasında Kuzey Kore devlet destekli 'TraderTraitor' APT grubunun olduğunu doğruladı. Bu olay şimdiye kadar kaydedilen en büyük kripto soygunu olurken devlete bağlı tehdit aktörlerinin finansal altyapılara yönelik yıkıcı etkisini gösteriyor.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Mirage2FA stole 4,561 M365 session cookies despite MFA via AiTM proxy (CVE-2026-69836 CVSS 10.0) : detection rules and WHfB/Cloud Kerberos Trust hardening guide](https://www.reddit.com/r/netsec/comments/1xkzjb0/mirage2fa_stole_4561_m365_session_cookies_despite/)
**Category:** `Vulnerability / Authentication Bypass` | **Source:** `r/netsec`

An Adversary-in-the-Middle (AiTM) proxy campaign dubbed Mirage2FA bypassed Multi-Factor Authentication (MFA) to exfiltrate 4,561 Microsoft 365 session cookies. Critical vulnerability CVE-2026-69836 (CVSS 10.0) highlights advanced session hijacking risks, prompting detection engineering rules and WHfB/Cloud Kerberos Trust hardening guidelines.

### 2. [Widespread PHP Flaw May Cause Many Site Outages Today](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/)
**Category:** `Vulnerability / RCE` | **Source:** `Krebs on Security`

A pair of critical vulnerabilities in core PHP software affecting nearly 70 percent of global websites allows remote attackers to gain full server control. With active exploit code available, security experts warn of widespread service disruptions and server compromise risks for unpatched environments.

### 3. [FBI links $6.3 billion Binance crypto heist to North Korean hackers](https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/)
**Category:** `Cyber Crime / APT` | **Source:** `BleepingComputer`

The FBI confirmed that North Korean state-sponsored APT group TraderTraitor was responsible for the record-breaking $6.3 billion cryptocurrency theft from Binance. Standing as the largest crypto heist in history, the incident underscores the massive operational capability of nation-state actors targeting financial ecosystems.

