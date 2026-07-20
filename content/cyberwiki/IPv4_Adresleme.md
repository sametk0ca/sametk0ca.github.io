+++
title = "IPv4 Adresleme ve Sınıflar | IPv4 Addressing and Classes"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

IPv4 (Internet Protocol version 4) is a 32-bit addressing system that allows devices on the network to recognize each other. It consists of 4 octets separated by dots (Ex: 192.168.1.1).

### 1. Address Structure
Each octet is worth 8 bits (0-255). Offers a total address capacity of approximately 4.3 billion ($2^{32}$); This has led to the depletion of addresses today.

### 2. IP Classes (Classful Addressing)
The classification that was formerly used but is still critical to know the basics is:
- **Class A (1-126):** For large institutions. The first octet is the network, the remaining are the host.
- **Class B (128-191):** For medium-sized networks. The first two octets are the network.
- **Class C (192-223):** For small networks (Houses). The first three octets are the network.
- **Class D (224-239):** For multicast broadcasts.
- **Class E (240-255):** For research and experiments.
- **Private Address (127.0.0.1):** Loopback address; points to the device itself.

### 3. Public vs Private IP (NAT Requirement)
Due to lack of addresses, "Private IP" blocks have been defined. These addresses cannot be forwarded on the Internet:
- 10.0.0.0 - 10.255.255.255
- 172.16.0.0 - 172.31.255.255
- 192.168.0.0 - 192.168.255.255
**Security Note:** When devices on the internal network go to the Internet, they are hidden behind a single Public IP using NAT (Network Address Translation). This provides a layer of security by sealing off the internal structure from direct access from the outside.

### 4. Security and Analytics
- **IP Spoofing:** An attacker sends a packet disguised as a trusted internal IP. It should be prevented by firewall rules (Ingress/Egress filtering).
- **Reconnaissance:** Attackers try to understand which devices are active by scanning the IP range of a network. "Scanning" is the first step of an attack.
- **Geopolitics/Forensics:** Geographic location estimation (Geo-IP) can be made through IP addresses, but the use of VPN or Proxy may mislead this analysis.
