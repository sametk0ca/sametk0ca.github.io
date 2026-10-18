---
title: "Week 42 - 12/10 - 18/10"
date: 2026-10-18
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [PwnEscape: KVM Sanal Makineden Ana Bilgisayara Sızma Zafiyeti (CVE-2026-99999)](https://www.reddit.com/r/netsec/comments/1x7cvh3/pwnescape_guesttohost_kvm_escape_cve202699999/)
**Kategori:** `Vulnerability` | **Kaynak:** `r/netsec`

PwnEscape (CVE-2026-99999), saldırganların konuk sanal makine (guest) ortamından kaçarak doğrudan ana bilgisayar (host) üzerinde yetkisiz kod çalıştırmasına olanak tanıyan kritik bir hipervizör zafiyetidir. Sanallaştırma katmanını hedef alan bu açık, bulut altyapıları ve veri merkezleri için en yüksek teknik tehdit seviyesini temsil etmektedir.

### 2. [Saldırganlar ConnectWise Tedarik Zinciri Saldırısı ile Microsoft 365 Kiracılarına Sızdı](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)
**Kategori:** `Supply Chain Attack` | **Kaynak:** `BleepingComputer`

ConnectWise, saldırganların uygulama kimliklerini ele geçirip müşterilerin Microsoft 365 ortamlarını tehlikeye atması üzerine Cloud Backup hizmetine erişimi durdurdu. Tedarik zinciri yöntemiyle gerçekleştirilen bu karmaşık saldırı, güvenilir üçüncü taraf entegrasyonlarının yetkilerini kötüye kullanarak çok sayıda kurumsal kiracıya izinsiz erişim sağladı.

### 3. [Microsoft, 1.400'den Fazla Güvenlik Zafiyetini Kapattığı Rekor Güncelleme Paketini Yayınladı](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/)
**Kategori:** `Vulnerability` | **Kaynak:** `Krebs on Security`

Microsoft, Windows işletim sistemleri ve kurumsal yazılımlarındaki 1.400'den fazla güvenlik açığını gideren tarihi büyüklükte bir Salı Güncellemesi paketini erişime sundu. Önceki rekorları katlayan bu yama döngüsü, sistem mimarisindeki çok sayıda kritik ve uzaktan kod yürütme (RCE) zafiyetini kapatmaktadır.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [PwnEscape: Guest-to-Host KVM Escape (CVE-2026-99999)](https://www.reddit.com/r/netsec/comments/1x7cvh3/pwnescape_guesttohost_kvm_escape_cve202699999/)
**Category:** `Vulnerability` | **Source:** `r/netsec`

PwnEscape (CVE-2026-99999) is a critical hypervisor vulnerability that allows attackers to escape a virtual machine guest environment and execute code directly on the host system. Targeting the virtualization layer, this flaw represents a high-severity technical threat to cloud infrastructure and data centers.

### 2. [Hackers breach Microsoft 365 tenants via ConnectWise supply-chain attack](https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/)
**Category:** `Supply Chain Attack` | **Source:** `BleepingComputer`

ConnectWise suspended customer access to its Cloud Backup service after attackers compromised application identities to breach Microsoft 365 tenants. This sophisticated supply-chain attack leveraged trusted third-party integrations to gain unauthorized access to multiple enterprise tenants.

### 3. [Microsoft Patches More Than 1,400 Security Flaws](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/)
**Category:** `Vulnerability` | **Source:** `Krebs on Security`

Microsoft released an unprecedented Patch Tuesday update resolving over 1,400 security vulnerabilities across Windows operating systems and enterprise software. Shattering previous patch volume records, this cycle addresses numerous critical and remote code execution (RCE) flaws within core system architecture.

