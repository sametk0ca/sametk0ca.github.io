+++
title = "MFA (Multi-Factor Authentication) Türleri | MFA (Multi-Factor Authentication) Types"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
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

---

## English Version

Only username and password are no longer secure. MFA (Multi-Factor Authentication) is the system that requires you to provide evidence from at least two different categories to enter the account.

### 1. Authentication Factors
To prove it's you, someone must use at least two of these three categories:
1. **Something You Know:** Password, PIN, secret question.
2. **Something You Have:** SMS code sent to your phone, Authenticator application, smart card, USB security key (YubiKey).
3. **Something You Are:** Fingerprint, facial recognition, eye retina (Biometric data).
*(Sometimes additional factors such as "Where You Are" - Location or "Something You Do" - Typing speed are also used).*

### 2. MFA Types and Security Levels
- **SMS / Email Codes:** The most common but least secure. It can be stolen through "SIM Swapping" (SIM card copying) attacks.
- **Authenticator Applications (Google/Microsoft):** Generates codes (TOTP) that change every 30 seconds. It is much more secure than SMS.
- **Push Notification:** "Are you the one trying to log in?" Saying "Yes" to the question. It's easy, but it's vulnerable to the "MFA Fatigue" attack.
- **Physical Security Keys (FIDO2/U2F):** It is the most secure method. It is a USB device that plugs into the computer and you have to physically touch it.

### 3. Some Terms You Should Know
- **2FA (Two-Factor Authentication):** It is the use of only two factors. MFA covers two or more.
- **TOTP (Time-based One-Time Password):** Time-based one-time password (like Authenticator codes).
- **SIM Swapping:** An attack in which an attacker deceives the operator into transferring your number to his/her own SIM card and capturing your SMS codes.
- **MFA Fatigue:** A social engineering method in which the attacker sends hundreds of confirmation requests in a row, causing the user to eventually get fed up and click "Yes".

### Real World Analogy
MFA is like needing both a key (What you have) and knowing the combination lock on the door (What you know) to open the door to your house. Even if the thief steals the key, he cannot get in because he does not know the password.
