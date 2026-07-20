+++
title = "IDS vs IPS (Saldırı Tespit ve Önleme Sistemleri) | IDS vs IPS (Intrusion Detection and Prevention Systems)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Ağ trafiğini izleyen bu sistemler, ağın "güvenlik kameraları" ve "otomatik kapı kilitleri" gibidir. Şüpheli bir hareket gördüklerinde ne yapacaklarına göre birbirlerinden ayrılırlar.

### 1. IDS (Intrusion Detection System - Saldırı Tespit Sistemi)
Sadece izler ve raporlar.
- **Mantık:** Ağ trafiğini kopyalar ve inceler. Zararlı bir paket gördüğünde güvenliğe (SOC ekibine) alarm gönderir.
- **Karakteristik:** Trafiğin "yanında" durur (Out-of-band). Paketi durdurma yetkisi yoktur.
- **Avantajı:** Ağı yavaşlatmaz.

### 2. IPS (Intrusion Prevention System - Saldırı Önleme Sistemi)
İzler, raporlar ve durdurur.
- **Mantık:** Trafiğin tam ortasında durur (Inline). Gelen her paket önce IPS'ten geçer. Zararlı bir şey görürse paketi çöpe atar ve bağlantıyı keser.
- **Karakteristik:** Aktif koruma sağlar.
- **Risk:** Yanlışlıkla (False Positive) gerçek bir müşterinin trafiğini de "saldırı" sanıp engelleyebilir.

### 3. Bilmen Gereken Bazı Terimler
- **Signature-based Detection (İmza Tabanlı):** Bildiği virüslerin "parmak izlerine" bakar. Hızlıdır ama yepyeni virüsleri (Zero-day) kaçırabilir.
- **Anomaly-based Detection (Anomali Tabanlı):** Ağın "normal" halini öğrenir. Normal dışı her şeyi (Örn: Gece yarısı devasa veri transferi) şüpheli bulur.
- **False Positive:** Zararsız bir hareketin "saldırı" sanılması.
- **False Negative:** Gerçek bir saldırının "normal" sanılıp kaçırılması (En tehlikelisi!).

### Gerçek Dünya Analojisi
- **IDS:** Bir binanın her yerini gören bir güvenlik kamerası ve ekran başında oturan bir görevli gibidir. Hırsızı görür, telsizle anons eder ama hırsıza dokunamaz.
- **IPS:** Binanın girişindeki, parmak izi okuyuculu ve dedektörlü otomatik kapı gibidir. Eğer üzerinizde silah (Zararlı kod) varsa kapı kilitlenir ve içeri asla giremezsiniz.

---

## English Version

These systems that monitor network traffic are like the network's "security cameras" and "automatic door locks." They differ from each other in terms of what to do when they see suspicious activity.

### 1. IDS (Intrusion Detection System)
Just monitors and reports.
- **Logic:** Copies and examines network traffic. When it sees a malicious packet, it sends an alarm to security (SOC team).
- **Characteristic:** Stops "next to" traffic (Out-of-band). There is no authority to stop the package.
- **Advantage:** Does not slow down the network.

### 2. IPS (Intrusion Prevention System)
Monitors, reports and stops.
- **Logic:** It stops right in the middle of traffic (Inline). Every incoming packet first passes through IPS. If it sees anything harmful, it throws away the packet and disconnects.
- **Characteristic:** Provides active protection.
- **Risk:** It may mistakenly (False Positive) block the traffic of a real customer, thinking it is an "attack".

### 3. Some Terms You Should Know
- **Signature-based Detection:** It looks at the "fingerprints" of the viruses it knows. It is fast but can miss brand new viruses (Zero-day).
- **Anomaly-based Detection:** Learns the "normal" state of the network. It finds anything out of the ordinary (e.g. massive data transfer in the middle of the night) suspicious.
- **False Positive:** Mistaking a harmless action as an "attack".
- **False Negative:** Mistaking a real attack as "normal" and missing it (The most dangerous thing!).

### Real World Analogy
- **IDS:** It is like a security camera that sees every part of a building and an officer sitting in front of the screen. He sees the thief, announces it via radio, but cannot touch the thief.
- **IPS:** It is like an automatic door with fingerprint reader and detector at the entrance of the building. If you have a weapon (malicious code) on you, the door will be locked and you will never be able to enter.
