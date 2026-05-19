+++
title = "Kerberos - Bilet Tabanlı Kimlik Doğrulama Mekanizması"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Kerberos, güvensiz ağlarda bile güvenli kimlik doğrulaması sağlamak için tasarlanmış, "bilet" (ticket) sistemine dayalı bir protokoldür. Windows Active Directory'nin temel taşıdır.

### 1. Temel Bileşenler (KDC - Key Distribution Center)
Kerberos ekosisteminde üç ana aktör vardır:
- **Client (İstemci):** Servis kullanmak isteyen kullanıcı.
- **Server (Sunucu):** Erişilmek istenen servis (Örn: Dosya sunucusu).
- **KDC:** Güvenilir üçüncü taraf. İki parçadan oluşur:
    - **AS (Authentication Service):** Kullanıcının kimliğini doğrular.
    - **TGS (Ticket Granting Service):** Servislere erişim için bilet dağıtır.

### 2. Çalışma Süreci (6 Adım)
1. **AS Request:** Kullanıcı kullanıcı adını gönderir.
2. **AS Reply:** Sunucu, kullanıcıya bir **TGT (Ticket Granting Ticket)** ve bir oturum anahtarı döner (Kullanıcının şifresinden türetilen anahtarla şifreli).
3. **TGS Request:** Kullanıcı, "Şu servise gitmek istiyorum" diyerek TGT'sini sunar.
4. **TGS Reply:** Sunucu, kullanıcıya o servis için özel bir **Service Ticket** döner.
5. **AP Request:** Kullanıcı, aldığı servis biletini hedef sunucuya sunar.
6. **AP Reply:** Hedef sunucu bileti doğrular ve erişim izni verir.

### 3. Kerberos Neden Güvenlidir?
- **Şifre Ağda Taşınmaz:** Şifrenin kendisi asla ağ üzerinden gönderilmez; sadece şifreden türetilen anahtarlar kullanılır.
- **Zaman Damgaları (Timestamps):** Biletlerin içine zaman damgası eklenir. Eğer bir saldırgan bileti çalarsa, biletin süresi (genellikle 5 dakika) geçmeden kullanamaz (Replay attack önlemi).
- **Tek Seferlik Giriş (SSO):** Bir kez TGT aldıktan sonra, şifre girmeden birçok farklı servise erişebilirsiniz.

### 4. Kerberos Saldırıları (Active Directory)
- **Golden Ticket:** KDC'nin (krbtgt) anahtarını ele geçiren bir saldırganın, ağdaki her şeye erişebilecek sahte bir bilet oluşturması.
- **Silver Ticket:** Sadece belirli bir servise (Örn: SQL) tam yetkiyle erişmek için oluşturulan sahte bilet.
- **Kerberoasting:** Servis biletlerini (TGS) toplayıp çevrimdışı (offline) olarak şifrelerini kırmaya çalışmak.

### Gerçek Dünya Analojisi
Bir eğlence merkezine (Ağ) girdiğinizi düşünün. Kapıda (AS) kimlik gösterip bir bileklik (TGT) alırsınız. Bu bileklikle içerideki her oyuncağa (Servis) gidebilirsiniz. Her oyuncak sırasına girdiğinizde biletinizi (TGS) gösterirsiniz ve görevli size geçiş izni verir.