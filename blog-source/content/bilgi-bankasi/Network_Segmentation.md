+++
title = "Network Segmentation (Ağ Segmentasyonu)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
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