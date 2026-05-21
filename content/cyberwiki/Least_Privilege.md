+++
title = "Least Privilege (En Az Yetki) Prensibi | Least Privilege Principle"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

En Az Yetki Prensibi (PoLP), bir kullanıcıya veya sürece, yalnızca görevini yerine getirmesi için mutlak suretle gerekli olan minimum yetkilerin verilmesi gerektiğini savunan güvenlik konseptidir.

### Özet
Bu prensip, bir sistemdeki potansiyel hasarı sınırlamayı amaçlar. Bir hesap veya süreç ele geçirilse bile, saldırganın sahip olacağı yetkiler kısıtlı kalacaktır.

### Teknik Detaylar
- **Kullanıcı Yetkileri:** Standart kullanıcıların admin haklarına sahip olmaması.
- **Servis Hesapları:** Bir web sunucusunun veritabanında sadece `SELECT` yetkisine sahip olması (yazma gerekmiyorsa).
- **Zaman Sınırlı Yetki:** Just-In-Time (JIT) erişim ile yetkilerin sadece ihtiyaç anında verilip sonra geri alınması.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Varsayılan Engel (Default Deny):** Tüm yetkileri kapalı tutun ve sadece gerekli olanları tek tek açın.
- **Yetki Denetimi:** Kimin hangi yetkiye sahip olduğunu düzenli olarak raporlayın ve gereksiz yetkileri temizleyin.
- **Süreç Ayrımı:** Kritik işlemleri (örn: yedekleme, kullanıcı silme) farklı yetkilere sahip farklı hesaplarla yapın.

---

## English Version

The Principle of Least Privileges (PoLP) is the security concept that holds that a user or process should be granted only the minimum privileges that are absolutely necessary to perform its task.

### Summary
This principle aims to limit potential damage to a system. Even if an account or process is compromised, the attacker's powers will remain limited.

### Technical Details
- **User Authorizations:** Standard users do not have admin rights.
- **Service Accounts:** A web server has only `SELECT` authority on the database (if no writes are required).
- **Time-Limited Authorization:** With Just-In-Time (JIT) access, authorizations are granted only when needed and then withdrawn.

### Security Approach and Best Practices
- **Default Deny:** Keep all permissions disabled and enable only the necessary ones one by one.
- **Authority Audit:** Regularly report who has which authority and clear unnecessary authorities.
- **Process Separation:** Perform critical operations (e.g. backup, user deletion) with different accounts with different privileges.
