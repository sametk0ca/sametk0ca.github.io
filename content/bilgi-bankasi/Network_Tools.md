+++
title = "Ağ ve Analiz Araçları"
date = "2026-05-19"
draft = false
categories = ["Tools"]
type = "bilgi-bankasi"
+++

Siber güvenlikte, ağları keşfetmek, trafiği analiz etmek ve sistemleri denetlemek için kullanılan temel araçlar şunlardır:

## 🔍 Keşif ve Bilgi Toplama (Discovery)

- **ping:** Bir sunucunun ayakta olup olmadığını kontrol eder.
- **nmap (Network Mapper):** Ağdaki cihazları ve açık portları tarar. Siber güvenliğin İsviçre çakısıdır.
- **nslookup & dig:** DNS kayıtlarını sorgulamak için kullanılır. `dig` daha detaylı bilgi verir.
- **whois:** Bir alan adının kime ait olduğunu ve kayıt bilgilerini gösterir.

## 🕸️ Paket Analizi ve İzleme

- **Wireshark:** Ağ trafiğini anlık olarak yakalayan ve analiz eden grafik arayüzlü bir araçtır.
- **tcpdump:** Komut satırı üzerinden ağ paketlerini yakalar. Sunucularda hızlı analiz için idealdir.
- **hping3:** Özel TCP/IP paketleri oluşturarak ağ testleri ve DDoS simülasyonları yapmanızı sağlar.

## 💻 Sistem ve Dosya Komutları

- **ipconfig / ifconfig:** Cihazın IP adresini ve ağ yapılandırmasını gösterir.
- **netstat:** Aktif ağ bağlantılarını ve dinlenen portları listeler.
- **arp:** ARP tablosunu (IP-MAC eşleşmeleri) yönetir.
- **tracert / traceroute:** Bir paketin hedefe giderken geçtiği yolları (router'ları) gösterir.

## 📂 Dosya ve Veri İşleme

- **cat, head, tail:** Dosya içeriğini okumak için kullanılır. `tail -f` logları canlı izlemek için harikadır.
- **grep:** Metin dosyaları içinde arama yapar.
- **dd:** Disk imajı almak veya veri kopyalamak için kullanılan güçlü bir komuttur.
- **curl:** URL üzerinden veri transferi yapar, API testleri için sıkça kullanılır.

## 🔬 Adli Bilişim (Forensics)

- **Autopsy:** Dijital adli bilişim analizleri için kullanılan kapsamlı bir platformdur.
- **WinHex:** Hex (onaltılık) düzenleyici olarak dosya ve disk analizi yapmaya yarar.

---
**Önemli:** Bu araçları kullanırken her zaman yasal sınırlara uyun ve sadece izinli olduğunuz ağlarda tarama yapın.