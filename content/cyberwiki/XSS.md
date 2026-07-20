+++
title = "Cross-Site Scripting (XSS)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

XSS is an attack where an attacker inserts malicious software (usually JavaScript codes) into a trusted website and executes these codes in the browsers of other users who visit that site.

### 1. Attack Logic
While SQL Injection targets the database, XSS directly targets **other users**. Malicious code placed on the site can steal the passwords or hijack the sessions of innocent users visiting that site.

### 2. Types of XSS
- **Stored (Persistent) XSS:** It is the most dangerous. Malicious code is saved on the server (e.g. in a comment section or profile description). Anyone who opens the page is exposed to this code.
- **Reflected XSS:** The code is not saved to the server. It is usually hidden inside a link. When the user clicks on that link, the code is "reflected" in the browser and runs.
- **DOM-based XSS:** The attack occurs entirely in the user's browser (client side).

### 3. Some Terms You Should Know
- **JavaScript:** The language that adds pizzazz to websites. It is the main tool of XSS attacks.
- **Session Cookie:** It is a "remember me" card that is kept in your browser after you log in to the site. If this card is stolen via XSS, the attacker can log in to the site on your behalf.
- **Payload:** The actual piece of malicious code executed by the attacker.
- **SOP (Same-Origin Policy):** It is the basic security rule that prevents the code on one website from accessing data on another website. XSS attempts to break this rule.

### 4. Ways of Protection
- **Output Encoding:** While displaying the data coming from the user on the page, disabling the HTML characters (`<`, `>`) in it (For example: writing `&lt;` instead of `<`).
- **CSP (Content Security Policy):** It is a firewall layer that ensures that the website says "Only run code from these trusted sources".
- **HttpOnly Cookies:** Marking cookies so that JavaScript cannot read them.

### Real World Analogy
XSS is like someone secretly sticking a needle (Malicious Code) into a school's public bulletin board (Website). Any student (User) who comes to look at the board may touch that needle and get hurt. Those who manage the board (Developers) need to control everything posted on the board.
