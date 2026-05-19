+++
title = "macOS Dosya Sistemi (APFS)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "OS"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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