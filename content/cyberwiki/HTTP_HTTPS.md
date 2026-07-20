+++
title = "HTTP vs HTTPS (Port 80 vs 443)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

These are the two main protocols used when communicating with websites. The main difference between them is "security" and "encryption".

### 1. HTTP (HyperText Transfer Protocol) - Port 80
It is the basic, but insecure protocol of the Internet.
- **How ​​It Works:** Data is transmitted as "Cleartext". So, if someone on the network intervenes, they can read your passwords and messages as they are.
- **Area of ​​Use:** It is now only used in local development environments or very old systems. Modern browsers mark HTTP sites as "Not Secure".

### 2. HTTPS (HTTP Secure) - Port 443
It is a security layer (SSL/TLS) added on top of HTTP.
- **How ​​It Works:** Data is encrypted before being sent. An interloper sees only meaningless characters.
- **Security Components:** Provides Confidentiality (Encryption), Data Integrity and Authentication.

### 3. Why HTTPS is a Must?
- **Data Privacy:** Prevents theft of user data.
- **Trust:** It guarantees the user that "this site is really google.com" (thanks to the Certificate).
- **SEO:** Search engines rank sites using HTTPS higher.
- **Modern Features:** Many modern web technologies (Service Workers, Location Intelligence) only work over HTTPS.

### 4. Safety Notes
- **HSTS (HTTP Strict Transport Security):** Allows a website to tell the browser "From now on, always connect to me over HTTPS only." This prevents "Downgrade" attacks by forcing HTTPS.
- **SSL Stripping:** This is when the attacker tries to steal data by downgrading the HTTPS connection to HTTP. HSTS prevents this attack.

### Real World Analogy
HTTP is like sending a "postcard" that you write on a card and anyone can read it. HTTPS, on the other hand, is like putting the same message in a steel safe (Encryption) and sending it with a locked box, the key to which only the recipient has.
