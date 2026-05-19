+++
title = "Cloud IAM Yönetimi"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cloud"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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