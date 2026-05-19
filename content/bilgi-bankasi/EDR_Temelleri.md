+++
title = "EDR (Endpoint Detection and Response)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

EDR, eski tip antivirüslerin yerini alan, bilgisayarların (uç noktaların) içindeki her türlü hareketi izleyen ve şüpheli bir durumda otomatik müdahale eden modern bir koruma sistemidir.

### 1. Neden Antivirüs Yetmiyor?
Eski antivirüsler sadece "bildikleri" virüsleri (imzaları) durdurabilirler. Ancak modern saldırganlar her gün yeni ve daha önce hiç görülmemiş (Zero-day) virüsler üretir. EDR, "dosyanın adına" değil, "dosyanın ne yaptığına" bakar.

### 2. EDR'ın Temel Görevleri
- **İzleme:** Bilgisayardaki her dosya açılışını, ağ bağlantısını ve komut çalışmasını kaydeder.
- **Tespit:** "Bu program normalde yapmaması gereken bir şeyi yapıyor, galiba virüs" diyerek şüpheli davranışı yakalar.
- **Yanıt (Response):** Şüpheli bir bilgisayarı tek tıkla ağdan izole edebilir (dış dünya ile bağını kesebilir) veya zararlı süreci anında öldürebilir.

### 3. Bilmen Gereken Bazı Terimler
- **Endpoint (Uç Nokta):** Ağa bağlı olan her türlü son cihaz (Laptop, sunucu, telefon).
- **Behavioral Analysis (Davranışsal Analiz):** Bir yazılımın neye benzediğine değil, ne yaptığına bakarak karar verme yöntemi.
- **Isolation (İzolasyon):** Virüs bulaşmış bir bilgisayarın diğerlerine virüs yaymaması için ağdan sanal olarak koparılması.
- **Zero-day:** Henüz yaması veya antivirüs tanımı çıkmamış, yepyeni bir güvenlik açığı veya virüs.

### 4. Popüler Araçlar
- CrowdStrike, SentinelOne, Carbon Black, Microsoft Defender for Endpoint.

### Gerçek Dünya Analojisi
Eski antivirüsler, kapıda duran ve elindeki "arananlar listesine" (İmzalar) bakan bir görevli gibidir. Eğer hırsız listede yoksa içeri girer. EDR ise bina içindeki her odayı izleyen ve "Bu adam neden kasanın kilidini kurcalıyor?" diye sorup hırsızı kolundan yakalayan sivil polistir.