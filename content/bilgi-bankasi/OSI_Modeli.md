+++
title = "OSI Modeli - 7 Katman Detayı ve Güvenlik Bakışı"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

OSI (Open Systems Interconnection) modeli, farklı bilgisayar sistemlerinin birbirleriyle iletişim kurabilmesi için ISO tarafından geliştirilmiş teorik bir çerçevedir. Ağı 7 ayrı katmana bölerek karmaşıklığı azaltır ve her katmanın sadece bir üst ve bir alt katmanla konuşmasını sağlar.

### 1. Katman: Fiziksel (Physical Layer)
Verinin kablolar, radyo dalgaları veya fiber optik üzerinden "bit" (0 ve 1) olarak iletildiği katmandır.
- **Teknik Detay:** Voltaj seviyeleri, kablo tipleri (Cat6, Fiber) ve hub cihazları bu katmandadır.
- **Güvenlik Analojisi:** Bir binanın kapısındaki fiziksel kilitler gibidir. Kabloyu kesmek veya bir "tapper" cihazı ile sinyali dinlemek bu katmana yönelik saldırılardır.

### 2. Katman: Veri Bağı (Data Link Layer)
Fiziksel katmandan gelen bitlerin "çerçevelere" (frames) dönüştürüldüğü ve MAC adresleri kullanılarak yerel ağda iletildiği katmandır.
- **Teknik Detay:** Switch'ler ve Ethernet protokolü burada çalışır. Hata kontrolü (CRC) yapılır.
- **Güvenlik (MAC Spoofing & ARP Poisoning):** Saldırganlar kendi MAC adreslerini kurbanınkiyle değiştirerek (spoofing) veya sahte ARP yanıtları göndererek trafiği kendi üzerlerine çekebilirler.

### 3. Katman: Ağ (Network Layer)
Verinin farklı ağlar arasında yönlendirildiği (routing) ve IP adreslerinin kullanıldığı katmandır. Veri birimi "paket" (packet) adını alır.
- **Teknik Detay:** Router'lar ve IP (IPv4/v6), ICMP protokolleri bu katmandadır.
- **Güvenlik (IP Spoofing & DoS):** Paketlerin kaynağını gizleyerek yapılan saldırılar ve ağın paketlerle boğulması (ICMP Flood) bu katmanda gerçekleşir.

### 4. Katman: Taşıma (Transport Layer)
Verinin uçtan uca hatasız iletilmesini sağlar. Veri birimi "segment" (TCP) veya "datagram" (UDP) olarak adlandırılır.
- **Teknik Detay:** TCP (güvenli/bağlantılı) ve UDP (hızlı/bağlantısız) protokolleri buradadır. Port numaraları (0-65535) burada tanımlanır.
- **Güvenlik (SYN Flood):** TCP 3-way handshake sürecini suistimal ederek sistem kaynaklarını tüketme saldırıları bu katmanı hedefler.

### 5. Katman: Oturum (Session Layer)
Uygulamalar arasındaki bağlantıların açılması, yönetilmesi ve kapatılmasını sağlar.
- **Teknik Detay:** RPC, NetBIOS ve SQL oturumları bu katmanda yönetilir.
- **Güvenlik:** Session Hijacking (Oturum Çalma) saldırıları, aktif bir oturumu ele geçirmeyi hedefler.

### 6. Katman: Sunum (Presentation Layer)
Verinin "anlaşılabilir" hale getirildiği katmandır. Karakter kodlama (ASCII/UTF-8), şifreleme ve sıkıştırma burada yapılır.
- **Teknik Detay:** SSL/TLS (modern yapılarda katmanlar arası geçiş yapsa da teoride buradadır) ve MIME bu katmandadır.
- **Güvenlik:** Yanlış yapılandırılmış şifreleme algoritmaları veya veri formatı üzerinden yapılan saldırılar.

### 7. Katman: Uygulama (Application Layer)
Kullanıcının doğrudan etkileşime girdiği katmandır.
- **Teknik Detay:** HTTP, FTP, SMTP, DNS protokolleri burada çalışır.
- **Güvenlik (L7 Attacks):** SQL Injection, XSS gibi web uygulama saldırıları ve bot trafikleri bu katmanın konusudur. En karmaşık ve tespit edilmesi en zor saldırılar genellikle buradadır.