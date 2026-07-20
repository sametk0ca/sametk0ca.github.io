---
title: "MFA Fatigue"
date: 2026-03-31
draft: false
tags:
  - MFA
  - Social Engineering
  - Cybersecurity
  - Identity
categories:
  - Security Awareness
---

### Türkçe

MFA Yorgunluğu (MFA Yorması veya Push Bombardımanı olarak da bilinir), kullanıcının kimlik bilgilerini zaten ele geçirmiş bir saldırganın art arda çok faktörlü kimlik doğrulama isteklerini tetiklediği bir sosyal mühendislik saldırısıdır. Amaç, bildirimleri durdurmak için kullanıcının en sonunda "Onayla" düğmesine tıklamasını sağlayana kadar onu bunaltmak veya "yormaktır".

### Nasıl Çalışır?
1. Saldırgan, şifreyi ele geçirir (oltalama veya veri sızıntısı yoluyla).
2. Saldırgan giriş yapar ve bir Push (anlık) bildirimi tetikler.
3. Saldırgan bunu genellikle geceleri olmak üzere düzinelerce veya yüzlerce kez tekrarlar.
4. Kullanıcı, rahatsız olduğundan veya kafası karıştığından en sonunda onay verir.

### Önleme:
- Sayı eşleştirmeyi (kullanıcının ekranda gösterilen kodu yazması gereken yöntem) kullanın.
- Kullanıcıları, beklenmedik istekleri asla onaylamamaları konusunda eğitin.
- Uyarlanabilir kimlik doğrulamayı (birden fazla başarısız giriş denemesini engelleme) etkinleştirin.

---

### English

MFA Fatigue (also known as MFA Bombing or Push Spam) is a social engineering attack where an attacker who has already stolen a user's credentials repeatedly triggers multi-factor authentication requests. The goal is to overwhelm or "fatigue" the user until they finally click "Approve" just to stop the notifications.

### How it works:
1. Attacker steals the password (via phishing or breach).
2. Attacker logs in, triggering a Push notification.
3. Attacker repeats this dozens or hundreds of times, often at night.
4. User, annoyed or confused, eventually approves.

### Prevention:
- Use number matching (where the user must type a code shown on the screen).
- Educate users never to approve unexpected prompts.
- Implement adaptive authentication (blocking multiple failed attempts).
