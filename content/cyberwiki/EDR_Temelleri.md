+++
title = "EDR (Endpoint Detection and Response)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
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

---

## English Version

EDR is a modern protection system that replaces old-style antiviruses, monitoring any movement inside computers (endpoints) and automatically intervening in a suspicious situation.

### 1. Why is Antivirus Not Enough?
Old antiviruses can only stop viruses (signatures) that they "know". However, modern attackers produce new and never-before-seen (Zero-day) viruses every day. EDR looks at "what the file does" rather than "the name of the file".

### 2. Basic Tasks of EDR
- **Monitoring:** Records every file opening, network connection and command execution on the computer.
- **Detection:** It detects suspicious behavior by saying "This program is doing something it shouldn't normally do, it seems it is a virus."
- **Response:** It can isolate a suspicious computer from the network (cut off its connection with the outside world) with a single click or kill the malicious process instantly.

### 3. Some Terms You Should Know
- **Endpoint:** Any end device (Laptop, server, phone) connected to the network.
- **Behavioral Analysis:** A method of making decisions by looking at what a software does, not what it looks like.
- **Isolation:** Virtually separating an infected computer from the network so that it does not spread the virus to others.
- **Zero-day:** A brand new vulnerability or virus for which no patch or antivirus definition has been released yet.

### 4. Popular Tools
- CrowdStrike, SentinelOne, Carbon Black, Microsoft Defender for Endpoint.

### Real World Analogy
Old antiviruses are like an officer standing at the door looking at the "wanted list" (Signatures) in his hand. If the thief is not on the list, he gets in. EDR, on the other hand, monitors every room in the building and asks, "Why is this man tampering with the lock of the safe?" It is the plainclothes police officer who asks and grabs the thief by the arm.
