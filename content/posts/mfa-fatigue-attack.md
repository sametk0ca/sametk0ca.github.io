---
title: "MFA Fatigue"
date: 2026-03-31
description: "How MFA fatigue (push bombing) tricks users into approving a login, and how number matching and phishing-resistant MFA stop it. / MFA yorgunluğu (push bombardımanı) saldırısının kullanıcıyı onaya nasıl zorladığı ve sayı eşleştirme ile oltalamaya dirençli MFA'nın nasıl engellediği."
draft: false
tags: ["MFA", "Social Engineering", "Cybersecurity", "Identity"]
categories: ["Security Awareness"]
related:
  - "[[MFA_Turleri|MFA (Multi-Factor Authentication) Türleri]]"
---

## 🇹🇷 Türkçe (TR)

MFA Yorgunluğu (MFA Yorması veya Push Bombardımanı olarak da bilinir), kullanıcının kimlik bilgilerini zaten ele geçirmiş bir saldırganın art arda çok faktörlü kimlik doğrulama isteklerini tetiklediği bir sosyal mühendislik saldırısıdır. Amaç, bildirimleri durdurmak için kullanıcının en sonunda "Onayla" düğmesine tıklamasını sağlayana kadar onu bunaltmak veya "yormaktır".

### Nasıl Çalışır?

1. Saldırgan, şifreyi ele geçirir (oltalama veya veri sızıntısı yoluyla).
2. Saldırgan giriş yapar ve bir Push (anlık) bildirimi tetikler.
3. Saldırgan bunu genellikle geceleri olmak üzere düzinelerce veya yüzlerce kez tekrarlar.
4. Kullanıcı, rahatsız olduğundan veya kafası karıştığından en sonunda onay verir.

Saldırganlar çoğu zaman kurbanı ayrıca arayıp BT departmanından olduğunu söyleyerek "onayla" demesini de ister. Bu yöntem 2022'deki Uber ve Cisco ihlallerinde kullanıldı.

### Önleme

- **Sayı eşleştirmeyi (number matching)** kullanın: kullanıcı, giriş ekranında görünen sayıyı uygulamaya yazmak zorunda kalır. Bu, körü körüne "Onayla" demesini engeller.
- Kısa sürede gelen çok sayıda push isteğini **hız sınırlamasıyla** kısıtlayın ve bu durumda hesabı geçici olarak kilitleyip uyarı üretin.
- Push bildirimlerine konum ve uygulama bilgisi gibi bağlam ekleyin.
- Mümkünse oltalamaya dirençli yöntemlere (FIDO2 güvenlik anahtarları, passkey) geçin.
- Kullanıcıları, beklenmedik istekleri asla onaylamamaları ve bunları hemen bildirmeleri konusunda eğitin.

---

## 🇬🇧 English (EN)

MFA Fatigue (also known as MFA Bombing or Push Spam) is a social engineering attack where an attacker who has already stolen a user's credentials repeatedly triggers multi-factor authentication requests. The goal is to overwhelm or "fatigue" the user until they finally click "Approve" just to stop the notifications.

### How it works:

1. Attacker steals the password (via phishing or breach).
2. Attacker logs in, triggering a Push notification.
3. Attacker repeats this dozens or hundreds of times, often at night.
4. User, annoyed or confused, eventually approves.

Attackers often also contact the victim, posing as IT support and asking them to "approve" the prompt. The technique was used in the 2022 Uber and Cisco breaches.

### Prevention

- Use **number matching**: the user must type the number shown on the login screen into the app, which prevents blindly tapping "Approve".
- **Rate limit** bursts of push requests, and temporarily lock the account and raise an alert when that happens.
- Add context, such as location and application, to push notifications.
- Where possible, move to phishing-resistant methods (FIDO2 security keys, passkeys).
- Educate users never to approve unexpected prompts and to report them immediately.
