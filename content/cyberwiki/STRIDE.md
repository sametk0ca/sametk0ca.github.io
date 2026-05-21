+++
title = "STRIDE Framework"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

STRIDE, Microsoft tarafından geliştirilen ve sistemlerdeki potansiyel güvenlik tehditlerini sınıflandırmak için kullanılan bir tehdit modelleme metodolojisidir.

### Özet
STRIDE, ismini altı farklı tehdit kategorisinin baş harflerinden alır. Geliştiricilerin "Ne yanlış gidebilir?" sorusuna yapılandırılmış bir cevap vermesine yardımcı olur.

### Teknik Detaylar
- **S (Spoofing):** Başkasının kimliğini taklit etme (örn: sahte kullanıcı girişi).
- **T (Tampering):** Veriyi yetkisiz değiştirme (örn: veritabanı manipülasyonu).
- **R (Repudiation):** Yapılan bir eylemi inkar etme (örn: logların silinmesi).
- **I (Information Disclosure):** Hassas verilerin sızdırılması (örn: config dosyası sızıntısı).
- **D (Denial of Service):** Sistemin hizmet veremez hale getirilmesi.
- **E (Elevation of Privilege):** Yetki yükseltme (örn: normal kullanıcının admin olması).

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Tasarım Aşamasında Uygulayın:** Kod yazılmadan önce mimari üzerinde STRIDE analizi yapın.
- **Veri Akış Diyagramları (DFD):** Sistemin bileşenlerini ve veri akışını çizerek tehditleri bu akışlar üzerinde arayın.
- **Önceliklendirme:** Tespit edilen tehditleri risk puanına göre sıralayın.

---

## English Version

STRIDE is a threat modeling methodology developed by Microsoft and used to classify potential security threats in systems.

### Summary
STRIDE takes its name from the initials of six different threat categories. Developers' "What could go wrong?" It helps to give a structured answer to the question.

### Technical Details
- **S (Spoofing):** Impersonating someone else's identity (e.g. fake user login).
- **T (Tampering):** Unauthorized modification of data (e.g. database manipulation).
- **R (Repudiation):** Denying an action taken (eg: deleting logs).
- **I (Information Disclosure):** Leak of sensitive data (eg: config file leak).
- **D (Denial of Service):** Making the system unserviceable.
- **E (Elevation of Privilege):** Elevation of privilege (eg: normal user becomes admin).

### Security Approach and Best Practices
- **Apply in Design Phase:** Perform STRIDE analysis on the architecture before the code is written.
- **Data Flow Diagrams (DFD):** Draw the components of the system and the data flow and look for threats on these flows.
- **Prioritization:** Sort detected threats by risk score.
