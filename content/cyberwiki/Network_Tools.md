+++
title = "Ağ ve Analiz Araçları | Network and Analysis Tools"
date = "2026-05-19"
draft = false
categories = ["Tools"]
type = "cyberwiki"
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

---

## English Version

In cybersecurity, the basic tools used to discover networks, analyze traffic and audit systems are:

## 🔍 Discovery and Information Gathering (Discovery)

- **ping:** Checks whether a server is up or not.
- **nmap (Network Mapper):** Scans devices and open ports on the network. It is the Swiss army knife of cyber security.
- **nslookup & dig:** Used to query DNS records. `dig` gives more detailed information.
- **whois:** Shows who owns a domain name and registration information.

## 🕸️ Package Analysis and Tracking

- **Wireshark:** It is a tool with a graphical interface that instantly captures and analyzes network traffic.
- **tcpdump:** Captures network packets via the command line. Ideal for fast analysis on servers.
- **hping3:** Allows you to perform network tests and DDoS simulations by creating custom TCP/IP packets.

## 💻 System and File Commands

- **ipconfig / ifconfig:** Shows the device's IP address and network configuration.
- **netstat:** Lists active network connections and listened ports.
- **arp:** Manages the ARP table (IP-MAC mappings).
- **tracert / traceroute:** Shows the routes (routers) that a packet passes through on its way to the destination.

## 📂 File and Data Processing

- **cat, head, tail:** Used to read file content. `tail -f` logs are great for viewing live.
- **grep:** Searches within text files.
- **dd:** It is a powerful command used to take a disk image or copy data.
- **curl:** Transfers data via URL, frequently used for API tests.

## 🔬 Forensics

- **Autopsy:** It is a comprehensive platform used for digital forensic analysis.
- **WinHex:** As a hex editor, it is used to analyze files and disks.

---
**Important:** When using these tools, always comply with legal limits and only scan on networks for which you are authorized.
