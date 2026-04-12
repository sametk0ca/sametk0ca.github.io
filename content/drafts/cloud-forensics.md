---
title: "Cloud Forensics: Bulut Bilişimde Adli Bilişim ve Zorluklar"
date: 2026-04-11
draft: true
tags: ["Cloud Security", "Forensics", "DFIR", "CyBOK"]
categories: ["Digital Forensics"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png"
    alt: "Cloud Forensics"
    relative: false
---

![](https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png)

Bulut bilişimin yaygınlaşması, adli bilişim (forensics) süreçlerini "fiziksel erişim" paradigmasından "uzaktan ve API tabanlı" bir yapıya dönüştürmüştür. **Cloud Forensics (Bulut Adli Bilişimi)**, bulut ortamlarında (IaaS, PaaS, SaaS) gerçekleşen siber olayların tespiti, analizi ve kanıtlanması sürecidir. Bu disiplin, geleneksel adli bilişime kıyasla benzersiz teknik ve hukuksal zorluklar barındırır.

### Teknik Katmanlar ve Kanıt Toplama

Bulut adli bilişimi, CyBOK "Digital Forensics" ve "Cloud Security" alanlarının kesişiminde yer alır. Kanıt toplama süreci, bulut hizmet modeline bağlı olarak değişen "Paylaşımlı Sorumluluk Modeli" (Shared Responsibility Model) çerçevesinde şekillenir:

1. **Yönetim Katmanı (Control Plane):** Saldırganın bulut altyapısını yönetmek için kullandığı API çağrılarının analizidir. AWS CloudTrail, Azure Activity Log ve Google Cloud Audit Logs bu katmandaki temel kanıt kaynaklarıdır.
2. **Ağ Katmanı (Network Plane):** Bulut içindeki sanal ağ trafiğinin analizidir. VPC Flow Logs gibi araçlar, geleneksel paket yakalama (PCAP) yöntemlerinin yerini almaktadır.
3. **Veri Katmanı (Data Plane):** Nesne depolama (S3, Blob Storage) ve veritabanı loglarının analizidir. Verinin şifrelenmiş olması, adli bilişim uzmanları için anahtar yönetimi (KMS) süreçlerinin kritik bir parçası haline gelmesine neden olur.
4. **Konteyner ve Sunucusuz (Serverless) Forensics:** Ephemeral (geçici) yapılar nedeniyle, kanıtların sistem kapanmadan önce gerçek zamanlı olarak akış şeklinde (streaming) toplanması gereklidir.

### Standartlar ve Yasal Zorluklar

ISO/IEC 27017 (Bulut Hizmetleri Güvenlik Kontrolleri) ve ISO/IEC 27050 (Elektronik Keşif - eDiscovery) standartları, bulut ortamlarında kanıt yönetiminin temelini oluşturur. Ancak, verilerin birden fazla coğrafi bölgede (jurisdiction) saklanması, veri egemenliği (sovereignty) ve yasal erişim yetkileri (legal chain of custody) gibi konularda ciddi teknik ve hukuki engeller yaratmaktadır. "Multi-tenancy" yapısı nedeniyle, diğer kullanıcıların verilerine zarar vermeden kanıt toplama ("forensic isolation") süreci büyük bir hassasiyet gerektirir.

---

### Cloud Forensics: Digital Forensics and Challenges in Cloud Computing

The proliferation of cloud computing has transformed digital forensics from a "physical access" paradigm to a "remote and API-driven" structure. **Cloud Forensics** is the process of detecting, analyzing, and proving cyber incidents occurring within cloud environments (IaaS, PaaS, SaaS). This discipline presents unique technical and legal challenges compared to traditional forensics.

### Technical Layers and Evidence Collection

Cloud forensics sits at the intersection of the CyBOK "Digital Forensics" and "Cloud Security" knowledge areas. The evidence collection process is shaped by the "Shared Responsibility Model," which varies depending on the cloud service model:

1. **Control Plane:** Analysis of API calls used by an adversary to manage cloud infrastructure. AWS CloudTrail, Azure Activity Log, and Google Cloud Audit Logs are primary sources of evidence at this layer.
2. **Network Plane:** Analysis of virtual network traffic within the cloud. Tools like VPC Flow Logs are increasingly replacing traditional packet capture (PCAP) methods.
3. **Data Plane:** Analysis of object storage (S3, Blob Storage) and database logs. Data encryption makes key management (KMS) processes a critical part of the forensic investigation.
4. **Container and Serverless Forensics:** Due to ephemeral structures, evidence must be collected in real-time as a stream before the system terminates.

### Standards and Legal Challenges

The ISO/IEC 27017 (Cloud Service Security Controls) and ISO/IEC 27050 (Electronic Discovery) standards form the basis for evidence management in cloud environments. However, the storage of data across multiple geographical jurisdictions creates significant technical and legal hurdles regarding data sovereignty and the legal chain of custody. Due to multi-tenancy, the process of "forensic isolation"—collecting evidence without compromising the data of other users—requires extreme precision.
