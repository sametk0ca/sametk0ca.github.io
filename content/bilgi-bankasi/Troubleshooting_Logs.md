+++
title = "Troubleshooting - Event Viewer  Syslog Okuma"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "OS"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Loglar (kayıtlar), bir sistemin geçmişte ne yaptığını gösteren kara kutulardır. Siber güvenlik uzmanı (özellikle SOC Analisti) için log okumak, bir dedektifin delil incelemesi gibidir.

### 1. Windows Event Viewer
Windows sistemlerindeki her önemli olayı kaydeder. 3 ana kategori kritiktir:
- **System:** Sürücü hataları, sistem açılış/kapanış bilgileri.
- **Application:** Yazılım hataları ve çökmeleri.
- **Security:** Başarılı/başarısız giriş denemeleri, yetki değişiklikleri. (Event ID'ler çok önemlidir: 4624 - Başarılı Giriş, 4625 - Hatalı Şifre).

### 2. Linux Syslog ve Journalctl
Linux'ta loglar genellikle `/var/log` altında toplanır.
- `/var/log/auth.log` veya `/var/log/secure`: Kimlik doğrulama logları. (SSH giriş denemeleri buradan izlenir).
- `/var/log/syslog` veya `/var/log/messages`: Genel sistem mesajları.
- **Journalctl:** `systemd` kullanan sistemlerde logları okumak için kullanılan güçlü bir araçtır. (`journalctl -u ssh` ile sadece ssh logları süzülebilir).

### 3. Log Seviyeleri (Severity)
Her logun bir önem seviyesi vardır:
- **Critical/Alert:** Sistem acil müdahale bekliyor.
- **Error:** Bir işlem başarısız oldu.
- **Warning:** Gelecekte sorun yaratabilecek bir durum.
- **Info/Debug:** Genel bilgilendirme ve geliştirme amaçlı detaylar.

### 4. SIEM Entegrasyonu
Loglar binlerce satır olabilir. Bir saldırganı yakalamak için loglar merkezi bir sistemde (Splunk, ELK, Microsoft Sentinel) toplanır ve "Korelasyon Kuralları" ile analiz edilir.
- **Log Erasure:** Saldırganlar izlerini silmek için ilk olarak bu log dosyalarını temizlemeye veya log servisini durdurmaya çalışır. Bu yüzden logların başka bir sunucuya (Remote Logging) anlık olarak gönderilmesi hayati önem taşır.