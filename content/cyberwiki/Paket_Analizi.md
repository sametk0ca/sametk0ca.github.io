+++
title = "Paket Analizi: Wireshark  tcpdump Temelleri | Packet Analysis: Wireshark tcpdump Basics"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

Packet analysis is the process of "sniffing" traffic on the network and examining the inside of each data packet in minute detail. For cybersecurity experts, it's like taking an x-ray of the network.

### 1. Wireshark
It is the world's most popular graphical interface packet analysis tool.
- **Usage:** Captures live traffic on the network and displays it with a colorful interface. 
- **Why is it used?** It is used to see whether a password is in clear text, to find slowness in the network, or to trace the traces of an attack (Ex: SQL Injection).
- **Meaning of Colors:** Wireshark facilitates analysis by coloring lines according to packet types (TCP, UDP, HTTP).

### 2. tcpdump
It is a very fast and lightweight packet capture tool that works via the command line.
- **Usage:** Typically used on servers or devices without a graphical interface to quickly capture traffic and save it to a `.pcap` file. This file can then be examined with Wireshark.

### 3. Some Terms You Should Know
- **Sniffing:** The act of listening to network traffic without permission or permission.
- **PCAP (Packet Capture):** Standard file format in which captured network traffic is saved.
- **Three-Way Handshake:** TCP connection establishment phase (SYN -> SYN-ACK -> ACK). Seeing this in Wireshark lets you know if a connection is starting off healthy.
- **Follow TCP Stream:** It is the feature of Wireshark that extracts only a single conversation (stream) from hundreds of packets and presents it to you as a text document.

### 4. Safety Warnings
- Root/Admin authority is required to perform package analysis.
- It is a crime to listen to someone else's traffic without permission. You should always use these tools on your own network or in authorized environments.

### Real World Analogy
Think of the network as a highway. `tcpdump` is a camera on the side of the highway; records all license plates and vehicle passes. 'Wireshark' is the detective who takes these records and examines the brand of the vehicles, the passengers inside and even the items in the trunk.
