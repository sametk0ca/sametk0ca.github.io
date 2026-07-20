+++
title = "Saldırı Yüzeyi Haritalama (Attack Surface Mapping) | Attack Surface Mapping"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

The attack surface is the sum of all entry points (ports, APIs, forms, human factor) through which a system can be attacked from the outside.

### Summary
The mapping process asks “where can an attacker break into our system?” It aims to list all the endpoints and weak links of the system in order to find the answer to the question.

### Technical Details
- **Network Surface:** Open ports, IP addresses, firewall rules.
- **Application Surface:** API endpoints, admin panels, login forms.
- **Human/Process Surface:** Social engineering vulnerabilities, poorly audited processes.
- **Data Surface:** The points where data is stored and moved.

### Security Approach and Best Practices
- **Minimize the Surface:** Close unused ports, disable unnecessary APIs.
- **Continuous Discovery:** Continuously scan to find Shadow IT assets.
- **Least Exposure:** Never expose internal services directly to the internet, keep them behind a VPN or Proxy.
