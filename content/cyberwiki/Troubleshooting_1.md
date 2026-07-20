+++
title = "Sorun Giderme Araçları - Bölüm 1: ping ve traceroute | Troubleshooting Tools - Part 1: ping and traceroute"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Ağda bir sorun olduğunda (bağlantı kopması, yavaşlık vb.) ilk başvurulan araçlar bunlardır. Hepsi "Komut Satırı" (CLI) üzerinden çalışır.

### 1. ping (İnternet Kontrol Mesaj Protokolü - ICMP)
Hedef cihazın "hayatta" olup olmadığını kontrol eder.
- **Nasıl Çalışır?** Karşı tarafa bir "Yankı İsteği" (Echo Request) gönderir. Karşı taraf da "Yankı Yanıtı" (Echo Reply) döner.
- **Güvenlik Notu:** Bazı sunucular güvenlik nedeniyle ping isteklerine yanıt vermez (ICMP paketlerini bloklar). Bu, o sunucunun kapalı olduğu anlamına gelmez, sadece "benimle konuşma" dediği anlamına gelir.
- **Terim - TTL (Time To Live):** Bir paketin ağda ne kadar "ömrü" olduğunu belirleyen sayıdır. Her router üzerinden geçtiğinde bu sayı 1 azalır. 0 olduğunda paket yok edilir. Bu, paketlerin ağda sonsuza kadar dönüp durmasını (loop) engeller.

### 2. traceroute (veya Windows'ta tracert)
Paketinizin hedefe giderken hangi yollardan (router'lardan) geçtiğini gösterir.
- **Nasıl Çalışır?** TTL değerini bilerek 1'den başlayarak artırır. Paket her router'da patladığında (TTL=0 olduğunda), o router size "Hata: Paket bende öldü" diye mesaj atar. Böylece yol üzerindeki tüm durakları tek tek öğrenmiş olursunuz.
- **Kullanım Amacı:** İnternet yavaşsa, yavaşlığın tam olarak hangi noktadan (ISS, deniz altı kablosu, sunucu yanı vb.) kaynaklandığını bulmanızı sağlar.

### 3. Bilmen Gereken Bazı Terimler
- **Hop (Durak):** Paketinizin geçtiği her bir yönlendiriciye (router) denir.
- **RTT (Round Trip Time):** Bir paketin hedefe gidip geri gelmesi için geçen toplam süre (Milisaniye - ms cinsinden).
- **Packet Loss (Paket Kaybı):** Gönderilen paketlerin bazılarını geri gelmemesi. Ciddi bir ağ sorunu veya saldırı (DoS) belirtisidir.

### Gerçek Dünya Analojisi
- **ping:** Bir arkadaşınızın kapısını çalıp "Orada mısın?" diye bağırmak gibidir. "Evet!" derse ping başarılıdır.
- **traceroute:** Arkadaşınıza giden yol üzerindeki her kavşakta durup "Burası neresi? Bir sonraki kavşak neresi?" diye sormak gibidir.

---

## English Version

These are the first tools used when there is a problem with the network (disconnection, slowness, etc.). They all work via the "Command Line" (CLI).

### 1. ping (Internet Control Message Protocol - ICMP)
Checks if the target device is "alive".
- **How ​​Does It Work?** It sends an "Echo Request" to the other party. The other party also returns an "Echo Reply".
- **Security Note:** Some servers do not respond to ping requests (block ICMP packets) for security reasons. This doesn't mean that server is down, it just means it says "don't talk to me".
- **Term - TTL (Time To Live):** It is the number that determines how long a packet "lives" on the network. This number decreases by 1 each time it passes through the router. When it is 0, the packet is destroyed. This prevents packets from looping around the network indefinitely.

### 2. traceroute (or tracert on Windows)
It shows which routes (routers) your package passes through on its way to its destination.
- **How ​​Does It Work?** It deliberately increases the TTL value starting from 1. When the packet explodes on each router (when TTL = 0), that router sends you a message saying "Error: The packet died for me". This way, you will learn all the stops on the road one by one.
- **Purpose of Use:** If the internet is slow, it allows you to find out exactly where the slowness is caused (ISP, submarine cable, server side, etc.).

### 3. Some Terms You Should Know
- **Hop:** Each router your package passes through is called a router.
- **RTT (Round Trip Time):** The total time it takes for a packet to travel to the destination and back (in Milliseconds - ms).
- **Packet Loss:** Some of the sent packages are not returned. It is a sign of a serious network problem or attack (DoS).

### Real World Analogy
- **ping:** Knock on a friend's door and ask "Are you there?" It's like shouting. "Yes!" If so, the ping is successful.
- **traceroute:** At every intersection on the way to your friend, you stop and ask, "Where is this? Where is the next intersection?" It's like asking.
