+++
title = "XDR (Extended Detection and Response)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "bilgi-bankasi"
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