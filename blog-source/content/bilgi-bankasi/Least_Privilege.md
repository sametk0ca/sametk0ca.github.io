+++
title = "Least Privilege (En Az Yetki) Prensibi"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "bilgi-bankasi"
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