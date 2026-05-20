+++
title = "Sorun Giderme Araçları - Bölüm 1: ping ve traceroute"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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