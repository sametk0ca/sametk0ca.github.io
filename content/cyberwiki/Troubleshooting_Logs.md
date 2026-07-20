+++
title = "Troubleshooting - Event Viewer  Syslog Okuma | Troubleshooting - Reading Event Viewer Syslog"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

Logs are black boxes that show what a system has done in the past. For a cybersecurity expert (especially a SOC Analyst), reading logs is like a detective examining evidence.

### 1. Windows Event Viewer
It records every important event in Windows systems. 3 main categories are critical:
- **System:** Driver errors, system startup/shutdown information.
- **Application:** Software errors and crashes.
- **Security:** Successful/unsuccessful login attempts, authorization changes. (Event IDs are very important: 4624 - Successful Login, 4625 - Incorrect Password).

### 2. Linux Syslog and Journalctl
In Linux, logs are usually collected under `/var/log`.
- `/var/log/auth.log` or `/var/log/secure`: Authentication logs. (SSH login attempts are tracked here).
- `/var/log/syslog` or `/var/log/messages`: General system messages.
- **Journalctl:** A powerful tool used to read logs on systems using `systemd`. (Only ssh logs can be filtered with `journalctl -u ssh`).

### 3. Log Levels (Severity)
Each log has a severity level:
- **Critical/Alert:** The system is waiting for urgent intervention.
- **Error:** An operation failed.
- **Warning:** A situation that may cause problems in the future.
- **Info/Debug:** Details for general information and development purposes.

### 4. SIEM Integration
Logs can have thousands of lines. To catch an attacker, logs are collected in a central system (Splunk, ELK, Microsoft Sentinel) and analyzed with "Correlation Rules".
- **Log Erasure:** Attackers first try to clear these log files or stop the log service to erase their traces. Therefore, it is vital to instantly send the logs to another server (Remote Logging).
