+++
title = "Public vs Private IP Farkları ve NAT Mekanizması | Public vs Private IP Differences and NAT Mechanism"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

İnternet dünyasında her cihazın bir kimliği (IP adresi) vardır. Ancak bu kimlikler "evrensel" ve "yerel" olmak üzere ikiye ayrılır.

### 1. Public IP (Genel IP)
İnternet servis sağlayıcınız (ISP) tarafından modeminize atanan, tüm dünyada benzersiz olan adrestir.
- **Karakteristik:** İnternet üzerindeki herhangi bir yerden bu adrese ulaşılabilir.
- **Güvenlik:** Public IP'niz doğrudan saldırı alabilir. Firewall (Güvenlik Duvarı) bu noktada ilk savunma hattıdır.

### 2. Private IP (Özel IP) - RFC 1918
Yerel ağınızda (ev, ofis) cihazların birbirleriyle konuşması için kullanılan adreslerdir.
- **Bloklar:**
    - `10.0.0.0 /8` (Büyük kurumsal ağlar)
    - `172.16.0.0 /12` (Orta ölçekli ağlar)
    - `192.168.0.0 /16` (Ev ve küçük ofisler)
- **Karakteristik:** İnternet üzerinden doğrudan bu adreslere ulaşılamaz. Bu durum, iç ağdaki cihazlar için doğal bir koruma sağlar.

### 3. NAT (Network Address Translation) Nedir?
Onlarca cihazın tek bir Public IP üzerinden internete çıkmasını sağlayan teknolojidir.
- **Nasıl Çalışır?** İç ağdaki bir cihaz (Örn: 192.168.1.10) internete bir istek gönderdiğinde, Router bu isteğin kaynağını kendi Public IP'si ile değiştirir ve hangi cihazın hangi isteği yaptığını bir tabloda (NAT Table) tutar. Yanıt geldiğinde, tabloya bakarak paketi içerdeki doğru cihaza iletir.
- **Güvenlik Avantajı:** Dışarıdaki bir saldırgan, iç ağdaki cihazın Private IP'sini bilse bile NAT tablosunda bir kayıt (istek) olmadığı sürece içeri sızamaz.

### 4. Statik IP ve Dinamik IP
- **Dinamik IP:** Çoğu ev kullanıcısında olduğu gibi, modem her açıldığında değişen IP'dir. Takibi biraz daha zordur.
- **Statik IP:** Hiç değişmeyen adrestir. Sunucular ve VPN ağları için gereklidir. Saldırganlar için "sabit bir hedef" oluşturduğu için ekstra koruma gerektirir.

### Gerçek Dünya Analojisi
Bir siteyi (apartman kompleksini) düşünün. Sitenin tek bir posta adresi vardır (Public IP). Ancak sitenin içinde yüzlerce daire (Private IP) bulunur. Postacı kargoyu site girişindeki güvenliğe (Router/NAT) bırakır. Güvenlik, paketin hangi daireye ait olduğunu kontrol edip içeri dağıtır. Dışarıdan kimse daire kapılarını doğrudan göremez.

---

## English Version

In the Internet world, every device has an ID (IP address). However, these identities are divided into two: "universal" and "local".

### 1. Public IP
It is the globally unique address assigned to your modem by your internet service provider (ISP).
- **Characteristic:** This address can be accessed from anywhere on the Internet.
- **Security:** Your public IP can be directly attacked. Firewall is the first line of defense at this point.

### 2. Private IP - RFC 1918
These are the addresses used for devices to talk to each other in your local network (home, office).
- **Blocks:**
    - `10.0.0.0 /8` (Large enterprise networks)
    - `172.16.0.0 /12` (Medium networks)
    - `192.168.0.0 /16` (Home and small offices)
- **Characteristic:** These addresses cannot be reached directly via the Internet. This provides natural protection for devices on the internal network.

### 3. What is NAT (Network Address Translation)?
It is the technology that allows dozens of devices to access the Internet via a single Public IP.
- **How ​​Does It Work?** When a device on the internal network (Ex: 192.168.1.10) sends a request to the internet, the Router replaces the source of this request with its own Public IP and keeps which device made which request in a table (NAT Table). When the response arrives, it looks at the table and forwards the packet to the correct device inside.
- **Security Advantage:** Even if an outside attacker knows the Private IP of the device on the internal network, he cannot infiltrate unless there is a record (request) in the NAT table.

### 4. Static IP and Dynamic IP
- **Dynamic IP:** As with most home users, this is the IP that changes every time the modem is turned on. It's a little more difficult to follow.
- **Static IP:** It is the address that never changes. Required for servers and VPN networks. It requires extra protection because it creates a "fixed target" for attackers.

### Real World Analogy
Consider a site (apartment complex). The site has a single mailing address (Public IP). However, there are hundreds of flats (Private IP) within the site. The postman leaves the cargo to the security (Router/NAT) at the site entrance. Security checks which apartment the package belongs to and distributes it inside. No one from outside can see the apartment doors directly.
