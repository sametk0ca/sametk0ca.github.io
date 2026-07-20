+++
title = "FTP  SFTP  FTPS Farkları | FTP SFTP FTPS Differences"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Dosya transferi için kullanılan bu üç protokol, isim olarak benzer olsa da güvenlik mimarileri tamamen farklıdır.

### 1. FTP (File Transfer Protocol) - Port 21
İnternetin en eski protokollerinden biridir.
- **Güvenlik Durumu:** **Sıfır Güvenlik.** Kullanıcı adı, şifre ve dosya içerikleri tamamen açık metin (cleartext) olarak gönderilir. Ağdaki herkes Wireshark ile bu bilgileri çalabilir.
- **Aktif/Pasif Mod:** Firewall yönetimini zorlaştıran karmaşık bir port yapısına sahiptir.

### 2. FTPS (FTP over SSL/TLS) - Port 990 veya 21
FTP'nin SSL/TLS ile şifrelenmiş halidir.
- **Çalışma Mantığı:** HTTP ve HTTPS arasındaki fark gibidir. Güvenli bir tünel kurar.
- **Zorluk:** FTP'nin veri kanalı (data channel) sorunlarını devam ettirdiği için modern ağlarda yapılandırılması zordur.

### 3. SFTP (SSH File Transfer Protocol) - Port 22
FTP ile isim benzerliği olsa da aslında SSH protokolünün bir parçasıdır.
- **Güvenlik Durumu:** **En Güvenli.** Tüm kontrol ve veri trafiği SSH tüneli içinden geçer.
- **Neden Tercih Edilir?** Tek bir port (22) üzerinden çalıştığı için firewall dostudur. Anahtar tabanlı (Public Key) kimlik doğrulamayı destekler. Modern sistemlerde standarttır.

### Özet Karşılaştırma Tablosu

| Özellik | FTP | FTPS | SFTP |
| :--- | :--- | :--- | :--- |
| **Port** | 21 | 990 / 21 | 22 |
| **Şifreleme** | Yok | Var (SSL/TLS) | Var (SSH) |
| **Güvenlik** | Çok Düşük | Orta / Yüksek | Çok Yüksek |
| **Yapılandırma** | Kolay | Zor | Çok Kolay |

### Gerçek Dünya Analojisi
FTP, postacıya şeffaf bir zarfta para göndermek gibidir; herkes görebilir. FTPS, zarfı mühürlü bir kutuya koymaktır. SFTP ise parayı zırhlı bir araç (SSH) ve özel eğitimli korumalarla göndermek gibidir.

---

## English Version

Although these three protocols used for file transfer are similar in name, their security architectures are completely different.

### 1. FTP (File Transfer Protocol) - Port 21
It is one of the oldest protocols of the Internet.
- **Security Status:** **Zero Security.** Username, password and file contents are sent completely in cleartext. Anyone on the network can steal this information with Wireshark.
- **Active/Passive Mode:** It has a complex port structure that makes firewall management difficult.

### 2. FTPS (FTP over SSL/TLS) - Port 990 or 21
It is the SSL/TLS encrypted version of FTP.
- **Working Logic:** It is like the difference between HTTP and HTTPS. Establishes a secure tunnel.
- **Difficulty:** FTP is difficult to configure in modern networks because it maintains data channel problems.

### 3. SFTP (SSH File Transfer Protocol) - Port 22
Although its name is similar to FTP, it is actually part of the SSH protocol.
- **Security Status:** **Most Secure.** All control and data traffic passes through the SSH tunnel.
- **Why is it preferred?** It is firewall friendly as it works over a single port (22). Supports key-based (Public Key) authentication. It is standard in modern systems.

### Summary

| Feature | FTP | FTPS | SFTP |
| :--- | :--- | :--- | :--- |
| **Port** | 21 | 990 / 21 | 22 |
| **Encryption** | None | Yes (SSL/TLS) | Yes (SSH) |
| **Security** | Very Low | Medium / High | Very High |
| **Configuration** | Easy | Difficult | Very Easy |

### Real World Analogy
FTP is like sending money to the postman in a clear envelope; everyone can see it. FTPS is putting the envelope in a sealed box. SFTP, on the other hand, is like sending money with an armored vehicle (SSH) and specially trained guards.
