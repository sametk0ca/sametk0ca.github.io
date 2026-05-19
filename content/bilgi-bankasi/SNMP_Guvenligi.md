+++
title = "SNMP (Simple Network Management Protocol) ve Güvenlik"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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