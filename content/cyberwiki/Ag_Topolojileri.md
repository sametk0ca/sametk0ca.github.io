+++
title = "Ağ Topolojileri (Mesh, Star, Ring, Bus) | Network Topologies (Mesh, Star, Ring, Bus)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

Network topology refers to how devices in a network are connected to each other physically or logically. Topology selection affects the performance, cost and most importantly the resilience of the network.

### 1. Star Topology
It is a structure in which all devices are connected to a central point (Switch or Hub). 99% of modern local networks (LANs) have this structure.
- **Advantage:** If a cable breaks, only that device falls off the network, the rest continue to work.
- **Security:** All network traffic can be managed and monitored by controlling the central device (Switch).

### 2. Mesh Topology
It is a structure in which each device is directly connected to all other devices (Full Mesh) or some (Partial Mesh).
- **Advantage:** Highest durability. If a road is cut off, there are always alternative routes.
- **Disadvantage:** Very expensive and complicated wiring.
- **Use Area:** Critical internet backbones and military networks.

### 3. Ring Topology
It is the structure in which data is transmitted from device to device in the form of a ring.
- **Disadvantage:** If a device on the ring fails, the entire network collapses (with technologies such as FDDI, this problem has been overcome with redundant rings).

### 4. Bus Topology
It is an old structure where all devices are connected to a single main cable (backbone).
- **Security Risk:** In this topology, all data passes over the main cable. A device's traffic can be physically "heard" by all other devices connected to that cable (perfect medium for Sniffing).

### Security Perspective: Redundancy and Attack Surface
- **SPOF (Single Point of Failure):** The central Switch in the star topology is a SPOF. If that goes down, the whole network is gone. That's why redundant switches are used in critical networks.
- **Physical Security:** Since there are many connections in the mesh topology, the attack surface expands; Every port needs to be protected.

### Real World Analogy
- **Star:** All phones in an office building are connected to the switchboard.
- **Mesh:** Every house in the city has a private path with every house (very safe but impossible).
- **Bus:** Old type series connected Christmas lights; If one goes out, all go out.
