+++
title = "Subnetting  CIDR (Classless Inter-Domain Routing)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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