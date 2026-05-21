+++
title = "Hub vs Switch vs Router Farkları | Hub vs Switch vs Router Differences"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

These three devices manage the traffic of the network, but their "intelligence" and the OSI layers on which they operate are different.

### 1. Hub (Dumb Device) - Layer 1
It copies the incoming data to all ports connected to it (Broadcast), regardless of which device it will go to.
- **Intelligence:** None.
- **Security Risk:** **Very High.** A packet that goes to one goes to everyone. Anyone on the network can monitor all traffic by turning on Wireshark. It is not used in modern networks.

### 2. Switch (Smart Device) - Layer 2
It looks at the MAC address in the incoming packet and sends the packet only to the port to which the relevant device is connected.
- **Intelligence:** There is a **MAC Address Table** that keeps which port the devices are on.
- **Security:** It is much more secure than the Hub because the data only goes to the destination. However, with "MAC Flooding" attacks, the Switch's table can be filled and the device can be forced to act as a Hub (Fail-open).

### 3. Router - Layer 3
It connects different networks (e.g. home network and Internet). It ensures that packages go to their destination in the shortest and most accurate way.
- **Intelligence:** Uses **Routing Tables** containing IP addresses.
- **Security:** It is the entrance gate of the network. It can filter traffic thanks to its ACLs and Firewall features.

### Summary

| Device | Layer | Addressing | Traffic Management |
| :--- | :--- | :--- | :--- |
| **Hub** | 1 (Physical) | None | Sends to everyone (Broadcast) |
| **Switch** | 2 (Data Link) | MAC Address | Sends only to destination (Unicast) |
| **Router** | 3 (Network) | IP Address | Routes between different networks |

### Real World Analogy
- **Hub:** Shouting someone in the middle of the class without saying their name; Everyone hears, but only those who are interested listen.
- **Switch:** The class president leaves the paper containing the message directly on the desk of the relevant student.
- **Router:** The counselor at the entrance of the school guides someone coming from outside on which class to go to.
