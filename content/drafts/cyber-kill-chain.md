---
title: "Cyber Kill Chain: Gelişmiş Tehdit Modelleme ve Savunma Stratejileri"
date: 2026-04-11
draft: true
tags: ["Cyber Security", "Blue Team", "Threat Intel", "CyBOK"]
categories: ["Knowledge Base"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png"
    alt: "Cyber Kill Chain"
    relative: false
---

![](https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png)

Siber Ölüm Zinciri (Cyber Kill Chain), Lockheed Martin tarafından geliştirilen ve bir siber saldırının aşamalarını sistematik bir şekilde analiz eden yapısal bir çerçevedir. Bu model, saldırganların hedeflerine ulaşmak için tamamlaması gereken yedi aşamalı bir süreci tanımlar. Modern siber güvenlik operasyonlarında, bu zincirin herhangi bir halkasını kırmak, saldırıyı etkisiz hale getirmek için yeterlidir.

### Teknik Aşamalar ve Mekanizmalar

Siber Ölüm Zinciri, CyBOK (Cyber Security Body of Knowledge) kapsamında "Adversarial Behaviour" ve "Malware & Attack Technologies" bilgi alanları ile doğrudan ilişkilidir. Aşamaların teknik detayları şu şekildedir:

1. **Keşif (Reconnaissance):** Saldırganın hedef hakkında bilgi topladığı aşamadır. Pasif keşif (OSINT, WHOIS kayıtları) ve aktif keşif (port tarama, servis versiyon tespiti) teknikleri kullanılır.
2. **Silahlandırma (Weaponization):** Tespit edilen bir zafiyete yönelik exploit'in (sömürü kodu) bir zararlı yazılım (payload) ile birleştirilmesidir. Bu aşama genellikle saldırganın altyapısında gerçekleşir.
3. **İletim (Delivery):** Hazırlanan zararlı içeriğin hedefe ulaştırılmasıdır. Kimlik avı (phishing) e-postaları, sulama deliği (watering hole) saldırıları veya enfekte edilmiş taşınabilir medyalar bu aşamanın temel araçlarıdır.
4. **Sömürme (Exploitation):** Zararlı kodun hedef sistemdeki bir yazılım veya donanım açığını tetikleyerek yetkisiz erişim sağlamasıdır. NIST SP 800-115 standartları, bu tür sızma testleri için metodolojik rehberlik sunar.
5. **Kurulum (Installation):** Saldırganın sistemde kalıcılık (persistence) sağlamak için arka kapılar (backdoor) veya kayıt defteri anahtarları oluşturmasıdır.
6. **Komuta ve Kontrol (C2):** Ele geçirilen sistemin dış bir sunucu ile iletişim kurarak talimat almasıdır. DNS tünelleme veya HTTP/S tabanlı beaconing sinyalleri bu aşamada kritik rol oynar.
7. **Hedefe Yönelik Eylemler (Actions on Objectives):** Saldırganın nihai amacına (veri sızıntısı, fidye yazılımı şifrelemesi veya sistem bozma) ulaştığı aşamadır.

### Savunma Stratejileri ve Standartlar

ISO/IEC 27035 (Olay Yönetimi) ve NIST SP 800-61 (Olay Müdahale Rehberi) çerçeveleri, bu zinciri kırmak için gerekli kontrolleri tanımlar. "Derinlemesine Savunma" (Defense-in-Depth) prensibi uyarınca, her aşama için özelleşmiş tespit (IDS/IPS), engelleme (NGFW) ve analiz (EDR/SIEM) çözümleri entegre edilmelidir.

---

### Cyber Kill Chain: Advanced Threat Modeling and Defense Strategies

The Cyber Kill Chain is a structural framework developed by Lockheed Martin to systematically analyze the stages of a cyber attack. This model defines a seven-stage process that adversaries must complete to achieve their objectives. In modern cybersecurity operations, breaking any link in this chain is sufficient to neutralize the attack.

### Technical Stages and Mechanisms

The Cyber Kill Chain is directly related to the "Adversarial Behaviour" and "Malware & Attack Technologies" knowledge areas within CyBOK (Cyber Security Body of Knowledge). The technical details of the stages are as follows:

1. **Reconnaissance:** The stage where the adversary gathers information about the target. Passive reconnaissance (OSINT, WHOIS records) and active reconnaissance (port scanning, service version detection) techniques are employed.
2. **Weaponization:** Coupling an exploit targeting a discovered vulnerability with a malicious payload. This stage typically occurs within the adversary's infrastructure.
3. **Delivery:** Transmitting the weaponized content to the target. Phishing emails, watering hole attacks, or infected removable media are the primary tools of this stage.
4. **Exploitation:** Triggering a software or hardware vulnerability on the target system to gain unauthorized access. NIST SP 800-115 standards provide methodological guidance for such penetration testing activities.
5. **Installation:** Creating backdoors or registry keys to ensure persistence within the target system.
6. **Command and Control (C2):** The compromised system communicating with an external server to receive instructions. DNS tunneling or HTTP/S-based beaconing signals play a critical role at this stage.
7. **Actions on Objectives:** The final stage where the adversary achieves their ultimate goal, such as data exfiltration, ransomware encryption, or system disruption.

### Defense Strategies and Standards

The ISO/IEC 27035 (Incident Management) and NIST SP 800-61 (Incident Handling Guide) frameworks define the controls necessary to break this chain. According to the "Defense-in-Depth" principle, specialized detection (IDS/IPS), prevention (NGFW), and analysis (EDR/SIEM) solutions must be integrated for each stage.

![](https://miro.medium.com/v2/resize:fit:1200/1*6T2gG0W1Y3E5Q-V6W7A8B9.png)
