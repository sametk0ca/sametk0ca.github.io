+++
title = "NFC (Near Field Communication) Mekanizması"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Hardware"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

NFC, 4-10 cm gibi çok kısa mesafelerde çalışan bir radyo frekans teknolojisidir. Temassız ödemeler, akıllı kartlar ve kimlik doğrulama için kullanılır.

### 1. Çalışma Modları
- **Reader/Writer:** Cihaz bir etiketi okur (Örn: otobüs kartı okuma).
- **Peer-to-Peer:** İki cihaz veri paylaşır (Örn: telefonlar arası dosya transferi).
- **Card Emulation:** Telefonun bir kredi kartı gibi davranması (Örn: Apple Pay / Google Pay).

### 2. Güvenlik Riskleri
- **Eavesdropping (Dinleme):** Mesafe kısa olsa da, hassas antenlerle NFC sinyali birkaç metre öteden yakalanabilir. Veri şifrelenmemişse (Örn: bazı eski toplu taşıma kartları) bilgiler çalınabilir.
- **Data Modification:** Saldırgan, araya girerek gönderilen veriyi bozabilir veya değiştirebilir.
- **Relay Attack (Röle Saldırısı):** En tehlikeli olanıdır. Saldırgan kurbanın NFC sinyalini yakalar ve internet üzerinden başka bir yerdeki ödeme terminaline ileterek kurbanın kartından harcama yapar.

### 3. Korunma
NFC iletişimi uygulama katmanında mutlaka şifrelenmeli (Secure Element kullanımı) ve işlem öncesi kullanıcı onayı (biyometrik veya şifre) şart koşulmalıdır.