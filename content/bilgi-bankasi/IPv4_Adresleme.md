+++
title = "IPv4 Adresleme ve Sınıflar"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

IPv4 (Internet Protocol version 4), ağdaki cihazların birbirini tanımasını sağlayan 32 bitlik bir adresleme sistemidir. Noktalarla ayrılmış 4 oktetten oluşur (Örn: 192.168.1.1).

### 1. Adres Yapısı
Her oktet 8 bit değerindedir (0-255 arası). Toplamda yaklaşık 4.3 milyar ($2^{32}$) adres kapasitesi sunar; bu da günümüzde adreslerin tükenmesine yol açmıştır.

### 2. IP Sınıfları (Classful Addressing)
Eskiden kullanılan ancak hala temelleri bilmek için kritik olan sınıflandırma şöyledir:
- **A Sınıfı (1-126):** Büyük kurumlar için. İlk oktet ağ (network), kalanlar ana bilgisayar (host).
- **B Sınıfı (128-191):** Orta ölçekli ağlar için. İlk iki oktet ağ.
- **C Sınıfı (192-223):** Küçük ağlar (Evler) için. İlk üç oktet ağ.
- **D Sınıfı (224-239):** Multicast yayınlar için.
- **E Sınıfı (240-255):** Araştırma ve deneyler için.
- **Özel Adres (127.0.0.1):** Loopback (Geri döngü) adresi; cihazın kendisini işaret eder.

### 3. Public vs Private IP (NAT Gerekliliği)
Adres yetersizliği nedeniyle "Özel IP" (Private IP) blokları tanımlanmıştır. Bu adresler internette yönlendirilemez:
- 10.0.0.0 - 10.255.255.255
- 172.16.0.0 - 172.31.255.255
- 192.168.0.0 - 192.168.255.255
**Security Note:** İç ağdaki cihazlar internete çıkarken NAT (Network Address Translation) kullanarak tek bir Public IP arkasına gizlenir. Bu, iç yapıyı dışarıdan doğrudan erişime kapatarak bir güvenlik katmanı sağlar.

### 4. Güvenlik ve Analiz
- **IP Spoofing:** Bir saldırganın, kaynağını güvenilir bir iç IP gibi göstererek paket göndermesi. Firewall kuralları (Ingress/Egress filtering) ile önlenmelidir.
- **Reconnaissance (Keşif):** Saldırganlar bir ağın IP aralığını tarayarak hangi cihazların aktif olduğunu anlamaya çalışırlar. "Scanning" bir saldırının ilk adımıdır.
- **Geopolitik/Forensics:** IP adresleri üzerinden coğrafi konum tahmini (Geo-IP) yapılabilir, ancak VPN veya Proxy kullanımı bu analizi yanıltabilir.