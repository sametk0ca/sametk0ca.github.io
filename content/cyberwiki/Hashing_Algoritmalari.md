+++
title = "Hashing Algoritmaları (MD5, SHA-1, SHA-256) | Hashing Algorithms (MD5, SHA-1, SHA-256)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
+++

**Hashing**, herhangi bir boyuttaki veriyi (bir kelime veya devasa bir dosya) alıp, onu sabit uzunlukta benzersiz bir karakter dizisine dönüştürme işlemidir. Hashing bir şifreleme değildir; geri döndürülemez (tek yönlüdür).

### 1. Hashing'in Temel Özellikleri
- **Tek Yönlülük:** Hash değerinden orijinal veriye ulaşılamaz.
- **Sabit Uzunluk:** Giriş verisi ne kadar büyük olursa olsun, çıktı her zaman aynı uzunluktadır.
- **Benzersizlik (Çakışma Direnci):** İki farklı verinin aynı hash değerini üretme ihtimali teorik olarak imkansıza yakın olmalıdır.
- **Çığ Etkisi (Avalanche Effect):** Giriş verisindeki en küçük bir değişiklik (örneğin bir nokta eklemek), hash değerini tamamen değiştirir.

### 2. Yaygın Hashing Algoritmaları
1. **MD5 (Message Digest 5):**
   - 128-bit uzunluğundadır.
   - Hızlıdır ancak artık güvenli kabul edilmez. "Collision" (iki farklı verinin aynı hash'i üretmesi) saldırılarına karşı savunmasızdır.
2. **SHA-1 (Secure Hash Algorithm 1):**
   - 160-bit uzunluğundadır.
   - Google ve diğer devler tarafından artık güvensiz kabul edilmektedir. Pratik saldırılarla çakışma üretilebilir.
3. **SHA-256 (SHA-2 Ailesi):**
   - 256-bit uzunluğundadır.
   - Günümüzde standart olarak kabul edilen, oldukça güvenli bir algoritmadır. Bitcoin ve birçok modern güvenlik protokolü SHA-256 kullanır.

### 3. Kullanım Alanları
- **Veri Bütünlüğü Kontrolü:** İnternetten indirdiğiniz bir dosyanın bozulup bozulmadığını veya değiştirilip değiştirilmediğini hash değerini karşılaştırarak anlayabilirsiniz.
- **Şifre Saklama:** Veritabanlarında şifreler asla açık metin olarak saklanmaz. Sadece şifrelerin hash değerleri saklanır.
- **Dijital İmzalar:** Bir belgenin hash değeri alınır ve göndericinin gizli anahtarı ile şifrelenir.

### 4. Çakışma (Collision) Nedir?
İki farklı verinin aynı hash sonucunu üretmesine denir. MD5 ve SHA-1'de bu durumun mümkün olduğu kanıtlandığı için siber güvenlikte artık bu algoritmalar tercih edilmez.

### Gerçek Dünya Analojisi
Hashing, bir insanın "parmak izi" gibidir. Bir insanın parmak izine bakarak o insanı yeniden inşa edemezsiniz (Tek yönlülük). Ama bir suç mahallinde bulunan parmak izi ile şüphelinin parmak izini karşılaştırarak (Bütünlük kontrolü) o kişinin o olup olmadığını %100 anlayabilirsiniz. Parmak izinde küçük bir yara izi bile oluşsa (Veride küçük bir değişiklik), artık o parmak izi eskisiyle eşleşmez.

---

## English Version

**Hashing** is the process of taking data of any size (a word or a huge file) and converting it into a fixed-length unique string of characters. Hashing is not encryption; is irreversible (one-way).

### 1. Basic Features of Hashing
- **One-Wayness:** The original data cannot be accessed from the hash value.
- **Fixed Length:** No matter how large the input data is, the output is always the same length.
- **Uniqueness (Collision Resistance):** The possibility of two different data producing the same hash value should be theoretically close to impossible.
- **Avalanche Effect:** The slightest change in the input data (for example, adding a dot) completely changes the hash value.

### 2. Common Hashing Algorithms
1. **MD5 (Message Digest 5):**
   - It is 128-bit long.
   - Fast but no longer considered safe. It is vulnerable to "collision" attacks (two different data producing the same hash).
2. **SHA-1 (Secure Hash Algorithm 1):**
   - It is 160-bit long.
   - It is now considered unsafe by Google and other giants. Conflict can be produced with practical attacks.
3. **SHA-256 (SHA-2 Family):**
   - It is 256-bit long.
   - It is a very secure algorithm that is considered standard today. Bitcoin and many modern security protocols use SHA-256.

### 3. Areas of Use
- **Data Integrity Check:** You can understand whether a file you downloaded from the internet is corrupted or modified by comparing its hash value.
- **Password Storage:** Passwords are never stored in clear text in databases. Only hash values ​​of passwords are stored.
- **Digital Signatures:** The hash value of a document is taken and encrypted with the sender's private key.

### 4. What is Collision?
It is when two different data produce the same hash result. Since it has been proven that this is possible in MD5 and SHA-1, these algorithms are no longer preferred in cyber security.

### Real World Analogy
Hashing is like a "fingerprint" of a person. You cannot reconstruct a person by looking at his fingerprint (One-sidedness). But by comparing the fingerprint found at a crime scene with the fingerprint of the suspect (Integrity check), you can understand 100% whether it is that person or not. Even if there is a small scar on the fingerprint (a small change in the data), that fingerprint will no longer match the old one.
