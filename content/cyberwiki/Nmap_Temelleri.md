+++
title = "Tarama: nmap Temel Kullanımı | Scanning: Basic Usage of nmap"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

Nmap (Network Mapper) is the most powerful tool for discovering devices on a network and understanding which services (and which versions) are running on these devices. It is known as the "Swiss Army Knife" of cybersecurity.

### 1. What to Do with Nmap?
- **Host Discovery:** Which devices are open on the network?
- **Port Scanning:** Which ports (ports) of the devices are open? (Ex: 80, 443, 22)
- **Service Version Detection:** Which program is running on the open port and what is its version? (Ex: Apache 2.4.41)
- **OS Detection:** What is the operating system of the device? (Windows or Linux?)

### 2. Basic Commands
- `nmap 192.168.1.1`: Scans the 1000 most common ports on the target.
- `nmap -sV 192.168.1.1`: Detects the version.
- `nmap -O 192.168.1.1`: Detects the operating system.
- `nmap -p- 192.168.1.1`: Scans all ports (65535).

### 3. Some Terms You Should Know
- **Port Status (Open/Closed/Filtered):**
    - **Open:** The door is open, the service is running.
    - **Closed:** The door is closed, there is no one inside.
    - **Filtered:** There is a guard (Firewall) in front of the door, it does not allow me to look inside.
- **Stealth Scan (SYN Scan - `-sS`):** This is the type of scanning performed without fully establishing the connection (without completing the 3-way handshake). It is faster and tries to leave less traces in the logs.
- **NSE (Nmap Scripting Engine):** Thanks to the small programs added to Nmap, it allows not only scanning but also vulnerability detection.

### 4. Safety and Ethics
Running an Nmap scan is like "trying to force every single door in a building". Many firewalls and IDS/IPS systems immediately detect these scans and ban your IP address. You should always scan on networks for which you have legal permission.

### Real World Analogy
Nmap is like a locksmith with a giant keychain. It visits every house in the neighborhood (Network), one by one, and reports which doors (Port) are open, which sounds (Service) come from inside, and the brand of the locks of the doors (Version).
