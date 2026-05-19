+++
title = "Tarama: nmap Temel Kullanımı"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Nmap (Network Mapper), bir ağdaki cihazları keşfetmek ve bu cihazlar üzerinde hangi servislerin (ve hangi versiyonların) çalıştığını anlamak için kullanılan en güçlü araçtır. Siber güvenliğin "İsviçre Çakısı" olarak bilinir.

### 1. Nmap ile Neler Yapılır?
- **Host Discovery:** Ağda hangi cihazlar açık?
- **Port Scanning:** Cihazların hangi kapıları (portları) açık? (Örn: 80, 443, 22)
- **Service Version Detection:** Açık portta hangi program çalışıyor ve versiyonu ne? (Örn: Apache 2.4.41)
- **OS Detection:** Cihazın işletim sistemi ne? (Windows mu, Linux mu?)

### 2. Temel Komutlar
- `nmap 192.168.1.1`: Hedefteki en yaygın 1000 portu tarar.
- `nmap -sV 192.168.1.1`: Versiyon tespiti yapar.
- `nmap -O 192.168.1.1`: İşletim sistemi tespiti yapar.
- `nmap -p- 192.168.1.1`: Tüm portları (65535 tane) tarar.

### 3. Bilmen Gereken Bazı Terimler
- **Port Status (Open/Closed/Filtered):**
    - **Open:** Kapı açık, servis çalışıyor.
    - **Closed:** Kapı kapalı, içeride kimse yok.
    - **Filtered:** Kapının önünde bir koruma (Firewall) var, içeri bakmama izin vermiyor.
- **Stealth Scan (SYN Scan - `-sS`):** Bağlantıyı tam kurmadan (3-way handshake'i tamamlamadan) yapılan tarama türüdür. Daha hızlıdır ve loglarda daha az iz bırakmaya çalışır.
- **NSE (Nmap Scripting Engine):** Nmap'in içine eklenen küçük programcıklar sayesinde sadece tarama değil, zafiyet tespiti de yapılmasını sağlar.

### 4. Güvenlik ve Etik
Nmap taraması yapmak, "bir binadaki tüm kapıları tek tek zorlamak" gibidir. Birçok firewall ve IDS/IPS sistemi bu taramaları anında fark eder ve IP adresinizi yasaklar. Her zaman yasal izin aldığınız ağlarda tarama yapmalısınız.

### Gerçek Dünya Analojisi
Nmap, elinde dev bir anahtarlık olan bir çilingir gibidir. Mahalledeki (Ağ) her evi tek tek gezer, hangi kapıların (Port) açık olduğunu, içeriden hangi seslerin (Servis) geldiğini ve kapıların kilidinin markasını (Versiyon) raporlar.