+++
title = "Cyber Kill Chain (Lockheed Martin) | Cyber ​​Kill Chain (Lockheed Martin)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

Cyber Kill Chain, bir siber saldırının başlangıcından hedefine ulaşana kadar geçtiği 7 aşamayı tanımlayan askeri kökenli bir modeldir. Güvenlik uzmanları saldırıyı ne kadar erken bir aşamada durdururlarsa ("Zinciri kırmak"), o kadar başarılı olurlar.

### 1. Saldırı Aşamaları
1. **Reconnaissance (Keşif):** Saldırgan hedefi araştırır (E-postalar, çalışanlar, sistem açıkları).
2. **Weaponization (Silahlanma):** Bir açığı suistimal edecek virüslü bir dosya (Örn: Virüslü bir PDF) hazırlar.
3. **Delivery (İletme):** Hazırlanan "silahı" kurbana gönderir (E-posta, USB vb.).
4. **Exploitation (Sömürme):** Kurban dosyayı açtığında zafiyet tetiklenir ve saldırgan içeri sızar.
5. **Installation (Yerleşme):** Saldırgan, bilgisayarda kalıcı olabilmek için gizli bir arka kapı (Backdoor) kurur.
6. **Command & Control (C2 - Komuta ve Kontrol):** Saldırgan, kurbanın bilgisayarıyla kendi sunucusu arasında bir iletişim hattı kurar ve uzaktan emir vermeye başlar.
7. **Actions on Objectives (Eylemler):** Saldırgan asıl amacını gerçekleştirir (Veri çalma, dosyaları şifreleme, sistemleri çökertme).

### 2. Neden Önemli?
- Bu model sayesinde saldırganın hangi aşamada olduğunu anlayabilir ve zincirin herhangi bir halkasını kırarak tüm saldırıyı bozabiliriz.

### 3. Bilmen Gereken Bazı Terimler
- **Indicator of Compromise (IoC):** Bir saldırının gerçekleştiğine dair kanıtlar (Örn: Belirli bir IP adresi veya virüslü dosya ismi).
- **Backdoor:** Sisteme sonradan gizlice girmek için kurulan kapı.
- **Exfiltration:** Çalınan verilerin sistem dışına çıkarılması işlemi.

### Gerçek Dünya Analojisi
Bir banka soygununu düşünün:
1. Bankanın planını inceleme (Keşif).
2. Maske ve silah hazırlama (Silahlanma).
3. Bankaya gitme (İletme).
4. Kapıyı kırıp içeri girme (Sömürme).
5. Kasanın başında bekleyen görevliyi etkisiz hale getirme (Yerleşme).
6. Arkadaşlarıyla telsizle konuşma (Komuta Kontrol).
7. Paraları çantaya doldurup kaçma (Eylem).
Polis bu aşamalardan herhangi birinde (Örn: Bankaya giderken) hırsızı yakalarsa soygun engellenmiş olur.

---

## English Version

Cyber ​​Kill Chain is a model of military origin that describes 7 stages that a cyber attack goes through from its inception until it reaches its target. The earlier security experts stop the attack ("Breaking the chain"), the more successful they will be.

### 1. Attack Phases
1. **Reconnaissance:** The attacker investigates the target (E-mails, employees, system vulnerabilities).
2. **Weaponization:** Prepares an infected file (Ex: An infected PDF) to exploit a vulnerability.
3. **Delivery:** Sends the prepared "weapon" to the victim (E-mail, USB, etc.).
4. **Exploitation:** When the victim opens the file, the vulnerability is triggered and the attacker infiltrates.
5. **Installation:** The attacker establishes a secret backdoor in order to remain permanently on the computer.
6. **Command & Control (C2):** The attacker establishes a communication line between the victim's computer and his own server and starts giving orders remotely.
7. **Actions on Objectives:** The attacker achieves his main goal (stealing data, encrypting files, crashing systems).

### 2. Why is it important?
- Thanks to this model, we can understand at what stage the attacker is and disrupt the entire attack by breaking any link in the chain.

### 3. Some Terms You Should Know
- **Indicator of Compromise (IoC):** Evidence that an attack has occurred (E.g. a specific IP address or infected file name).
- **Backdoor:** The door installed to secretly enter the system later.
- **Exfiltration:** The process of removing stolen data from the system.

### Real World Analogy
Consider a bank robbery:
1. Examining the bank's plan (Reconnaissance).
2. Preparing masks and weapons (Armament).
3. Going to the bank (Forwarding).
4. Breaking the door and entering (Exploitation).
5. Disabling the officer waiting at the cash register (Settlement).
6. Talking to friends via radio (Command and Control).
7. Put the money in the bag and run away (Action).
If the police catch the thief at any of these stages (e.g. going to the bank), the robbery is prevented.
