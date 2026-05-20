+++
title = "IPv6 Adresleme Temelleri"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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