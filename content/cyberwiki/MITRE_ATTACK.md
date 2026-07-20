+++
title = "MITRE ATTCK Framework Kullanımı | Using MITER ATTCK Framework"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

MITER ATT&CK is a huge, constantly updated knowledge base and roadmap that lists all the tactics and techniques used by attackers during an attack.

### 1. ATT&CK Matrix
It presents the steps followed by the attacker in a tabular form, from top to bottom (Tactics) and to the right (Techniques).
- **Tactics:** Tells "Why" the attacker did what he did. (Ex: Infiltrating the network, stealing information).
- **Techniques:** It tells "How" the attacker performs this tactic. (Ex: Infiltration with Phishing, using SQL Injection).

### 2. Why is it used?
- **Analysis:** When an attack occurs, "What stage is the attacker at now?" We can answer the question by looking at this matrix.
- **Defense:** "Which of these techniques are we vulnerable to?" We can close our shortcomings by saying:
- **Knowing the Enemy:** Allows us to learn which techniques certain hacker groups (APT) like.

### 3. Some Terms You Should Know
- **APT (Advanced Persistent Threat):** Very professional and long-lasting cyber attack groups, usually supported by a state.
- **Matrix:** Large table in ATT&CK. (There are separate matrices for Windows and separate matrices for Mobile).
- **Sub-techniques:** Lower and special versions of a technique.

### Real World Analogy
MITER ATT&CK is like an "opponent analysis report" in the hands of a football coach. He writes in full detail how the opponent uses corner kicks (Tactics) and which player runs where (Technical). You look at this report and build your defense accordingly.
