+++
title = "Cloud IAM Yönetimi | Cloud IAM Management"
date = "2026-05-19"
draft = false
categories = ["Cloud"]
type = "cyberwiki"
+++

Bulut Kimlik ve Erişim Yönetimi (IAM), bulut kaynaklarına (VM'ler, veritabanları, depolama) erişimi kontrol eden merkezi mekanizmadır.

### Özet
Bulut güvenliğinin yeni "perimetresi" kimliktir. Doğru yapılandırılmamış bir IAM politikası, tüm bulut altyapısının ele geçirilmesine neden olabilir.

### Teknik Detaylar
- **Users, Groups, Roles:** Erişim haklarının atandığı temel birimler.
- **Policies (JSON):** Erişimin detaylarını belirleyen dökümanlar.
- **Identity Federation:** Kurumsal kimlik sağlayıcıların (AD, Okta) bulut ile entegrasyonu.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **MFA Everywhere:** Tüm kullanıcılar ve özellikle admin hesapları için Multi-Factor Authentication zorunlu tutun.
- **Least Privilege Policies:** `AdministratorAccess` kullanmak yerine, sadece ilgili servis için gerekli minimum yetkiyi veren özel politikalar yazın.
- **Access Key Rotation:** Programatik erişim anahtarlarını düzenli olarak değiştirin ve mümkünse kısa süreli (temporary) anahtarlar kullanın.

---

## English Version

Cloud Identity and Access Management (IAM) is the central mechanism that controls access to cloud resources (VMs, databases, storage).

### Summary
The new “perimeter” of cloud security is identity. A poorly configured IAM policy can lead to the entire cloud infrastructure being compromised.

### Technical Details
- **Users, Groups, Roles:** Basic units to which access rights are assigned.
- **Policies (JSON):** Documents that specify the details of access.
- **Identity Federation:** Integration of corporate identity providers (AD, Okta) with the cloud.

### Security Approach and Best Practices
- **MFA Everywhere:** Require Multi-Factor Authentication for all users and especially admin accounts.
- **Least Privilege Policies:** Instead of using `AdministratorAccess`, write custom policies that grant only the minimum privileges required for the relevant service.
- **Access Key Rotation:** Change programmatic access keys regularly and use temporary keys if possible.
