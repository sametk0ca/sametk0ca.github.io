+++
title = "Bluetooth Protokolleri ve Güvenliği | Bluetooth Protocols and Security"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
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

---

## English Version

Bluetooth provides short-range "Personal Area Network" (PAN) communication. In cyber security, it is generally used to target endpoint devices (phone, headset, IoT).

### 1. Types of Bluetooth
- **Bluetooth Classic:** Higher data rate, more power consumption.
- **Bluetooth Low Energy (BLE):** Common in IoT and wearable devices. Often security measures are sacrificed for performance.

### 2. Basic Attack Types
- **Bluejacking:** Sending unauthorized advertisements or messages to the victim's device.
- **Bluesnarfing:** Unauthorized access to contacts, messages or files on the device.
- **Blueborne:** It is a series of critical vulnerabilities that occur only when Bluetooth is turned on, without the need for the device to be in pairing mode.

### 3. Security Mechanisms
- **Pairing:** Establishing a trust relationship between devices. The "Just Works" method is the most insecure because it does not require user confirmation.
- **Encryption:** Data transfer must be encrypted, but poor key management is common in BLE devices.
- **Visibility:** Leaving the device in "discoverable" mode at all times makes it easier for attackers to detect the device.
