+++
title = "XSS Önleme ve Sanitization | XSS Prevention and Sanitization"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Cross-Site Scripting (XSS), saldırganın web sayfalarına istemci taraflı scriptler (genellikle JavaScript) enjekte etmesine olanak tanıyan bir zafiyettir.

### Özet
XSS'i önlemenin temel mantığı, kullanıcıdan gelen veriyi asla doğrudan HTML içeriği olarak "yorumlamamak" ve veriyi görüntülemeden önce uygun şekilde temizlemektir.

### Teknik Detaylar
- **Output Encoding:** HTML, JavaScript, CSS ve URL bağlamlarına göre veriyi kodlayın (örn: `<` -> `&lt;`).
- **Sanitization:** Tehlikeli HTML etiketlerini ve özelliklerini (örn: `<script>`, `onerror`) güvenli bir kütüphane kullanarak temizleyin.
- **CSP (Content Security Policy):** Tarayıcıya hangi kaynaklardan script yüklenebileceğini söyleyen bir güvenlik katmanıdır.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Context-Aware Encoding:** Verinin nereye yazılacağına göre (HTML gövdesi, öznitelik, script bloğu) farklı kodlama metodları kullanın.
- **Modern Frameworks:** React, Angular gibi frameworkler varsayılan olarak birçok XSS türüne karşı koruma sağlar.
- **HttpOnly Cookies:** Session ID gibi hassas çerezleri JavaScript erişimine kapatın.

---

## English Version

Cross-Site Scripting (XSS) is a vulnerability that allows an attacker to inject client-side scripts (usually JavaScript) into web pages.

### Summary
The basic logic of preventing XSS is to never "interpret" data coming from the user directly as HTML content and to properly sanitize the data before displaying it.

### Technical Details
- **Output Encoding:** Encode data according to HTML, JavaScript, CSS and URL contexts (ex: `<` -> `&lt;`).
- **Sanitization:** Sanitize dangerous HTML tags and attributes (eg: `<script>`, `onerror`) using a safe library.
- **CSP (Content Security Policy):** It is a security layer that tells the browser from which sources scripts can be loaded.

### Security Approach and Best Practices
- **Context-Aware Encoding:** Use different encoding methods depending on where the data will be written (HTML body, attribute, script block).
- **Modern Frameworks:** Frameworks such as React and Angular provide protection against many types of XSS by default.
- **HttpOnly Cookies:** Block sensitive cookies such as Session ID from JavaScript access.
