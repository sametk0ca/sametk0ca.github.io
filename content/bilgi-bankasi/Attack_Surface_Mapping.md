+++
title = "Saldırı Yüzeyi Haritalama (Attack Surface Mapping)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Saldırı yüzeyi, bir sistemin dışarıdan saldırıya uğrayabileceği tüm giriş noktalarının (portlar, API'ler, formlar, insan faktörü) toplamıdır.

### Özet
Haritalama süreci, "bir saldırgan sistemimize nereden girebilir?" sorusunun cevabını bulmak için sistemin tüm uç noktalarını ve zayıf halkalarını listelemeyi amaçlar.

### Teknik Detaylar
- **Ağ Yüzeyi:** Açık portlar, IP adresleri, firewall kuralları.
- **Uygulama Yüzeyi:** API endpointleri, admin panelleri, giriş formları.
- **İnsan/Süreç Yüzeyi:** Sosyal mühendislik açıklıkları, yetersiz denetlenen süreçler.
- **Veri Yüzeyi:** Verinin depolandığı ve taşındığı noktalar.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Minimize the Surface:** Kullanılmayan portları kapatın, gereksiz API'leri devre dışı bırakın.
- **Continuous Discovery:** Gölge BT (Shadow IT) varlıklarını bulmak için sürekli tarama yapın.
- **Least Exposure:** İç servisleri asla doğrudan internete açmayın, VPN veya Proxy arkasına alın.