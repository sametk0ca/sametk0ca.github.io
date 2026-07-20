+++
title = "OSI Modeli - 7 Katman Detayı ve Güvenlik Bakışı | OSI Model - 7 Layers Details and Security Overview"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

OSI (Open Systems Interconnection) modeli, farklı bilgisayar sistemlerinin birbirleriyle iletişim kurabilmesi için ISO tarafından geliştirilmiş teorik bir çerçevedir. Ağı 7 ayrı katmana bölerek karmaşıklığı azaltır ve her katmanın sadece bir üst ve bir alt katmanla konuşmasını sağlar.

### 1. Katman: Fiziksel (Physical Layer)
Verinin kablolar, radyo dalgaları veya fiber optik üzerinden "bit" (0 ve 1) olarak iletildiği katmandır.
- **Teknik Detay:** Voltaj seviyeleri, kablo tipleri (Cat6, Fiber) ve hub cihazları bu katmandadır.
- **Güvenlik Analojisi:** Bir binanın kapısındaki fiziksel kilitler gibidir. Kabloyu kesmek veya bir "tapper" cihazı ile sinyali dinlemek bu katmana yönelik saldırılardır.

### 2. Katman: Veri Bağı (Data Link Layer)
Fiziksel katmandan gelen bitlerin "çerçevelere" (frames) dönüştürüldüğü ve MAC adresleri kullanılarak yerel ağda iletildiği katmandır.
- **Teknik Detay:** Switch'ler ve Ethernet protokolü burada çalışır. Hata kontrolü (CRC) yapılır.
- **Güvenlik (MAC Spoofing & ARP Poisoning):** Saldırganlar kendi MAC adreslerini kurbanınkiyle değiştirerek (spoofing) veya sahte ARP yanıtları göndererek trafiği kendi üzerlerine çekebilirler.

### 3. Katman: Ağ (Network Layer)
Verinin farklı ağlar arasında yönlendirildiği (routing) ve IP adreslerinin kullanıldığı katmandır. Veri birimi "paket" (packet) adını alır.
- **Teknik Detay:** Router'lar ve IP (IPv4/v6), ICMP protokolleri bu katmandadır.
- **Güvenlik (IP Spoofing & DoS):** Paketlerin kaynağını gizleyerek yapılan saldırılar ve ağın paketlerle boğulması (ICMP Flood) bu katmanda gerçekleşir.

### 4. Katman: Taşıma (Transport Layer)
Verinin uçtan uca hatasız iletilmesini sağlar. Veri birimi "segment" (TCP) veya "datagram" (UDP) olarak adlandırılır.
- **Teknik Detay:** TCP (güvenli/bağlantılı) ve UDP (hızlı/bağlantısız) protokolleri buradadır. Port numaraları (0-65535) burada tanımlanır.
- **Güvenlik (SYN Flood):** TCP 3-way handshake sürecini suistimal ederek sistem kaynaklarını tüketme saldırıları bu katmanı hedefler.

### 5. Katman: Oturum (Session Layer)
Uygulamalar arasındaki bağlantıların açılması, yönetilmesi ve kapatılmasını sağlar.
- **Teknik Detay:** RPC, NetBIOS ve SQL oturumları bu katmanda yönetilir.
- **Güvenlik:** Session Hijacking (Oturum Çalma) saldırıları, aktif bir oturumu ele geçirmeyi hedefler.

### 6. Katman: Sunum (Presentation Layer)
Verinin "anlaşılabilir" hale getirildiği katmandır. Karakter kodlama (ASCII/UTF-8), şifreleme ve sıkıştırma burada yapılır.
- **Teknik Detay:** SSL/TLS (modern yapılarda katmanlar arası geçiş yapsa da teoride buradadır) ve MIME bu katmandadır.
- **Güvenlik:** Yanlış yapılandırılmış şifreleme algoritmaları veya veri formatı üzerinden yapılan saldırılar.

### 7. Katman: Uygulama (Application Layer)
Kullanıcının doğrudan etkileşime girdiği katmandır.
- **Teknik Detay:** HTTP, FTP, SMTP, DNS protokolleri burada çalışır.
- **Güvenlik (L7 Attacks):** SQL Injection, XSS gibi web uygulama saldırıları ve bot trafikleri bu katmanın konusudur. En karmaşık ve tespit edilmesi en zor saldırılar genellikle buradadır.

---

## English Version

The OSI (Open Systems Interconnection) model is a theoretical framework developed by ISO for different computer systems to communicate with each other. It reduces complexity by dividing the network into 7 separate layers and ensures that each layer only talks to one upper and one lower layer.

### Layer 1: Physical (Physical Layer)
It is the layer where data is transmitted as "bits" (0 and 1) over cables, radio waves or fiber optics.
- **Technical Details:** Voltage levels, cable types (Cat6, Fiber) and hub devices are in this layer.
- **Security Analogy:** It is like physical locks on the door of a building. Cutting the cable or listening to the signal with a "tapper" device are attacks against this layer.

### Layer 2: Data Link Layer
It is the layer where bits coming from the physical layer are converted into "frames" and transmitted on the local network using MAC addresses.
- **Technical Details:** Switches and Ethernet protocol work here. Error checking (CRC) is performed.
- **Security (MAC Spoofing & ARP Poisoning):** Attackers can divert traffic by changing their MAC addresses with the victim's (spoofing) or by sending fake ARP responses.

### Layer 3: Network (Network Layer)
It is the layer where data is routed between different networks and IP addresses are used. The data unit is called "packet".
- **Technical Details:** Routers, IP (IPv4/v6), ICMP protocols are in this layer.
- **Security (IP Spoofing & DoS):** Attacks by hiding the source of packets and flooding the network with packets (ICMP Flood) occur in this layer.

### Layer 4: Transport (Transport Layer)
It ensures that data is transmitted end-to-end without errors. The unit of data is called a "segment" (TCP) or "datagram" (UDP).
- **Technical Details:** TCP (secure/connection) and UDP (fast/connectionless) protocols are here. Port numbers (0-65535) are defined here.
- **Security (SYN Flood):** Attacks that consume system resources by abusing the TCP 3-way handshake process target this layer.

### Layer 5: Session (Session Layer)
It allows opening, managing and closing connections between applications.
- **Technical Details:** RPC, NetBIOS and SQL sessions are managed in this layer.
- **Security:** Session Hijacking attacks aim to hijack an active session.

### Layer 6: Presentation Layer
It is the layer where the data is made "understandable". Character encoding (ASCII/UTF-8), encryption and compression are done here.
- **Technical Details:** SSL/TLS (in theory it is here even though it switches between layers in modern structures) and MIME are in this layer.
- **Security:** Attacks via misconfigured encryption algorithms or data format.

### 7th Layer: Application Layer
It is the layer with which the user directly interacts.
- **Technical Details:** HTTP, FTP, SMTP, DNS protocols work here.
- **Security (L7 Attacks):** Web application attacks such as SQL Injection, XSS and bot traffic are the subject of this layer. The most complex and hardest to detect attacks are often found here.
