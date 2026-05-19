+++
title = "IDS vs IPS (Saldırı Tespit ve Önleme Sistemleri)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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