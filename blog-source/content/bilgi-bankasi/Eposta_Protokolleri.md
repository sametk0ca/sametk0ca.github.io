+++
title = "SMTP  POP3  IMAP - E-posta Protokolleri ve Güvenlik"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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