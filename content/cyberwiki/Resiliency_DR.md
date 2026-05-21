+++
title = "Resiliency ve Olağanüstü Durum Kurtarma (DR) | Resiliency and Disaster Recovery (DR)"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
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

---

## English Version

Just taking a backup is not enough; It is also vital how quickly things return to normal in the event of a disaster. In this field, the concepts of "Resiliency" and "Disaster Recovery" come to the fore.

### 1. Resiliency
It is the ability of the system to continue working even when it receives an impact.
- **Logic:** If one part breaks down, the other one comes into play (Fault Tolerance). There will be no interruption.

### 2. DR (Disaster Recovery)
It is the process of restoring the system after a major disaster (earthquake, cyber war, data center explosion).

### 3. The Two Most Critical Terms You Need to Know (RTO & RPO)
These two terms determine how much loss a company can tolerate:
- **RTO (Recovery Time Objective):** "How long should I get up?" is the answer to the question. Determines the duration of the interruption. (Ex: If the RTO is 4 hours, the system must be operational within 4 hours).
- **RPO (Recovery Point Objective):** "How much data loss can I tolerate?" is the answer to the question. It depends on when you last took a backup. (Ex: If the RPO is 1 day, you only risk losing the last 24 hours of data).

### 4. Data Center Models
- **Hot Site:** It is the place where copies of everything (server, data, staff desk) are ready. In case of a disaster, you can reach here within minutes. It is very expensive.
- **Warm Site:** The infrastructure is ready, but it takes a few hours to load the final data. It is medium cost.
- **Cold Site:** There is only an empty room, electricity and internet line. It can take days to bring in and set up servers. It is cheap.

### 5. Some Terms You Should Know
- **Fault Tolerance:** Ability to continue working without any interruption when a fault occurs in the system.
- **High Availability (HA):** The target for the system to remain open 99.99% of the year (Four Nines).
- **Business Continuity:** The plan for the continuation of all operations of the company, not only technical but also where the personnel will work.

### Real World Analogy
- **Resiliency:** When your car's tire bursts, the spare tire is ready and you can continue your journey immediately.
- **Disaster Recovery:** Your car is completely burned and you buy a new car from the insurance and continue on your way. Here, RTO is the time you wait for the new car, while RPO is how old your belongings are in the burned car.
