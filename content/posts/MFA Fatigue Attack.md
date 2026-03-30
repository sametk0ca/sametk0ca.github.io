---
title: "MFA Fatigue: What Is It and How to Prevent It? | MFA Yorgunluğu Nedir?"
date: 2026-03-31
draft: false
tags: ["MFA", "Social Engineering", "Cybersecurity", "Identity"]
categories: ["Security Awareness"]
cover:
    image: "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?q=80&w=2070&auto=format&fit=crop"
    alt: "MFA Fatigue Attack"
    relative: false
---

# [TR] MFA Fatigue (Push Bombing) Nedir?

Günümüzde Multi-Factor Authentication (MFA), hesaplarımızı korumak için en temel güvenlik katmanlarından biri haline geldi. Ancak saldırganlar, teknik önlemleri aşmak yerine "insan psikolojisini" hedef alan yeni yöntemler geliştiriyor. Bunların en popüleri ise son zamanlarda sıkça duyduğumuz **MFA Fatigue (MFA Yorgunluğu)** saldırısıdır.

## MFA Fatigue Nedir?

MFA Fatigue, saldırganın bir kullanıcının kullanıcı adını ve şifresini ele geçirdikten sonra, kurbanın telefonuna art arda onlarca (bazen yüzlerce) MFA onay bildirimi göndermesidir. 

Bu saldırının amacı teknik bir açığı sömürmek değil, kurbanı **bıktırmaktır**. Kullanıcı, sürekli gelen bildirim seslerinden kurtulmak, yanlışlıkla onay vermek veya bir sistem hatası olduğunu düşünerek saldırganın giriş talebini onayladığında saldırı başarıya ulaşır.

## Saldırı Nasıl Gerçekleşir?

1. **Kimlik Bilgisi Hırsızlığı:** Saldırgan, Phishing (Oltalama) veya karanlık web'den satın aldığı sızıntılar yoluyla hedef kullanıcının şifresini elde eder.
2. **Onay Bombardımanı:** Saldırgan, hedef hesaba giriş yapmaya çalışır ve kurbanın cihazına sürekli "Push Notification" gönderir.
3. **Psikolojik Baskı:** Bu bildirimler genellikle kullanıcının dikkatinin en düşük olduğu zamanlarda (gece geç saatlerde veya çok yoğun olduğu anlarda) yapılır.
4. **Onay ve Erişim:** Kurban, bildirimlerin durması için "Onayla" (Approve) butonuna bastığı anda saldırgan içeridedir.

---

# [EN] What is MFA Fatigue (Push Bombing)?

Today, Multi-Factor Authentication (MFA) has become one of the most fundamental layers of security for protecting our accounts. However, attackers are developing new methods that target "human psychology" rather than bypassing technical measures. The most popular of these is the **MFA Fatigue** attack, which we have been hearing a lot about lately.

## What is MFA Fatigue?

MFA Fatigue occurs when an attacker, after obtaining a user's username and password, sends dozens (sometimes hundreds) of successive MFA approval notifications to the victim's phone.

The goal of this attack is not to exploit a technical vulnerability, but to **wear out** the victim. The attack succeeds when the user approves the attacker's login request to stop the constant notification sounds, by accident, or thinking it is a system error.

## How Does the Attack Work?

1. **Credential Theft:** The attacker obtains the target user's password through Phishing or leaks purchased from the dark web.
2. **Approval Bombardment:** The attacker attempts to log into the target account and continuously sends "Push Notifications" to the victim's device.
3. **Psychological Pressure:** These notifications are usually made when the user's attention is lowest (late at night or at very busy moments).
4. **Approval and Access:** Once the victim clicks the "Approve" button to stop the notifications, the attacker is in.

## Mitigation Strategies | Nasıl Korunuruz?

1. **Number Matching (Sayı Eşleştirme):** Instead of just pressing "Approve", users must enter a 2-digit number displayed on the login screen into the MFA app. (Sadece "Onayla" yerine ekrandaki sayıyı girmek.)
2. **Contextual Alerts (Bağlamsal Uyarılar):** Showing the geographic location and application name in the MFA notification. (MFA bildiriminde konum ve uygulama bilgisinin gösterilmesi.)
3. **FIDO2 & Hardware Keys (Donanım Anahtarları):** Physical security keys like YubiKey are the most resistant to these attacks. (YubiKey gibi fiziksel anahtarlar en güvenli yöntemdir.)
4. **User Awareness (Kullanıcı Farkındalığı):** Never approve unexpected MFA prompts and change your password immediately. (Beklenmedik bildirimleri asla onaylamayın ve şifrenizi hemen değiştirin.)

---

