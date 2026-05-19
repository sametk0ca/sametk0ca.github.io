+++
title = "Authentication vs Authorization (Kimlik vs Yetki)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Siber güvenlikte en çok karıştırılan iki kavramdır. Kısaca; biri "Kimsin?", diğeri "Ne yapabilirsin?" sorusuna yanıt verir.

### 1. Authentication (Kimlik Doğrulama)
Bir kullanıcının iddia ettiği kişi olduğunu kanıtlama sürecidir.
- **Soru:** Kimsin?
- **Yöntem:** Şifreler, MFA, biyometrik veriler.
- **Sonuç:** "Evet, bu kullanıcı gerçekten User."

### 2. Authorization (Yetkilendirme)
Kimliği doğrulanmış bir kullanıcının hangi kaynaklara erişebileceğini ve hangi işlemleri yapabileceğini belirleme sürecidir.
- **Soru:** Ne yapabilirsin?
- **Yöntem:** Erişim Kontrol Listeleri (ACL), Rol Tabanlı Erişim (RBAC).
- **Sonuç:** "User içeri girebilir ama dosyaları silemez."

### 3. Aralarındaki Farklar

| Özellik | Authentication (AuthN) | Authorization (AuthZ) |
| :--- | :--- | :--- |
| **Amacı** | Kimliği doğrulamak | İzinleri kontrol etmek |
| **Sıralama** | İlk önce yapılır | Kimlik doğrulandıktan sonra yapılır |
| **Örnek** | Şifre girme | "Sadece yöneticiler bu butona basabilir" |

### 4. Bilmen Gereken Bazı Terimler
- **RBAC (Role-Based Access Control):** Kullanıcılara tek tek yetki vermek yerine, rollere (Örn: Editör, Admin) yetki verilmesi sistemidir.
- **ABAC (Attribute-Based Access Control):** Daha gelişmiş bir sistemdir. Yetkiyi verirken konuma, saate veya departmana da bakar.
- **Principle of Least Privilege (POLP):** Bir önceki konuda gördüğümüz "En az yetki" prensibi. Authorization sürecinin temel kuralıdır.

### Gerçek Dünya Analojisi
Bir otele gittiğinizi düşünün.
- **Authentication:** Resepsiyona kimliğinizi gösterip kayıt olmanızdır. Resepsiyonist sizin gerçekten kimliğinizdeki kişi olduğunuzu doğrular.
- **Authorization:** Size verilen oda kartıdır. O kartla otelin ana kapısından girebilirsiniz (AuthN başarılı), ancak sadece *kendi odanızın* kapısını açabilirsiniz (AuthZ kısıtlı). Kral dairesine girmeye çalışırsanız kartınız çalışmaz çünkü oraya "yetkiniz" yoktur.