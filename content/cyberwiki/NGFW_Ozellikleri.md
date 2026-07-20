+++
title = "Next-Gen Firewall (NGFW) Özellikleri | Next-Gen Firewall (NGFW) Features"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
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

---

## English Version

While classic firewalls only look at the IP address and port (e.g. "open/close port 80"), New Generation Firewalls (NGFW) are much more "intelligent" and understand exactly what is in the traffic.

### 1. Difference of NGFW from Classic Firewall
- **Application Awareness (App-ID):** It doesn't just look at the port. "This traffic is going through port 80, but is it actually Facebook or is it a virus?" answers the question.
- **User-ID:** Allows you to write rules based on the "User" user, not the IP address.
- **Content Inspection (DPI):** Opens the package, reads the data inside and checks for hidden malware.

### 2. Critical Features
- **DPI (Deep Packet Inspection):** It is the technology of examining not only the envelope of the package but also the content of the letter inside.
- **SSL Decryption:** Today, 90% of internet traffic is encrypted (HTTPS). NGFW can temporarily decrypt this password and check for malware inside.
- **Integrated IPS:** NGFW has a built-in Intrusion Prevention System (IPS).
- **Sandboxing:** It first runs a suspicious file in its own safe area (sandbox) and tests whether it is harmful or not.

### 3. Some Terms You Should Know
- **Payload:** The actual data/payload carried within the package.
- **Threat Intelligence:** The "intelligence" stream that allows Firewall to learn about the latest attacks in the world.
- **Egress Filtering:** The process of blocking data that tries to leak from inside to outside, not from outside.

### Real World Analogy
A classic firewall is like a courier who only looks at the address on a package and lets it in. NGFW, on the other hand, is like a customs officer who opens the package, checks whether the product inside is fake, looks at the invoice and verifies the identity of the buyer.
