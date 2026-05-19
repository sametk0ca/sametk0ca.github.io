+++
title = "Sorun Giderme Araçları - Bölüm 3: ipconfig, netstat, arp"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Bu araçlar, kendi bilgisayarınızın ağ ayarlarını ve o andaki ağ bağlantılarını görmenizi sağlar.

### 1. ipconfig (veya Linux/macOS'ta ifconfig / ip addr)
Bilgisayarınızın ağ arayüzlerinin (Wi-Fi, Ethernet) o andaki IP adresini, Subnet Mask'ını ve Default Gateway'ini (modem adresi) gösterir.
- **ipconfig /release & /renew:** DHCP sunucusundan yeni bir IP adresi istemek için kullanılır. Bağlantı sorunlarını çözmekte çok etkilidir.
- **ipconfig /displaydns:** Bilgisayarınızın hafızasında tuttuğu DNS kayıtlarını gösterir.

### 2. netstat (Network Statistics)
Bilgisayarınızdaki tüm aktif ağ bağlantılarını ve hangi portların "dinlemede" (Listening) olduğunu gösterir.
- **Güvenlik Analizi:** `netstat -ano` komutuyla bilgisayarınızın arka planda tanımadığınız bir IP adresiyle konuşup konuşmadığını görebilirsiniz. Eğer bir virüs (trojan) bulaştıysa, saldırganın sunucusuyla olan bağlantısı burada görünür.

### 3. arp (Address Resolution Protocol)
IP adreslerini fiziksel MAC adreslerine eşleyen tabloyu (ARP Cache) gösterir.
- **ARP Poisoning:** Bir saldırgan bu tabloyu bozarak kendi MAC adresini "modemin adresi" gibi gösterebilir. Böylece tüm trafiğiniz önce saldırgana gider. `arp -a` komutuyla aynı MAC adresine sahip birden fazla IP olup olmadığını kontrol etmek bu saldırıyı tespit etmeye yarar.

### 4. Bilmen Gereken Bazı Terimler
- **Default Gateway:** Sizin ağınızdan çıkıp internete giden ana kapıdır (genellikle modemin IP'si).
- **Listening Port:** Bilgisayarınızda bir servisin (Örn: Web sunucusu veya uzak masaüstü) dışarıdan gelecek bağlantıları beklediği porttur.
- **Promiscuous Mode:** Bir ağ kartının sadece kendisine gelenleri değil, ağdaki tüm paketleri okuyabilmesini sağlayan özel bir moddur (Sniffing için gereklidir).

### Gerçek Dünya Analojisi
- **ipconfig:** Kimlik kartınıza bakıp "Benim adım ne, hangi evde yaşıyorum?" demek gibidir.
- **netstat:** O anda kiminle telefonda konuştuğunuzu veya kapıda kimin beklediğini gösteren bir listedir.
- **arp:** Apartmandaki daire numaralarıyla (IP), o dairelerde oturanların isimlerini (MAC) eşleştiren kapıcı listesi gibidir.