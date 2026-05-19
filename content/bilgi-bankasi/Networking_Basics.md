+++
title = "Ağ Temelleri (Networking Basics)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

Ağ temelleri, cihazların birbirleriyle nasıl iletişim kurduğunu, verinin nasıl paketlendiğini ve yönlendirildiğini anlamayı sağlayan temel bilgi kümesidir.

### Özet
DevSecOps süreçlerinde ağ temellerini bilmek; altyapı güvenliği (IaC), konteynerler arası iletişim ve bulut ağ yapılandırmalarını güvenli hale getirmek için zorunludur.

### Teknik Detaylar
- **IP Adresleme:** Cihazların ağ üzerindeki kimlikleri (IPv4/v6).
- **Protokoller:** Veri iletim kuralları (TCP, UDP, ICMP).
- **Portlar:** Servislerin dinlediği kapılar (0-65535).
- **Routing & Switching:** Verinin bir noktadan diğerine nasıl iletildiği.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Default Deny:** Ağ trafiğini varsayılan olarak engelleyin ve sadece gerekli izinleri tanımlayın.
- **Trafik Analizi:** Ağ üzerindeki trafiği sürekli izleyerek (Monitoring) anormal aktiviteleri tespit edin.
- **Sıkılaştırma:** Kullanılmayan tüm servisleri ve portları kapatın.