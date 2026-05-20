+++
title = "HTTP vs HTTPS (Port 80 vs 443)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

Web siteleriyle iletişim kurarken kullanılan iki ana protokoldür. Aralarındaki en temel fark "güvenlik" ve "şifreleme"dir.

### 1. HTTP (HyperText Transfer Protocol) - Port 80
İnternetin temel, ancak güvensiz protokolüdür.
- **Çalışma Şekli:** Veriler "Cleartext" (açık metin) olarak iletilir. Yani ağdaki birisi araya girerse şifrelerinizi, mesajlarınızı olduğu gibi okuyabilir.
- **Kullanım Alanı:** Artık sadece yerel geliştirme ortamlarında veya çok eski sistemlerde kalmıştır. Modern tarayıcılar HTTP siteleri "Güvenli Değil" olarak işaretler.

### 2. HTTPS (HTTP Secure) - Port 443
HTTP'nin üzerine bir güvenlik katmanı (SSL/TLS) eklenmiş halidir.
- **Çalışma Şekli:** Veriler gönderilmeden önce şifrelenir. Araya giren biri sadece anlamsız karakterler görür.
- **Güvenlik Bileşenleri:** Gizlilik (Encryption), Veri Bütünlüğü (Integrity) ve Kimlik Doğrulama (Authentication) sağlar.

### 3. Neden HTTPS Şart?
- **Veri Gizliliği:** Kullanıcı verilerinin çalınmasını önler.
- **Güven:** Kullanıcıya "bu site gerçekten google.com" garantisi verir (Sertifika sayesinde).
- **SEO:** Arama motorları HTTPS kullanan siteleri daha üst sıralara taşır.
- **Modern Özellikler:** Birçok modern web teknolojisi (Service Workers, Konum Bilgisi) sadece HTTPS üzerinde çalışır.

### 4. Güvenlik Notları
- **HSTS (HTTP Strict Transport Security):** Bir web sitesinin tarayıcıya "Bundan sonra bana her zaman sadece HTTPS üzerinden bağlan" demesini sağlar. Bu, HTTPS'e zorlama yaparak "Downgrade" (güvenliği düşürme) saldırılarını engeller.
- **SSL Stripping:** Saldırganın HTTPS bağlantısını HTTP'ye düşürerek verileri çalmaya çalışmasıdır. HSTS bu saldırıyı önler.

### Gerçek Dünya Analojisi
HTTP, bir karta yazdığınız ve herkesin okuyabileceği bir "kartpostal" göndermek gibidir. HTTPS ise aynı mesajı çelik bir kasanın (Şifreleme) içine koyup, anahtarı sadece alıcıda olan kilitli bir kutuyla göndermek gibidir.