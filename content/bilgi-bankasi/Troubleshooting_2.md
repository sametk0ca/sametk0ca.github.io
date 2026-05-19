+++
title = "Sorun Giderme Araçları - Bölüm 2: nslookup ve dig"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Bu araçlar "DNS" sorunlarını teşhis etmek için kullanılır. "Bir sitenin ismini yazdığımda neden IP'sini bulamıyorum?" sorusunun yanıtı buradadır.

### 1. nslookup (Name System Lookup)
Hem Windows hem de Linux'ta bulunan temel bir DNS sorgulama aracıdır.
- **Kullanım:** `nslookup google.com` yazdığınızda size Google'ın hangi IP adreslerinde olduğunu söyler.
- **Interactive Mode:** Sadece `nslookup` yazıp enter'a basarsanız, istediğiniz bir DNS sunucusunu (Örn: 8.8.8.8) kullanarak sorgu yapabileceğiniz özel bir moda girersiniz.

### 2. dig (Domain Information Groper)
Linux ve macOS'ta standart olarak gelen, çok daha detaylı ve profesyonel bir araçtır.
- **Neden dig?** `nslookup`'tan çok daha fazla bilgi verir. Sorgunun kaç milisaniyede yapıldığını, hangi DNS sunucusundan yanıt geldiğini ve DNS kayıtlarının tüm detaylarını (A, MX, TXT vb.) net bir şekilde gösterir.
- **Güvenlik Analizi:** Bir sızma testi (penetration test) sırasında saldırganlar, `dig` kullanarak bir şirketin tüm DNS kayıtlarını çekmeye (Zone Transfer) çalışabilirler.

### 3. Bilmen Gereken Bazı Terimler
- **FQDN (Fully Qualified Domain Name):** Bir domain'in tam ve eksiksiz adı (Örn: `www.google.com.` - Sondaki nokta bile önemlidir).
- **Zone Transfer (AXFR):** Bir DNS sunucusundaki tüm kayıtların bir kerede başka bir yere aktarılmasıdır. Eğer düzgün kapatılmazsa, şirketin tüm iç ağ yapısı (sunucu isimleri vb.) bir saldırganın eline geçebilir.
- **Authoritative Answer:** Yanıtın, o domain'den bizzat sorumlu olan "resmi" sunucudan geldiğini belirtir.

### Gerçek Dünya Analojisi
- **nslookup:** Mahallenin bakkalına "Ali Amca, muhtarın telefon numarası kaç?" diye sormak gibidir. Bakkal defterine (cache) bakıp size söyler.
- **dig:** Doğrudan muhtarlığa gidip, tüm resmi kayıtları (telefon, adres, MX kayıtları) incelemek ve belgenin mühürlü olup olmadığını kontrol etmek gibidir.