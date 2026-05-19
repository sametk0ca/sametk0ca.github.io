+++
title = "SSH (Secure Shell) - Güvenli Erişim ve Anahtar Tabanlı Kimlik Doğrulama"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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