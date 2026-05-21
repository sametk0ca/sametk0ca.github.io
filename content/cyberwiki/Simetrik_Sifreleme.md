+++
title = "Simetrik Şifreleme (AES, DES) | Symmetric Encryption (AES, DES)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
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

---

## English Version

**Symmetric Encryption** is a cryptography method in which the **same key** is used to encrypt and decrypt data. It is fast and ideal for encrypting large amounts of data.

### 1. Working Logic
The sender (Ali) encrypts the data with a key and sends it to the receiver (Ayşe). The receiver restores the data to its original state using the same key. The biggest challenge is sharing this private key securely.

### 2. Common Symmetric Algorithms
1. **DES (Data Encryption Standard):**
   - Developed in the 1970s.
   - Since it uses a short key such as 56-bit, it can be broken within minutes with "brute force" attacks today. It is now considered unsafe.
2. **AES (Advanced Encryption Standard):**
   - It is today's world standard.
   - Supports 128, 192 or 256-bit key lengths.
   - It is used everywhere, from banking transactions to state secrets. It is considered impossible to break with current technology.
3. **ChaCha20:**
   - It is a modern and safe alternative that works fast, especially on mobile devices and software applications.

### 3. Advantages and Disadvantages
- **Advantages:** It is very fast and requires little effort on the processor. It is very efficient for encrypting large files.
- **Disadvantages:** Key Management Problem. If Ali and Ayşe are at opposite ends of the world, how will they deliver the key to each other safely? If the key falls into the hands of an attacker, all communications can be read.

### 4. Areas of Use
- Disk encryption (BitLocker, FileVault).
- Wi-Fi encryption (WPA2/WPA3).
- The main data transmission phase of HTTPS connections (the actual data transfer in SSL/TLS).

### Real World Analogy
Symmetric encryption is like a "Steel Safe" with a single key. Ali puts the document in the safe and locks it with his own key. In order for Ayşe to read the document, she must have the **exact same key** that Ali used. If someone steals the key while you're sending it in the mail, the safe is worth nothing.
