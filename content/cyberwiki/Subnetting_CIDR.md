+++
title = "Subnetting  CIDR (Classless Inter-Domain Routing) | Subnetting CIDR (Classless Inter-Domain Routing)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Subnetting, büyük bir ağı daha küçük, yönetilebilir ve güvenli parçalara bölme işlemidir. CIDR ise eski sınıflı (A, B, C) sistemin yerine geçen, esnek bir adresleme yöntemidir.

### 1. Neden Subnetting Yapılır?
- **Performans:** Broadcast trafiğini sınırlar. Bir ağda çok fazla cihaz varsa, broadcast paketleri ağı yavaşlatır.
- **Güvenlik (İzolasyon):** Muhasebe departmanını yazılım ekibinden ayırarak, bir taraftaki saldırının diğer tarafa yayılmasını (Lateral Movement) engeller.
- **Verimlilik:** IP adreslerini israf etmeden ihtiyaca göre dağıtır.

### 2. CIDR Notasyonu
Eski sistemdeki Alt Ağ Maskesi (Subnet Mask - 255.255.255.0) yerine `/24` gibi gösterimler kullanılır. Bu sayı, adresin kaç bitinin ağ (network) kısmına ait olduğunu söyler.
- `/24`: 256 adres (254 host)
- `/30`: 4 adres (2 host) - Genellikle router'lar arası bağlantı (Point-to-Point) için kullanılır.

### 3. Teknik Hesaplama Mantığı
Bir alt ağda iki adres kullanılamaz:
1. **Network Address (Ağ Adresi):** Ağın kendisini temsil eder (Host bitleri hep 0).
2. **Broadcast Address (Yayın Adresi):** O ağdaki herkese mesaj göndermek için kullanılır (Host bitleri hep 1).
- **Kullanılabilir IP Sayısı:** $2^n - 2$ (n = host bit sayısı).

### 4. Güvenlik Perspektifi: VLAN ve Subnet İlişkisi
Subnetting genellikle mantıksal bir ayırımdır. Gerçek fiziksel ayırım veya katman 2 ayırımı için **VLAN** kullanılır.
- **Ağ Segmentasyonu:** Saldırı yüzeyini küçültmenin en etkili yoludur. Kritik sunucular (Database) her zaman dış dünyadan izole edilmiş farklı bir subnet'te tutulmalıdır.
- **ACL (Access Control Lists):** Router veya Layer 3 Switch'ler üzerinde hangi subnet'in hangisiyle konuşabileceği ACL kurallarıyla belirlenir. Bu, "Zero Trust" modelinin temelidir.

### Gerçek Dünya Analojisi
Bir oteli düşünün. Otelin ana adresi (Network ID) tektir. Ancak her kat (Subnet) kendi içinde odalara (Hosts) ayrılmıştır. Bir kattaki yangının (Saldırı) diğer katlara sıçramasını önlemek için yangın kapıları (Firewall/ACL) kullanılır.

---

## English Version

Subnetting is the process of dividing a large network into smaller, manageable and secure pieces. CIDR is a flexible addressing method that replaces the old class (A, B, C) system.

### 1. Why Subnetting?
- **Performance:** Limits broadcast traffic. If there are too many devices on a network, broadcast packets slow down the network.
- **Security (Isolation):** By separating the accounting department from the software team, it prevents the attack on one side from spreading to the other side (Lateral Movement).
- **Efficiency:** Distributes IP addresses as needed without wasting them.

### 2. CIDR Notation
Representations such as `/24` are used instead of the Subnet Mask (Subnet Mask - 255.255.255.0) in the old system. This number tells you how many bits of the address belong to the network part.
- `/24`: 256 addresses (254 hosts)
- `/30`: 4 addresses (2 hosts) - Generally used for connection between routers (Point-to-Point).

### 3. Technical Calculation Logic
Two addresses cannot be used in one subnet:
1. **Network Address:** Represents the network itself (Host bits are always 0).
2. **Broadcast Address:** Used to send messages to everyone on that network (Host bits are always 1).
- **Number of Available IPs:** $2^n - 2$ (n = number of host bits).

### 4. Security Perspective: VLAN and Subnet Relationship
Subnetting is generally a logical distinction. **VLAN** is used for actual physical separation or layer 2 separation.
- **Network Segmentation:** It is the most effective way to reduce the attack surface. Critical servers (Database) should always be kept in a different subnet isolated from the outside world.
- **ACL (Access Control Lists):** Which subnet can talk to which on the Router or Layer 3 Switches is determined by ACL rules. This is the basis of the "Zero Trust" model.

### Real World Analogy
Think of a hotel. The hotel's main address (Network ID) is unique. However, each floor (Subnet) is divided into its own rooms (Hosts). Fire doors (Firewall/ACL) are used to prevent fire (attack) on one floor from spreading to other floors.
