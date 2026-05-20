+++
title = "FTP  SFTP  FTPS Farkları"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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