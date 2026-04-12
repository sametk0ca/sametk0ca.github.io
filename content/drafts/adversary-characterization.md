---
title: "Adversary Characterization: Tehdit Aktörlerinin Analizi ve TTP Modelleme"
date: 2026-04-11
draft: true
tags: ["Cyber Security", "Threat Intel", "Adversary Characterization", "CyBOK"]
categories: ["Knowledge Base"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png"
    alt: "Adversary Characterization"
    relative: false
---

![](https://miro.medium.com/v2/resize:fit:1200/1*b_Xb-V7i-e_7n06yG9vWyg.png)

Siber tehdit istihbaratı (CTI) dünyasında, bir saldırıyı anlamak sadece kullanılan zararlı yazılımı bilmekten ibaret değildir. **Adversary Characterization (Saldırgan Karakterizasyonu)**, saldırganın motivasyonunu, kapasitesini, niyetini ve kullandığı metodolojileri (TTPs - Tactics, Techniques, and Procedures) sistematik bir şekilde tanımlama sürecidir. Bu süreç, savunma stratejilerinin "reaktif" bir yapıdan "proaktif" bir yapıya geçmesini sağlar.

### Analitik Modeller ve Metodolojiler

Saldırgan davranışlarının karakterizasyonu, CyBOK "Adversarial Behaviour" bilgi alanı çerçevesinde çeşitli analitik modeller aracılığıyla gerçekleştirilir:

1. **Diamond Model:** Bir saldırı olayını dört temel köşe (Adversary, Infrastructure, Capability, Victim) üzerinden analiz eder. Bu köşeler arasındaki ilişkiler, saldırganın operasyonel mantığını ortaya koyar.
2. **TTP Analizi:** Saldırganın taktik (amaç), teknik (yöntem) ve prosedür (adım adım uygulama) hiyerarşisini tanımlar. MITRE ATT&CK matrisi, bu TTP'lerin standardize edilmiş bir kütüphanesi olarak kullanılır.
3. **Saldırgan Profilleme:** Tehdit aktörlerini motivasyonlarına göre (Nation-State, Cyber-Criminal, Hacktivist) sınıflandırır. Bu sınıflandırma, potansiyel hedef seçimi ve saldırı şiddeti hakkında öngörü sağlar.

### Standartlar ve Teknik Zorluklar

NIST SP 800-150 (Guide to Cyber Threat Information Sharing) standardı, tehdit bilgisinin nasıl karakterize edileceği ve paydaşlar arasında nasıl paylaşılacağı konusunda rehberlik sunar. Ancak, karakterizasyon sürecinde "Attribution" (Atıf Yapma) problemi, saldırganların "False Flag" operasyonları ve gelişmiş gizleme teknikleri nedeniyle en büyük teknik zorluklardan biri olarak kalmaktadır. Gelişmiş saldırganlar, kendi izlerini silmek için "Living off the Land" (LotL) tekniklerini kullanarak meşru sistem araçlarını istismar ederler.

---

### Adversary Characterization: Analysis of Threat Actors and TTP Modeling

In the world of Cyber Threat Intelligence (CTI), understanding an attack is not merely about knowing the malware used. **Adversary Characterization** is the process of systematically defining an attacker's motivation, capability, intent, and the methodologies they employ (TTPs - Tactics, Techniques, and Procedures). This process enables defense strategies to transition from a "reactive" to a "proactive" stance.

### Analytical Models and Methodologies

Characterization of adversarial behavior is performed through various analytical models within the framework of the CyBOK "Adversarial Behaviour" knowledge area:

1. **Diamond Model:** Analyzes an attack event across four fundamental vertices: Adversary, Infrastructure, Capability, and Victim. The relationships between these vertices reveal the attacker's operational logic.
2. **TTP Analysis:** Defines the hierarchy of an attacker's tactics (objective), techniques (method), and procedures (step-by-step implementation). The MITRE ATT&CK matrix serves as a standardized library for these TTPs.
3. **Adversary Profiling:** Categorizes threat actors based on their motivations (Nation-State, Cyber-Criminal, Hacktivist). This categorization provides insights into potential target selection and attack severity.

### Standards and Technical Challenges

The NIST SP 800-150 (Guide to Cyber Threat Information Sharing) standard provides guidance on how to characterize threat information and share it among stakeholders. However, the problem of "Attribution" remains one of the greatest technical challenges in the characterization process due to "False Flag" operations and advanced obfuscation techniques employed by adversaries. Sophisticated attackers exploit legitimate system tools using "Living off the Land" (LotL) techniques to erase their tracks.
