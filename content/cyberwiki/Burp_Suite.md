+++
title = "Burp Suite Temelleri | Burp Suite Basics"
date = "2026-05-19"
draft = false
categories = ["Tools"]
type = "cyberwiki"
+++

Burp Suite, web uygulaması güvenlik testleri (pentest) için kullanılan endüstri standardı bir entegre platformdur.

### Özet
Burp Suite, tarayıcı ile sunucu arasındaki trafiği yakalayan bir "interception proxy" olarak çalışır. Uygulamanın nasıl çalıştığını anlamak ve zafiyetleri manuel/otomatik olarak tespit etmek için kullanılır.

### Teknik Detaylar
- **Proxy:** HTTP/S trafiğini durdurup manipüle etmenizi sağlar.
- **Repeater:** Bir isteği defalarca değiştirip tekrar göndermek için kullanılır.
- **Intruder:** Brute force ve fuzzing gibi otomatik saldırılar için kullanılır.
- **Scanner (Pro):** Otomatik olarak zafiyet taraması yapar.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Kapsam (Scope) Belirleme:** Sadece izin verilen hedefleri taradığınızdan emin olun.
- **Manuel İnceleme:** Otomatik tarayıcıların kaçırdığı mantıksal hataları yakalamak için Proxy ve Repeater araçlarını etkin kullanın.
- **Eklenti Desteği (BApp Store):** Burp'ün yeteneklerini topluluk tarafından geliştirilen eklentilerle artırın.

---

## English Version

Burp Suite is an industry-standard integrated platform used for web application security testing (pentest).

### Summary
Burp Suite works as an "interception proxy" that captures traffic between the browser and the server. It is used to understand how the application works and to detect vulnerabilities manually/automatically.

### Technical Details
- **Proxy:** Allows you to intercept and manipulate HTTP/S traffic.
- **Repeater:** It is used to change and resend a request many times.
- **Intruder:** Used for automatic attacks such as brute force and fuzzing.
- **Scanner (Pro):** Automatically scans for vulnerabilities.

### Security Approach and Best Practices
- **Scope Determination:** Make sure to scan only permitted targets.
- **Manual Review:** Use Proxy and Repeater tools effectively to catch logical errors that automatic scanners miss.
- **Plugin Support (BApp Store):** Extend Burp's capabilities with community-developed plugins.
