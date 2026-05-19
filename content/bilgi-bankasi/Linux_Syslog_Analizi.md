+++
title = "Linux Syslog Analizi"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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