+++
title = "Infrared (Kızılötesi) İletişimi | Infrared Communication"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
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

---

## English Version

Infrared (IR) is an old but still widespread technology that transmits data with light waves. It requires line-of-sight vision.

### 1. Areas of Use
- **Remote Controls:** TV, air conditioner, etc. control of devices.
- **Biometric Sensors:** Some facial recognition systems use IR light for Liveness detection.
- **Smartphones:** Available as "IR Blaster" on some models.

### 2. Cybersecurity Perspective
- **Replay Attack:** IR signals are generally not encrypted. An attacker (for example, with a device like Flipper Zero) can control the device by recording the control signal and replaying it later.
- **Isolation:** IR communication is considered more "isolated" than radio waves (WiFi/BT) because light cannot pass through walls. IR traffic in a room cannot be listened to without infiltrating that room.
- **Biometric Deception:** Weak IR sensors can be deceived with high-resolution photos or special masks.

### 3. Modern Situation
Although it has been replaced by Bluetooth for data transfer, it continues to be preferred in simple control systems and optical sensors due to its low cost and low power consumption.
