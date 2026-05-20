+++
title = "Asimetrik Şifreleme (RSA, ECC, Diffie-Hellman)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "bilgi-bankasi"
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