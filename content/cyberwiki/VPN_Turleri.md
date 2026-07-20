+++
title = "VPN (Virtual Private Network) Türleri ve Güvenlik | VPN (Virtual Private Network) Types and Security"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

VPN, internet gibi güvensiz bir ağ üzerinde iki nokta arasında şifreli ve güvenli bir "tünel" oluşturma teknolojisidir. Uzaktan çalışma ve şubeler arası güvenli bağlantı için vazgeçilmezdir.

### 1. Temel Çalışma Mantığı
Veriler orijinal haliyle internete çıkmadan önce VPN protokolü tarafından şifrelenir ve bir paket içine (encapsulation) konur. Bu sayede servis sağlayıcılar veya ağdaki saldırganlar verinin içeriğini göremez.

### 2. Yaygın VPN Türleri
- **Remote Access VPN (İstemciden Ağa):** Tek bir kullanıcının (Örn: Evden çalışan personel) kurum ağına bağlanması. Genellikle SSL/TLS veya IPsec kullanılır.
- **Site-to-Site VPN (Ağdan Ağa):** İki farklı fiziksel konumun (Örn: İstanbul ve Ankara ofisleri) internet üzerinden tek bir ağmış gibi bağlanması. IPsec standarttır.

### 3. Kullanılan Protokoller
- **IPsec (Internet Protocol Security):** Ağ katmanında (Layer 3) çalışır. Çok güçlü şifreleme sunar. Genellikle Site-to-Site bağlantılarda tercih edilir.
- **SSL/TLS VPN:** Uygulama katmanında çalışır. Web tarayıcısı üzerinden bile bağlanılabilir (AnyConnect, OpenVPN). Esnekliği nedeniyle Remote Access için idealdir.
- **WireGuard:** Çok daha modern, hızlı ve basit kod yapısına sahip, yüksek güvenlikli yeni nesil bir protokoldür.

### 4. Kritik Kavramlar ve Güvenlik
- **Split Tunneling:** İnternet trafiğinin (Örn: YouTube) normal internetten, şirket trafiğinin ise VPN'den gitmesi. Performans sağlar ama risklidir (Kullanıcı cihazı üzerinden iç ağa sızıntı olabilir).
- **Full Tunneling:** Tüm trafiğin VPN üzerinden geçmesi. En güvenli yöntemdir; kurum tüm trafiği denetleyebilir.
- **MFA (Multi-Factor Authentication):** VPN girişlerinde sadece şifre yetmez; mutlaka SMS veya uygulama onayı (MFA) eklenmelidir.

### Gerçek Dünya Analojisi
VPN, kalabalık bir şehirde (İnternet) size özel, görünmez ve zırhlı bir yer altı tüneli kazmak gibidir. Dışarıdakiler tünelin giriş ve çıkışını görebilir ama içinden ne geçtiğini asla bilemezler.

---

## English Version

VPN is a technology for creating an encrypted and secure "tunnel" between two points on an insecure network such as the internet. It is indispensable for remote working and secure connection between branches.

### 1. Basic Working Logic
Before the data is released to the internet in its original form, it is encrypted by the VPN protocol and placed in a packet (encapsulation). In this way, service providers or attackers on the network cannot see the content of the data.

### 2. Common VPN Types
- **Remote Access VPN (Client to Network):** Connecting a single user (e.g. staff working from home) to the corporate network. Usually SSL/TLS or IPsec is used.
- **Site-to-Site VPN (Network to Network):** Connecting two different physical locations (Ex: Istanbul and Ankara offices) over the internet as if they were a single network. IPsec is standard.

### 3. Protocols Used
- **IPsec (Internet Protocol Security):** It works at the network layer (Layer 3). It offers very strong encryption. It is generally preferred in Site-to-Site connections.
- **SSL/TLS VPN:** Works at the application layer. It can even be connected via web browser (AnyConnect, OpenVPN). It is ideal for Remote Access due to its flexibility.
- **WireGuard:** It is a new generation protocol with high security, with a much more modern, faster and simpler code structure.

### 4. Critical Concepts and Security
- **Split Tunneling:** Internet traffic (e.g. YouTube) goes through the normal internet and company traffic goes through the VPN. It provides performance but is risky (there may be leakage to the internal network through the user device).
- **Full Tunneling:** All traffic passes through VPN. It is the safest method; The institution can monitor all traffic.
- **MFA (Multi-Factor Authentication):** Password alone is not enough for VPN logins; SMS or application approval (MFA) must be added.

### Real World Analogy
VPN is like digging a private, invisible and armored underground tunnel in a crowded city (the Internet). Outsiders can see the entrance and exit of the tunnel, but they never know what goes through it.
