+++
title = "JavaScript  Node.js"
date = "2026-05-19"
draft = false
categories = ["Programming"]
type = "bilgi-bankasi"
+++

JavaScript, web tarayıcılarında başlayan yolculuğuna Node.js ile sunucu tarafında da devam eden, asenkron yapısıyla güçlü bir dildir.

### Özet
Hem web uygulamalarının ön yüzünde hem de sunucu tarafında (Node.js) kullanılması, saldırganlar için geniş bir saldırı yüzeyi; güvenlik uzmanları içinse derinlemesine analiz gerektiren bir alan oluşturur.

### Teknik Detaylar
- **Asynchronous I/O:** Event-driven yapısı ile yüksek trafikli ağ uygulamaları için idealdir.
- **NPM (Node Package Manager):** Dünyanın en büyük paket ekosistemine sahiptir, ancak bu durum tedarik zinciri risklerini de beraberinde getirir.
- **Single Threaded:** Tek bir iş parçacığı üzerinde çalışır ancak asenkron operasyonlarla engellenmeden devam eder.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **NPM Audit:** Projenize dahil ettiğiniz paketleri `npm audit` ile her zaman tarayın.
- **XSS Koruması:** Kullanıcı verilerini her zaman sanitize edin; asla `eval()` veya `innerHTML` gibi tehlikeli metodları kullanmayın.
- **Secrets Management:** `.env` dosyalarını asla kod deposuna (Git) eklemeyin.