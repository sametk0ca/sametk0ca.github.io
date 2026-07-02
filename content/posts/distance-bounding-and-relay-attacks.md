---
title: "Distance Bounding & Relay Attacks"
date: 2026-06-14
description: "Anahtarsız giriş ve temassız ödeme sistemlerinin röle saldırılarıyla nasıl istismar edildiği ve fiziksel katmanda mesafe sınırlandırma yöntemleriyle nasıl korunduğu. / How keyless entry and contactless payment systems are exploited by relay attacks and secured using physical-layer distance bounding protocols."
tags: ["Physical Security", "Relay Attack", "Distance Bounding", "Wireless Security"]
categories: ["Blog"]
ShowToc: true
math: true
mermaid: true
cover:
    image: "/img/cover-1549317661-bd32c8ce0db2.jpg"
    alt: "Wireless relay and signal distance bounding representation"
    relative: false
---

## Türkçe (TR)

### Giriş
Kablosuz iletişim teknolojileri hayatımızı kolaylaştırırken, fiziksel yakınlığı bir "güven ve yetki" kriteri olarak kabul eden pek çok sistemi de beraberinde getirdi. Örneğin, anahtarsız giriş (Keyless Entry) sistemine sahip bir araca yaklaştığınızda kapıların otomatik açılması veya temassız kredi kartınızı POS cihazına yaklaştırdığınızda ödemenin gerçekleşmesi bu mantığa dayanır. Ancak siber saldırganlar, fiziksel yakınlık varsayımını istismar etmenin son derece yaratıcı bir yolunu buldular: **Röle (Sinyal Taşıma) Saldırıları**. Bu fiziksel katman tehdidine karşı geliştirilen en güçlü savunma mekanizması ise sinyalin gidiş-dönüş süresini fizik kurallarına dayanarak ölçen **Mesafe Sınırlandırma (Distance Bounding)** protokolleridir.

### Tehdit: Röle (Wormhole) Saldırıları
Röle saldırılarında, saldırganlar iki adet köprü (aracı) cihaz kullanarak birbirinden çok uzak olan iki meşru cihaz arasındaki iletişimi uzatır. En popüler örnek, otoparktaki arabanız ile evinizin içindeki masada duran anahtarınız arasında yapılan saldırıdır:
1.  **Araba Yanındaki Saldırgan**: Arabanın kapı koluna dokunarak arabanın anahtara bir sorgu sinyali (challenge) göndermesini tetikler. Bu sinyali kendi elindeki güçlü bir vericiyle evdeki iş ortağına aktarır.
2.  **Ev Yanındaki Saldırgan**: Gelen sinyali ev kapısının yakınında tuttuğu antenle içerideki anahtara iletir.
3.  **Anahtarın Yanıtı**: Anahtar geçerli ve doğru bir kriptografik yanıt üretir. Bu yanıt aynı yolla arabaya geri taşınır ve araba sahibinin gerçekten orada olduğunu varsayarak kapıları açar.

Bu saldırı türünün en kritik yönü, standart kriptografik önlemlerin (şifreleme, dijital imza vb.) bunu engelleyememesidir. Çünkü anahtar tamamen geçerli ve doğru yanıtlar vermektedir; tek sorun, bu yanıtları yüzlerce metre uzaktan veriyor olmasıdır.

### Çözüm: Mesafe Sınırlandırma (Distance Bounding)
Mesafe sınırlandırma protokolleri, doğrulayıcı (Verifier - Araba/POS) ile kanıtlayıcı (Prover - Anahtar/Kart) arasındaki fiziksel mesafenin üst sınırını, gönderilen sinyalin gidiş-dönüş süresi (Round-Trip Time - RTT) üzerinden hesaplar.
*   **Çalışma Mantığı**: Doğrulayıcı, kanıtlayıcıya tek bitlik çok hızlı sorgular gönderir. Kanıtlayıcı bu sorguyu nanosaniyeler içinde yanıtlamak zorundadır (örneğin donanımsal düzeyde tek bir XOR işlemiyle).
*   **Fizik Yasası**: Evrendeki hiçbir sinyal ışık hızından ($c \approx 30 \text{ cm/ns}$) daha hızlı hareket edemez. Bu nedenle, gidiş-dönüş süresi mesafe için kesin bir fiziksel sınır oluşturur:
    $$d \le \frac{RTT \times c}{2}$$
    Eğer saldırgan sinyali başka bir mesafeye taşımaya kalkarsa, bu taşıma işlemi milisaniyeler veya mikrosaniyeler düzeyinde bir gecikme ekleyecek ve gidiş-dönüş süresinin aşılmasıyla saldırı anında tespit edilecektir.

### İletişim Akışı ve Röle Saldırısı Anatomisi
Aşağıdaki diyagramda, standart bir röle saldırısının nasıl gerçekleştiği ve gidiş-dönüş süresinin (RTT) uzamasıyla bu saldırının nasıl tespit edilebileceği gösterilmektedir:

![Diyagram / Diagram](/img/mermaid-distance-bounding-and-relay-attacks-1-abd3b7d6.svg)

### Uygulama Alanları ve Zafiyetler
*   **NFC ve RSSI Zafiyeti**: Çoğu temassız kart ve eski nesil anahtarlar mesafe sınırlandırma yapmaz; sadece sinyal gücüne (RSSI) güvenir. Saldırganlar sinyal yükselticilerle gücü artırarak bu sistemleri kolayca kandırabilir.
*   **UWB (Ultra Geniş Bant - Ultra-Wideband)**: Günümüzün cm hassasiyetinde mesafe ölçen en güvenli teknolojisidir. Çok kısa radyo palsları (2-3 ns) kullandığı için sinyali yakalayıp manipüle etmek veya gecikmeyi gizlemek fiziksel olarak imkansıza yakındır.

---

## English (EN)

### Introduction
As wireless communication technologies make our daily lives more convenient, they also introduce systems that rely heavily on physical proximity as a metric for trust. For instance, Passive Keyless Entry (PKE) systems unlock car doors as you approach, and contactless payment terminals complete transactions when a credit card is brought near. However, attackers have designed a highly effective bypass for this proximity assumption: **Relay (Wormhole) Attacks**. The most robust defense against this physical-layer threat is **Distance Bounding**, a technique that calculates the physical distance between devices based on the fundamental laws of physics.

### The Threat: Relay Attacks
In a relay attack, two adversaries use surrogate devices to bridge the communication gap between two legitimate entities that are far apart. The most common scenario involves a target car in a driveway and its key fob inside the house:
1.  **Attacker near the car**: Triggers the car's door handle, causing the car to broadcast a cryptographic challenge. The attacker captures this signal and relays it over a high-powered transmitter to their partner near the house.
2.  **Attacker near the house**: Receives the relayed signal and broadcasts it to the key fob inside.
3.  **The Key Fob**: Computes a valid cryptographic response and sends it back. This response is relayed back to the car, which unlocks, assuming the owner is standing right next to it.

Traditional cryptographic protections like encryption or digital signatures cannot stop this. The key fob is generating valid cryptographic signatures; it is simply doing so from a different location.

### The Solution: Distance Bounding
Distance bounding protocols establish an upper limit on the physical distance between a **Verifier** (e.g., the car or payment terminal) and a **Prover** (e.g., the key fob or card) by measuring the Round-Trip Time (RTT) of a rapid signal exchange.
*   **Mechanism**: The Verifier sends a series of single-bit challenges. The Prover must process and respond to these bits almost instantaneously (usually via hardware-level single-bit operations like XOR).
*   **Physics Limit**: Since signals cannot travel faster than the speed of light ($c \approx 30 \text{ cm/ns}$), the gidiş-dönüş süresi (RTT) sets a strict boundary on distance:
    $$d \le \frac{RTT \times c}{2}$$
    If an attacker attempts to relay the signals, the processing and transmission over the relay link introduce a latency of microseconds or milliseconds. The Verifier detects this timeout and rejects the transaction.

### Communication Flow and Relay Anatomy
The diagram below shows how a relay attack operates and how measuring the RTT detects the added latency:

![Diyagram / Diagram](/img/mermaid-distance-bounding-and-relay-attacks-2-0d9712dc.svg)

### Technologies and Vulnerabilities
*   **NFC and RSSI Weakness**: Many contactless cards and older entry systems rely solely on Received Signal Strength Indication (RSSI) to determine proximity. Attackers can bypass this by using high-gain directional antennas and amplifiers.
*   **IR-UWB (Impulse-Radio Ultra-Wideband)**: The state-of-the-art secure ranging technology. It uses ultra-short pulses (2-3 ns), making it physically difficult for an attacker to manipulate the signal's arrival time without detection. UWB is now widely integrated into modern smartphones and high-end automotive key systems to block relay attacks.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / distance-bounding-and-relay-attacks]]*
