+++
title = "DMZ (Demilitarized Zone) Mimarisi"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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