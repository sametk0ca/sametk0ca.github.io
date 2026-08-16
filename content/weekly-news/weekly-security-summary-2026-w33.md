---
title: "Week 33 - 10/08 - 16/08"
date: 2026-08-16
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [CVE-2026-33696: n8n Platformunda Şema Adından Uzaktan Kod Çalıştırmaya (RCE)](https://www.reddit.com/r/netsec/comments/1vpx6ku/cve202633696_from_a_schema_name_to_rce_in_n8n/)
**Kategori:** `Vulnerability` | **Kaynak:** `r/netsec`

Popüler iş akışı otomasyon platformu n8n'de tespit edilen CVE-2026-33696 zafiyeti, güvensiz girdi doğrulaması nedeniyle şema adları üzerinden hedef sunucuda uzaktan kod çalıştırılmasına (RCE) imkan tanımaktadır. Bu zafiyet, karmaşık otomasyon süreçlerinin ve entegrasyonların manipüle edilerek sistem genelinde tam kontrol elde edilmesine yol açabileceğinden kritik öneme sahiptir.

### 2. [Microsoft Yaklaşık 400 Güvenlik Açığını Yamaladı](https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/)
**Kategori:** `Zero-Day` | **Kaynak:** `Krebs on Security`

Microsoft, Windows işletim sistemleri ve ilişkili yazılımlarında, biri aktif olarak istismar edilen sıfır-gün (zero-day) olmak üzere toplamda 398 güvenlik açığını kapatan devasa bir güncelleme paketi yayınladı. Aktif istismardaki zafiyetlerin varlığı ve kapatılan açıkların hacmi, kurumsal ağların savunulması için acil yama yönetimini kritik kılmaktadır.

### 3. [Yeni AmnesiaStealer macOS Zararlı Yazılımı Uzaktan Kontrol ile Tarayıcı Oturumlarını Ele Geçiriyor](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)
**Kategori:** `Malware` | **Kaynak:** `BleepingComputer`

macOS kullanıcılarını hedef alan AmnesiaStealer isimli yeni bilgi hırsızı zararlı yazılım, 'ClickFix' sosyal mühendislik yöntemleriyle yayılmakta ve entegre bir ekran yayını modülü barındırmaktadır. Bu modül sayesinde saldırganlar, kurbanın web tarayıcısını uzaktan ve etkileşimli olarak kontrol ederek aktif oturum çerezlerini ve hassas verileri doğrudan ele geçirebilmektedir.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [CVE-2026-33696: From a Schema Name to RCE in n8n](https://www.reddit.com/r/netsec/comments/1vpx6ku/cve202633696_from_a_schema_name_to_rce_in_n8n/)
**Category:** `Vulnerability` | **Source:** `r/netsec`

The CVE-2026-33696 vulnerability in the popular workflow automation platform n8n enables Remote Code Execution (RCE) by abusing inadequate input validation within schema names. This critical flaw allows attackers to compromise host systems and take full control over automated server environments.

### 2. [Microsoft Plugs Nearly 400 Security Holes](https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/)
**Category:** `Zero-Day` | **Source:** `Krebs on Security`

Microsoft released security updates patching nearly 400 vulnerabilities across its Windows ecosystems, including one actively exploited zero-day and two publicly disclosed flaws. The massive scale of these patches combined with in-the-wild exploitation demands immediate remediation from system administrators.

### 3. [New AmnesiaStealer macOS malware hijacks browser sessions via remote control](https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/)
**Category:** `Malware` | **Source:** `BleepingComputer`

A new macOS information stealer named AmnesiaStealer spreads via 'ClickFix' social engineering lures and features an interactive streaming module. This mechanism allows attackers to remotely control the victim's web browser in real-time, effectively hijacking active browser sessions and exfiltrating highly sensitive credentials.

