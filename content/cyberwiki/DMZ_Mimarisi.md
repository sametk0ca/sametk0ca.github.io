+++
title = "DMZ (Demilitarized Zone) Mimarisi | DMZ (Demilitarized Zone) Architecture"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

DMZ (Arındırılmış Bölge), bir kurumun iç ağı (Local LAN) ile dış dünya (İnternet) arasında konumlandırılan, her iki tarafa da doğrudan bağlı olmayan tampon bölgedir.

### 1. Neden DMZ Kullanılır?
Dış dünyaya servis veren sunucuların (Web sunucusu, E-posta sunucusu, DNS) internetten gelen isteklere yanıt vermesi gerekir. Ancak bu sunucular saldırıya en açık noktalardır.
- **Mantık:** Eğer internete açık bir sunucu ele geçirilirse, saldırganın doğrudan iç ağdaki kritik verilere (Maaş listeleri, veritabanları) ulaşmasını engellemek.

### 2. Mimari Yapı (Triple-Homed Firewall)
Genellikle bir güvenlik duvarının üç bacağı olur:
1. **Dış Bacak (Untrusted):** İnternet bağlantısı.
2. **DMZ Bacağı (Semi-Trusted):** İnternete açık sunucuların bulunduğu bölge.
3. **İç Bacak (Trusted):** Sadece çalışanların ve kritik sunucuların bulunduğu güvenli iç ağ.

### 3. Güvenlik Kuralları
- **Dışardan DMZ'ye:** Sadece gerekli portlara (Örn: 80, 443) izin verilir.
- **DMZ'den İçeriye:** **Asla doğrudan izin verilmez.** DMZ'deki bir sunucu iç ağdaki bir veritabanına ulaşacaksa, sadece o veritabanı portuna çok kısıtlı bir izin tanımlanır.
- **İçerden DMZ'ye:** Yönetim amaçlı erişime izin verilir.

### 4. Honeypot Kullanımı
Bazı durumlarda DMZ içinde sahte sunucular (Honeypot) kurulur. Bu sunucuların tek amacı saldırganın dikkatini çekmek, onu oyalamak ve saldırı yöntemleri hakkında bilgi toplamaktır.

### Gerçek Dünya Analojisi
DMZ, bir bankanın bekleme salonu gibidir. Müşteriler (İnternet) içeri girebilir, memurlarla (Sunucular) konuşabilir. Ancak bekleme salonundan bankanın kasasına (İç ağ) doğrudan bir kapı yoktur. Kasaya sadece memurlar özel yetkilerle ulaşabilir.

---

## English Version

DMZ (Decontaminated Zone) is a buffer zone located between an organization's internal network (Local LAN) and the outside world (Internet), not directly connected to either side.

### 1. Why Use DMZ?
Servers that serve the outside world (Web server, E-mail server, DNS) must respond to requests from the internet. However, these servers are the most vulnerable points to attack.
- **Logic:** If a server open to the internet is compromised, to prevent the attacker from directly accessing critical data (Salary lists, databases) on the internal network.

### 2. Architectural Structure (Triple-Homed Firewall)
Typically, a firewall has three legs:
1. **Outer Leg (Untrusted):** Internet connection.
2. **DMZ Leg (Semi-Trusted):** The region where servers open to the Internet are located.
3. **Internal Leg (Trusted):** Secure internal network where only employees and critical servers are located.

### 3. Security Rules
- **External to DMZ:** Only necessary ports (Ex: 80, 443) are allowed.
- **From DMZ to Inside:** **Never direct permission.** If a server in the DMZ will reach a database on the internal network, a very limited permission is defined only for that database port.
- **Inside to DMZ:** Access for administrative purposes is allowed.

### 4. Using Honeypot
In some cases, fake servers (Honeypot) are set up within the DMZ. The sole purpose of these servers is to attract the attention of the attacker, distract him and collect information about attack methods.

### Real World Analogy
The DMZ is like a bank waiting room. Customers (Internet) can come in, talk to clerks (Servers). However, there is no direct door from the waiting room to the bank's vault (Internal network). Only officers can access the safe with special powers.
