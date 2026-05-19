+++
title = "TCPIP Modeli - 4 Katmanlı Yapı ve Güvenlik"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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