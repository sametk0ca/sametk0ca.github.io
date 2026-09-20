---
title: "Week 38 - 14/09 - 20/09"
date: 2026-09-20
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Cisco Sıfır Gün Açıklığı API Uç Noktası Kimlik Doğrulama Sorunlarını Gözler Önüne Seriyor](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)
**Kategori:** `Zero-Day` | **Kaynak:** `Dark Reading`

Cisco Identity Services Engine (ISE) ürününü etkileyen bir kimlik doğrulama atlatma zafiyeti (CVE-2026-76460), en yüksek düzey olan 10.0 CVSS skoru almıştır. Bu aktif sömürülen sıfır gün (zero-day) açığı, uzak saldırganların kimlik doğrulama mekanizmalarını tamamen devre dışı bırakmasına olanak tanıyarak API uç noktası güvenliğindeki kritik zayıflıkları ortaya koymaktadır.

### 2. [Araştırmacılar OpenAI Codex Sandbox'ından Kaçarak Ana Makinede Komut Çalıştırdı](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host)
**Kategori:** `Vulnerability` | **Kaynak:** `BleepingComputer`

Güvenlik araştırmacıları, iki farklı yöntem kullanarak OpenAI'ın Codex sandbox (kum havuzu) ortamını başarıyla atlatmış ve geliştirici makinesinde uzaktan kod çalıştırma (RCE) elde etmiştir. OpenAI tarafından yamalanan bu açıklar, büyük dil modellerinde kod yürütme ortamlarının güvenliğini sağlamanın siber güvenlik dünyasındaki zorluklarını göstermektedir.

### 3. [Zararlı NPM Paketleri Çalışma Zamanında Kurulum Betiği Korumalarını Atlatıyor](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)
**Kategori:** `Malware` | **Kaynak:** `BleepingComputer`

Özellikle 'indexed-btree' paketini içeren zararlı bir npm yazılım tedarik zinciri kampanyası, geleneksel statik analiz ve kurulum betiği (install-script) savunmalarını çalışma zamanında (runtime) zararlı kod çalıştırarak aşmaktadır. Bu çalışma zamanı kaçınma taktiği, zararlı aktiviteleri meşru kod akışları içinde gizleyerek tespit edilmesini zorlaştırmaktadır.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Cisco Zero-Day Highlights API Endpoint Authentication Issues](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)
**Category:** `Zero-Day` | **Source:** `Dark Reading`

An authentication bypass vulnerability (CVE-2026-76460) impacting Cisco's Identity Services Engine (ISE) has received a maximum CVSS score of 10.0. The zero-day flaw highlights critical issues in API endpoint security, allowing remote attackers to bypass authentication mechanisms entirely.

### 2. [Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host)
**Category:** `Vulnerability` | **Source:** `BleepingComputer`

Security researchers successfully bypassed OpenAI's Codex sandbox environment using two distinct methods, achieving remote code execution (RCE) on the host developer machine. These flaws, which have now been patched, demonstrate the significant challenges of securing code execution environments within large language models.

### 3. [Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/)
**Category:** `Malware` | **Source:** `BleepingComputer`

A malicious npm software supply chain campaign, notably involving the 'indexed-btree' package, bypasses traditional static analysis and installation-script defenses by executing payload activity during standard application runtime. This runtime evasion tactic poses a stealthier threat as malicious actions are masked within legitimate execution flows.

