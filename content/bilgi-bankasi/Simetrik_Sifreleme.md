+++
title = "Simetrik Şifreleme (AES, DES)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cryptography"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

**Simetrik Şifreleme**, veriyi şifrelemek ve şifresini çözmek için **aynı anahtarın** kullanıldığı bir kriptografi yöntemidir. Hızlıdır ve büyük miktardaki verileri şifrelemek için idealdir.

### 1. Çalışma Mantığı
Gönderici (Ali) veriyi bir anahtar ile şifreler ve alıcıya (Ayşe) gönderir. Alıcı, aynı anahtarı kullanarak veriyi orijinal haline getirir. En büyük zorluk, bu gizli anahtarın güvenli bir şekilde paylaşılmasıdır.

### 2. Yaygın Simetrik Algoritmalar
1. **DES (Data Encryption Standard):**
   - 1970'lerde geliştirilmiştir.
   - 56-bit gibi kısa bir anahtar kullandığı için günümüzde "brute force" saldırıları ile dakikalar içinde kırılabilir. Artık güvensiz kabul edilir.
2. **AES (Advanced Encryption Standard):**
   - Günümüzün dünya standardıdır.
   - 128, 192 veya 256-bit anahtar uzunluklarını destekler.
   - Bankacılık işlemlerinden devlet sırlarına kadar her yerde kullanılır. Mevcut teknolojiyle kırılması imkansız kabul edilir.
3. **ChaCha20:**
   - Özellikle mobil cihazlarda ve yazılımsal uygulamalarda hızlı çalışan modern ve güvenli bir alternatiftir.

### 3. Avantajlar ve Dezavantajlar
- **Avantajlar:** Çok hızlıdır ve işlemciyi az yorar. Büyük dosyaları şifrelemek için çok verimlidir.
- **Dezavantajlar:** Anahtar Yönetimi Sorunu. Eğer Ali ve Ayşe dünyanın iki farklı ucundaysa, anahtarı birbirlerine nasıl güvenle ulaştıracaklar? Eğer anahtar saldırganın eline geçerse, tüm iletişim okunabilir.

### 4. Kullanım Alanları
- Disk şifreleme (BitLocker, FileVault).
- Wi-Fi şifreleme (WPA2/WPA3).
- HTTPS bağlantılarının ana veri iletim aşaması (SSL/TLS içindeki asıl veri transferi).

### Gerçek Dünya Analojisi
Simetrik şifreleme, tek bir anahtarı olan bir "Çelik Kasa" gibidir. Ali, evrağı kasaya koyar ve kendi anahtarıyla kilitler. Ayşe'nin evrağı okuyabilmesi için Ali'nin kullandığı anahtarın **tıpatıp aynısına** sahip olması gerekir. Eğer anahtarı postayla gönderirken biri çalarsa, kasanın hiçbir anlamı kalmaz.