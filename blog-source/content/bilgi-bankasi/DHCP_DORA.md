+++
title = "DHCP (Dynamic Host Configuration Protocol) - DORA Süreci"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

DHCP, ağa yeni katılan cihazlara otomatik olarak IP adresi, alt ağ maskesi, varsayılan ağ geçidi ve DNS bilgilerini atayan protokoldür. Bu sayede manuel IP yapılandırma zahmetinden kurtulunur.

### 1. DORA Süreci (4 Adım)
Bir cihaz ağa bağlandığında şu adımları izler:
1. **Discover (Keşif):** Cihaz ağa "Kimse yok mu? Bana bir IP lazım!" diye bir broadcast mesajı yayınlar.
2. **Offer (Teklif):** Ağdaki DHCP sunucusu "Ben buradayım, sana 192.168.1.50 adresini verebilirim" diye yanıt döner.
3. **Request (İstek):** Cihaz "Tamam, bu adresi kabul ediyorum, bana rezerve et" der.
4. **Acknowledge (Onay):** Sunucu "Tamam, bu adres senindir, şu kadar süre (Lease Time) kullanabilirsin" diyerek işlemi bitirir.

### 2. DHCP Terimleri
- **Scope (Kapsam):** Sunucunun dağıtabileceği IP aralığı (Örn: 100 ile 200 arası).
- **Lease Time (Kiralama Süresi):** IP'nin cihaza ne kadar süreyle verildiği. Süre bitmeden cihaz yenileme (Renewal) talebi gönderir.
- **Exclusion (Hariç Tutma):** Dağıtılacak aralıkta statik olarak ayrılmış (Yazıcılar, sunucular) IP'lerin DHCP tarafından verilmemesi için yapılan ayardır.

### 3. DHCP ve Güvenlik
- **DHCP Starvation (DHCP Aç bırakma):** Bir saldırgan sahte MAC adresleriyle binlerce istek göndererek sunucudaki tüm IP'leri tüketir. Yeni cihazlar ağa bağlanamaz (DoS).
- **Rogue DHCP Server (Sahte DHCP Sunucusu):** Saldırgan ağa kendi sunucusunu kurar. Kullanıcılara kendi belirlediği Gateway ve DNS bilgilerini verir. Böylece tüm trafiği kendi üzerinden geçirip çalabilir (MitM).
- **DHCP Snooping:** Switch seviyesinde yapılan bir güvenlik ayarıdır. Sadece güvenilen (trusted) portlardan gelen DHCP paketlerine izin vererek sahte sunucuları engeller.

### Gerçek Dünya Analojisi
Yeni bir işe başladığınızı ve ofiste boş bir masa aradığınızı düşünün. İK'ya (DHCP) sorarsınız, onlar size uygun bir masa (IP) gösterir ve "burada 1 ay çalışabilirsin" derler. 1 ay sonra masa tekrar boşa çıkar veya siz kalmaya devam edersiniz.