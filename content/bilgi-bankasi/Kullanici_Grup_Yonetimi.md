+++
title = "Kullanıcı ve Grup Yönetimi (IAM Temelleri)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "OS"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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