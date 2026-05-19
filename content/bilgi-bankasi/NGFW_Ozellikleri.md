+++
title = "Next-Gen Firewall (NGFW) Özellikleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Klasik firewall'lar sadece IP adresine ve porta (Örn: "80 portunu aç/kapat") bakarken, Yeni Nesil Firewall'lar (NGFW) çok daha "zekidir" ve trafiğin içinde ne olduğunu tam olarak anlar.

### 1. NGFW'nun Klasik Firewall'dan Farkı
- **Uygulama Farkındalığı (App-ID):** Sadece porta bakmaz. "Bu trafik 80 portundan geçiyor ama aslında Facebook mu, yoksa bir virüs mü?" sorusuna yanıt verir.
- **Kullanıcı Kimliği (User-ID):** IP adresine değil, "User" kullanıcısına göre kural yazmanızı sağlar.
- **İçerik İnceleme (DPI):** Paketi açar, içindeki veriyi okur ve gizli bir zararlı yazılım olup olmadığını kontrol eder.

### 2. Kritik Özellikler
- **DPI (Deep Packet Inspection):** Paketin sadece zarfına değil, içindeki mektubun içeriğine de bakma teknolojisidir.
- **SSL Decryption (Şifre Çözme):** Günümüzde internet trafiğinin %90'ı şifrelidir (HTTPS). NGFW, bu şifreyi geçici olarak çözüp içindeki zararlıları kontrol edebilir.
- **Bütünleşik IPS:** NGFW içinde yerleşik bir Saldırı Önleme Sistemi (IPS) barındırır.
- **Sandboxing:** Şüpheli bir dosyayı önce kendi içindeki güvenli bir alanda (kum havuzu) çalıştırıp zararlı olup olmadığını test eder.

### 3. Bilmen Gereken Bazı Terimler
- **Payload:** Paketin içinde taşınan asıl veri/yük.
- **Threat Intelligence:** Firewall'un dünyadaki en yeni saldırıları öğrenmesini sağlayan "istihbarat" akışı.
- **Egress Filtering:** Dışarıdan geleni değil, içeriden dışarıya sızmaya çalışan veriyi engelleme işlemi.

### Gerçek Dünya Analojisi
Klasik firewall, bir paketin sadece üzerindeki adrese bakıp içeri alan bir kurye gibidir. NGFW ise paketi açan, içindeki ürünün sahte olup olmadığını kontrol eden, faturasına bakan ve alıcının kimliğini doğrulayan bir gümrük memuru gibidir.