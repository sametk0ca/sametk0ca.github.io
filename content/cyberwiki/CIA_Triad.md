+++
title = "CIA Triad (Gizlilik, Bütünlük, Erişilebilirlik) | CIA Triad (Confidentiality, Integrity, Availability)"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
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

---

## English Version

The CIA Triad is the “Holy Trinity” of cybersecurity. It is the basic model used to measure how secure a system or data is.

### 1. Confidentiality
It is to ensure that the data can only be seen by authorized persons.
- **Threat:** Data leaks, shoulder surfing, password theft.
- **Solution:** Encryption, access control lists (ACL), two-factor authentication (MFA).
- **Analogy:** Putting a letter in a sealed envelope. Only the recipient can open and read the envelope.

### 2. Integrity
It is to ensure that the accuracy of the data is maintained and that it is not changed by unauthorized persons.
- **Threat:** Alteration of data en route, database manipulation.
- **Solution:** Digital signatures, Hashing algorithms, version control.
- **Analogy:** The number on a check is written in writing next to it to prevent it from being changed later, or the bank verifies that check.

### 3. Availability
The system and data are available to authorized users whenever needed.
- **Threat:** DoS/DDoS attacks, power outages, hardware failures.
- **Solution:** Redundancy, uninterruptible power supplies (UPS), DDoS protection services.
- **Analogy:** Emergency service (112) phones are always available. If the lines are busy or not working, "accessibility" is impaired.

### Critical Note: A Matter of Balance
In cyber security, it is always necessary to establish a balance between these three. For example, you encrypt a data so much (Confidentiality) that it takes hours to open and the user cannot access it in time (Accessibility is broken).

### Some Terms You Should Know
- **Shoulder Surfing:** The act of stealing and stealing someone's password while they are entering it.
- **Hashing:** It is the process of converting a data into a unique mathematical fingerprint. If the data changes even by one letter, the hash changes completely; This allows us to check the "integrity".
- **Redundancy:** Having more than one of the same part so that the system does not stop when a part breaks down (Ex: Dual power supply).
