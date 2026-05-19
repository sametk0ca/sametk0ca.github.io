+++
title = "Güvenli Ağ Bölgeleme (Network Zoning)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

Güvenli ağ bölgeleme, bir organizasyonun ağını güvenlik seviyelerine ve iş fonksiyonlarına göre mantıksal "zonlara" ayırma işlemidir.

### Özet
Zoning, "iç ağ güvenlidir" varsayımını yıkar. Her bölge (DMZ, Production, Management, Dev) kendi güvenlik kurallarına sahip olmalı ve bölgeler arası trafik sıkı denetlenmelidir.

### Teknik Detaylar
- **DMZ (Demilitarized Zone):** Dışa açık sunucuların bulunduğu tampon bölge.
- **Trusted Zone:** Hassas iç verilerin ve uygulama sunucularının bulunduğu bölge.
- **Management Zone:** Sadece admin erişimine açık olan, kritik cihazların yönetildiği bölge.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Micro-segmentation:** Bölge içindeki iş yüklerini bile birbirinden izole edin.
- **Inter-Zone Firewalls:** Her bölge geçişinde bir firewall veya IPS/IDS katmanı bulundurun.
- **Jump Hosts / Bastion Hosts:** Management zonuna erişimi sadece özel, izlenen sunucular üzerinden yapın.