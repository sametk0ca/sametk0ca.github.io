+++
title = "DNS Poisoning  Hijacking | DNS Poisoning Hijacking"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

DNS (İsim Çözümleme) saldırıları, internetin "telefon rehberini" bozarak sizi gitmek istediğiniz site yerine saldırganın hazırladığı sahte bir siteye yönlendirmeyi hedefler.

### 1. DNS Poisoning (Zehirlenme)
DNS sunucularının önbelleğine (cache) sahte kayıtlar yerleştirme işlemidir.
- **Nasıl Çalışır?** Bir DNS sunucusu başka bir sunucudan bilgi beklerken, saldırgan çok hızlı davranıp sahte cevabı gönderir. Sunucu bu cevabı gerçek sanıp hafızasına kaydeder. O andan itibaren o sunucuyu kullanan herkes yanlış siteye gider.

### 2. DNS Hijacking (Gasp)
Bilgisayarınızın veya modeminizin DNS ayarlarının doğrudan değiştirilmesidir.
- **Nasıl Çalışır?** Bilgisayarınıza bulaşan bir virüs, DNS ayarlarınızı "8.8.8.8" (Google) yerine saldırganın kendi sunucusuna çevirir. Artık her aramanızda kontrol tamamen saldırgandadır.

### 3. Bilmen Gereken Bazı Terimler
- **DNS Cache:** Hız kazanmak için IP bilgilerinin geçici olarak hafızada tutulması.
- **Authoritative Server:** Bir domain adının (Örn: `google.com`) gerçek ve kesin IP bilgisini tutan ana sunucu.
- **DNSSEC:** DNS verilerini dijital olarak imzalayarak, verinin yolda değiştirilmesini engelleyen güvenlik protokolü.

### 4. Korunma Yolları
- **Güncel Yazılım:** İşletim sisteminizi ve modem yazılımınızı (firmware) güncel tutun.
- **Güvenilir DNS:** Google (8.8.8.8) veya Cloudflare (1.1.1.1) gibi güvenilir ve DNSSEC destekleyen sunucular kullanın.
- **Modem Şifresi:** Modemin arayüz şifresini asla varsayılan (admin/admin) bırakmayın; saldırganlar modeme girip DNS'i oradan değiştirirler.

### Gerçek Dünya Analojisi
Mahalledeki muhtarın (DNS Sunucusu) masasında duran telefon rehberini düşünün. Bir hırsız gizlice rehbere girip "Polis İmdat" numarasının karşısına kendi telefon numarasını yazar. Siz polisi aradığınızı sanırken hırsızın evine bağlanırsınız.

---

## English Version

DNS (Name Resolution) attacks aim to corrupt the internet's "phone book" and direct you to a fake site prepared by the attacker instead of the site you want to go to.

### 1. DNS Poisoning
It is the process of placing fake records in the cache of DNS servers.
- **How ​​Does It Work?** While a DNS server is waiting for information from another server, the attacker acts very quickly and sends the fake response. The server thinks this answer is real and saves it in its memory. From then on, everyone who uses that server goes to the wrong site.

### 2. DNS Hijacking (Extortion)
It is a direct change of the DNS settings of your computer or modem.
- **How ​​Does It Work?** A virus that infects your computer changes your DNS settings to the attacker's own server instead of "8.8.8.8" (Google). Now, every time you call, the attacker has complete control.

### 3. Some Terms You Should Know
- **DNS Cache:** Temporarily keeping IP information in memory to gain speed.
- **Authoritative Server:** The main server that keeps the real and precise IP information of a domain name (Ex: `google.com`).
- **DNSSEC:** Security protocol that prevents the data from being changed in transit by digitally signing DNS data.

### 4. Ways of Protection
- **Current Software:** Keep your operating system and modem software (firmware) up to date.
- **Trusted DNS:** Use reliable servers that support DNSSEC, such as Google (8.8.8.8) or Cloudflare (1.1.1.1).
- **Modem Password:** Never leave the modem's interface password as default (admin/admin); attackers break into the modem and change the DNS from there.

### Real World Analogy
Think of the phone book sitting on the desk of the neighborhood headman (DNS Server). A thief secretly enters the phone book and writes his own phone number opposite the "Police Emergency" number. While you think you are calling the police, you are connected to the thief's house.
