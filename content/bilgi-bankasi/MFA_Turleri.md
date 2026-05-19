+++
title = "MFA (Multi-Factor Authentication) Türleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Sadece kullanıcı adı ve şifre artık güvenli değil. MFA (Çok Faktörlü Kimlik Doğrulama), hesaba girmek için en az iki farklı kategoriden kanıt sunmanızı isteyen sistemdir.

### 1. Kimlik Doğrulama Faktörleri
Birinin siz olduğunu kanıtlamak için şu üç kategoriden en az ikisini kullanması gerekir:
1. **Bildiğiniz Bir Şey (Something You Know):** Şifre, PIN, gizli soru.
2. **Sahip Olduğunuz Bir Şey (Something You Have):** Telefonunuza gelen SMS kodu, Authenticator uygulaması, akıllı kart, USB güvenlik anahtarı (YubiKey).
3. **Olduğunuz Bir Şey (Something You Are):** Parmak izi, yüz tanıma, göz retinası (Biyometrik veriler).
*(Bazen "Bulunduğunuz Yer" - Konum veya "Yaptığınız Bir Şey" - Yazma hızı gibi ek faktörler de kullanılır).*

### 2. MFA Türleri ve Güvenlik Seviyeleri
- **SMS / E-posta Kodları:** En yaygın ama en az güvenli olanıdır. "SIM Swapping" (SIM kart kopyalama) saldırılarıyla çalınabilir.
- **Authenticator Uygulamaları (Google/Microsoft):** 30 saniyede bir değişen kodlar (TOTP) üretir. SMS'ten çok daha güvenlidir.
- **Push Notification:** Telefona gelen "Giriş yapmaya çalışan siz misiniz?" sorusuna "Evet" demek. Kolaydır ama "MFA Fatigue" saldırısına açıktır.
- **Fiziksel Güvenlik Anahtarları (FIDO2/U2F):** En güvenli yöntemdir. Bilgisayara takılan bir USB cihazıdır ve fiziksel olarak dokunmanız gerekir.

### 3. Bilmen Gereken Bazı Terimler
- **2FA (Two-Factor Authentication):** Sadece iki faktör kullanılmasıdır. MFA ise iki veya daha fazlasını kapsar.
- **TOTP (Time-based One-Time Password):** Zaman tabanlı tek kullanımlık şifre (Authenticator kodları gibi).
- **SIM Swapping:** Bir saldırganın, operatörü kandırarak sizin numaranızı kendi SIM kartına taşıması ve SMS kodlarınızı ele geçirmesi saldırısı.
- **MFA Fatigue (MFA Yorgunluğu):** Saldırganın arka arkaya yüzlerce onay isteği göndererek, kullanıcının en sonunda bıkıp "Evet"e basmasını sağladığı sosyal mühendislik yöntemi.

### Gerçek Dünya Analojisi
MFA, evinizin kapısını açmak için hem bir anahtara (Sahip olduğunuz şey) hem de kapıdaki şifreli kilidi bilmeye (Bildiğiniz şey) ihtiyaç duymak gibidir. Hırsız anahtarı çalsa bile şifreyi bilmediği için içeri giremez.