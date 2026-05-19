+++
title = "Büyük Ölçekli Kimlik Stratejileri (Large Scale Identity)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

Büyük ölçekli kimlik stratejileri, binlerce kullanıcı ve servisin bulunduğu karmaşık sistemlerde kimlik yönetimini (IAM) güvenli, ölçeklenebilir ve yönetilebilir kılma sanatıdır.

### Özet
Geleneksel kullanıcı adı/şifre yöntemleri büyük ölçekte yetersiz kalır. Bunun yerine merkezi, federasyon tabanlı ve otomatize edilmiş sistemler tercih edilir.

### Teknik Detaylar
- **Identity Federation:** SAML, OIDC kullanarak farklı platformlar arasında kimlik paylaşımı.
- **Single Sign-On (SSO):** Kullanıcının tek bir girişle tüm yetkili sistemlere erişebilmesi.
- **Directory Services:** Active Directory, Azure AD (Entra ID) veya LDAP gibi merkezi dizin yapıları.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **MFA Adoption:** Büyük ölçekte donanımsal anahtarlar (YubiKey) veya biyometrik doğrulamaları standartlaştırın.
- **Lifecycle Management:** İşe giriş ve işten çıkış süreçlerinde kimliklerin otomatik açılıp kapanmasını sağlayın.
- **Risk-Based Authentication:** Kullanıcının konumu, saati ve cihazı şüpheliyse ek doğrulama isteyin.