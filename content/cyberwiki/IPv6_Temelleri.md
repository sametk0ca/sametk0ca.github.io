+++
title = "IPv6 Adresleme Temelleri | IPv6 Addressing Fundamentals"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

IPv4 adreslerinin tükenmesi üzerine geliştirilen IPv6, 128 bitlik devasa bir adres alanı sunar. Bu, dünyadaki her kum tanesine binlerce IP adresi verilebileceği anlamına gelir.

### 1. Adres Yapısı ve Yazımı
IPv6 adresleri 16 bitlik 8 gruptan oluşur ve onaltılık (hexadecimal) tabanda yazılır (Örn: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
- **Kısaltma Kuralları:**
    - Bir gruptaki baştaki sıfırlar atılabilir.
    - Arka arkaya gelen sıfır grupları bir kez olmak şartıyla `::` ile gösterilebilir.
    - Örn: `2001:db8:85a3::8a2e:370:7334`.

### 2. Öne Çıkan Özellikler
- **IPSec Desteği:** IPv6 tasarlanırken güvenlik (IPSec) protokolü yerleşik bir zorunluluk olarak düşünülmüştür (IPv4'te sonradan eklenmiştir).
- **No More NAT:** Adres bolluğu sayesinde cihazlar doğrudan internete çıkabilir. Ancak bu, cihazların internetten doğrudan saldırı alabileceği anlamına da gelir (Stateful Firewall gereklidir).
- **Stateless Address Autoconfiguration (SLAAC):** Cihazlar bir DHCP sunucusu olmadan da kendi IP'lerini MAC adreslerini kullanarak otomatik oluşturabilirler.

### 3. IPv6 Güvenlik Zorlukları
- **Reconnaissance (Keşif) Zorluğu:** IPv4 ağları saniyeler içinde taranabilirken, bir IPv6 alt ağını taramak (brute-force) adres alanının büyüklüğü nedeniyle imkansıza yakındır.
- **Neighbor Discovery Protocol (NDP) Saldırıları:** IPv4'teki ARP'nin yerini alan NDP, benzer şekilde zehirlenebilir (NDP Spoofing). Bu, yerel ağda MitM saldırılarına yol açar.
- **Tünelleme Riskleri:** IPv4 üzerinden IPv6 taşıyan tüneller (6to4, Teredo), güvenlik duvarlarını atlamak için kullanılabilir. Saldırganlar bu tünelleri görünmez yollar oluşturmak için suistimal edebilir.

### 4. Coexistence (Birlikte Yaşama)
Şu an internet "Dual-Stack" (hem IPv4 hem IPv6 aktif) dönemindedir. Güvenlik yapılandırmaları her iki protokol için de ayrı ayrı ve eksiksiz yapılmalıdır; genellikle IPv6 unutulduğu için bir güvenlik açığı oluşturur.

---

## English Version

Developed to address the exhaustion of IPv4 addresses, IPv6 offers a massive 128-bit address space. This means that every grain of sand on Earth can be assigned thousands of IP addresses.

### 1. Address Structure and Writing
IPv6 addresses consist of 8 groups of 16 bits and are written in hexadecimal base (Ex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
- **Abbreviation Rules:**
    - Leading zeros in a group can be dropped.
    - Consecutive zero groups can be represented with `::` only once.
    - Ex: `2001:db8:85a3::8a2e:370:7334`.

### 2. Highlights
- **IPSec Support:** When IPv6 was designed, the security (IPSec) protocol was considered a built-in necessity (added later in IPv4).
- **No More NAT:** Thanks to the abundance of addresses, devices can access the internet directly. However, this also means that devices can receive direct attacks from the internet (Stateful Firewall is required).
- **Stateless Address Autoconfiguration (SLAAC):** Devices can automatically create their own IPs using their MAC addresses, even without a DHCP server.

### 3. IPv6 Security Challenges
- **Reconnaissance Difficulty:** While IPv4 networks can be scanned in seconds, scanning (brute-force) an IPv6 subnet is almost impossible due to the size of the address space.
- **Neighbor Discovery Protocol (NDP) Attacks:** NDP, which replaces ARP in IPv4, can be similarly poisoned (NDP Spoofing). This leads to MitM attacks on the local network.
- **Tunneling Risks:** Tunnels carrying IPv6 over IPv4 (6to4, Teredo) can be used to bypass firewalls. Attackers can exploit these tunnels to create invisible paths.

### 4. Coexistence
Currently, the internet is in the "Dual-Stack" era (both IPv4 and IPv6 are active). Security configurations must be made separately and completely for both protocols; IPv6 often creates a security vulnerability because it is forgotten.
