# 🛡️ Siber Güvenlik Yol Haritası (Cybersecurity Roadmap)

## 0. Hazırlık ve Pratik Platformları
- [x] [[CTF_Platformlari|CTF Platformları (HackTheBox, TryHackMe, VulnHub, picoCTF)]]

## 1. Bilişim Temelleri (IT Foundations)
### Donanım (Hardware)
- [x] [[CPU|CPU (Merkezi İşlem Birimi)]] - Çalışma mantığı
- [x] [[RAM|RAM (Bellek)]] - Türleri ve Volatility
- [x] [[Anakart_Chipset|Anakart (Motherboard) & Chipset]]
- [x] [[Depolama_Birimleri|Depolama Birimleri (HDD, SSD, NVMe)]]
- [x] [[PSU_Enerji|Güç Kaynağı (PSU) ve Enerji Verimliliği]]
- [x] [[WiFi_Standartlari|WiFi Standartları (802.11 a/b/g/n/ac/ax)]]
- [x] [[Bluetooth_Guvenligi|Bluetooth Protokolleri ve Güvenliği]]
- [x] [[NFC_Mekanizmasi|NFC (Near Field Communication) Mekanizması]]
- [x] [[Infrared_Iletisimi|Infrared (Kızılötesi) İletişimi]]
### İşletim Sistemleri (OS)
- [x] [[NTFS_Izinler|Windows Dosya Sistemi (NTFS) & İzinler]]
- [x] [[Linux_Dosya_Sistemi|Linux Dosya Sistemi (Ext4) & İzinler]]
- [x] [[macOS_Dosya_Sistemi|macOS Dosya Sistemi (APFS)]]
- [x] [[Windows_Registry|Windows Registry Mantığı]]
- [x] [[Linux_Kernel_Dagıtimlar|Linux Kernel ve Dağıtımlar]]
- [x] [[CLI_Navigasyonu|CLI (Komut Satırı) Navigasyonu - Temel Komutlar]]
- [x] [[Kullanici_Grup_Yonetimi|Kullanıcı ve Grup Yönetimi (IAM Temelleri)]]
- [x] [[Troubleshooting_Logs|Troubleshooting - Event Viewer & Syslog Okuma]]
### Sanallaştırma (Virtualization)
- [x] [[Hypervisor_Turleri|Hypervisor Türleri (Type 1 vs Type 2)]]
- [x] [[VMware_ESXi|VMware Workstation/ESXi]]
- [x] [[VirtualBox_Yapilandirma|VirtualBox Yapılandırması]]
- [x] [[Proxmox_Konteyner|Proxmox & Konteyner Sanallaştırma]]
- [x] [[Snapshot_Klonlama|Snapshot ve Klonlama Yönetimi]]

## 2. Ağ Bilgisi (Networking)
### Temeller ve Protokoller
- [x] [[OSI_Modeli|OSI Modeli - 7 Katman Detayı]]
- [x] [[TCPIP_Modeli|TCP/IP Modeli - 4 Katman Detayı]]
- [x] [[IPv4_Adresleme|IPv4 Adresleme ve Sınıflar]]
- [x] [[IPv6_Temelleri|IPv6 Adresleme Temelleri]]
- [x] [[Subnetting_CIDR|Subnetting & CIDR Hesaplama]]
- [x] [[Public_Private_IP|Public vs Private IP Farkları]]
- [x] [[DNS_Mekanizmasi|DNS (Domain Name System) - Kayıt Türleri]]
- [x] [[DHCP_DORA|DHCP (Dynamic Host Configuration Protocol) - DORA Süreci]]
- [x] [[HTTP_HTTPS|HTTP vs HTTPS (Port 80 vs 443)]]
- [x] [[SSL_TLS_Handshake|SSL / TLS El Sıkışma (Handshake) Mekanizması]]
- [x] [[SSH_Guvenligi|SSH (Secure Shell) - Anahtar Tabanlı Erişim]]
- [x] [[RDP_Guvenligi|RDP (Remote Desktop Protocol) Güvenliği]]
- [x] [[FTP_SFTP_FTPS|FTP / SFTP / FTPS Farkları]]
- [x] [[Eposta_Protokolleri|SMTP / POP3 / IMAP - E-posta Protokolleri]]
- [x] [[Kerberos_Mantigi|Kerberos - Bilet Tabanlı Kimlik Doğrulama]]
- [x] [[RADIUS_TACACS|RADIUS & TACACS+]]
- [x] [[LDAP_Mekanizmasi|LDAP (Lightweight Directory Access Protocol)]]
- [x] [[SNMP_Guvenligi|SNMP (Simple Network Management Protocol)]]
### Ağ Yapısı ve Cihazlar
- [x] [[Ag_Topolojileri|Ağ Topolojileri (Mesh, Star, Ring, Bus)]]
- [x] [[Ag_Cihazlari|Hub vs Switch vs Router Farkları]]
- [x] [[VLAN_Trunking|VLAN (Virtual LAN) ve Trunking]]
- [x] [[DMZ_Mimarisi|DMZ (Demilitarized Zone) Mimarisi]]
- [x] [[VPN_Turleri|VPN (Virtual Private Network) Türleri (IPsec, OpenVPN)]]
- [x] [[Firewall_Prensipleri|Firewall (Güvenlik Duvarı) Çalışma Prensipleri]]
- [x] [[Proxy_Sunuculari|Proxy Sunucuları (Forward vs Reverse Proxy)]]
- [x] [[Troubleshooting_1|Sorun Giderme: ping, tracert/traceroute]]
- [x] [[Troubleshooting_2|Sorun Giderme: nslookup, dig]]
- [x] [[Troubleshooting_3|Sorun Giderme: ipconfig/ifconfig, netstat, arp]]
- [x] [[Paket_Analizi|Paket Analizi: Wireshark & tcpdump Temelleri]]
- [x] [[Nmap_Temelleri|Tarama: nmap Temel Kullanımı]]

## 3. Güvenlik Kavramları ve Mimari
- [x] [[CIA_Triad|CIA Triad (Confidentiality, Integrity, Availability)]]
- [x] [[Defense_in_Depth|Defense in Depth (Çok Katmanlı Savunma)]]
- [x] [[Zero_Trust|Zero Trust Architecture (Hiçbir Zaman Güvenme)]]
- [x] [[Risk_Yonetimi|Risk Tanımı ve Değerlendirmesi]]
- [x] [[Yedekleme_Stratejileri|Backup (Yedekleme) Stratejileri (3-2-1 Kuralı)]]
- [x] [[Resiliency_DR|Resiliency ve Olağanüstü Durum Kurtarma (DR)]]
- [x] [[MFA_Turleri|MFA (Multi-Factor Authentication) Türleri]]
- [x] [[SSO_Mekanizmalari|SSO (Single Sign-On) Mekanizmaları]]
- [x] [[Auth_vs_Auth|Authentication vs Authorization (Kimlik vs Yetki)]]

## 4. Saldırı Türleri ve Metodolojileri (Attacks)
### Sosyal Mühendislik
- [x] [[Phishing|Phishing (Oltalama) Teknikleri]]
- [x] [[Smishing_Vishing|Smishing (SMS) & Vishing (Sesli)]]
- [x] [[Whaling_BEC|Whaling & Business Email Compromise (BEC)]]
- [x] [[Impersonation|Impersonation (Kimlik Taklidi)]]
- [x] [[Tailgating_Piggybacking|Tailgating & Piggybacking (Fiziksel Erişim)]]
- [x] [[Dumpster_Shoulder|Dumpster Diving & Shoulder Surfing]]
- [x] [[Watering_Hole|Watering Hole Attack]]
### Teknik Saldırılar
- [x] [[DoS_DDoS|DoS vs DDoS (Denial of Service)]]
- [x] [[MitM_ARP|MitM (Man-in-the-Middle) - ARP Poisoning]]
- [x] [[DNS_Saldirilari|DNS Poisoning & Hijacking]]
- [x] [[VLAN_Hopping|VLAN Hopping]]
- [x] [[SQL_Injection|SQL Injection (SQLi)]]
- [x] [[XSS|Cross-Site Scripting (XSS)]]
- [x] [[CSRF|Cross-Site Request Forgery (CSRF)]]
- [x] [[IDOR|IDOR (Insecure Direct Object Reference)]]
- [x] [[Directory_Traversal|Directory Traversal (Path Traversal)]]
- [x] [[Buffer_Overflow|Buffer Overflow Mantığı]]
- [x] [[Memory_Leak|Memory Leak (Bellek Sızıntısı)]]
- [x] [[Pass_the_Hash_Ticket|Pass the Hash & Golden Ticket]]
- [x] [[Password_Attacks|Brute Force vs Password Spraying]]
### Metodolojiler ve Çerçeveler
- [x] [[Guvenlik_Frameworkleri|Güvenlik Frameworkleri (MITRE ATT&CK, Cyber Kill Chain, NIST CSF)]]

## 5. Savunma, İzleme ve Analiz (Defense)
- [x] [[SIEM_Temelleri|SIEM (Security Information and Event Management) - Splunk/ELK]]
- [x] [[EDR_Temelleri|EDR (Endpoint Detection and Response)]]
- [x] [[XDR_Temelleri|XDR (Extended Detection and Response)]]
- [x] [[IDS_IPS|IDS vs IPS (Intrusion Detection/Prevention)]]
- [x] [[NGFW_Ozellikleri|Next-Gen Firewall (NGFW) Özellikleri]]
- [x] [[Windows_Logs|Windows Event Logs Analizi]]
- [x] [[Linux_Syslog_Analizi|Linux Syslog Analizi]]
- [x] [[Digital_Forensics|Digital Forensics - Disk İmajı ve Bellek Analizi]]
- [x] [[Malware_Static|Malware Analizi - Statik Analiz Temelleri]]
- [x] [[Malware_Dynamic|Malware Analizi - Dinamik (Sandbox) Analiz]]
- [x] [[Analiz_Araclari|Analiz Araçları: VirusTotal, Any.run, WHOIS]]
- [x] [[Olay_Mudahale|Olay Müdahale (Incident Response) ve Tehdit Avcılığı]]

## 6. Kriptografi
- [x] [[Hashing_Algoritmalari|Hashing Algoritmaları (MD5, SHA-1, SHA-256)]]
- [x] [[Salting_Peppering|Salting ve Peppering (Şifre Güvenliği)]]
- [x] [[Simetrik_Sifreleme|Simetrik Şifreleme (AES, DES)]]
- [x] [[Asimetrik_Sifreleme|Asimetrik Şifreleme (RSA, ECC, Diffie-Hellman)]]
- [x] [[PKI_Bilesenleri|PKI (Public Key Infrastructure) Bileşenleri]]
- [x] [[Dijital_Imza_Sertifika|Sayısal İmzalar ve Sertifika Otoriteleri (CA)]]

## 7. Bulut Güvenliği (Cloud Security)
- [x] [[Bulut_Guvenligi|Bulut Güvenliği (AWS, Azure, SaaS, PaaS, IaC)]]

## 8. Programlama ve Araçlar
- [x] [[Programlama_Dilleri|Siber Güvenlikte Programlama (Python, Bash, Go, PowerShell)]]
- [x] [[Siber_Guvenlik_Araclari|Güvenlik Araçları ve Dağıtımları (Kali, Parrot, Metasploit, nmap)]]

## 9. Yönetişim, Risk ve Uyumluluk (GRC)
- [x] [[Uyumluluk_ve_Hukuk|Hukuk, Uyumluluk ve İnsan Kaynakları]]

## 10. Sertifikasyon Yolculuğu
- [x] [[Sertifikalar|Siber Güvenlik Sertifikaları (A+, Security+, OSCP, CISSP)]]

---
## ⚙️ Uzmanlık Alanı
- [[devsecops|DevSecOps Uzmanlık Yol Haritası]]

---
**Kaynaklar:** [[raw/cyber-security.pdf]], [[cyber-security.txt]]
