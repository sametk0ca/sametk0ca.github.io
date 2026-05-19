+++
title = "SSO (Single Sign-On) Mekanizmaları"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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