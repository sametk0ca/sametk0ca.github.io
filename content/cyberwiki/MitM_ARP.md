+++
title = "MitM (Man-in-the-Middle) ve ARP Poisoning | MitM (Man-in-the-Middle) and ARP Poisoning"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

A MitM (Man in the Middle) attack is the act of an attacker eavesdropping, intercepting or altering communications between two parties.

### 1. MitM Logic
When you enter a site on the internet, you think that the data goes directly. In a MitM attack, the attacker intervenes. You think you are sending the packet to the server, but you are actually sending it to the attacker. The attacker reads the packet and then forwards it to the server. Even your soul can't hear it.

### 2. ARP Poisoning
It is the most common way to do MitM on a local network (Wi-Fi or Office network).
- **How ​​Does It Work?** In the local network, devices talk using physical MAC addresses, not IP addresses. The attacker shouts "I'm the modem!" to all devices on the network. and tell the modem "Everyone is mine!" he lies.
- **Result:** All traffic on the network first goes to the attacker's computer, passes it through and releases it to the internet.

### 3. Some Terms You Should Know
- **Cleartext:** Unencrypted, plaintext data. (like HTTP). When MitM is done, everything can be read.
- **Packet Sniffing:** The act of capturing and monitoring packets passing through the network (done with Wireshark).
- **SSL Stripping:** It is when the attacker intervenes and downgrades your HTTPS (secure) connection to HTTP (insecure) and steals your passwords.
- **ARP Cache:** It is the memory that your computer keeps for "whose IP is at which MAC address". Poisoning corrupts this place.

### 4. Ways of Protection
- **Use VPN:** It encrypts all your traffic so that the man in the middle cannot understand anything.
- **HTTPS Control:** Make sure that the sites you enter have a lock sign in the address bar and that the connection is not dropped.
- **Static ARP:** Manually fixing the ARP table in critical systems (difficult but safe).
- **Public Wi-Fi:** Try not to do banking on public networks such as cafes and airports.

### Real World Analogy
Imagine two friends (A and B) exchange letters by throwing paper airplanes at each other. C (Aggressor) stands in the middle. When A launches the plane, he catches it in the air, reads its insides, maybe changes the message, and then throws it to B. A and B still think they are talking to each other.
