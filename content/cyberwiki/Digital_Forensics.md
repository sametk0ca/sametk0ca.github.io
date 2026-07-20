+++
title = "Digital Forensics (Adli Bilişim) | Digital Forensics"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Digital Forensics, dijital cihazlarda (bilgisayar, telefon, sunucu) meydana gelen olayların kanuni olarak kabul edilebilir kanıtlarını toplama, koruma, analiz etme ve raporlama sürecidir. Siber güvenlikte bir saldırının "nasıl" ve "ne zaman" gerçekleştiğini anlamak için kullanılır.

### 1. Adli Bilişimin Temel Aşamaları
1. **Muhafaza (Preservation):** Kanıtların bozulmaması için cihazın imajı alınır. Orijinal disk üzerinde asla çalışma yapılmaz.
2. **Tanımlama (Identification):** Hangi cihazların ve verilerin inceleneceği belirlenir.
3. **Analiz (Analysis):** Silinmiş dosyalar, internet geçmişi, kayıt defteri girdileri ve bellek dökümleri incelenir.
4. **Raporlama (Reporting):** Bulguların teknik olmayan bir dille, kanıtlarıyla birlikte sunulması.

### 2. Disk Forensics (Disk Analizi)
Sabit diskler, SSD'ler veya USB bellekler üzerindeki verilerin incelenmesidir.
- **Write Blocker:** Diske veri yazılmasını fiziksel olarak engelleyen cihazdır. Kanıt bütünlüğünü korur.
- **Disk İmajı (Bit-stream Image):** Diskin her bir sektörünün (boş alanlar dahil) birebir kopyasıdır. `.ad1`, `.e01` veya `.raw` formatlarında olabilir.
- **Timeline Analizi:** Dosyaların ne zaman oluşturulduğu, değiştirildiği veya erişildiği kronolojik olarak dizilir (MAC times: Modification, Access, Creation).

### 3. Memory Forensics (Bellek Analizi)
Bilgisayarın RAM'indeki verilerin incelenmesidir. RAM, bilgisayar kapandığında silindiği için (volatile) canlı müdahale sırasında ilk toplanması gereken kanıttır.
- **Neden Önemlidir?** Bazı gelişmiş zararlı yazılımlar sadece RAM'de çalışır (fileless malware). Şifreli disklerin anahtarları veya aktif ağ bağlantıları sadece RAM'den okunabilir.
- **Araçlar:** Bellek analizinde dünya standardı **Volatility** aracıdır.

### 4. Temel Kavramlar
- **Chain of Custody (Zapturapt Altında Tutma):** Kanıtın ele geçirildiği andan mahkemeye kadar kimlerin elinden geçtiğinin belgelenmesidir.
- **Hash Değeri:** Bir dosyanın veya disk imajının dijital parmak izidir (MD5, SHA-1). İmaj alındıktan sonra hash değeri hesaplanır; eğer analiz sırasında bu değer değişirse kanıt geçersiz sayılır.

### Gerçek Dünya Analojisi
Digital Forensics, bir cinayet mahalline gelen olay yeri inceleme ekibi gibidir. Polisler (Adli Bilişim Uzmanları), yerdeki parmak izlerini (Loglar), kurbanın son aradığı kişileri (Bellek) ve katilin düşürdüğü eşyaları (Silinmiş dosyalar) toplar. En önemli kural şudur: "Olay yerindeki hiçbir şeye çıplak elle dokunma" (Yani orijinal diske müdahale etme, imajını al).

---

## English Version

Digital Forensics is the process of collecting, preserving, analyzing and reporting legally acceptable evidence of events occurring on digital devices (computer, phone, server). It is used in cybersecurity to understand "how" and "when" an attack occurs.

### 1. Basic Stages of Computer Forensics
1. **Preservation:** An image of the device is taken to prevent damage to the evidence. No work is ever done on the original disc.
2. **Identification:** It is determined which devices and data will be examined.
3. **Analysis:** Deleted files, internet history, registry entries and memory dumps are examined.
4. **Reporting:** Presenting the findings together with their evidence in a non-technical language.

### 2. Disk Forensics (Disk Analysis)
It is the examination of data on hard disks, SSDs or USB sticks.
- **Write Blocker:** It is a device that physically prevents data from being written to the disk. Maintains the integrity of evidence.
- **Disk Image (Bit-stream Image):** It is an exact copy of each sector of the disk (including free areas). It can be in `.ad1`, `.e01` or `.raw` formats.
- **Timeline Analysis:** When files were created, modified or accessed is listed chronologically (MAC times: Modification, Access, Creation).

### 3. Memory Forensics
It is the examination of data in the computer's RAM. Since RAM is volatile when the computer is turned off, it is the first evidence to be collected during live intervention.
- **Why is it important?** Some advanced malware runs only in RAM (fileless malware). Keys to encrypted disks or active network connections can only be read from RAM.
- **Tools:** The world standard in memory analysis is the **Volatility** tool.

### 4. Basic Concepts
- **Chain of Custody:** It is the documentation of whose hands the evidence passed from the moment it was seized until the court.
- **Hash Value:** It is the digital fingerprint (MD5, SHA-1) of a file or disk image. After the image is received, the hash value is calculated; If this value changes during analysis, the evidence is considered invalid.

### Real World Analogy
Digital Forensics is like a crime scene investigation team arriving at a murder scene. Police (Forensic Computer Experts) collect fingerprints on the ground (Logs), last contacts of the victim (Memory) and items dropped by the killer (Deleted files). The most important rule is: "Do not touch anything at the scene with bare hands" (i.e. do not tamper with the original disk, take its image).
