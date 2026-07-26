---
title: "Week 30 - 20/07 - 26/07"
date: 2026-07-26
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Microsoft, Rekor Düzeyde 570 Güvenlik Açığını Yamaladı](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)
**Kategori:** `Vulnerability` | **Kaynak:** `Krebs on Security`

Microsoft, Windows işletim sistemleri ve diğer yazılımlarındaki rekor düzeydeki 570 güvenlik açığını kapatmak için toplu bir güncelleme paketi yayınladı. Geçen ayın rekorunu neredeyse üçe katlayan bu kritik yama döngüsü, siber saldırganların sistemler üzerinde yetki yükseltmesi ve uzaktan kod yürütmesini engellemeyi amaçlıyor.

### 2. [CVE-2026-46331 ile Claude Cowork Yerel VM Korumalı Alanından (Sandbox) Kaçış](https://www.reddit.com/r/netsec/comments/1v52lix/escaping_claude_coworks_local_vm_sandbox_via/)
**Kategori:** `Zero-Day` | **Kaynak:** `r/netsec`

Claude Cowork'un yerel sanal makine (VM) korumalı alanından (sandbox) kaçmayı sağlayan CVE-2026-46331 zafiyeti, AI tabanlı geliştirme araçlarının güvenlik sınırlarını hedef alıyor. Bu teknik zafiyet, saldırganların kısıtlı ortamları aşarak ana bilgisayar sisteminde izinsiz kod çalıştırmasına ve hassas verilere erişmesine olanak tanıyor.

### 3. [Zararlı Siteler Tarayıcı Belleğinde Kötü Amaçlı Yazılım Derlemek İçin JavaScript Kullanıyor](https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/)
**Kategori:** `Malware` | **Kaynak:** `BleepingComputer`

Büyük ölçekli bir kötü amaçlı reklamcılık (malvertising) kampanyası, popüler platformların sahte sürümlerini kullanarak tarayıcı belleğinde doğrudan zararlı yazılım oluşturuyor. JavaScript tabanlı HTML kaçakçılığı (HTML smuggling) yöntemini kullanan bu teknik, geleneksel disk taraması yapan güvenlik araçlarını atlatarak payload'u doğrudan RAM üzerinde birleştiriyor.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Microsoft Patches a Record 570 Security Flaws](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)
**Category:** `Vulnerability` | **Source:** `Krebs on Security`

Microsoft released software updates to patch a record-breaking 570 security vulnerabilities across Windows operating systems and other software, nearly tripling the previous month's record. This massive patch release aims to mitigate critical security flaws that could lead to unauthorized privilege escalation and remote code execution (RCE).

### 2. [Escaping Claude Cowork’s local VM sandbox via CVE-2026-46331](https://www.reddit.com/r/netsec/comments/1v52lix/escaping_claude_coworks_local_vm_sandbox_via/)
**Category:** `Zero-Day` | **Source:** `r/netsec`

The discovery of CVE-2026-46331, which enables escaping Claude Cowork's local virtual machine (VM) sandbox, highlights critical security challenges in local AI runtime environments. This vulnerability allows malicious actors to bypass containerization barriers, execute unauthorized code on the host operating system, and access sensitive data.

### 3. [Malicious sites use JavaScript to build malware in browser memory](https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/)
**Category:** `Malware` | **Source:** `BleepingComputer`

A massive malvertising campaign employs sophisticated spoofing of popular financial platforms to assemble malware directly in the browser's memory using malicious JavaScript. Utilizing HTML smuggling techniques, this attack evades traditional file-based endpoint detection (EDR) systems by reconstructing payloads dynamically inside RAM.

