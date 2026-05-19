+++
title = "Paket Analizi: Wireshark  tcpdump Temelleri"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

Paket analizi, ağdaki trafiği "koklamak" (sniffing) ve her bir veri paketinin içini en ince ayrıntısına kadar incelemektir. Siber güvenlik uzmanları için ağın röntgenini çekmek gibidir.

### 1. Wireshark
Dünyanın en popüler grafik arayüzlü paket analiz aracıdır.
- **Kullanım:** Ağdaki trafiği canlı olarak yakalar ve renkli bir arayüzle gösterir. 
- **Neden Kullanılır?** Bir şifrenin açık metin gidip gitmediğini görmek, ağdaki yavaşlığı bulmak veya bir saldırının (Örn: SQL Injection) izlerini sürmek için kullanılır.
- **Renklerin Anlamı:** Wireshark, paket türlerine göre (TCP, UDP, HTTP) satırları renklendirerek analizi kolaylaştırır.

### 2. tcpdump
Komut satırı üzerinden çalışan, çok hızlı ve hafif bir paket yakalama aracıdır.
- **Kullanım:** Genellikle sunucularda veya grafik arayüzü olmayan cihazlarda trafiği hızlıca yakalayıp bir `.pcap` dosyasına kaydetmek için kullanılır. Sonrasında bu dosya Wireshark ile incelenebilir.

### 3. Bilmen Gereken Bazı Terimler
- **Sniffing (Koklama):** Ağ trafiğini izinsiz veya izinli olarak dinleme eylemi.
- **PCAP (Packet Capture):** Yakalanan ağ trafiklerinin kaydedildiği standart dosya formatı.
- **Three-Way Handshake (Üçlü El Sıkışma):** TCP bağlantısının kurulma aşaması (SYN -> SYN-ACK -> ACK). Wireshark'ta bunu görmek, bir bağlantının sağlıklı başlayıp başlamadığını anlamanızı sağlar.
- **Follow TCP Stream:** Wireshark'ın, yüzlerce paket arasından sadece tek bir sohbeti (akışı) ayıklayıp size bir metin belgesi gibi sunma özelliğidir.

### 4. Güvenlik Uyarıları
- Paket analizi yapmak için yönetici (Root/Admin) yetkisi gerekir.
- Başkasının trafiğini izinsiz dinlemek suçtur. Bu araçları her zaman kendi ağınızda veya izinli olduğunuz ortamlarda kullanmalısınız.

### Gerçek Dünya Analojisi
Ağı bir otoyol olarak düşünün. `tcpdump`, otoyol kenarındaki bir kameradır; tüm plakaları ve araç geçişlerini kaydeder. `Wireshark` ise bu kayıtları alıp araçların markasını, içindeki yolcuları ve hatta bagajdaki eşyaları inceleyen dedektiftir.