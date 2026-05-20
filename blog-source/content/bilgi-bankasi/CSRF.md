+++
title = "Cross-Site Request Forgery (CSRF)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
+++

CSRF (Deniz Aşırı İstek Sahteciliği), bir saldırganın kurbanın tarayıcısını kullanarak, kurbanın giriş yapmış olduğu bir web sitesinde (Örn: Banka, Sosyal Medya) habersizce işlem yapmasını sağlamasıdır.

### 1. Saldırı Mantığı
XSS'te saldırgan kod çalıştırırken, CSRF'te sadece **istek gönderir.** Saldırgan sizin banka şifrenizi bilmez ama sizin tarayıcınız zaten bankaya giriş yapmış olduğu için (Oturum açık), tarayıcınızı "Para Gönder" butonuna basmaya zorlar.

### 2. Nasıl Çalışır?
1. Siz `banka.com` adresine giriş yaparsınız (Oturumunuz açık kalır).
2. Başka bir sekmede saldırganın hazırladığı "Bedava Hediye" sitesine girersiniz.
3. Bu sitenin arka planında gizli bir kod, sizin haberiniz olmadan `banka.com` adresine "Şu hesaba 1000 TL gönder" isteği atar.
4. Banka, isteğin sizin tarayıcınızdan geldiğini görür ve "Hah, User para göndermek istiyor" diyerek işlemi onaylar.

### 3. Bilmen Gereken Bazı Terimler
- **Anti-CSRF Token:** CSRF'i engelleyen en güçlü yöntemdir. Her işlem için sunucu tarafından üretilen benzersiz ve gizli bir koddur. Saldırgan bu kodu bilmediği için sahte istek oluşturamaz.
- **SameSite Cookie:** Tarayıcıya "Bu çerezi (cookie) sadece benim sitemden gelen isteklerde gönder, başka sitelerden gelen isteklerde gönderme" demektir.

### 4. Korunma Yolları
- **Token Kullanımı:** Her form ve işlem için gizli bir "Token" doğrulaması yapın.
- **Kritik İşlemlerde Onay:** Para gönderme veya şifre değiştirme gibi işlemlerde tekrar şifre veya SMS onayı (MFA) isteyin.
- **Oturumu Kapatmak:** İşiniz bittiğinde sitelerden "Çıkış Yap" (Logout) butonuna basarak çıkın.

### Gerçek Dünya Analojisi
Sizin imzanızın olduğu boş bir kağıt (Açık Oturum) masada duruyor. Bir hırsız (Saldırgan) siz bakmazken kağıdın üzerine "Tüm paramı hırsıza ver" yazıyor. Banka memuru imzayı görüyor ve "İmza gerçek, o zaman ödeme yapalım" diyor. Siz aslında o emri vermediniz ama imzanız (Oturumunuz) kullanıldı.