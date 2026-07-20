+++
title = "Authentication vs Authorization (Kimlik vs Yetki) | Authentication vs Authorization"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
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

---

## English Version

These are the two most confused concepts in cyber security. Briefly; one "Who are you?", the other "What can you do?" answers the question.

### 1. Authentication
It is the process of proving that a user is who they claim to be.
- **Question:** Who are you?
- **Method:** Passwords, MFA, biometric data.
- **Result:** "Yes, this user is indeed User."

### 2. Authorization
It is the process of determining what resources an authenticated user can access and what actions they can perform.
- **Question:** What can you do?
- **Method:** Access Control Lists (ACL), Role Based Access (RBAC).
- **Result:** "User can enter but cannot delete files."

### 3. Differences Between Them

| Feature | Authentication (AuthN) | Authorization (AuthZ) |
| :--- | :--- | :--- |
| **Purpose** | Verifying identity | Checking permissions |
| **Sorting** | It is done first | Done after authentication |
| **Example** | Entering password | "Only administrators can press this button" |

### 4. Some Terms You Should Know
- **RBAC (Role-Based Access Control):** It is a system of granting authorization to roles (e.g. Editor, Admin) instead of granting authorization to users one by one.
- **ABAC (Attribute-Based Access Control):** It is a more advanced system. When granting authority, it also looks at the location, time or department.
- **Principle of Least Privilege (POLP):** The "Least Power" principle that we saw in the previous topic. It is the basic rule of the Authorization process.

### Real World Analogy
Imagine going to a hotel.
- **Authentication:** You show your ID at the reception and register. The receptionist verifies that you are indeed the person you identify as.
- **Authorization:** This is the room card given to you. With that card, you can enter the main door of the hotel (AuthN successful), but you can only open the door of *your own room* (AuthZ limited). If you try to enter the king suite, your card will not work because you are not "authorized" there.
