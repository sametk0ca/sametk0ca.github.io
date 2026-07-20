+++
title = "Sorun Giderme Araçları - Bölüm 2: nslookup ve dig | Troubleshooting Tools - Part 2: nslookup and dig"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Bu araçlar "DNS" sorunlarını teşhis etmek için kullanılır. "Bir sitenin ismini yazdığımda neden IP'sini bulamıyorum?" sorusunun yanıtı buradadır.

### 1. nslookup (Name System Lookup)
Hem Windows hem de Linux'ta bulunan temel bir DNS sorgulama aracıdır.
- **Kullanım:** `nslookup google.com` yazdığınızda size Google'ın hangi IP adreslerinde olduğunu söyler.
- **Interactive Mode:** Sadece `nslookup` yazıp enter'a basarsanız, istediğiniz bir DNS sunucusunu (Örn: 8.8.8.8) kullanarak sorgu yapabileceğiniz özel bir moda girersiniz.

### 2. dig (Domain Information Groper)
Linux ve macOS'ta standart olarak gelen, çok daha detaylı ve profesyonel bir araçtır.
- **Neden dig?** `nslookup`'tan çok daha fazla bilgi verir. Sorgunun kaç milisaniyede yapıldığını, hangi DNS sunucusundan yanıt geldiğini ve DNS kayıtlarının tüm detaylarını (A, MX, TXT vb.) net bir şekilde gösterir.
- **Güvenlik Analizi:** Bir sızma testi (penetration test) sırasında saldırganlar, `dig` kullanarak bir şirketin tüm DNS kayıtlarını çekmeye (Zone Transfer) çalışabilirler.

### 3. Bilmen Gereken Bazı Terimler
- **FQDN (Fully Qualified Domain Name):** Bir domain'in tam ve eksiksiz adı (Örn: `www.google.com.` - Sondaki nokta bile önemlidir).
- **Zone Transfer (AXFR):** Bir DNS sunucusundaki tüm kayıtların bir kerede başka bir yere aktarılmasıdır. Eğer düzgün kapatılmazsa, şirketin tüm iç ağ yapısı (sunucu isimleri vb.) bir saldırganın eline geçebilir.
- **Authoritative Answer:** Yanıtın, o domain'den bizzat sorumlu olan "resmi" sunucudan geldiğini belirtir.

### Gerçek Dünya Analojisi
- **nslookup:** Mahallenin bakkalına "Ali Amca, muhtarın telefon numarası kaç?" diye sormak gibidir. Bakkal defterine (cache) bakıp size söyler.
- **dig:** Doğrudan muhtarlığa gidip, tüm resmi kayıtları (telefon, adres, MX kayıtları) incelemek ve belgenin mühürlü olup olmadığını kontrol etmek gibidir.

---

## English Version

These tools are used to diagnose "DNS" problems. "Why can't I find the IP of a site when I type its name?" The answer to the question is here.

### 1. nslookup (Name System Lookup)
It is a basic DNS query tool available on both Windows and Linux.
- **Usage:** When you type `nslookup google.com` it tells you which IP addresses Google is on.
- **Interactive Mode:** If you just type `nslookup` and press enter, you will enter a special mode where you can query using a DNS server of your choice (Ex: 8.8.8.8).

### 2. dig (Domain Information Groper)
It is a much more detailed and professional tool that comes standard on Linux and macOS.
- **Why dig?** It gives much more information than `nslookup`. It clearly shows how many milliseconds it took for the query to be made, which DNS server the response came from, and all the details of the DNS records (A, MX, TXT, etc.).
- **Security Analysis:** During a penetration test, attackers may try to pull all DNS records of a company (Zone Transfer) using `dig`.

### 3. Some Terms You Should Know
- **FQDN (Fully Qualified Domain Name):** The full and complete name of a domain (Ex: `www.google.com.` - Even the dot at the end is important).
- **Zone Transfer (AXFR):** It is the transfer of all records on a DNS server to another place at once. If not shut down properly, the company's entire internal network structure (server names, etc.) can be compromised by an attacker.
- **Authoritative Answer:** Indicates that the response comes from the "official" server that is personally responsible for that domain.

### Real World Analogy
- **nslookup:** "Uncle Ali, what is the phone number of the headman?" to the neighborhood grocery store. It's like asking. The grocery store looks at its cache and tells you.
- **dig:** It is like going directly to the headman's office, examining all official records (phone, address, MX records) and checking whether the document is sealed.
