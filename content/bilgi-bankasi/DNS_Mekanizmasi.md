+++
title = "DNS (Domain Name System) - İsim Çözümleme ve Kayıt Türleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

DNS, internetin telefon rehberidir. İnsanların anlayabileceği web adreslerini (google.com) makinelerin anlayabileceği IP adreslerine (142.250.184.206) dönüştürür.

### 1. DNS Hiyerarşisi
DNS sorgusu yukarıdan aşağıya bir yol izler:
1. **Root Name Servers:** En üsttedir, sorguyu TLD sunucularına yönlendirir.
2. **TLD Servers:** `.com`, `.org`, `.tr` gibi uzantıları yönetir.
3. **Authoritative Servers:** İlgili domain'in gerçek IP bilgisini tutan son duraktır.

### 2. Kritik DNS Kayıt Türleri
- **A Kaydı:** Bir domain adını IPv4 adresine yönlendirir.
- **AAAA Kaydı:** Bir domain adını IPv6 adresine yönlendirir.
- **CNAME (Canonical Name):** Bir domain'i başka bir domain'e yönlendirir (takma ad).
- **MX (Mail Exchanger):** E-postaların hangi sunucuya gideceğini belirtir.
- **TXT:** Metin verilerini tutar. Genellikle sahiplik doğrulaması ve güvenlik (SPF, DKIM, DMARC) için kullanılır.
- **NS (Name Server):** Domain'in hangi sunucular tarafından yönetildiğini söyler.

### 3. DNS ve Güvenlik
- **DNS Hijacking (DNS Gaspı):** Saldırganın DNS ayarlarına müdahale ederek sizi sahte bir web sitesine yönlendirmesi.
- **DNS Cache Poisoning (Önbellek Zehirleme):** DNS sunucusunun hafızasına sahte kayıtlar ekleyerek birçok kullanıcıyı yanlış yöne sevk etmek.
- **DNSSEC:** DNS verilerinin dijital olarak imzalanmasını sağlayarak verinin değiştirilmediğini garanti eder.
- **DoH / DoT (DNS over HTTPS/TLS):** DNS sorgularının şifrelenerek gizlenmesini sağlar, böylece ağdaki birisi hangi sitelere girdiğinizi göremez.

### Gerçek Dünya Analojisi
Siz "sarı taksi" çağırmak istiyorsunuz. DNS sunucusu sizin için rehbere bakıp taksi durağının numarasını (IP) bulur. Eğer biri rehberi değiştirirse (Hijacking), sizi sahte bir durağa yönlendirebilir.