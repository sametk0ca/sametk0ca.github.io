+++
title = "SSH (Secure Shell) - Güvenli Erişim ve Anahtar Tabanlı Kimlik Doğrulama | SSH (Secure Shell) - Secure Access and Key-Based Authentication"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

SSH, güvensiz bir ağ üzerinden uzak bir sisteme güvenli (şifreli) bir şekilde erişmek için kullanılan bir protokoldür. Telnet gibi eski ve güvensiz (cleartext) yöntemlerin yerini almıştır.

### 1. Çalışma Mantığı ve Port 22
SSH, istemci ve sunucu arasındaki tüm trafiği şifreler. Varsayılan olarak TCP 22 portunu kullanır. Bağlantı kurulurken sunucu kendi "host key" bilgisini sunar; bu, istemcinin doğru sunucuya bağlandığından emin olmasını sağlar.

### 2. Şifre vs. Anahtar Tabanlı Erişim
- **Şifre ile Giriş:** Kullanıcı adı ve şifre gerektirir. Brute-force (kaba kuvvet) saldırılarına karşı çok hassastır.
- **Anahtar Tabanlı Giriş (RSA/ED25519):** Çok daha güvenlidir. Bir "Açık Anahtar" (Public Key) sunucuya (`~/.ssh/authorized_keys`) eklenir. İstemci ise "Gizli Anahtar" (Private Key) ile giriş yapar. Gizli anahtar çalınmadığı sürece sisteme girilmesi imkansıza yakındır.

### 3. SSH Güvenlik Sıkılaştırma (Hardening)
- **Root Girişini Kapatmak:** `PermitRootLogin no` ayarıyla doğrudan root erişimini engellemek, saldırganların hedefini küçültür.
- **Port Değiştirmek:** 22 yerine rastgele bir port (Örn: 2202) kullanmak otomatik bot taramalarından korunmayı sağlar.
- **Fail2Ban Kullanımı:** Belirli bir sayıda hatalı deneme yapan IP adreslerini geçici olarak yasaklar.
- **2FA/MFA:** SSH erişimine Google Authenticator gibi ikinci bir katman eklemek güvenliği zirveye taşır.

### 4. SSH Tünelleme (SSH Tunneling)
SSH sadece terminal erişimi için değil, güvensiz bir trafiği (Örn: HTTP veya veritabanı trafiği) SSH üzerinden şifreli bir tünelle taşımak için de kullanılabilir (Local/Remote Port Forwarding).

### Gerçek Dünya Analojisi
Şifre ile girmek, kapı numarasını bilen herkesin deneme yapabileceği basit bir anahtarla girmek gibidir. Anahtar tabanlı erişim ise, sadece sizde olan ve kopyalanması imkansız olan biyometrik bir kartla girmek gibidir.

---

## English Version

SSH is a protocol used to securely (encryptedly) access a remote system over an unsecured network. It has replaced old and insecure (cleartext) methods such as Telnet.

### 1. Working Logic and Port 22
SSH encrypts all traffic between client and server. By default it uses TCP port 22. When establishing a connection, the server provides its own "host key" information; This ensures that the client is connecting to the correct server.

### 2. Password etc. Key Based Access
- **Login with Password:** Requires username and password. It is very sensitive to brute-force attacks.
- **Key Based Login (RSA/ED25519):** Much more secure. A "Public Key" is added to the server (`~/.ssh/authorized_keys`). The client logs in with the "Private Key". It is almost impossible to enter the system unless the private key is stolen.

### 3. SSH Security Hardening
- **Closing Root Login:** Preventing direct root access with the `PermitRootLogin no` setting reduces the target of attackers.
- **Changing Port:** Using a random port (Ex: 2202) instead of 22 provides protection from automatic bot scans.
- **Fail2Ban Usage:** Temporarily bans IP addresses that make a certain number of failed attempts.
- **2FA/MFA:** Adding a second layer to SSH access, such as Google Authenticator, takes security to the top.

### 4. SSH Tunneling
SSH can be used not only for terminal access, but also to transport insecure traffic (e.g. HTTP or database traffic) via an encrypted tunnel over SSH (Local/Remote Port Forwarding).

### Real World Analogy
Entering with a password is like entering with a simple key that anyone who knows the door number can try. Key-based access, on the other hand, is like entering with a biometric card that only you have and is impossible to clone.
