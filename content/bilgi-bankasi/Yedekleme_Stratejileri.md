+++
title = "Backup (Yedekleme) Stratejileri ve 3-2-1 Kuralı"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "bilgi-bankasi"
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