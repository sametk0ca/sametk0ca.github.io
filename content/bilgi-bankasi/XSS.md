+++
title = "Cross-Site Scripting (XSS)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

XSS, bir saldırganın güvenilir bir web sitesine zararlı yazılımlar (genellikle JavaScript kodları) yerleştirmesi ve bu siteyi ziyaret eden diğer kullanıcıların tarayıcılarında bu kodları çalıştırması saldırısıdır.

### 1. Saldırı Mantığı
SQL Injection veritabanını hedef alırken, XSS doğrudan **diğer kullanıcıları** hedef alır. Siteye yerleştirilen zararlı kod, o siteyi ziyaret eden masum kullanıcıların şifrelerini çalabilir veya oturumlarını (session) ele geçirebilir.

### 2. XSS Türleri
- **Stored (Kalıcı) XSS:** En tehlikelisidir. Zararlı kod sunucuya (Örn: Bir yorum kısmına veya profil açıklamasına) kaydedilir. Sayfayı açan herkes bu koda maruz kalır.
- **Reflected (Yansıtılan) XSS:** Kod sunucuya kaydedilmez. Genellikle bir linkin içine gizlenir. Kullanıcı o linke tıkladığında kod tarayıcıya "yansır" ve çalışır.
- **DOM-based XSS:** Saldırı tamamen kullanıcının tarayıcısında (istemci tarafında) gerçekleşir.

### 3. Bilmen Gereken Bazı Terimler
- **JavaScript:** Web sitelerine hareketlilik katan dil. XSS saldırılarının ana aracıdır.
- **Session Cookie (Oturum Çerezi):** Siteye giriş yaptıktan sonra tarayıcınızda tutulan "beni hatırla" kartıdır. XSS ile bu kart çalınırsa, saldırgan sizin adınıza siteye giriş yapabilir.
- **Payload:** Saldırganın çalıştırdığı asıl zararlı kod parçası.
- **SOP (Same-Origin Policy):** Bir web sitesindeki kodun, başka bir web sitesindeki verilere erişmesini engelleyen temel güvenlik kuralıdır. XSS bu kuralı delmeye çalışır.

### 4. Korunma Yolları
- **Output Encoding:** Kullanıcıdan gelen veriyi sayfada gösterirken, içindeki HTML karakterlerini ( `<` , `>` ) etkisiz hale getirmek (Örn: `<` yerine `&lt;` yazmak).
- **CSP (Content Security Policy):** Web sitesinin "Sadece şu güvenilir kaynaklardan kod çalıştır" demesini sağlayan bir güvenlik duvarı katmanıdır.
- **HttpOnly Cookies:** Çerezleri (Cookie) JavaScript'in okuyamayacağı şekilde işaretlemek.

### Gerçek Dünya Analojisi
XSS, bir okulun ortak duyuru panosuna (Web Sitesi) birinin gizlice iğne (Zararlı Kod) batırması gibidir. Panoya bakmaya gelen her öğrenci (Kullanıcı) o iğneye dokunup zarar görebilir. Panoyu yönetenlerin (Geliştiriciler) panoya asılan her şeyi kontrol etmesi gerekir.