+++
title = "Ağ Topolojileri (Mesh, Star, Ring, Bus)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Ağ topolojisi, bir ağdaki cihazların fiziksel veya mantıksal olarak nasıl birbirine bağlandığını ifade eder. Topoloji seçimi ağın performansını, maliyetini ve en önemlisi dayanıklılığını (resiliency) etkiler.

### 1. Yıldız (Star) Topolojisi
Tüm cihazların merkezi bir noktaya (Switch veya Hub) bağlı olduğu yapıdır. Modern yerel ağların (LAN) %99'u bu yapıdadır.
- **Avantaj:** Bir kablo koparsa sadece o cihaz ağdan düşer, geri kalanlar çalışmaya devam eder.
- **Güvenlik:** Merkezi cihaz (Switch) kontrol edilerek tüm ağ trafiği yönetilebilir ve izlenebilir.

### 2. Örgü (Mesh) Topolojisi
Her cihazın diğer tüm cihazlara (Full Mesh) veya bazılarına (Partial Mesh) doğrudan bağlı olduğu yapıdır.
- **Avantaj:** En yüksek dayanıklılık. Bir yol kesilirse alternatif yollar her zaman vardır.
- **Dezavantaj:** Çok pahalı ve karmaşık kablolama.
- **Kullanım Alanı:** Kritik internet omurgaları ve askeri ağlar.

### 3. Halka (Ring) Topolojisi
Verinin cihazdan cihaza bir halka şeklinde iletildiği yapıdır.
- **Dezavantaj:** Halkadaki bir cihaz bozulursa tüm ağ çöker (FDDI gibi teknolojilerle bu sorun yedekli halkalarla aşılmıştır).

### 4. Ortak Yol (Bus) Topolojisi
Tüm cihazların tek bir ana kabloya (omurga) bağlı olduğu eski bir yapıdır.
- **Güvenlik Riski:** Bu topolojide tüm veri ana kablo üzerinden geçer. Bir cihazın trafiği, o kabloya bağlı tüm diğer cihazlar tarafından fiziksel olarak "duyulabilir" (Sniffing için mükemmel ortam).

### Güvenlik Perspektifi: Yedeklilik ve Saldırı Yüzeyi
- **SPOF (Single Point of Failure):** Yıldız topolojisindeki merkezi Switch bir SPOF'tur. O bozulursa tüm ağ gider. Bu yüzden kritik ağlarda yedekli (Redundant) Switch'ler kullanılır.
- **Fiziksel Güvenlik:** Mesh topolojisinde çok fazla bağlantı olduğu için saldırı yüzeyi genişler; her bağlantı noktasının korunması gerekir.

### Gerçek Dünya Analojisi
- **Star:** Bir ofis binasındaki tüm telefonların santrale bağlı olması.
- **Mesh:** Şehirdeki her evin her evle özel bir yolu olması (çok güvenli ama imkansız).
- **Bus:** Eski tip seri bağlı yılbaşı ışıkları; biri sönerse hepsi söner.