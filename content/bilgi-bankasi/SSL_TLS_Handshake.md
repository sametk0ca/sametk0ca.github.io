+++
title = "SSL  TLS El Sıkışma (Handshake) Mekanizması"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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