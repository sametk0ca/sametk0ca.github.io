+++
title = "Sayısal İmzalar ve Sertifika Otoriteleri (CA)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cryptography"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

**Sayısal İmzalar**, bir dijital belgenin kim tarafından oluşturulduğunu (Kimlik Doğrulama) ve belge üzerinde herhangi bir değişiklik yapılmadığını (Bütünlük) ispatlayan matematiksel bir yöntemdir. **Sertifika Otoriteleri (CA)** ise bu imzaların temelindeki "güven" kaynağıdır.

### 1. Sayısal İmza Nasıl Çalışır?
Sayısal imza, asimetrik şifrelemenin tersine çalışır:
- **Adım 1 (Hashleme):** Belgenin hash değeri alınır (Örn: SHA-256).
- **Adım 2 (Şifreleme):** Bu hash değeri, göndericinin **Gizli Anahtarı (Private Key)** ile şifrelenir. İşte bu "şifrelenmiş hash", **Sayısal İmzadır**.
- **Adım 3 (Doğrulama):** Alıcı, göndericinin **Açık Anahtarını (Public Key)** kullanarak imzayı çözer ve hash değerini elde eder. Sonra belgenin hashini kendisi de hesaplar. Eğer iki hash eşleşirse:
  1. Belge yolda değişmemiştir (Bütünlük).
  2. Bu imza sadece o gizli anahtarla atılmış olabilir (İnkar Edilemezlik).

### 2. Sertifika Otoritesi (CA) Nedir?
CA, dijital sertifikaları düzenleyen ve "Bu açık anahtar gerçekten bu kişiye aittir" diyen güvenilir bir kurumdur.
- **Kök Sertifikalar (Root Certificates):** Tarayıcınızda ve işletim sisteminizde önceden yüklü olan "en üst düzey" güvenilir CA'ların sertifikalarıdır.
- **Güven Zinciri (Chain of Trust):** Bir sertifika, bir üstteki CA tarafından imzalanır, o da bir üstteki... En sonunda güven, Kök CA'ya kadar uzanır.

### 3. Dijital Sertifikalar (X.509)
Bir dijital sertifika şunları içerir:
- Sahibinin adı ve bilgileri.
- Sahibinin Açık Anahtarı.
- Sertifikanın geçerlilik süresi.
- CA'nın dijital imzası.

### 4. İnkar Edilemezlik (Non-Repudiation) Nedir?
Sayısal imza kullanıldığında, gönderici daha sonra "Bu mesajı ben atmadım" diyemez. Çünkü o imza sadece ona ait gizli anahtarla oluşturulabilir. Bu özellik, e-ticaret ve resmi belgelerde kritik öneme sahiptir.

### Gerçek Dünya Analojisi
Sayısal imza, bir belgenin üzerine vurulan "Islak İmza" ve "Mühür" gibidir.
- **Islak İmza:** Belgeyi kimin onayladığını gösterir (Kimlik Doğrulama).
- **Balmumu Mühür:** Eğer mühür kırıksa, mektubun açıldığını anlarsınız (Bütünlük).
- **CA (Noter):** Noter, imzanın gerçekten size ait olduğunu tasdik eden kurumdur. Eğer bir belge noter huzurunda imzalanmışsa, "Bu benim imzam değil" diyemezsiniz (İnkar edilemezlik).