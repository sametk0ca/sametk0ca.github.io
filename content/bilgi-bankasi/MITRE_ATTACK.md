+++
title = "MITRE ATTCK Framework Kullanımı"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

MITRE ATT&CK, saldırganların bir saldırı sırasında kullandığı tüm taktik ve tekniklerin listelendiği, sürekli güncellenen devasa bir bilgi bankası ve yol haritasıdır.

### 1. ATT&CK Matrisi
Saldırganın izlediği adımları yukarıdan aşağıya (Taktikler) ve sağa doğru (Teknikler) bir tablo şeklinde sunar.
- **Taktikler (Tactics):** Saldırganın "Neden" yaptığını söyler. (Örn: Ağa sızmak, Bilgi çalmak).
- **Teknikler (Techniques):** Saldırganın bu taktiği "Nasıl" gerçekleştirdiğini söyler. (Örn: Phishing ile sızmak, SQL Injection kullanmak).

### 2. Neden Kullanılır?
- **Analiz:** Bir saldırı olduğunda "Saldırgan şu an hangi aşamada?" sorusunu bu matrise bakarak yanıtlayabiliriz.
- **Savunma:** "Biz bu tekniklerden hangilerine karşı korumasızız?" diyerek eksiklerimizi kapatabiliriz.
- **Düşmanı Tanıma:** Belirli hacker gruplarının (APT) hangi teknikleri sevdiğini öğrenmemizi sağlar.

### 3. Bilmen Gereken Bazı Terimler
- **APT (Advanced Persistent Threat):** Genellikle bir devlet tarafından desteklenen, çok profesyonel ve uzun süreli siber saldırı grupları.
- **Matrix:** ATT&CK içindeki büyük tablo. (Windows için ayrı, Mobil için ayrı matrisler vardır).
- **Sub-techniques:** Bir tekniğin daha alt ve özel halleri.

### Gerçek Dünya Analojisi
MITRE ATT&CK, bir futbol teknik direktörünün elindeki "rakip analiz raporu" gibidir. Rakibin köşe vuruşlarını (Taktik) nasıl kullandığını, hangi oyuncunun nereye koştuğunu (Teknik) tüm detaylarıyla yazar. Siz de bu rapora bakarak defansınızı (Savunma) ona göre kurarsınız.