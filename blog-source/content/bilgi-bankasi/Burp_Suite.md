+++
title = "Burp Suite Temelleri"
date = "2026-05-19"
draft = false
categories = ["Tools"]
type = "bilgi-bankasi"
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