+++
title = "NFC (Near Field Communication) Mekanizması | NFC (Near Field Communication) Mechanism"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
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

---

## English Version

NFC is a radio frequency technology that works at very short distances such as 4-10 cm. Used for contactless payments, smart cards and authentication.

### 1. Operating Modes
- **Reader/Writer:** The device reads a tag (Ex: bus pass reading).
- **Peer-to-Peer:** Two devices share data (Ex: file transfer between phones).
- **Card Emulation:** Making the phone act like a credit card (Ex: Apple Pay / Google Pay).

### 2. Security Risks
- **Eavesdropping (Listening):** Even though the distance is short, the NFC signal can be captured from a few meters away with sensitive antennas. If the data is not encrypted (e.g. some old public transport cards) the information can be stolen.
- **Data Modification:** The attacker can corrupt or change the sent data by intercepting it.
- **Relay Attack:** It is the most dangerous one. The attacker captures the victim's NFC signal and transmits it over the Internet to a payment terminal elsewhere to spend money on the victim's card.

### 3. Prevention
NFC communication must be encrypted at the application layer (use of Secure Element) and user approval (biometrics or password) must be required before the transaction.
