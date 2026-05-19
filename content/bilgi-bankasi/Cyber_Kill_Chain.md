+++
title = "Cyber Kill Chain (Lockheed Martin)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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