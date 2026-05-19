+++
title = "CIA Triad (Gizlilik, Bütünlük, Erişilebilirlik)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

CIA Triad, siber güvenliğin "Kutsal Üçlüsü"dür. Bir sistemin veya verinin ne kadar güvende olduğunu ölçmek için kullanılan temel modeldir.

### 1. Confidentiality (Gizlilik)
Verinin sadece yetkili kişiler tarafından görülmesini sağlamaktır.
- **Tehdit:** Veri sızıntıları, omuz üzerinden bakma (shoulder surfing), şifre çalma.
- **Çözüm:** Şifreleme (Encryption), erişim kontrol listeleri (ACL), iki faktörlü doğrulama (MFA).
- **Analoji:** Bir mektubu mühürlü bir zarfa koymak. Sadece alıcı zarfı açıp okuyabilir.

### 2. Integrity (Bütünlük)
Verinin doğruluğunun korunması ve yetkisiz kişilerce değiştirilmemesini sağlamaktır.
- **Tehdit:** Verinin yolda değiştirilmesi, veritabanı manipülasyonu.
- **Çözüm:** Dijital imzalar, Hashing algoritmaları, versiyon kontrolü.
- **Analoji:** Bir çekin üzerindeki rakamın sonradan değiştirilmemesi için yanına yazı ile de yazılması veya bankanın o çeki doğrulaması.

### 3. Availability (Erişilebilirlik)
Sistemin ve verinin ihtiyaç duyulduğu her an yetkili kullanıcılara açık olmasıdır.
- **Tehdit:** DoS/DDoS saldırıları, elektrik kesintileri, donanım arızaları.
- **Çözüm:** Yedekli sistemler (Redundancy), kesintisiz güç kaynakları (UPS), DDoS koruma servisleri.
- **Analoji:** Acil servisin (112) telefonlarının her zaman ulaşılabilir olması. Eğer hatlar meşgulse veya çalışmıyorsa "erişilebilirlik" bozulmuş demektir.

### Kritik Not: Denge Meselesi
Siber güvenlikte bu üçü arasında her zaman bir denge kurmak gerekir. Örneğin, bir veriyi o kadar çok şifrelersiniz ki (Gizlilik), açılması saatler sürer ve kullanıcı ona zamanında ulaşamaz (Erişilebilirlik bozulur).

### Bilmen Gereken Bazı Terimler
- **Shoulder Surfing:** Birinin şifresini girerken arkasından gizlice bakıp çalma eylemi.
- **Hashing:** Bir veriyi benzersiz bir matematiksel parmak izine dönüştürme işlemidir. Veri bir harf bile değişse hash tamamen değişir; bu da "bütünlüğü" kontrol etmemizi sağlar.
- **Redundancy (Yedeklilik):** Bir parça bozulduğunda sistemin durmaması için aynı parçadan birden fazla bulundurma (Örn: Çift güç kaynağı).