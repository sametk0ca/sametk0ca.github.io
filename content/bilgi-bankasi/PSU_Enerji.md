+++
title = "Güç Kaynağı (PSU) ve Enerji Verimliliği"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
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