+++
title = "Resiliency ve Olağanüstü Durum Kurtarma (DR)"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "bilgi-bankasi"
+++

Sadece yedek almak yetmez; bir felaket anında işlerin ne kadar hızlı normale döneceği de hayatidir. Bu alanda "Dayanıklılık" (Resiliency) ve "Felaket Kurtarma" (Disaster Recovery) kavramları öne çıkar.

### 1. Resiliency (Dayanıklılık)
Sistemin bir darbe aldığında bile çalışmaya devam edebilme yeteneğidir.
- **Mantık:** Bir parça bozulursa diğeri devreye girer (Fault Tolerance). Kesinti yaşanmaz.

### 2. DR (Disaster Recovery - Felaket Kurtarma)
Büyük bir felaket (Deprem, siber savaş, veri merkezi patlaması) sonrası sistemin yeniden ayağa kaldırılması sürecidir.

### 3. Bilmen Gereken En Kritik İki Terim (RTO & RPO)
Bu iki terim, bir şirketin ne kadar kayba tahammülü olduğunu belirler:
- **RTO (Recovery Time Objective):** "Ne kadar sürede ayağa kalkmalıyım?" sorusunun yanıtıdır. Kesintinin süresini belirler. (Örn: RTO 4 saat ise, sistem 4 saat içinde çalışır hale gelmeli).
- **RPO (Recovery Point Objective):** "Ne kadar veri kaybına tahammülüm var?" sorusunun yanıtıdır. En son ne zaman yedek aldığınızla ilgilidir. (Örn: RPO 1 gün ise, sadece son 24 saatlik veriyi kaybetmeyi göze alıyorsunuz demektir).

### 4. Veri Merkezi Modelleri
- **Hot Site:** Her şeyin kopyasının (sunucu, veri, personel masası) hazır beklediği yerdir. Bir felaket anında dakikalar içinde buraya geçilebilir. Çok pahalıdır.
- **Warm Site:** Altyapı hazırdır ancak verilerin son halinin yüklenmesi birkaç saat sürer. Orta maliyetlidir.
- **Cold Site:** Sadece boş bir oda, elektrik ve internet hattı vardır. Sunucuları getirip kurmak günler sürebilir. Ucuzdur.

### 5. Bilmen Gereken Bazı Terimler
- **Fault Tolerance:** Sistemdeki bir hata (fault) oluştuğunda hiç kesinti yaşanmadan çalışmaya devam edebilmesi.
- **High Availability (HA):** Sistemin yılın %99.99'unda (Dört Dokuz) açık kalması hedefi.
- **Business Continuity (İş Sürekliliği):** Sadece teknik değil, personelin nerede çalışacağı gibi şirketin tüm operasyonlarının devam etmesi planı.

### Gerçek Dünya Analojisi
- **Resiliency:** Arabanızın lastiği patladığında stepnenin hazır olması ve yolunuza hemen devam etmeniz.
- **Disaster Recovery:** Arabanızın tamamen yanması ve kaskodan yeni bir araba alıp yola devam etmeniz. RTO burada yeni arabayı bekleme sürenizdir, RPO ise yanan arabadaki eşyalarınızın ne kadar eski olduğudur.