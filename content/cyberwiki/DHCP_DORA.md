+++
title = "DHCP (Dynamic Host Configuration Protocol) - DORA Süreci | DHCP (Dynamic Host Configuration Protocol) - DORA Process"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

DHCP is the protocol that automatically assigns IP address, subnet mask, default gateway and DNS information to devices that newly join the network. In this way, the trouble of manual IP configuration is eliminated.

### 1. DORA Process (4 Steps)
When a device connects to the network, it follows these steps:
1. **Discover:** The device tells the network "Is there anyone there? I need an IP!" It broadcasts a broadcast message saying:
2. **Offer:** The DHCP server on the network responds, "I'm here, I can give you the address 192.168.1.50."
3. **Request:** The device says "OK, I accept this address, reserve it for me."
4. **Acknowledge:** The server completes the process by saying "Okay, this address is yours, you can use it for this long (Lease Time)".

### 2. DHCP Terms
- **Scope:** IP range that the server can distribute (Ex: 100 to 200).
- **Lease Time:** How long the IP is given to the device. The device sends a Renewal request before the period expires.
- **Exclusion:** This is the setting to prevent statically allocated IPs (Printers, servers) in the range to be distributed by DHCP.

### 3. DHCP and Security
- **DHCP Starvation:** An attacker consumes all IPs on the server by sending thousands of requests with spoofed MAC addresses. New devices cannot connect to the network (DoS).
- **Rogue DHCP Server:** The attacker installs his own server on the network. It provides users with their own Gateway and DNS information. Thus, it can pass all traffic through itself and steal it (MitM).
- **DHCP Snooping:** It is a security setting made at the switch level. It blocks rogue servers by only allowing DHCP packets from trusted ports.

### Real World Analogy
Imagine you've started a new job and you're looking for an empty desk in the office. You ask HR (DHCP), they show you a suitable desk (IP) and say "you can work here for 1 month". After 1 month, the table becomes vacant again or you continue to stay.
