+++
title = "TCPIP Modeli - 4 Katmanlı Yapı ve Güvenlik | TCPIP Model - 4-Layer Structure and Security"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

OSI modeli teorik bir standart iken, TCP/IP modeli bugün internetin üzerinde çalıştığı pratik ve gerçek dünya modelidir. 1970'lerde Savunma İleri Araştırma Projeleri Ajansı (DARPA) tarafından geliştirilmiştir.

### 1. Ağ Arayüzü Katmanı (Network Interface Layer)
OSI'nin Fiziksel ve Veri Bağı katmanlarının birleşimidir. Verinin fiziksel ortamda nasıl iletileceğini belirler.
- **Teknik Detay:** Ethernet, Wi-Fi ve PPP protokolleri burada yer alır. Cihazlar arası MAC adresi tabanlı iletişim kurulur.
- **Security:** Bu katmanda ağın koklanması (sniffing) ve fiziksel erişim güvenliği kritiktir.

### 2. İnternet Katmanı (Internet Layer)
Verinin ağlar arasında yönlendirilmesinden (routing) sorumludur. OSI'nin Ağ katmanına denk gelir.
- **Teknik Detay:** IP (Internet Protocol), ICMP, IGMP ve ARP bu katmanın temel taşlarıdır. IP adresleme sistemi burada çalışır.
- **Güvenlik (Fragman Saldırıları):** Büyük IP paketleri küçük parçalara (fragments) bölünerek gönderilebilir. Saldırganlar bu parçaları hatalı veya çakışan şekilde göndererek (Teardrop attack) hedef sistemi çökertebilir.

### 3. Taşıma Katmanı (Transport Layer)
Bilgisayarlar arasındaki veri akışını yönetir. OSI'nin Taşıma katmanıyla aynıdır.
- **TCP (Transmission Control Protocol):** Güvenilir, bağlantı odaklıdır. 3-way handshake (SYN, SYN-ACK, ACK) ile bağlantı kurar. Hata kontrolü ve akış kontrolü yapar.
- **UDP (User Datagram Protocol):** Hızlı, bağlantısızdır. "Gönder ve unut" mantığıyla çalışır. Video yayını ve oyunlar gibi hızın hatasız iletimden önemli olduğu yerlerde kullanılır.
- **Güvenlik:** Port taraması (Scanning) saldırıları bu katmanı analiz ederek hangi servislerin açık olduğunu belirler.

### 4. Uygulama Katmanı (Application Layer)
Kullanıcının kullandığı tüm uygulama protokollerini kapsar (OSI'nin 5, 6 ve 7. katmanları).
- **Teknik Detay:** HTTP (Web), SMTP (E-posta), DNS (İsim Çözümleme), SSH (Güvenli Bağlantı) gibi protokoller burada çalışır.
- **Güvenlik:** Protokol suistimalleri (Exploitler) burada gerçekleşir. Örneğin, savunmasız bir HTTP sunucusuna gönderilen özel hazırlanmış bir istek sunucunun kontrolünü ele geçirmeye yarayabilir.

### OSI vs TCP/IP: Gerçek Dünya Analojisi
OSI modelini bir mimarlık planına, TCP/IP modelini ise o plana göre inşa edilmiş bitmiş bir binaya benzetebiliriz. Biri "nasıl olması gerektiğini" anlatır, diğeri ise "nasıl çalıştığını" gösterir. Güvenlik uzmanları için OSI katmanlara ayırıp sorunu tespit etmek için mükemmeldir ("Hangi katmanda sorun var?"), TCP/IP ise trafiği analiz etmek için daha pratiktir.

---

## English Version

While the OSI model is a theoretical standard, the TCP/IP model is the practical, real-world model on which the Internet operates today. It was developed by the Defense Advanced Research Projects Agency (DARPA) in the 1970s.

### 1. Network Interface Layer
It is the combination of OSI's Physical and Data Link layers. It determines how data will be transmitted in the physical environment.
- **Technical Details:** Ethernet, Wi-Fi and PPP protocols are included here. MAC address-based communication is established between devices.
- **Security:** At this layer, network sniffing and physical access security are critical.

### 2nd Internet Layer
It is responsible for routing data between networks. It corresponds to the Network layer of OSI.
- **Technical Details:** IP (Internet Protocol), ICMP, IGMP and ARP are the cornerstones of this layer. The IP addressing system works here.
- **Security (Fragment Attacks):** Large IP packets can be divided into small fragments and sent. Attackers can crash the target system by sending these parts incorrectly or conflictingly (Teardrop attack).

### 3. Transport Layer
It manages the flow of data between computers. It is the same as the Transport layer of OSI.
- **TCP (Transmission Control Protocol):** Reliable, connection-oriented. It establishes a connection with 3-way handshake (SYN, SYN-ACK, ACK). It performs error checking and flow control.
- **UDP (User Datagram Protocol):** Fast, connectionless. It works on the "send and forget" principle. It is used in places where speed is more important than error-free transmission, such as video streaming and games.
- **Security:** Port scanning attacks analyze this layer and determine which services are open.

### 4. Application Layer
It covers all application protocols used by the user (layers 5, 6 and 7 of the OSI).
- **Technical Details:** Protocols such as HTTP (Web), SMTP (E-mail), DNS (Name Resolution), SSH (Secure Connection) work here.
- **Security:** Protocol abuses (exploits) occur here. For example, a specially crafted request sent to a vulnerable HTTP server could be used to take control of the server.

### OSI vs TCP/IP: Real World Analogy
We can compare the OSI model to an architectural plan, and the TCP/IP model to a finished building built according to that plan. One tells "how it should be", the other shows "how it works". For security professionals, OSI is great for breaking down layers and troubleshooting (“Which layer is wrong?”), while TCP/IP is more practical for analyzing traffic.
