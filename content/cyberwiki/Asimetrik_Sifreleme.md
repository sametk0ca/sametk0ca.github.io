+++
title = "Asimetrik Şifreleme (RSA, ECC, Diffie-Hellman) | Asymmetric Cryptography (RSA, ECC, Diffie-Hellman)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
+++

**Asimetrik Şifreleme** (veya Açık Anahtarlı Kriptografi), birbiriyle matematiksel olarak bağlantılı ama farklı iki anahtarın kullanıldığı yöntemdir: **Açık Anahtar (Public Key)** ve **Gizli Anahtar (Private Key)**.

### 1. Çalışma Mantığı
- **Açık Anahtar (Public Key):** Herkesle paylaşılabilir. Veriyi şifrelemek için kullanılır.
- **Gizli Anahtar (Private Key):** Sadece sahibi tarafından bilinir. Şifrelenmiş veriyi çözmek için kullanılır.

**Senaryo:** Ali, Ayşe'ye gizli bir mesaj göndermek istiyor. Ayşe'nin "Açık Anahtarını" internetten bulur ve mesajı onunla şifreler. Bu mesajı artık dünyada sadece Ayşe, kendi "Gizli Anahtarı" ile açabilir. Ali bile şifrelediği mesajı geri açamaz!

### 2. Yaygın Asimetrik Algoritmalar
1. **RSA (Rivest-Shamir-Adleman):** En eski ve en yaygın algoritmadır. Güvenlik için anahtar uzunluğunun (örneğin 2048-bit veya 4096-bit) çok büyük olması gerekir.
2. **ECC (Elliptic Curve Cryptography):** RSA'dan çok daha kısa anahtarlarla aynı (hatta daha fazla) güvenliği sağlar. Daha hızlıdır ve mobil cihazlar için idealdir.
3. **Diffie-Hellman:** İki tarafın, birbirlerine anahtar göndermeden, güvensiz bir kanal üzerinden ortak bir gizli anahtar oluşturmasını sağlayan anahtar değişim protokolüdür.

### 3. Avantajlar ve Dezavantajlar
- **Avantajlar:** "Anahtar Paylaşımı" sorununu çözer. Gizli anahtarınızı asla kimseye göndermeniz gerekmez. Kimlik doğrulama (Dijital İmza) sağlar.
- **Dezavantajlar:** Simetrik şifrelemeye göre çok daha yavaştır. İşlemciyi daha fazla yorar. Bu yüzden genellikle sadece küçük verileri (örneğin simetrik şifreleme anahtarını) şifrelemek için kullanılır.

### 4. Kullanım Alanları
- **HTTPS (SSL/TLS):** Tarayıcınız ve sunucu arasındaki ilk bağlantıda anahtar değişimi için kullanılır.
- **SSH:** Sunuculara şifresiz, anahtar tabanlı giriş yapmak için kullanılır.
- **E-posta Şifreleme (PGP/GPG):** Mesajların sadece alıcı tarafından okunmasını sağlamak için.
- **Kripto Paralar:** Cüzdan adresiniz bir "Açık Anahtar", cüzdanınıza erişim sağlayan kelimeler ise "Gizli Anahtar" mantığıyla çalışır.

### Gerçek Dünya Analojisi
Asimetrik şifreleme, asma kilitli bir "Posta Kutusu" gibidir.
- **Açık Anahtar:** Herkesin görebileceği posta kutusunun deliğidir. İsteyen herkes içeri mektup atabilir ama atılan mektubu oradan geri çıkaramaz.
- **Gizli Anahtar:** Posta kutusunun arkasındaki kapağı açan gerçek anahtardır. Sadece kutunun sahibi olan Ayşe'de bulunur ve mektupları sadece o okuyabilir.

---

## English Version

**Asymmetric Encryption** (or Public Key Cryptography) is a method in which two mathematically related but different keys are used: **Public Key** and **Private Key**.

### 1. Working Logic
- **Public Key:** Can be shared with anyone. It is used to encrypt data.
- **Private Key:** Only known by the owner. It is used to decrypt encrypted data.

**Scenario:** Ali wants to send a secret message to Ayşe. He finds Ayşe's "Public Key" on the internet and encrypts the message with it. Now only Ayşe in the world can open this message with her "Secret Key". Even Ali cannot unlock the message he encrypted!

### 2. Common Asymmetric Algorithms
1. **RSA (Rivest-Shamir-Adleman):** It is the oldest and most common algorithm. For security, the key length must be very large (e.g. 2048-bit or 4096-bit).
2. **ECC (Elliptic Curve Cryptography):** Provides the same (or even greater) security with much shorter keys than RSA. It is faster and ideal for mobile devices.
3. **Diffie-Hellman:** It is a key exchange protocol that allows two parties to create a common secret key over an insecure channel without sending keys to each other.

### 3. Advantages and Disadvantages
- **Advantages:** Solves the "Key Sharing" problem. You never need to send your private key to anyone. Provides authentication (Digital Signature).
- **Disadvantages:** It is much slower than symmetric encryption. It makes the processor more tired. So it is generally only used to encrypt small data (e.g. symmetric encryption key).

### 4. Areas of Use
- **HTTPS (SSL/TLS):** Used for key exchange at the first connection between your browser and the server.
- **SSH:** Used for password-free, key-based login to servers.
- **Email Encryption (PGP/GPG):** To ensure that messages can only be read by the recipient.
- **Cryptocurrencies:** Your wallet address works as a "Public Key", and the words that provide access to your wallet work as a "Private Key".

### Real World Analogy
Asymmetric encryption is like a padlocked "Mailbox".
- **Public Key:** It is the hole in the mailbox that everyone can see. Anyone who wants can throw a letter in, but they cannot take the thrown letter back from there.
- **Secret Key:** It is the real key that opens the cover behind the mailbox. Only Ayşe, the owner of the box, has it and only she can read the letters.
