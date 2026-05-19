+++
title = "MitM (Man-in-the-Middle) ve ARP Poisoning"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

MitM (Aradaki Adam) saldırısı, bir saldırganın iki taraf arasındaki iletişimi gizlice dinlemesi, kesmesi veya değiştirmesi eylemidir.

### 1. MitM Mantığı
Siz internette bir siteye girdiğinizde verilerin doğrudan gittiğini sanırsınız. MitM saldırısında saldırgan araya girer. Siz paketi sunucuya gönderdiğinizi sanırsınız ama aslında saldırgana gönderirsiniz. Saldırgan paketi okur ve sonra sunucuya iletir. Ruhunuz bile duymaz.

### 2. ARP Poisoning (ARP Zehirlemesi)
Yerel bir ağda (Wi-Fi veya Ofis ağı) MitM yapmanın en yaygın yoludur.
- **Nasıl Çalışır?** Yerel ağda cihazlar IP adreslerini değil, fiziksel MAC adreslerini kullanarak konuşur. Saldırgan ağdaki tüm cihazlara "Modem benim!" ve modeme de "Herkes benim!" diye yalan söyler.
- **Sonuç:** Ağdaki tüm trafik önce saldırganın bilgisayarına gider, o üzerinden geçirip internete salar.

### 3. Bilmen Gereken Bazı Terimler
- **Cleartext:** Şifrelenmemiş, düz metin veri. (HTTP gibi). MitM yapıldığında her şey okunabilir.
- **Packet Sniffing:** Ağdan geçen paketleri yakalayıp izleme eylemi (Wireshark ile yapılır).
- **SSL Stripping:** Saldırganın araya girerek sizin HTTPS (güvenli) bağlantınızı HTTP'ye (güvensiz) düşürmesi ve şifrelerinizi çalmasıdır.
- **ARP Cache:** Bilgisayarınızın "kimin IP'si hangi MAC adresinde" diye tuttuğu hafızadır. Zehirleme burayı bozar.

### 4. Korunma Yolları
- **VPN Kullanın:** Tüm trafiğinizi şifreleyerek aradaki adamın bir şey anlamamasını sağlar.
- **HTTPS Kontrolü:** Girdiğiniz sitelerin adres çubuğunda kilit işareti olduğundan ve bağlantının düşürülmediğinden emin olun.
- **Statik ARP:** Kritik sistemlerde ARP tablosunu elle sabitlemek (zordur ama güvenlidir).
- **Public Wi-Fi:** Kafe ve havalimanı gibi herkese açık ağlarda bankacılık işlemi yapmamaya çalışın.

### Gerçek Dünya Analojisi
İki arkadaşın (A ve B) birbirine kağıttan uçak atarak mektuplaştığını düşünün. C (Saldırgan) ortada durur. A uçağı fırlattığında havada yakalar, içini okur, belki mesajı değiştirir ve sonra B'ye fırlatır. A ve B hala birbirleriyle konuştuklarını sanırlar.