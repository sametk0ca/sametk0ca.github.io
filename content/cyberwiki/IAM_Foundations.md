+++
title = "IAM (Identity  Access Management) Temelleri | IAM (Identity Access Management) Fundamentals"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
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

---

## English Version

IAM is the policy and technology framework that ensures that the right people or systems have access to the right resources, at the right time and for the right reasons.

### Summary
IAM is at the heart of modern security architecture. "Who are you?" (Identification), "Are you that person?" (Authentication) and “What are you authorized to do?” Answers (Authorization) questions.

### Technical Details
- **Identification:** Username or ID.
- **Authentication (AuthN):** Password, MFA, Certificate, Biometrics.
- **Authorization (AuthZ):** Authorizations (Read/Write), Roles (RBAC), Policies (ABAC).
- **Accounting/Auditing:** A record of who did what and when.

### Security Approach and Best Practices
- **Centralized Identity:** Perform identity management from a single point (e.g. AD, Okta, Cloud IAM).
- **MFA Mandatory:** Don't just rely on the password, always use a second authentication factor.
- **Least Privilege:** Always apply the principle of least privilege.
