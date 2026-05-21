+++
title = "Güç Kaynağı (PSU) ve Enerji Verimliliği | Power Supply (PSU) and Energy Efficiency"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
+++

Güvenlik sadece yazılım değil, sürekliliktir (Availability).

### 1. PSU ve Sistemsel Kararlılık
Kalitesiz bir PSU, ani voltaj dalgalanmalarında donanımın fiziksel olarak hasar görmesine (Physical Denial of Service) yol açabilir. Sunucu odalarında bu risk, **Redundant PSU** (Yedekli Güç Kaynağı) ile minimize edilir.

### 2. UPS (Kesintisiz Güç Kaynağı)
Elektrik kesildiğinde sistemin kontrollü kapanmasını veya çalışmaya devam etmesini sağlar. Veritabanı bütünlüğü (Integrity) için kritiktir; ani kesintiler veri bozulmasına (Corruption) neden olur.

### 3. Side-Channel Attacks (Yan Kanal Saldırıları)
Çok ileri seviye saldırılarda, bir cihazın harcadığı enerji miktarı (Power Analysis) takip edilerek, CPU'nun o an hangi şifreleme anahtarını işlediği tahmin edilebilir.

### 4. Enerji Verimliliği (80 Plus)
Verimlilik sadece maliyet değil, daha az ısı demektir. Aşırı ısınan donanım yavaşlar veya çöker, bu da sistemin erişilebilirliğini (Availability) tehdit eder.

---

## English Version

Security is not just software, it is availability.

### 1. PSU and System Stability
A poor quality PSU may cause physical damage to the hardware (Physical Denial of Service) during sudden voltage fluctuations. In server rooms, this risk is minimized with **Redundant PSU** (Redundant Power Supply).

### 2. UPS (Uninterruptible Power Supply)
It allows the system to shut down or continue operating in a controlled manner when there is a power cut. It is critical for database integrity; Sudden interruptions cause data corruption.

### 3. Side-Channel Attacks
In very advanced attacks, by monitoring the amount of energy consumed by a device (Power Analysis), it can be predicted which encryption key the CPU is currently processing.

### 4. Energy Efficiency (80 Plus)
Efficiency isn't just about cost, it means less heat. Overheating hardware slows down or crashes, threatening system availability.
