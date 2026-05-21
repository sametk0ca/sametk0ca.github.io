+++
title = "Sayısal İmzalar ve Sertifika Otoriteleri (CA) | Digital Signatures and Certificate Authorities (CA)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
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

---

## English Version

**Digital Signatures** is a mathematical method that proves who created a digital document (Authentication) and that no changes have been made to the document (Integrity). **Certificate Authorities (CA)** are the source of "trust" underlying these signatures.

### 1. How Does a Digital Signature Work?
Digital signature works in contrast to asymmetric encryption:
- **Step 1 (Hashing):** The hash value of the document is taken (Ex: SHA-256).
- **Step 2 (Encryption):** This hash value is encrypted with the sender's **Private Key**. This "encrypted hash" is the **Digital Signature**.
- **Step 3 (Verification):** The receiver decrypts the signature using the sender's **Public Key** and obtains the hash value. Then it calculates the hash of the document itself. If two hashes match:
  1. The document is unchanged en route (Integrity).
  2. This signature can only be made with that secret key (Non-Repudiation).

### 2. What is a Certificate Authority (CA)?
A CA is a trusted institution that issues digital certificates and says, "This public key really belongs to this person."
- **Root Certificates:** These are the certificates of the "top level" trusted CAs that are pre-installed in your browser and operating system.
- **Chain of Trust:** A certificate is signed by a higher CA, which in turn is signed by a higher CA... Finally, the trust extends to the Root CA.

### 3. Digital Certificates (X.509)
A digital certificate includes:
- Owner's name and information.
- Owner's Public Key.
- Validity period of the certificate.
- Digital signature of the CA.

### 4. What is Non-Repudiation?
When a digital signature is used, the sender cannot later say, "I did not send this message." Because that signature can only be created with its private key. This feature is critical in e-commerce and government documents.

### Real World Analogy
Digital signature is like a "Wet Signature" and "Seal" stamped on a document.
- **Wet Signature:** Shows who approved the document (Authentication).
- **Wax Seal:** If the seal is broken, you will know that the letter has been opened (Integrity).
- **CA (Notary):** Notary is the institution that certifies that the signature really belongs to you. If a document is signed in the presence of a notary, you cannot say "This is not my signature" (Non-Repudiation).
