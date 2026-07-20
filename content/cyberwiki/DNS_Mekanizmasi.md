+++
title = "DNS (Domain Name System) - İsim Çözümleme ve Kayıt Türleri | DNS (Domain Name System) - Name Resolution and Record Types"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

DNS is the telephone directory of the internet. It converts human-understandable web addresses (google.com) into machine-understandable IP addresses (142.250.184.206).

### 1. DNS Hierarchy
The DNS query follows a top-down path:
1. **Root Name Servers:** It is at the top, directs the query to the TLD servers.
2. **TLD Servers:** Manages extensions such as `.com`, `.org`, `.tr`.
3. **Authoritative Servers:** It is the last stop that holds the real IP information of the relevant domain.

### 2. Critical DNS Record Types
- **A Record:** Routes a domain name to an IPv4 address.
- **AAAA Record:** Routes a domain name to an IPv6 address.
- **CNAME (Canonical Name):** Redirects a domain to another domain (alias).
- **MX (Mail Exchanger):** Specifies which server the e-mails will go to.
- **TXT:** Holds text data. Often used for ownership verification and security (SPF, DKIM, DMARC).
- **NS (Name Server):** It tells which servers the domain is managed by.

### 3. DNS and Security
- **DNS Hijacking:** Attacker redirects you to a fake website by interfering with DNS settings.
- **DNS Cache Poisoning:** Misleading many users by adding fake records to the DNS server's memory.
- **DNSSEC:** Ensures that DNS data is digitally signed, ensuring that the data has not been modified.
- **DoH / DoT (DNS over HTTPS/TLS):** Enables DNS queries to be encrypted and hidden so that someone on the network cannot see which sites you visit.

### Real World Analogy
You want to call a "yellow taxi". The DNS server looks up the directory and finds the taxi rank number (IP) for you. If someone changes the guide (Hijacking), they can redirect you to a fake stop.
