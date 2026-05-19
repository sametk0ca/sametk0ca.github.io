+++
title = "Hub vs Switch vs Router Farkları"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

Bu üç cihaz ağın trafiğini yönetir ancak "zekaları" ve çalıştıkları OSI katmanları farklıdır.

### 1. Hub (Aptal Cihaz) - Katman 1
Gelen veriyi hangi cihaza gideceğine bakmadan, kendisine bağlı tüm portlara kopyalar (Broadcast).
- **Zeka:** Yok.
- **Güvenlik Riski:** **Çok Yüksek.** Birine giden paket herkese gider. Ağdaki herhangi biri Wireshark açarak tüm trafiği izleyebilir. Modern ağlarda kullanılmaz.

### 2. Switch (Zeki Cihaz) - Katman 2
Gelen paketin içindeki MAC adresine bakar ve paketi sadece ilgili cihazın bağlı olduğu porta gönderir.
- **Zeka:** Cihazların hangi portta olduğunu tutan bir **MAC Adres Tablosu** vardır.
- **Güvenlik:** Hub'a göre çok daha güvenlidir çünkü veri sadece hedefe gider. Ancak "MAC Flooding" saldırılarıyla Switch'in tablosu doldurulup cihaz Hub gibi davranmaya (Fail-open) zorlanabilir.

### 3. Router (Yol Gösterici) - Katman 3
Farklı ağları (Örn: Ev ağı ve İnternet) birbirine bağlar. Paketlerin en kısa ve en doğru yoldan hedefe gitmesini sağlar.
- **Zeka:** IP adreslerini içeren **Yönlendirme Tabloları (Routing Tables)** kullanır.
- **Güvenlik:** Ağın giriş kapısıdır. Üzerindeki ACL'ler ve Firewall özellikleri sayesinde trafiği filtreleyebilir.

### Özet Karşılaştırma

| Cihaz | Katman | Adresleme | Trafik Yönetimi |
| :--- | :--- | :--- | :--- |
| **Hub** | 1 (Fiziksel) | Yok | Herkese gönderir (Broadcast) |
| **Switch** | 2 (Veri Bağı) | MAC Adresi | Sadece hedefe gönderir (Unicast) |
| **Router** | 3 (Ağ) | IP Adresi | Farklı ağlar arası yönlendirir |

### Gerçek Dünya Analojisi
- **Hub:** Sınıfın ortasında birinin adını söylemeden bağırması; herkes duyar ama sadece ilgilenen dinler.
- **Switch:** Sınıf başkanının, mesajı içeren kağıdı doğrudan ilgili öğrencinin sırasına bırakması.
- **Router:** Okulun girişindeki danışmanın, dışarıdan gelen birini hangi sınıfa gideceği konusunda yönlendirmesi.