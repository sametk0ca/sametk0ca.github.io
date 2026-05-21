+++
title = "Defense in Depth (Çok Katmanlı Savunma) | Defense in Depth (Multi-Layered Defense)"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

Defense in Depth (Derinlemesine Savunma), tek bir güvenlik önlemine güvenmek yerine, birbirini destekleyen birden fazla güvenlik katmanı oluşturma stratejisidir.

### 1. Neden Tek Bir Önlem Yetmez?
Siber güvenlikte "mükemmel" bir araç yoktur. Her duvarın bir deliği, her kilidin bir maymuncuğu olabilir. Eğer hırsız dış kapıyı geçerse, içeride başka engellerle karşılaşmalıdır.

### 2. Savunma Katmanları
- **Fiziksel Katman:** Kameralar, güvenlik görevlileri, kilitli kapılar, veri merkezi giriş kartları.
- **Ağ Katmanı:** Firewall, IPS/IDS, ağ segmentasyonu (VLAN), VPN.
- **Sistem (Host) Katmanı:** Antivirüs/EDR yazılımları, güncel işletim sistemi (Patch management), disk şifreleme.
- **Uygulama Katmanı:** Güvenli kod yazımı, web uygulama güvenlik duvarları (WAF).
- **Veri Katmanı:** Şifreleme, veri tabanı erişim logları.
- **İnsan Katmanı:** Güvenlik farkındalığı eğitimleri, güçlü şifre politikaları.

### 3. Bilmen Gereken Bazı Terimler
- **Patch Management:** Yazılımlardaki güvenlik açıklarını kapatmak için düzenli olarak güncellemelerin (yamaların) yüklenmesi süreci.
- **WAF (Web Application Firewall):** Sadece web sitelerine gelen karmaşık saldırıları (Örn: SQL Injection) durdurmak için tasarlanmış özel bir güvenlik duvarı.
- **Social Engineering (Sosyal Mühendislik):** Teknolojiyi değil, insan psikolojisini kullanarak (kandırma yoluyla) bilgi çalma eylemi. Bu stratejideki "İnsan" katmanını hedefler.

### 4. Peynir Modeli (Swiss Cheese Model)
Güvenlik katmanlarını yan yana dizilmiş delikli İsviçre peyniri dilimleri gibi düşünün. Her dilimin (güvenlik önlemi) kendi içinde delikleri (zafiyetleri) vardır. Defense in Depth stratejisinin amacı, bu dilimleri öyle bir dizmektir ki, bir dilimdeki delik diğer dilimin sağlam tarafına denk gelsin. Böylece saldırgan (ışık sızması gibi) tüm katmanları bir kerede geçemez.

### Gerçek Dünya Analojisi
Değerli bir elmasın saklandığı bir müzeyi düşünün.
1. Müzenin etrafında yüksek duvarlar ve dikenli teller var (Fiziksel).
2. Girişte kimlik kontrolü yapılıyor (Ağ).
3. Elmasın olduğu oda kameralarla izleniyor (Sistem).
4. Elmas, camı kırılınca alarm veren bir kasanın içinde (Uygulama).
5. Kasanın şifresini sadece iki farklı kişi biliyor (İnsan/MFA).
Hırsız duvarı aşsa bile kameraya yakalanır, kamerayı atlasa bile kasayı açamaz.

---

## English Version

Defense in Depth is a strategy of creating multiple layers of security that reinforce each other, rather than relying on a single security measure.

### 1. Why Is One Precaution Not Enough?
There is no "perfect" tool in cybersecurity. Every wall can have a hole, every lock can have a lock. If the thief gets past the outer door, he must encounter other obstacles inside.

### 2. Layers of Defense
- **Physical Layer:** Cameras, security guards, locked doors, data center access cards.
- **Network Layer:** Firewall, IPS/IDS, network segmentation (VLAN), VPN.
- **System (Host) Layer:** Antivirus/EDR software, current operating system (Patch management), disk encryption.
- **Application Layer:** Secure coding, web application firewalls (WAF).
- **Data Layer:** Encryption, database access logs.
- **Human Layer:** Security awareness training, strong password policies.

### 3. Some Terms You Should Know
- **Patch Management:** The process of regularly installing updates (patches) to close security vulnerabilities in software.
- **WAF (Web Application Firewall):** A special firewall designed only to stop complex attacks (E.g. SQL Injection) coming to websites.
- **Social Engineering:** The act of stealing information (through deception) using human psychology, not technology. This targets the "Human" layer in the strategy.

### 4. Cheese Model (Swiss Cheese Model)
Think of security layers like slices of Swiss cheese with holes placed side by side. Each slice (security measure) has its own holes (vulnerabilities). The aim of the Defense in Depth strategy is to arrange these slices in such a way that the hole in one slice coincides with the solid side of the other slice. This way the attacker cannot get through all the layers at once (like light leakage).

### Real World Analogy
Think of a museum where a valuable diamond is kept.
1. There are high walls and barbed wire around the museum (Physical).
2. Identity check is performed at the entrance (Network).
3. The room where the diamond is located is monitored by cameras (System).
4. The diamond is in a safe that sounds an alarm when the glass is broken (Application).
5. Only two different people know the password to the safe (Human/MFA).
Even if the thief climbs over the wall, he will be caught on camera; even if he bypasses the camera, he will not be able to open the safe.
