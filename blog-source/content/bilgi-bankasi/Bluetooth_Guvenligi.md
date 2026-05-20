+++
title = "Bluetooth Protokolleri ve Güvenliği"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
+++

Bluetooth, kısa mesafeli "Personal Area Network" (PAN) iletişimi sağlar. Siber güvenlikte genellikle uç nokta cihazlarının (telefon, kulaklık, IoT) hedef alınmasında kullanılır.

### 1. Bluetooth Türleri
- **Bluetooth Classic:** Daha yüksek veri hızı, daha fazla güç tüketimi.
- **Bluetooth Low Energy (BLE):** IoT ve giyilebilir cihazlarda yaygındır. Genellikle güvenlik önlemleri performans için feda edilir.

### 2. Temel Saldırı Türleri
- **Bluejacking:** Kurbanın cihazına izinsiz reklam veya mesaj gönderilmesi.
- **Bluesnarfing:** Cihazdaki rehber, mesaj veya dosyalara izinsiz erişim.
- **Blueborne:** Cihazın eşleşme modunda olmasına gerek kalmadan, sadece Bluetooth'un açık olmasıyla gerçekleştirilen kritik bir açıklar silsilesidir.

### 3. Güvenlik Mekanizmaları
- **Pairing (Eşleştirme):** Cihazlar arası güven ilişkisi kurulması. "Just Works" metodu en güvensiz olanıdır çünkü kullanıcı onayı gerektirmez.
- **Encryption:** Veri transferi şifrelenmelidir ancak BLE cihazlarında zayıf anahtar yönetimi sıkça görülür.
- **Visibility:** Cihazın sürekli "keşfedilebilir" modda bırakılması, saldırganların cihazı tespit etmesini kolaylaştırır.