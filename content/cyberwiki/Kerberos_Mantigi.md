+++
title = "Kerberos - Bilet Tabanlı Kimlik Doğrulama Mekanizması | Kerberos - Ticket-Based Authentication Mechanism"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

Kerberos is a "ticket"-based protocol designed to provide secure authentication even on insecure networks. It is the cornerstone of Windows Active Directory.

### 1. Basic Components (KDC - Key Distribution Center)
There are three main actors in the Kerberos ecosystem:
- **Client:** The user who wants to use the service.
- **Server:** The service to be accessed (Ex: File server).
- **KDC:** Trusted third party. It consists of two parts:
    - **AS (Authentication Service):** Verifies the user's identity.
    - **TGS (Ticket Granting Service):** Distributes tickets for access to services.

### 2. Working Process (6 Steps)
1. **AS Request:** User sends username.
2. **AS Reply:** The server returns a **TGT (Ticket Granting Ticket)** and a session key to the user (encrypted with the key derived from the user's password).
3. **TGS Request:** The user submits his TGT by saying "I want to go to that service".
4. **TGS Reply:** The server returns a special **Service Ticket** to the user for that service.
5. **AP Request:** The user submits the service ticket he received to the target server.
6. **AP Reply:** The target server verifies the ticket and grants access.

### 3. Why is Kerberos Secure?
- **Password is not carried over the network:** The password itself is never sent over the network; only keys derived from the password are used.
- **Timestamps:** Timestamps are added to the tickets. If an attacker steals the ticket, he cannot use it until the ticket expires (usually 5 minutes) (Replay attack precaution).
- **One-Time Login (SSO):** Once you get TGT, you can access many different services without entering a password.

### 4. Kerberos Attacks (Active Directory)
- **Golden Ticket:** An attacker who obtains the key of the KDC (krbtgt) creates a fake ticket that can access everything on the network.
- **Silver Ticket:** A fake ticket created to access only a specific service (Ex: SQL) with full authority.
- **Kerberoasting:** Collecting service tickets (TGS) and trying to crack their passwords offline.

### Real World Analogy
Imagine walking into an entertainment center (Network). You show your ID at the door (AS) and receive a wristband (TGT). With this wristband you can go to every toy (Service) inside. When you enter each toy row, you show your ticket (TGS) and the officer gives you permission to pass.
