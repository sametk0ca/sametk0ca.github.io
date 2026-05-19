+++
title = "STRIDE Framework"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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