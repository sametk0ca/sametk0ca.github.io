+++
title = "SSL  TLS El Sıkışma (Handshake) Mekanizması | SSL TLS Handshake Mechanism"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

SSL (Secure Sockets Layer) ve onun daha modern ve güvenli halefi olan TLS (Transport Layer Security), internet üzerindeki iletişimi şifrelemek için kullanılır. İletişim başlamadan önce istemci ve sunucu arasında yapılan bu ön görüşmeye "El Sıkışma" denir.

### 1. El Sıkışma Adımları (TLS 1.2 Örneği)
1. **Client Hello:** İstemci sunucuya "Selam, ben güvenli bağlanmak istiyorum. Desteklediğim şifreleme yöntemleri (cipher suites) şunlar" der.
2. **Server Hello:** Sunucu "Selam, senin yöntemlerinden en uygunu şu. Bu da benim dijital sertifikam (ve açık anahtarım)" diye yanıt döner.
3. **Authentication (Doğrulama):** İstemci, sunucunun sertifikasını güvenilir bir otorite (CA) üzerinden kontrol eder. "Evet, bu gerçekten o" derse devam eder.
4. **Key Exchange (Anahtar Değişimi):** İstemci, sadece o oturumda kullanılacak olan bir "oturum anahtarı" oluşturur. Bunu sunucunun açık anahtarıyla şifreleyip sunucuya gönderir.
5. **Cipher Spec / Finished:** Artık her iki taraf da aynı oturum anahtarına sahiptir. "Bundan sonra her şeyi bu anahtarla şifreleyeceğiz" derler ve güvenli iletişim başlar.

### 2. Kritik Kavramlar
- **Asimetrik Şifreleme:** El sıkışma sırasında (anahtar değişimi için) kullanılır. Çok güvenli ama yavaştır.
- **Simetrik Şifreleme:** El sıkışma bittikten sonra (asıl veriyi taşımak için) kullanılır. Çok hızlıdır.
- **TLS 1.3:** Modern versiyondur. El sıkışma adımlarını azaltarak hem hızı artırır hem de eski, güvensiz şifreleme yöntemlerini (legacy ciphers) kaldırarak güvenliği maksimize eder.

### 3. Güvenlik Riskleri
- **MitM (Man-in-the-Middle):** Eğer istemci sertifika doğrulamasını düzgün yapmazsa, saldırgan araya girip kendi sertifikasını sunabilir ve tüm trafiği okuyabilir.
- **Expired/Self-Signed Certificates:** Süresi dolmuş veya bilinmeyen bir otorite tarafından imzalanmış sertifikalar güvenli değildir. Tarayıcılar bu durumda büyük kırmızı uyarılar verir.
- **Downgrade Attacks:** Saldırganın zorla daha eski ve zayıf bir TLS versiyonu (Örn: TLS 1.0) kullandırtmaya çalışması.

### Gerçek Dünya Analojisi
İki casusun bir parkta buluştuğunu düşünün. Önce birbirlerinin kimliklerini kontrol ederler (Authentication). Sonra fısıldaşarak sadece o gün kullanacakları bir parola belirlerler (Key Exchange). Bundan sonra tüm mesajlarını bu parolayla şifreli yazarlar.

---

## English Version

SSL (Secure Sockets Layer) and its more modern and secure successor, TLS (Transport Layer Security), are used to encrypt communications on the Internet. This preliminary conversation between the client and the server before communication begins is called "Handshake".

### 1. Handshake Steps (TLS 1.2 Example)
1. **Client Hello:** The client says to the server, "Hi, I want to connect securely. The encryption methods (cipher suites) I support are these."
2. **Server Hello:** The server responds, "Hello, the most suitable of your methods is this. This is my digital certificate (and public key)."
3. **Authentication:** The client checks the server's certificate against a trusted authority (CA). If he says, "Yes, that's really him," he continues.
4. **Key Exchange:** The client creates a "session key" that will be used only in that session. It encrypts it with the server's public key and sends it to the server.
5. **Cipher Spec / Finished:** Now both parties have the same session key. They say, "From now on, we will encrypt everything with this key," and secure communication begins.

### 2. Critical Concepts
- **Asymmetric Encryption:** Used during handshake (for key exchange). It is very safe but slow.
- **Symmetric Encryption:** It is used after the handshake is completed (to transport the actual data). It's very fast.
- **TLS 1.3:** It is the modern version. It both increases speed by reducing handshake steps and maximizes security by removing old, insecure encryption methods (legacy ciphers).

### 3. Security Risks
- **MitM (Man-in-the-Middle):** If the client does not perform certificate verification properly, an attacker can intercept and present his own certificate and read all traffic.
- **Expired/Self-Signed Certificates:** Certificates that have expired or have been signed by an unknown authority are not secure. Browsers give big red warnings in this case.
- **Downgrade Attacks:** The attacker tries to force the user to use an older and weaker TLS version (e.g. TLS 1.0).

### Real World Analogy
Imagine two spies meeting in a park. First, they check each other's identities (Authentication). Then, they whisper and determine a password that they will use only that day (Key Exchange). From now on, they write all their messages encrypted with this password.
