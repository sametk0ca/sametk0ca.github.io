+++
title = "IAM (Identity  Access Management) Temelleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

IAM, doğru kişilerin veya sistemlerin, doğru kaynaklara, doğru zamanda ve doğru nedenlerle erişebilmesini sağlayan politika ve teknoloji çerçevesidir.

### Özet
IAM, modern güvenlik mimarisinin merkezindedir. "Kimsin?" (Identification), "Sen o kişi misin?" (Authentication) ve "Neye yetkin var?" (Authorization) sorularına yanıt verir.

### Teknik Detaylar
- **Identification:** Kullanıcı adı veya ID.
- **Authentication (AuthN):** Şifre, MFA, Sertifika, Biyometri.
- **Authorization (AuthZ):** Yetkiler (Read/Write), Roller (RBAC), Politikalar (ABAC).
- **Accounting/Auditing:** Kimin ne zaman ne yaptığının kaydı.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Centralized Identity:** Kimlik yönetimini tek bir noktadan (örn: AD, Okta, Cloud IAM) yapın.
- **MFA Zorunluluğu:** Sadece şifreye güvenmeyin, her zaman ikinci bir doğrulama faktörü kullanın.
- **Least Privilege:** Her zaman en az yetki prensibini uygulayın.