---
title: "Week 29 - 13/07 - 19/07"
date: 2026-07-19
draft: false
tags: ["Weekly Summary", "Cyber Security", "Haftalık Özet"]
categories: ["Weekly Summary"]
ShowToc: true
---

## Türkçe

Bu hafta siber güvenlik dünyasında öne çıkan en kritik gelişmeler ve teknik detayları:

### 1. [Inc Ransomware Grubu, SonicWall SMA Zero-Day Zafiyetlerini İstismar Ediyor](https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days)
**Kategori:** `Zero-Day` | **Kaynak:** `Dark Reading`

Inc Ransomware fidye yazılımı aktörleri, SonicWall'un Güvenli Mobil Erişim (SMA) ağ geçitlerindeki iki adet sıfır gün (zero-day) zafiyetini aktif olarak suistimal etmektedir. Bu iki güvenlik açığının zincirleme (chaining) olarak kullanılması, saldırganların kimlik doğrulamayı atlayarak hedef ağ cihazlarında doğrudan en yetkili kullanıcı olan 'root' seviyesinde erişim kazanmalarına yol açmaktadır.

### 2. [WordPress Çekirdeğindeki 'wp2shell' RCE Zafiyetleri İçin Genel İstismar Kodları Yayınlandı](https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/)
**Kategori:** `Vulnerability` | **Kaynak:** `BleepingComputer`

WordPress çekirdek (core) yapısını etkileyen kritik 'wp2shell' uzaktan kod yürütme (RCE) zafiyetleri için çalışan genel istismar (exploit) kodları kamuoyuyla paylaşıldı. Bu durum, yetkisiz saldırganların savunmasız web sunucuları üzerinde tam kontrol ele geçirmesini son derece kolaylaştırdığı için sistem yöneticilerinin acilen güncelleme yapması gerekmektedir.

### 3. [Hemen Güncelleyin: 7-Zip, Zararlı Arşivlerle Tetiklenebilen RCE Zafiyetini Giderdi](https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/)
**Kategori:** `Vulnerability` | **Kaynak:** `BleepingComputer`

7-Zip'in 26.02 sürümü, özel olarak manipüle edilmiş sıkıştırılmış arşiv dosyalarının açılması sırasında tetiklenen kritik bir uzaktan kod yürütme (RCE) zafiyetini kapatmaktadır. Bellek bozma (memory corruption) temelli bu güvenlik açığı, hedef kullanıcının yalnızca zararlı bir arşivi açmasıyla saldırganların sistem üzerinde yetkisiz kod çalıştırmasına olanak tanımaktadır.

---

## English

The most critical cybersecurity developments and technical insights of the week:

### 1. [Inc Ransomware Exploits SonicWall SMA Zero-Days](https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days)
**Category:** `Zero-Day` | **Source:** `Dark Reading`

Threat actors associated with Inc Ransomware are actively exploiting two zero-day vulnerabilities in SonicWall's Secure Mobile Access (SMA) appliances. By chaining these two security flaws together, attackers can bypass security controls and gain root-level privileges on the targeted gateway devices.

### 2. [WordPress Core "wp2shell" RCE flaws get public exploits, patch now](https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/)
**Category:** `Vulnerability` | **Source:** `BleepingComputer`

Public exploits have been released for the critical 'wp2shell' remote code execution (RCE) vulnerabilities affecting the WordPress Core. This development allows unauthenticated attackers to execute arbitrary code on vulnerable servers, making immediate patch deployment highly critical for administrators.

### 3. [Update now: 7-Zip fixes RCE flaw exploitable with malicious archives](https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/)
**Category:** `Vulnerability` | **Source:** `BleepingComputer`

7-Zip version 26.02 addresses a critical remote code execution (RCE) vulnerability triggered during the parsing of specially crafted malicious archive files. This memory corruption flaw allows remote threat actors to execute arbitrary code on a victim's system simply by convincing them to open a compressed archive.

