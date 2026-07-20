+++
title = "Backup (Yedekleme) Stratejileri ve 3-2-1 Kuralı | Backup Strategies and the 3-2-1 Rule"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

Yedekleme, verilerinizin bir kopyasını alarak sistem çökmesi, siber saldırı (Ransomware) veya fiziksel felaket durumunda verilerinizi geri getirebilme işlemidir. Siber güvenliğin son savunma hattıdır.

### 1. Altın Kural: 3-2-1 Kuralı
Dünya standartlarında kabul edilen en güvenli yedekleme yöntemidir:
- **3 Adet Kopya:** Verinizin 1 aslı ve en az 2 adet yedeği olmalı.
- **2 Farklı Ortam:** Yedekler farklı fiziksel cihazlarda tutulmalı (Örn: Bir kopya harici diskte, bir kopya NAS cihazında).
- **1 Uzak Lokasyon:** Yedeklerden en az biri şirket/ev dışındaki farklı bir coğrafi konumda (Örn: Bulut depolama veya başka bir ofis) saklanmalı. Yangın veya su baskını durumunda her şeyin yok olmasını engeller.

### 2. Yedekleme Türleri
- **Full Backup (Tam Yedek):** Her şeyi her seferinde yedekler. Çok yer kaplar ve uzun sürer.
- **Incremental Backup (Artımlı Yedek):** Sadece en son yedekten bu yana "değişen" kısımları yedekler. Hızlıdır ve az yer kaplar.
- **Differential Backup (Fark Yedeği):** En son "tam yedek"ten bu yana değişen her şeyi yedekler.

### 3. Bilmen Gereken Bazı Terimler
- **Ransomware (Fidye Yazılımı):** Dosyalarınızı şifreleyip açmak için sizden para isteyen virüs türü. Yedekleriniz varsa fidye ödemezsiniz.
- **Off-site Backup:** Verinin fiziksel olarak binanın dışında bir yerde tutulması.
- **Air-gapped Backup:** Yedeğin internete veya ağa hiç bağlı olmayan bir cihazda (Örn: Çekmecedeki bir disk) durması. Saldırganların yedeğe ulaşmasını imkansız hale getirir.
- **Cold vs Hot Storage:** Çok nadir bakılan yedekler "Cold" (yavaş ve ucuz), her an lazım olabilecekler "Hot" (hızlı ve pahalı) depolama alanlarında tutulur.

### Gerçek Dünya Analojisi
Çok önemli bir aile fotoğrafınız olduğunu düşünün.
- Bir kopyası bilgisayarınızda (Asıl).
- Bir kopyası evdeki USB bellekte (Farklı ortam).
- Bir kopyası da Google Drive'da (Uzak lokasyon).
Bilgisayar bozulursa USB'den alırsınız. Ev yanarsa Google Drive'dan alırsınız. Bu 3-2-1 kuralıdır.

---

## English Version

Backup is the process of making a copy of your data so that you can restore your data in case of system crash, cyber attack (Ransomware) or physical disaster. It is the last line of defense of cyber security.

### 1. Golden Rule: 3-2-1 Rule
It is the safest backup method accepted at world standards:
- **3 Copies:** Your data must have 1 original and at least 2 backups.
- **2 Different Media:** Backups should be kept on different physical devices (Ex: One copy on an external disk, one copy on a NAS device).
- **1 Remote Location:** At least one of the backups must be stored in a different geographical location outside the company/home (Ex: Cloud storage or another office). It prevents everything from being destroyed in case of fire or flood.

### 2. Backup Types
- **Full Backup:** Backs up everything every time. It takes up a lot of space and takes a long time.
- **Incremental Backup:** Backs up only the parts that have "changed" since the last backup. It is fast and takes up little space.
- **Differential Backup:** Backs up everything that has changed since the last "full backup".

### 3. Some Terms You Should Know
- **Ransomware:** A type of virus that asks you for money to encrypt and unlock your files. If you have backups, you won't pay ransom.
- **Off-site Backup:** Keeping the data physically outside the building.
- **Air-gapped Backup:** The backup is kept on a device that is not connected to the internet or network at all (Ex: A disk in the drawer). It makes it impossible for attackers to reach the backup.
- **Cold vs Hot Storage:** Backups that are rarely viewed are kept in "Cold" (slow and cheap) storage areas, while those that may be needed at any time are kept in "Hot" (fast and expensive) storage areas.

### Real World Analogy
Imagine you have a very important family photo.
- A copy on your computer (Original).
- A copy is on a USB stick at home (different media).
- A copy is also on Google Drive (Remote location).
If the computer breaks down, you can get it from USB. If the house burns down, you'll get it from Google Drive. This is the 3-2-1 rule.
