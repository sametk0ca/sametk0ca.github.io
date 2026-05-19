+++
title = "RADIUS  TACACS - Merkezi Kimlik Doğrulama (AAA)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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