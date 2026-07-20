+++
title = "Network Segmentation (Ağ Segmentasyonu) | Network Segmentation"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Ağ segmentasyonu, bir bilgisayar ağını daha küçük, izole edilmiş alt ağlara (segmentlere) bölme işlemidir.

### Özet
Segmentasyon, bir saldırganın ağa sızması durumunda ağ içerisinde yatayda hareket etmesini (lateral movement) engellemeyi ve saldırı yüzeyini küçültmeyi amaçlar.

### Teknik Detaylar
- **VLAN (Virtual LAN):** Mantıksal olarak ağı katman 2 seviyesinde böler.
- **Subnetting:** IP adresleme üzerinden ağı katman 3 seviyesinde böler.
- **Micro-segmentasyon:** Konteyner ve bulut ortamlarında iş yükü bazlı, çok daha dar kapsamlı izolasyon sağlar.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Kritik Varlık İzolasyonu:** Veritabanları ve hassas veriler, genel erişime açık web sunucularından izole edilmelidir.
- **DMZ Kullanımı:** Dış dünyaya açık servisleri iç ağdan ayrı bir bölgede tutun.
- **ZTA (Zero Trust) Entegrasyonu:** Segmentler arası geçişlerde her zaman kimlik doğrulaması şartı koşun.

---

## English Version

Network segmentation is the process of dividing a computer network into smaller, isolated subnets (segments).

### Summary
Segmentation aims to prevent an attacker from moving horizontally within the network and reducing the attack surface in case of infiltration of the network.

### Technical Details
- **VLAN (Virtual LAN):** Logically divides the network at layer 2 level.
- **Subnetting:** Splits the network at layer 3 level via IP addressing.
- **Micro-segmentation:** Provides workload-based, much more narrow-scope isolation in container and cloud environments.

### Security Approach and Best Practices
- **Critical Asset Isolation:** Databases and sensitive data should be isolated from publicly accessible web servers.
- **DMZ Usage:** Keep services open to the outside world in a separate region from the internal network.
- **ZTA (Zero Trust) Integration:** Always require authentication when switching between segments.
