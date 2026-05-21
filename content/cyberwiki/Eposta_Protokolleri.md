+++
title = "SMTP  POP3  IMAP - E-posta Protokolleri ve Güvenlik | SMTP POP3 IMAP - Email Protocols and Security"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

E-posta sistemi, gönderim ve alım için farklı protokollerin bir arada çalıştığı bir ekosistemdir.

### 1. SMTP (Simple Mail Transfer Protocol) - Gönderme
E-postaları bir sunucudan diğerine veya istemciden sunucuya iletmek için kullanılır.
- **Portlar:**
    - `25`: Eski standart, şifresiz. Genellikle spam engellemek için ISP'ler tarafından bloklanır.
    - `587`: Modern standart (Submission). STARTTLS ile şifreleme sağlar.
    - `465`: SMTPS (Implicit TLS). Başından itibaren şifreli bağlantı kurar.

### 2. POP3 (Post Office Protocol v3) - Alım
E-postaları sunucudan bilgisayarınıza indirmek için kullanılır.
- **Mantık:** E-postayı indirir ve genellikle sunucudan siler. Tek bir cihazdan erişim için uygundur.
- **Portlar:** `110` (Şifresiz), `995` (SSL/TLS).

### 3. IMAP (Internet Message Access Protocol) - Senkronizasyon
E-postaları sunucuda tutar ve cihazlar arasında senkronize eder.
- **Mantık:** E-posta sunucuda kalır, siz sadece bir kopyasını görürsünüz. Telefon, tablet ve bilgisayardan aynı anda erişim için idealdir.
- **Portlar:** `143` (Şifresiz), `993` (SSL/TLS).

### 4. E-posta Güvenliği Katmanları (Anti-Spoofing)
Sadece protokolleri şifrelemek yetmez, e-postanın kimden geldiğini doğrulamak için şu kayıtlar şarttır:
- **SPF (Sender Policy Framework):** "Benim adıma sadece şu IP adresleri e-posta gönderebilir" listesidir.
- **DKIM (DomainKeys Identified Mail):** E-postaya dijital bir imza ekler, içeriğin yolda değişmediğini kanıtlar.
- **DMARC:** SPF ve DKIM başarısız olursa ne yapılacağını (Karantina veya Red) belirler.

### Gerçek Dünya Analojisi
SMTP, mektubu postaneye teslim etmektir. POP3, mektubu kutudan alıp eve götürmek ve kutuyu boşaltmaktır. IMAP ise mektubun postanede kalması ve sizin gidip orada okumanız, her cihazdan aynı mektubu görebilmenizdir.

---

## English Version

An email system is an ecosystem where different protocols work together for sending and receiving.

### 1. SMTP (Simple Mail Transfer Protocol) - Sending
It is used to forward emails from one server to another or from client to server.
- **Ports:**
    - `25`: Old standard, no password. It is usually blocked by ISPs to prevent spam.
    - `587`: Modern standard (Submission). Provides encryption with STARTTLS.
    - `465`: SMTPS (Implicit TLS). It establishes an encrypted connection from the very beginning.

### 2. POP3 (Post Office Protocol v3) - Reception
It is used to download emails from the server to your computer.
- **Logic:** Downloads the email and usually deletes it from the server. Suitable for access from a single device.
- **Ports:** `110` (No Password), `995` (SSL/TLS).

### 3. IMAP (Internet Message Access Protocol) - Synchronization
It keeps emails on the server and syncs them across devices.
- **Logic:** The email remains on the server, you only see a copy. Ideal for simultaneous access from phone, tablet and computer.
- **Ports:** `143` (No Password), `993` (SSL/TLS).

### 4. Layers of Email Security (Anti-Spoofing)
Just encrypting protocols is not enough; the following records are essential to verify who the e-mail is from:
- **SPF (Sender Policy Framework):** This is the "Only the following IP addresses can send e-mail on my behalf" list.
- **DKIM (DomainKeys Identified Mail):** Adds a digital signature to the email, proving that the content has not changed in transit.
- **DMARC:** Determines what to do (Quarantine or Reject) if SPF and DKIM fail.

### Real World Analogy
SMTP is delivering the letter to the post office. POP3 is taking the letter out of the box, taking it home and emptying the box. IMAP means that the letter stays at the post office and you go and read it there, and you can see the same letter from every device.
