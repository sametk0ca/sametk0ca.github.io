+++
title = "RBAC (Role-Based Access Control)"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

RBAC, erişim haklarının bireysel kullanıcılara değil, organizasyon içindeki rollere atandığı bir erişim kontrol mekanizmasıdır.

### Özet
Kullanıcılar rollerine (örn: "Geliştirici", "IK", "Admin") göre yetkilendirilir. Bu yaklaşım, büyük ölçekli organizasyonlarda yetki yönetimini basitleştirir ve hata payını azaltır.

### Teknik Detaylar
- **Roller:** İş fonksiyonlarına göre tanımlanmış yetki kümeleri.
- **İzinler:** Belirli bir kaynağa (dosya, veritabanı, uygulama) erişim hakkı.
- **Hiyerarşi:** Üst rollerin alt rollerin yetkilerini miras alabilmesi.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Görevler Ayrılığı (SoD):** Bir kişinin aynı anda hem talep eden hem de onaylayan rolünde olmasını engelleyin.
- **Dinamik Atama:** Kullanıcı iş değiştirdiğinde veya ayrıldığında rolünü merkezi olarak güncelleyerek yetkilerini anında kesin.
- **Minimum Rol Sayısı:** Karmaşıklığı önlemek için sadece ihtiyaç duyulan net roller tanımlayın.

---

## English Version

RBAC is an access control mechanism where access rights are assigned to roles within the organization, rather than to individual users.

### Summary
Users are authorized based on their roles (e.g. "Developer", "IK", "Admin"). This approach simplifies authority management and reduces the margin of error in large-scale organizations.

### Technical Details
- **Roles:** Sets of authority defined by job functions.
- **Permissions:** The right to access a specific resource (file, database, application).
- **Hierarchy:** The ability of higher roles to inherit the powers of lower roles.

### Security Approach and Best Practices
- **Separation of Duties (SoD):** Prevent one person from being in the role of requester and approver at the same time.
- **Dynamic Assignment:** Instantly deprive users by centrally updating their role when they change jobs or leave.
- **Minimum Number of Roles:** Define only the clear roles needed to avoid confusion.
