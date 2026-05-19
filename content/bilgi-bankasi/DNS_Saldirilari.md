+++
title = "DNS Poisoning  Hijacking"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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