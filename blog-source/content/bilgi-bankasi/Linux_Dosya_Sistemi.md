+++
title = "Linux Dosya Sistemi (Ext4)  Teknik Detaylar"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "bilgi-bankasi"
+++

Linux dünyasında "her şey bir dosyadır". Bir donanım cihazı, bir ağ soketi veya bir süreç (process), dosya sistemi üzerinde birer dosya olarak temsil edilir.

### 1. Inode (Index Node) - Dosyanın Kimlik Kartı
Disk üzerinde bir dosya oluşturduğunuzda, ismi dışındaki tüm bilgiler (boyut, sahip, izinler, oluşturulma tarihi) bir **Inode** içinde saklanır.
- **Teknik Detay:** Bir klasör, aslında dosya isimlerini Inode numaralarıyla eşleştiren basit bir listedir.
- **Security:** Inode'lar sınırlıdır. Bir saldırgan sistemde milyonlarca boş dosya oluşturarak disk alanı bitmese bile Inode'ları tüketebilir ve sistemin yeni dosya (ve dolayısıyla log) oluşturmasını engelleyebilir (DoS).

### 2. Bağlama (Mounting) Güvenliği
Linux'ta bir diski veya bölüntüyü sisteme bağlarken (mount) kullanılan parametreler doğrudan güvenliği etkiler:
- **`noexec`:** O disk bölüntüsü içindeki hiçbir dosyanın çalıştırılmasına (execute) izin vermez. `/tmp` veya `/home` gibi kullanıcıların dosya yükleyebildiği yerlerde bu parametre hayat kurtarır.
- **`nosuid`:** O diskteki dosyaların SUID bitlerini (yetki yükseltme açıklarını) yok sayar.

### 3. Kritik Dizinler ve Forensics
- **`/proc`:** Fiziksel bir dizin değil, bellekteki (RAM) süreçleri dosya gibi gösteren sanal bir dizindir. Bir saldırganın hangi dosyaları açık tuttuğunu veya hangi ağ bağlantılarını yaptığını `ls /proc/[PID]/fd` ile görebilirsin.
- **`/etc`:** Sistemin tüm konfigürasyon dosyaları buradadır. `/etc/shadow` dosyası, kullanıcı şifrelerinin hashlenmiş hallerini tutar; sadece root tarafından okunabilmelidir.
- **`/var/log`:** Adli inceleme için en kritik dizin. Loglar buradadır.

### 4. Sembolik ve Sert Linkler (Symlinks vs Hardlinks)
- **Symlink (Sembolik Link):** Bir dosyanın yoluna işaret eden kısayoldur.
- **Hardlink:** Doğrudan dosyanın Inode'una işaret eder. Orjinal dosya silinse bile Hardlink silinmediği sürece veri diskten silinmez.
- **Saldırı Riski:** "Symlink Race" saldırılarıyla, bir programın meşru bir dosyaya yazdığını sanırken saldırganın yarattığı bir kısayol üzerinden sistem dosyalarını değiştirmesi sağlanabilir.