+++
title = "Infrared (Kızılötesi) İletişimi"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
+++

Infrared (IR), veriyi ışık dalgalarıyla ileten eski ama hala yaygın olan bir teknolojidir. Hatt-ı zatında (line-of-sight) görüş gerektirir.

### 1. Kullanım Alanları
- **Uzaktan Kumandalar:** TV, klima vb. cihazların kontrolü.
- **Biyometrik Sensörler:** Bazı yüz tanıma sistemleri (Liveness detection) için IR ışığı kullanır.
- **Akıllı Telefonlar:** Bazı modellerde "IR Blaster" olarak bulunur.

### 2. Siber Güvenlik Bakış Açısı
- **Replay Attack:** IR sinyalleri genellikle şifrelenmez. Bir saldırgan (örneğin Flipper Zero gibi bir cihazla) kumanda sinyalini kaydedip daha sonra tekrar oynatarak cihazı kontrol edebilir.
- **İzolasyon:** Işık duvarlardan geçemediği için IR iletişimi radyo dalgalarına (WiFi/BT) göre daha "izole" kabul edilir. Bir odaya sızmadan o odadaki IR trafiği dinlenemez.
- **Biyometrik Kandırma:** Zayıf IR sensörleri, yüksek çözünürlüklü fotoğraflar veya özel maskelerle kandırılmaya çalışılabilir.

### 3. Modern Durum
Veri transferi için yerini Bluetooth'a bırakmış olsa da, basit kontrol sistemleri ve optik sensörlerde düşük maliyeti ve düşük güç tüketimi nedeniyle tercih edilmeye devam eder.