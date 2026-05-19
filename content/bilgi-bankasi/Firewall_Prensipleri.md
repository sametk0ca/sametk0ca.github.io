+++
title = "Firewall (Güvenlik Duvarı) Çalışma Prensipleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Firewall, ağınızın kapısındaki "güvenlik görevlisi"dir. Gelen ve giden ağ trafiğini önceden belirlenmiş güvenlik kurallarına göre denetler ve ya izin verir ya da engeller.

### 1. Temel Mantık: İzin Verilmeyen Her Şey Yasaktır
Güvenlik dünyasında iki yaklaşım vardır:
- **Blacklisting (Kara Liste):** Her şeye izin ver, sadece kötüleri engelle. (Çok risklidir).
- **Whitelisting (Beyaz Liste):** Her şeyi engelle, sadece güvenli olduğunu bildiklerine izin ver. (Firewall'lar genellikle bu mantıkla, yani **Implicit Deny** kuralı ile çalışır).

### 2. Firewall Türleri
- **Packet Filtering (Paket Filtreleme):** En temel seviyedir. Sadece IP adresine ve porta bakar. "Hangi mektup nereden geliyor?" diye bakar ama mektubun içini okumaz.
- **Stateful Inspection (Durumsal Denetim):** Daha zekidir. Bağlantının durumunu (state) takip eder. Eğer siz bir web sitesine istek gönderdiyseniz, o siteden gelen yanıtın "beklenen bir yanıt" olduğunu anlar ve izin verir. Dışarıdan durup dururken gelen bağlantıları engeller.
- **Next-Gen Firewall (NGFW):** Günümüzün modern duvarlarıdır. Sadece porta değil, uygulamanın kendisine de bakar. Örneğin, 80 portundan (HTTP) geçen trafiğin Facebook mu yoksa bir virüs mü olduğunu ayırt edebilir.

### 3. Bilmen Gereken Bazı Terimler
- **IDS (Intrusion Detection System):** Saldırı Tespit Sistemi. Sadece "Hırsız var!" diye bağırır ama müdahale etmez.
- **IPS (Intrusion Prevention System):** Saldırı Önleme Sistemi. Hırsızı görür ve kapıyı kilitleyerek girmesini engeller.
- **Teardrop Saldırısı:** Bir saldırganın, hedef bilgisayara bilerek "parçalanmış ve üst üste binen" (overlapping fragments) IP paketleri göndermesidir. Bilgisayar bu paketleri birleştirmeye çalışırken kafası karışır ve sistemi çöker. Modern firewall'lar bu paketleri temizleyerek içeri sokmaz.

### Gerçek Dünya Analojisi
Firewall, bir sitenin girişindeki güvenlik kulübesi gibidir. Görevli, gelen arabanın plakasına (IP) ve kime geldiğine (Port) bakar. Eğer listede varsanız (Rules) kapıyı açar. Next-Gen bir görevli ise arabanın bagajını da açtırıp (DPI - Deep Packet Inspection) içinde tehlikeli bir madde olup olmadığına bakar.