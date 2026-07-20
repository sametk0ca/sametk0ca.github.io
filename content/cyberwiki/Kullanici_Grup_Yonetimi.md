+++
title = "Kullanıcı ve Grup Yönetimi (IAM Temelleri) | User and Group Management (IAM Basics)"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
+++

IAM (Identity and Access Management), "doğru kişinin, doğru kaynaklara, doğru sebeple erişmesini" sağlayan disiplindir.

### 1. Kimlik Doğrulama (Authentication)
Kullanıcının kim olduğunu kanıtlamasıdır.
- **Factor 1:** Bildiğiniz bir şey (Şifre).
- **Factor 2:** Sahip olduğunuz bir şey (Telefon, Token).
- **Factor 3:** Olduğunuz bir şey (Biyometrik).

### 2. Yetkilendirme (Authorization)
Kimliği doğrulanmış kullanıcının ne yapabileceğine karar verilmesidir.
- **RBAC (Role-Based Access Control):** Kişiye değil, role yetki verilir (Örn: "Muhasebe" grubu her şeyi okur).
- **ABAC (Attribute-Based Access Control):** Daha dinamiktir; konuma, saate veya cihaza göre yetki verir.

### 3. Linux'ta Kullanıcı Yönetimi
- `/etc/passwd`: Tüm kullanıcıların listesi.
- `/etc/shadow`: Şifrelerin hashlenmiş hallerinin tutulduğu yer. Sadece root okuyabilir.
- **Group Management:** Kullanıcıları gruplara ekleyerek (sudo, docker vb.) yetki yönetimi yapılır.

### 4. Windows ve Active Directory (AD)
Kurumsal ağlarda kullanıcı yönetimi merkezi bir yapıda (Domain Controller) yapılır.
- **Group Policy Objects (GPO):** Binlerce bilgisayara tek merkezden güvenlik politikası (Örn: "USB takmak yasak") uygulanmasını sağlar.
- **Privileged Identity Management (PIM):** Admin yetkilerinin sadece ihtiyaç duyulduğunda (Just-In-Time) ve belirli bir süreliğine verilmesi prensibidir.
- **Least Privilege:** Bir kullanıcıya sadece işini yapmasına yetecek kadar minimum yetki verilmesi kuralıdır.

---

## English Version

IAM (Identity and Access Management) is the discipline that ensures "the right person has access to the right resources for the right reason".

### 1. Authentication
It proves who the user is.
- **Factor 1:** Something you know (Password).
- **Factor 2:** Something you own (Phone, Token).
- **Factor 3:** Something you are (Biometrics).

### 2. Authorization
It is the decision of what the authenticated user can do.
- **RBAC (Role-Based Access Control):** Authorization is given to the role, not the person (Ex: "Accounting" group reads everything).
- **ABAC (Attribute-Based Access Control):** It is more dynamic; Authorizes based on location, time or device.

### 3. User Management in Linux
- `/etc/passwd`: List of all users.
- `/etc/shadow`: Where hashed passwords are kept. Only root can read it.
- **Group Management:** Authorization management is done by adding users to groups (sudo, docker, etc.).

### 4. Windows and Active Directory (AD)
In corporate networks, user management is done in a central structure (Domain Controller).
- **Group Policy Objects (GPO):** Enables security policy to be applied to thousands of computers from a single center (e.g. "USB insertion is prohibited").
- **Privileged Identity Management (PIM):** It is the principle that admin privileges are given only when needed (Just-In-Time) and for a certain period of time.
- **Least Privilege:** It is the rule that a user is given minimum privileges, just enough to do his/her job.
