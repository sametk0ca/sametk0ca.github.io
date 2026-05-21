+++
title = "Ağ Temelleri (Networking Basics) | Networking Basics"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

Network fundamentals are the basic set of information that enables understanding how devices communicate with each other and how data is packaged and routed.

### Summary
Knowing network basics in DevSecOps processes; infrastructure security (IaC) is imperative to secure inter-container communication and cloud network configurations.

### Technical Details
- **IP Addressing:** Identification of devices on the network (IPv4/v6).
- **Protocols:** Data transmission rules (TCP, UDP, ICMP).
- **Ports:** Ports that services listen on (0-65535).
- **Routing & Switching:** How data is transmitted from one point to another.

### Security Approach and Best Practices
- **Default Deny:** Block network traffic by default and define only necessary permissions.
- **Traffic Analysis:** Detect abnormal activities by constantly monitoring the traffic on the network.
- **Hardening:** Close all unused services and ports.
