+++
title = "Hashing Algoritmaları (MD5, SHA-1, SHA-256)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cryptography"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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