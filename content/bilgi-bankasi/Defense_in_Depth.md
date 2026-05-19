+++
title = "Defense in Depth (Çok Katmanlı Savunma)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Defense in Depth (Derinlemesine Savunma), tek bir güvenlik önlemine güvenmek yerine, birbirini destekleyen birden fazla güvenlik katmanı oluşturma stratejisidir.

### 1. Neden Tek Bir Önlem Yetmez?
Siber güvenlikte "mükemmel" bir araç yoktur. Her duvarın bir deliği, her kilidin bir maymuncuğu olabilir. Eğer hırsız dış kapıyı geçerse, içeride başka engellerle karşılaşmalıdır.

### 2. Savunma Katmanları
- **Fiziksel Katman:** Kameralar, güvenlik görevlileri, kilitli kapılar, veri merkezi giriş kartları.
- **Ağ Katmanı:** Firewall, IPS/IDS, ağ segmentasyonu (VLAN), VPN.
- **Sistem (Host) Katmanı:** Antivirüs/EDR yazılımları, güncel işletim sistemi (Patch management), disk şifreleme.
- **Uygulama Katmanı:** Güvenli kod yazımı, web uygulama güvenlik duvarları (WAF).
- **Veri Katmanı:** Şifreleme, veri tabanı erişim logları.
- **İnsan Katmanı:** Güvenlik farkındalığı eğitimleri, güçlü şifre politikaları.

### 3. Bilmen Gereken Bazı Terimler
- **Patch Management:** Yazılımlardaki güvenlik açıklarını kapatmak için düzenli olarak güncellemelerin (yamaların) yüklenmesi süreci.
- **WAF (Web Application Firewall):** Sadece web sitelerine gelen karmaşık saldırıları (Örn: SQL Injection) durdurmak için tasarlanmış özel bir güvenlik duvarı.
- **Social Engineering (Sosyal Mühendislik):** Teknolojiyi değil, insan psikolojisini kullanarak (kandırma yoluyla) bilgi çalma eylemi. Bu stratejideki "İnsan" katmanını hedefler.

### 4. Peynir Modeli (Swiss Cheese Model)
Güvenlik katmanlarını yan yana dizilmiş delikli İsviçre peyniri dilimleri gibi düşünün. Her dilimin (güvenlik önlemi) kendi içinde delikleri (zafiyetleri) vardır. Defense in Depth stratejisinin amacı, bu dilimleri öyle bir dizmektir ki, bir dilimdeki delik diğer dilimin sağlam tarafına denk gelsin. Böylece saldırgan (ışık sızması gibi) tüm katmanları bir kerede geçemez.

### Gerçek Dünya Analojisi
Değerli bir elmasın saklandığı bir müzeyi düşünün.
1. Müzenin etrafında yüksek duvarlar ve dikenli teller var (Fiziksel).
2. Girişte kimlik kontrolü yapılıyor (Ağ).
3. Elmasın olduğu oda kameralarla izleniyor (Sistem).
4. Elmas, camı kırılınca alarm veren bir kasanın içinde (Uygulama).
5. Kasanın şifresini sadece iki farklı kişi biliyor (İnsan/MFA).
Hırsız duvarı aşsa bile kameraya yakalanır, kamerayı atlasa bile kasayı açamaz.