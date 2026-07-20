+++
title = "XDR (Extended Detection and Response)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

XDR, siber güvenliğin "süper kahramanı"dır. EDR'ın (bilgisayar izleme) yaptığı işi alıp; ağ trafiği, e-postalar, bulut sistemleri ve kullanıcı kimlikleriyle birleştirerek tüm tabloyu tek bir yerden yöneten sistemdir.

### 1. Neden XDR'a İhtiyaç Var?
Saldırganlar sadece bilgisayara saldırmaz. Önce bir oltalama e-postası atar (Email), sonra şifrenizi çalar (Identity), sonra bilgisayara sızar (Endpoint) ve en son verileri dışarı sızdırır (Network). 
- **Eski Sorun:** Her bir savunma aracı kendi başına çalışıyordu (Silo yapısı). 
- **XDR Çözümü:** Tüm bu parçaları birbirine bağlar ve saldırının hikayesini baştan sona tek bir ekran üzerinden anlatır.

### 2. XDR'ın Avantajları
- **Görünürlük:** Sistemin hiçbir kör noktası kalmaz.
- **Hız:** Farklı araçlardan gelen verileri otomatik birleştirdiği için saldırıyı tespit etme süresi çok kısalır.
- **Otomasyon:** Bir saldırı tespit edildiğinde, XDR otomatik olarak e-postayı silebilir, kullanıcının şifresini sıfırlayabilir ve bilgisayarı ağdan atabilir.

### 3. Bilmen Gereken Bazı Terimler
- **Silos (Silolar):** Birbirinden kopuk, haberleşmeyen güvenlik sistemleri. XDR bunları yok eder.
- **TTP (Tactics, Techniques, and Procedures):** Saldırganların izlediği yollar. XDR bu yolları çok daha geniş bir çerçevede görür.
- **Telemetry:** Sistemlerin ürettiği her türlü veri akışı. XDR bu telemetri verileriyle beslenir.

### Gerçek Dünya Analojisi
EDR sadece evin içindeki kameraysa, XDR; mahallenin girişindeki plaka okuma sistemi, komşuların güvenlik kameraları, sizin telefonunuzdaki banka bildirimleri ve evdeki alarm sisteminin hepsinin aynı merkeze bağlı olması gibidir. Hırsız daha mahalleye girdiğinde (E-posta aşaması) sistem onu fark eder ve siz daha eve gelmeden önlemini alır.

---

## English Version

XDR is the “superhero” of cybersecurity. Take the work done by EDR (computer monitoring); It is a system that manages the entire table from a single place by combining network traffic, e-mails, cloud systems and user identities.

### 1. Why is XDR Needed?
Attackers don't just attack the computer. First it sends a phishing email (Email), then it steals your password (Identity), then it infiltrates the computer (Endpoint) and finally it exfiltrates the data (Network). 
- **Old Problem:** Each defense tool was running on its own (Silo structure). 
- **XDR Solution:** It connects all these parts and tells the story of the attack from start to finish on a single screen.

### 2. Advantages of XDR
- **Visibility:** The system has no blind spots.
- **Speed:** Since it automatically combines data from different tools, the time to detect the attack is very short.
- **Automation:** When an attack is detected, XDR can automatically delete the email, reset the user's password, and kick the computer off the network.

### 3. Some Terms You Should Know
- **Silos:** Security systems that are disconnected from each other and do not communicate. XDR destroys these.
- **TTP (Tactics, Techniques, and Procedures):** Routes followed by attackers. XDR sees these pathways in a much broader context.
- **Telemetry:** All kinds of data flows produced by systems. XDR is fed with this telemetry data.

### Real World Analogy
If EDR is just the camera inside the house, XDR; It is like the license plate reading system at the entrance of the neighborhood, the neighbors' security cameras, the bank notifications on your phone and the alarm system at home all connected to the same center. As soon as the thief enters the neighborhood (E-mail phase), the system notices him and takes precautions before you even get home.
