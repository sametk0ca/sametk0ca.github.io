+++
title = "RADIUS  TACACS - Merkezi Kimlik Doğrulama (AAA) | RADIUS TACACS - Centralized Authentication (AAA)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Büyük ağlarda her cihaz (Switch, Router, VPN) için ayrı ayrı kullanıcı oluşturmak imkansızdır. Bunun yerine, tüm cihazların sorduğu merkezi bir kimlik doğrulama sunucusu kullanılır. Bu sisteme **AAA (Authentication, Authorization, Accounting)** denir.

### 1. AAA Nedir?
- **Authentication (Kimlik Doğrulama):** "Kimsin?" (Kullanıcı adı/şifre kontrolü).
- **Authorization (Yetkilendirme):** "Ne yapabilirsin?" (Hangi komutları çalıştırabilirsin?).
- **Accounting (Denetleme/Muhasebe):** "Ne yaptın?" (Hangi saatte neyi değiştirdin?).

### 2. RADIUS (Remote Authentication Dial-In User Service)
- **Karakteristik:** Genellikle ağ erişimi (VPN, Wi-Fi 802.1X) için kullanılır.
- **Protokol:** UDP kullanır.
- **Güvenlik:** Sadece şifre alanını şifreler, paketin geri kalanı açıktır.
- **Yapı:** Authentication ve Authorization işlemlerini birleşik olarak yapar.

### 3. TACACS+ (Terminal Access Controller Access-Control System Plus)
- **Karakteristik:** Cisco tarafından geliştirilmiştir, genellikle ağ cihazlarının yönetimi (CLI erişimi) için kullanılır.
- **Protokol:** TCP port 49 kullanır (Daha güvenilir bağlantı).
- **Güvenlik:** Tüm paketi şifreler. Bu yüzden RADIUS'tan daha güvenlidir.
- **Yapı:** AAA bileşenlerini tamamen birbirinden ayırır. Bu sayede bir kullanıcıya sadece belirli komutları çalıştırma yetkisi (Authorization) vermek çok daha kolaydır.

### 4. Güvenlik Notu
Her iki protokol de "Shared Secret" (Paylaşılan Sır) denilen bir anahtar kullanır. Eğer bu anahtar zayıfsa veya ele geçirilirse, tüm ağ cihazlarının güvenliği tehlikeye girer.

### Gerçek Dünya Analojisi
RADIUS, bir gece kulübünün kapısındaki fedai gibidir; içeri girip giremeyeceğinize karar verir. TACACS+ ise kulübün içindeki her özel odanın kapısında bekleyen korumalar gibidir; her adımınızda yetkinizi kontrol eder ve ne yaptığınızı not alır.

---

## English Version

In large networks, it is impossible to create separate users for each device (Switch, Router, VPN). Instead, a central authentication server is used that all devices ask. This system is called **AAA (Authentication, Authorization, Accounting)**.

### 1. What is AAA?
- **Authentication:** "Who are you?" (Username/password check).
- **Authorization:** "What can you do?" (What commands can you run?).
- **Accounting:** "What did you do?" (What did you change at what time?).

### 2. RADIUS (Remote Authentication Dial-In User Service)
- **Characteristic:** Generally used for network access (VPN, Wi-Fi 802.1X).
- **Protocol:** Uses UDP.
- **Security:** Encrypts only the password field, the rest of the packet is open.
- **Structure:** It performs Authentication and Authorization operations in combination.

### 3. TACACS+ (Terminal Access Controller Access-Control System Plus)
- **Characteristic:** Developed by Cisco, often used for management (CLI access) of network devices.
- **Protocol:** Uses TCP port 49 (More reliable connection).
- **Security:** Encrypts the entire package. So it is safer than RADIUS.
- **Structure:** It completely separates the AAA components from each other. In this way, it is much easier to grant authorization to a user to run only certain commands.

### 4. Safety Note
Both protocols use a key called the "Shared Secret". If this key is weak or compromised, the security of all network devices is compromised.

### Real World Analogy
RADIUS is like the bouncer at the door of a nightclub; It decides whether you can come in or not. TACACS+, on the other hand, is like guards waiting at the door of every private room in the club; It checks your authority at every step and takes note of what you do.
