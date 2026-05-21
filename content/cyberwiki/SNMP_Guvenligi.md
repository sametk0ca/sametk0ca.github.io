+++
title = "SNMP (Simple Network Management Protocol) ve Güvenlik | SNMP (Simple Network Management Protocol) and Security"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

SNMP, ağ cihazlarını (Router, Switch, Yazıcı, Sunucu) izlemek, yönetmek ve performans verilerini toplamak için kullanılır.

### 1. Çalışma Mantığı
SNMP, yönetilen cihazlarda bulunan bir "Ajan" (Agent) ile merkezi bir "Yönetim İstasyonu" (NMS) arasındaki iletişimdir. Veriler **MIB (Management Information Base)** adı verilen bir yapıda tutulur. Her veri parçasının benzersiz bir **OID (Object Identifier)** numarası vardır.

### 2. Versiyonlar ve Güvenlik Farkları
- **SNMP v1:** Çok eskidir, sadece "Community String" (bir nevi şifre) kullanır ve bu şifre ağda açık metin olarak gider.
- **SNMP v2c:** Hala en yaygın olanıdır. Performans iyileştirmeleri getirse de güvenlik hala zayıftır (Açık metin şifre).
- **SNMP v3:** **Tek güvenli versiyondur.** Şunları sağlar:
    - **Authentication:** Kullanıcının kimliğini doğrular (MD5/SHA).
    - **Privacy (Encryption):** Veriyi şifreler (DES/AES). Böylece ağ koklayıcıları veriyi göremez.

### 3. Community Strings ve Riskler
Sıklıkla varsayılan olarak bırakılan `public` (okuma) ve `private` (yazma) şifreleri büyük bir risk oluşturur.
- **Risk:** Bir saldırgan `public` şifresiyle ağdaki tüm cihazların bilgilerini (IP'ler, servisler, açık portlar) çekebilir. `private` şifresiyle ise cihazın ayarlarını (Örn: Firewall kuralları) değiştirebilir.

### 4. Güvenlik Önerileri
- Sadece SNMP v3 kullanın.
- Eğer v2 kullanmak zorundaysanız, Community String'i karmaşık seçin ve ACL (Erişim Kontrol Listesi) ile sadece belirli IP'lerin SNMP sorgusu yapmasına izin verin.
- Gereksiz cihazlarda SNMP'yi tamamen kapatın.

### Gerçek Dünya Analojisi
SNMP, bir binadaki merkezi yönetim paneli gibidir. Her odadaki sensörlerden (sıcaklık, ışık, kapı durumu) bilgi alır. Eğer panelin şifresi "1234" ise (v1/v2), dışarıdan biri binadaki tüm gizli odaları görebilir. v3 ise bu panelin şifreli ve parmak izi okuyuculu modern versiyonudur.

---

## English Version

SNMP is used to monitor and manage network devices (Router, Switch, Printer, Server) and collect performance data.

### 1. Working Logic
SNMP is communication between an "Agent" located on managed devices and a central "Management Station" (NMS). Data is kept in a structure called **MIB (Management Information Base)**. Each piece of data has a unique **OID (Object Identifier)** number.

### 2. Versions and Security Differences
- **SNMP v1:** It is very old, it just uses a "Community String" (a kind of password) and this password travels on the network in clear text.
- **SNMP v2c:** Still the most common. Although it brings performance improvements, security is still weak (Cleartext password).
- **SNMP v3:** **The only secure version.** Provides:
    - **Authentication:** Authenticates the user (MD5/SHA).
    - **Privacy (Encryption):** Encrypts data (DES/AES). This way network sniffers cannot see the data.

### 3. Community Strings and Risks
`Public` (read) and `private` (write) passwords, which are often left by default, pose a great risk.
- **Risk:** An attacker can obtain the information (IPs, services, open ports) of all devices on the network with the `public` password. With the 'private' password, the device's settings (e.g. Firewall rules) can be changed.

### 4. Safety Recommendations
- Only use SNMP v3.
- If you have to use v2, choose Complex Community String and allow only certain IPs to make SNMP queries with ACL (Access Control List).
- Turn off SNMP completely on unnecessary devices.

### Real World Analogy
SNMP is like a central management panel in a building. It receives information from sensors (temperature, light, door status) in each room. If the panel's password is "1234" (v1/v2), an outsider can see all the secret rooms in the building. v3 is the modern version of this panel with password and fingerprint reader.
