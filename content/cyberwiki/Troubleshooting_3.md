+++
title = "Sorun Giderme Araçları - Bölüm 3: ipconfig, netstat, arp | Troubleshooting Tools - Part 3: ipconfig, netstat, arp"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

These tools allow you to view your own computer's network settings and current network connections.

### 1. ipconfig (or ifconfig / ip addr on Linux/macOS)
It shows the current IP address, Subnet Mask and Default Gateway (modem address) of your computer's network interfaces (Wi-Fi, Ethernet).
- **ipconfig /release & /renew:** Used to request a new IP address from the DHCP server. It is very effective in solving connection problems.
- **ipconfig /displaydns:** Shows the DNS records that your computer keeps in its memory.

### 2. netstat (Network Statistics)
It shows all active network connections on your computer and which ports are "listening".
- **Security Analysis:** You can see whether your computer is talking to an IP address you do not recognize in the background with the `netstat -ano` command. If it is infected with a virus (trojan), its connection to the attacker's server appears here.

### 3. arp (Address Resolution Protocol)
Shows the table (ARP Cache) that maps IP addresses to physical MAC addresses.
- **ARP Poisoning:** An attacker can corrupt this table and make his MAC address look like the "modem's address". So all your traffic goes to the attacker first. Checking if there is more than one IP with the same MAC address with the `arp -a` command helps detect this attack.

### 4. Some Terms You Should Know
- **Default Gateway:** It is the main gateway from your network to the internet (usually the IP of the modem).
- **Listening Port:** It is the port on your computer where a service (eg Web server or remote desktop) waits for external connections.
- **Promiscuous Mode:** It is a special mode that allows a network card to read all packets on the network, not just those coming to it (required for Sniffing).

### Real World Analogy
- **ipconfig:** You look at your ID card and ask "What is my name, which house do I live in?" It's like saying.
- **netstat:** It is a list that shows who you are currently talking to on the phone or who is waiting at the door.
- **arp:** It is like a concierge list that matches the apartment numbers (IP) in the apartment with the names (MAC) of the people living in those apartments.
