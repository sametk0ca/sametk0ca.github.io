+++
title = "Linux Syslog Analizi | Linux Syslog Analysis"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Linux işletim sistemlerinde sistem olayları, çekirdek mesajları, servis hataları ve kullanıcı aktiviteleri "Syslog" mekanizması ile kayıt altına alınır. Bu kayıtlar, sistem yönetimi ve güvenlik analizi için hayati önem taşır.

### 1. Logların Konumu ve Temel Dosyalar
Linux sistemlerde log dosyaları genellikle `/var/log` dizini altında bulunur:
- **/var/log/syslog** veya **/var/log/messages:** Genel sistem mesajlarını ve çoğu servisin loglarını içerir.
- **/var/log/auth.log** veya **/var/log/secure:** Kimlik doğrulama, `sudo` kullanımı ve SSH giriş denemeleri buraya kaydedilir (Güvenlik için en kritik dosya).
- **/var/log/kern.log:** Çekirdek (Kernel) mesajlarını ve donanım hatalarını içerir.
- **/var/log/dmesg:** Sistem açılış (boot) süreci mesajlarını içerir.
- **/var/log/apache2/** veya **/var/log/nginx/:** Web sunucusu erişim ve hata logları.

### 2. Syslog Standartları (Severity & Facility)
Syslog mesajları iki temel kritere göre sınıflandırılır:
1. **Facility (Kaynak):** Mesajın hangi sistem biriminden geldiğini belirtir (auth, cron, kern, mail vb.).
2. **Severity (Önem Derecesi):** 0'dan 7'ye kadar değişen ciddiyet seviyesidir:
   - **0 (Emergency):** Sistem kullanılamaz durumda.
   - **3 (Error):** Hata durumu.
   - **5 (Notice):** Normal ama önemli durum.
   - **6 (Informational):** Bilgi mesajı.
   - **7 (Debug):** Hata ayıklama mesajı.

### 3. Log İzleme Araçları
Logları analiz etmek için kullanılan temel komutlar:
- `tail -f /var/log/syslog`: Logları canlı olarak izlemek için.
- `grep "Failed password" /var/log/auth.log`: Başarısız giriş denemelerini bulmak için.
- `journalctl`: Modern Linux dağıtımlarında (systemd) logları sorgulamak için kullanılan güçlü bir araç.
  - `journalctl -u ssh`: Sadece SSH servisine ait logları gösterir.
  - `journalctl --since "1 hour ago"`: Son 1 saatteki logları gösterir.

### 4. Neden Önemlidir?
Bir saldırgan sisteme sızdığında genellikle izlerini gizlemek için logları silmeye çalışır. Merkezi bir log sunucusuna (SIEM gibi) gönderilen syslog kayıtları, saldırganın yerel logları silse bile yakalanmasını sağlar. Başarısız giriş denemeleri (Brute Force) veya beklenmedik `sudo` kullanımları syslog üzerinden anında tespit edilebilir.

### Gerçek Dünya Analojisi
Linux logları, bir geminin "seyir defteri" gibidir. Gemide kimin hangi saatte nöbet tuttuğu, motorun ne zaman arıza yaptığı veya izinsiz birinin güverteye çıkıp çıkmadığı bu deftere yazılır. Kaptan (Sistem Yöneticisi) veya Güvenlik Görevlisi (SOC Analisti), bir sorun olduğunda ilk olarak bu defteri kontrol eder.

---

## English Version

In Linux operating systems, system events, kernel messages, service errors and user activities are recorded with the "Syslog" mechanism. These logs are vital for system administration and security analysis.

### 1. Location of Logs and Basic Files
On Linux systems, log files are usually located under the `/var/log` directory:
- **/var/log/syslog** or **/var/log/messages:** Contains general system messages and logs of most services.
- **/var/log/auth.log** or **/var/log/secure:** Authentication, `sudo` usage and SSH login attempts are recorded here (The most critical file for security).
- **/var/log/kern.log:** Contains kernel messages and hardware errors.
- **/var/log/dmesg:** Contains system boot process messages.
- **/var/log/apache2/** or **/var/log/nginx/:** Web server access and error logs.

### 2. Syslog Standards (Severity & Facility)
Syslog messages are classified according to two basic criteria:
1. **Facility (Source):** Indicates from which system unit the message comes (auth, cron, kern, mail, etc.).
2. **Severity:** It is the severity level ranging from 0 to 7:
   - **0 (Emergency):** The system is unusable.
   - **3 (Error):** Error condition.
   - **5 (Notice):** Normal but important situation.
   - **6 (Informational):** Informational message.
   - **7 (Debug):** Debug message.

### 3. Log Monitoring Tools
Basic commands used to analyze logs:
- `tail -f /var/log/syslog`: To watch the logs live.
- `grep "Failed password" /var/log/auth.log`: To find failed login attempts.
- `journalctl`: A powerful tool used to query logs in modern Linux distributions (systemd).
  - `journalctl -u ssh`: Shows only the logs of the SSH service.
  - `journalctl --since "1 hour ago"`: Shows the logs of the last 1 hour.

### 4. Why is it important?
When an attacker infiltrates the system, they often try to delete logs to hide their tracks. Syslog records sent to a central log server (such as SIEM) allow the attacker to be caught even if they delete local logs. Unsuccessful login attempts (Brute Force) or unexpected `sudo` usage can be detected instantly via syslog.

### Real World Analogy
Linux logs are like a ship's "logbook". This book records who was on duty on the ship at what time, when the engine broke down, or whether anyone went on deck without permission. The Captain (System Administrator) or Security Officer (SOC Analyst) checks this ledger first when there is a problem.
