+++
title = "RBAC (Role-Based Access Control)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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