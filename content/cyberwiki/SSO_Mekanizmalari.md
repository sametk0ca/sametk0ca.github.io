+++
title = "SSO (Single Sign-On) Mekanizmaları | SSO (Single Sign-On) Mechanisms"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

SSO (Tekli Oturum Açma), bir kullanıcının tek bir kullanıcı adı ve şifre ile birden fazla farklı uygulamaya (Örn: E-posta, Slack, CRM) giriş yapabilmesini sağlayan bir teknolojidir.

### 1. Neden SSO Kullanılır?
- **Kullanıcı Kolaylığı:** Onlarca farklı şifre hatırlamak zorunda kalmazsınız.
- **Güvenlik Kontrolü:** İK bir çalışanı işten çıkardığında, sadece ana hesabı kapatarak tüm uygulamalara erişimini tek tıkla kesebilir.
- **Şifre Yorgunluğu:** Kullanıcıların her yere aynı şifreyi koyma riskini azaltır.

### 2. Nasıl Çalışır? (Güven İlişkisi)
SSO, bir "Identity Provider" (IdP - Kimlik Sağlayıcı) ile "Service Provider" (SP - Hizmet Sağlayıcı) arasındaki güven ilişkisine dayanır.
1. Kullanıcı uygulamaya (SP) gitmek ister.
2. Uygulama kullanıcıyı IdP'ye (Örn: Google veya Okta) yönlendirir.
3. Kullanıcı IdP'de giriş yapar.
4. IdP, uygulamaya "Bu kullanıcı güvenli, içeri alabilirsin" diyen imzalı bir dijital belge (Token) gönderir.

### 3. Kullanılan Protokoller
- **SAML (Security Assertion Markup Language):** Kurumsal uygulamalarda en yaygın olanıdır. XML formatında veri taşır.
- **OIDC (OpenID Connect):** Google/Facebook ile giriş yaparken kullanılan modern protokoldür. OAuth 2.0 üzerine inşa edilmiştir.

### 4. Bilmen Gereken Bazı Terimler
- **Identity Provider (IdP):** Kimlikleri saklayan ve doğrulayan merkez (Örn: Active Directory, Okta, Google).
- **Service Provider (SP):** Kullanmak istediğiniz son uygulama (Örn: Zoom, Slack).
- **Token:** Giriş yaptıktan sonra size verilen ve sistemlerin sizi tanımasını sağlayan dijital anahtar.
- **SPOF (Single Point of Failure):** SSO'nun en büyük riskidir. Eğer ana kimlik sağlayıcı (IdP) ele geçirilirse, saldırgan tüm uygulamalarınıza erişebilir.

### Gerçek Dünya Analojisi
SSO, bir lunapark bilekliği gibidir. Kapıda bir kez kimlik gösterip (Login) bilekliği (Token) alırsınız. Ondan sonra her oyuncağa (Uygulama) binerken tekrar kimlik göstermeniz gerekmez, sadece bilekliği göstermeniz yeterlidir.

---

## English Version

SSO (Single Sign-On) is a technology that allows a user to log in to multiple different applications (Ex: Email, Slack, CRM) with a single username and password.

### 1. Why Use SSO?
- **User Ease:** You don't have to remember dozens of different passwords.
- **Security Control:** When HR fires an employee, they can cut off their access to all applications with just one click by closing the main account.
- **Password Fatigue:** Reduces the risk of users putting the same password everywhere.

### 2. How Does It Work? (Trust Relationship)
SSO is based on a trust relationship between an "Identity Provider" (IdP) and a "Service Provider" (SP).
1. The user wants to go to the application (SP).
2. The application redirects the user to the IdP (Ex: Google or Okta).
3. The user logs in to the IdP.
4. The IdP sends a signed digital document (Token) to the application saying "This user is safe, you can let them in."

### 3. Protocols Used
- **SAML (Security Assertion Markup Language):** It is the most common in enterprise applications. It carries data in XML format.
- **OIDC (OpenID Connect):** It is the modern protocol used when logging in with Google/Facebook. It is built on OAuth 2.0.

### 4. Some Terms You Should Know
- **Identity Provider (IdP):** The center that stores and verifies identities (Ex: Active Directory, Okta, Google).
- **Service Provider (SP):** The last application you want to use (Ex: Zoom, Slack).
- **Token:** The digital key given to you after you log in and which allows the systems to recognize you.
- **SPOF (Single Point of Failure):** It is the biggest risk of SSO. If the main identity provider (IdP) is compromised, the attacker can access all your applications.

### Real World Analogy
SSO is like an amusement park wristband. You show your ID (Login) once at the door and receive the wristband (Token). After that, you do not need to show your ID again when riding each toy (App), you just need to show your wristband.
