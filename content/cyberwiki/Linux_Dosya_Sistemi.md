+++
title = "Linux Dosya Sistemi (Ext4)  Teknik Detaylar | Linux File System (Ext4) Technical Details"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

In the Linux world "everything is a file". A hardware device, a network socket, or a process is represented as a file on the file system.

### 1. Inode (Index Node) - ID Card of the File
When you create a file on disk, all information except its name (size, owner, permissions, creation date) is stored in an **Inode**.
- **Technical Details:** A folder is actually a simple list that maps filenames to Inode numbers.
- **Security:** Inodes are limited. An attacker can create millions of empty files in the system, consuming Inodes even if disk space is not exhausted, and preventing the system from creating new files (and therefore logs) (DoS).

### 2. Mounting Security
The parameters used when mounting a disk or partition in Linux directly affect security:
- **`noexec`:** It does not allow executing any file in that disk partition. This parameter is a lifesaver in places where users can upload files, such as `/tmp` or `/home`.
- **`nosuid`:** Ignores SUID bits (privileges escalation vulnerabilities) of files on that disk.

### 3. Critical Indexes and Forensics
- **`/proc`:** It is not a physical directory, but a virtual directory that displays processes in memory (RAM) as files. You can see what files an attacker keeps open or what network connections they make with `ls /proc/[PID]/fd`.
- **`/etc`:** All configuration files of the system are here. The `/etc/shadow` file holds hashes of user passwords; It should only be readable by root.
- **`/var/log`:** The most critical directory for forensic analysis. The logs are here.

### 4. Symbolic and Hard Links (Symlinks vs Hardlinks)
- **Symlink:** It is a shortcut that points to the path of a file.
- **Hardlink:** Points directly to the Inode of the file. Even if the original file is deleted, the data will not be deleted from the disk unless the Hardlink is deleted.
- **Risk of Attack:** With "Symlink Race" attacks, a program can be made to change system files through a shortcut created by the attacker, while thinking that it is writing to a legitimate file.
