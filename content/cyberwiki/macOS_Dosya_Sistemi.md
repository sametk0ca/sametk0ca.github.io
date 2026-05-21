+++
title = "macOS Dosya Sistemi (APFS) | macOS File System (APFS)"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
+++

APFS (Apple File System), Apple cihazlar için optimize edilmiş, güvenlik ve hız odaklı modern bir dosya sistemidir.

### 1. Space Sharing ve Containers
APFS'de fiziksel bir disk bölüntüsü yerine "Container" yapısı kullanılır. Bir container içindeki birden fazla volume (birim) aynı boş alanı paylaşır. 
- **Security:** Bu yapı, disk alanını dinamik yönetirken, birimler arası izolasyonu korur.

### 2. Encryption (Şifreleme)
Apple, APFS ile şifrelemeyi doğrudan dosya sistemi seviyesine entegre etmiştir.
- **FileVault:** macOS'in tam disk şifreleme özelliğidir.
- **Multi-key Encryption:** Her dosya için ayrı anahtarlar ve tüm birim için ayrı bir "metadata" anahtarı kullanılabilir. Bu, anahtarlardan biri ele geçse bile tüm verinin korunmasını sağlar.

### 3. Snapshots ve Read-Only System Volume
Modern macOS sürümlerinde işletim sistemi dosyaları "Read-Only" (Sadece Okunur) bir birimde tutulur.
- **Integrity:** Saldırganların sistem dosyalarını (kernel, driver vb.) değiştirmesi donanımsal seviyede engellenir. Güncellemeler bir snapshot üzerinden yapılır ve başarılı olursa sistem o snapshot'a geçer.

### 4. Extended Attributes (EA) ve Quarantine
macOS, dosyalar hakkında ek bilgileri EA olarak tutar.
- **com.apple.quarantine:** İnternetten indirilen dosyalara bu nitelik atanır. "Gatekeeper" özelliği bu etiketi kontrol ederek imzalanmamış yazılımların çalışmasını engeller. Adli incelemede bir dosyanın nereden ve ne zaman indirildiğini bulmak için kritiktir.

---

## English Version

APFS (Apple File System) is a modern file system focused on security and speed, optimized for Apple devices.

### 1. Space Sharing and Containers
In APFS, a "Container" structure is used instead of a physical disk partition. Multiple volumes within a container share the same free space. 
- **Security:** This structure maintains isolation between volumes while dynamically managing disk space.

### 2. Encryption
With APFS, Apple has integrated encryption directly at the file system level.
- **FileVault:** is the full disk encryption feature of macOS.
- **Multi-key Encryption:** Separate keys can be used for each file and a separate "metadata" key for the entire volume. This ensures that all data is protected even if one of the keys is compromised.

### 3. Snapshots and Read-Only System Volume
In modern versions of macOS, operating system files are kept on a "Read-Only" volume.
- **Integrity:** Attackers are prevented from changing system files (kernel, drivers, etc.) at the hardware level. Updates are made via a snapshot and if successful, the system moves to that snapshot.

### 4. Extended Attributes (EA) and Quarantine
macOS keeps additional information about files as EA.
- **com.apple.quarantine:** This attribute is assigned to files downloaded from the Internet. The "Gatekeeper" feature checks this tag and prevents unsigned software from running. It is critical in forensic investigation to find out where and when a file was downloaded.
