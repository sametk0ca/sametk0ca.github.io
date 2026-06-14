---
title: "TEMPEST: Understanding Compromising Emanations | TEMPEST: Sızan Sinyalleri Anlamak"
date: 2026-06-14
description: "Elektronik cihazların fiziksel sinyallerle gizli verileri nasıl sızdırdığı ve TEMPEST saldırılarına karşı korunma yöntemleri. / How electronic devices leak confidential data through physical signals and how to defend against TEMPEST attacks."
tags: ["Physical Security", "TEMPEST", "Side-Channel", "Hardware Security"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: true
cover:
    image: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&auto=format&fit=crop"
    alt: "TEMPEST signal leakage and hardware security representation"
    relative: false
---

## Türkçe (TR)

### Giriş
Çalışan her elektronik cihaz, aslında küçük bir radyo vericisidir. Entegre devrelerden akım geçtikçe, transistörler durum değiştirdikçe ve sinyaller bakır yollardan iletildikçe, etrafa istem dışı fiziksel yan etkiler yayılır. Elektromanyetik dalgalardan akustik titreşimlere ve hafif ışık titremelerine kadar uzanan bu yan etkiler, çoğu zaman işlenen veriyle doğrudan ilişkilidir. Eğer bir saldırgan bu "sızan sinyalleri" (compromising emanations) yakalayıp nasıl çözeceğini bilirse; şifreleme anahtarlarını, klavyede basılan tuşları veya ekrandaki görüntüyü uzaktan yeniden oluşturabilir. Bu sızıntıların incelenmesini ve bunlara karşı koruma standartlarını tanımlayan askeri kod adı **TEMPEST**'tir.

### Veri Fiziksel Olarak Nasıl Sızar?
Sızan sinyaller birkaç temel fiziksel ortamda kendisini gösterir:

1. **Elektromanyetik (EM) Radyasyon**: En yaygın sızıntı vektörüdür. Bilgisayarın işlemcisi (CPU), ekran kartı (GPU) veya görüntü kablolarındaki ani akım değişimleri radyo frekansı yayar. Klasik bir saldırı yöntemi olan **Van Eck Phreaking**, monitör veya HDMI/VGA kablosundan yayılan elektromanyetik dalgaları havadan yakalayarak, ekrandaki görüntüyü uzak bir mesafeden gerçek zamanlı olarak yeniden çizmeyi hedefler.
2. **Akustik Sızıntı**: Birçok elektronik bileşen çalışırken yüksek frekanslı, duyulması zor sesler çıkarır. Anakart üzerindeki voltaj regülatör kapasitörleri, işlemci yüküne göre farklı tizlikte öter. Bu "kapasitör ötüşü" bazen kriptografik işlemlerin (örneğin RSA şifre çözme adımlarının) sızmasına yol açabilir. Benzer şekilde, klavye tuşlarının çıkardığı benzersiz ses imzaları bir mikrofonla kaydedilerek kullanıcının ne yazdığı tespit edilebilir.
3. **Optik Sızıntı**: Cihazlar görsel olarak da veri sızdırabilir. Sabit disklerin veya yönlendiricilerin üzerindeki durum LED'leri, veri akışına göre çok hızlı şekilde titrer. Yüksek hızlı bir fotodiyot bu LED'lere doğrultularak akan veri paketleri çözülebilir. Hatta yakındaki bir kaşıktan, şişeden veya kullanıcının göz retinasından yansıyan ekran görüntüleri teleskopik kameralarla analiz edilerek ekrandaki veriler okunabilir.

### Saldırı Akışı
Aşağıdaki mimari diyagram, sızan sinyallerin sistemden nasıl ayrıldığını ve pasif bir gözlemci tarafından nasıl yakalanıp işlendiğini göstermektedir:

![Diyagram / Diagram](/img/mermaid-compromising-emanations-tempest-1-cea59abd.svg)

### Korunma ve Savunma Yöntemleri (TEMPEST Zırhlama)
TEMPEST saldırılarına karşı korunmak, fiziksel katmanda alınacak önlemlere dayanır:
*   **Faraday Kafesleri**: Hassas donanımları topraklanmış metal kutuların veya odaların içine almak, dışarı elektromanyetik dalga çıkmasını engeller.
*   **Sinyal Filtreleme**: Güç kaynaklarına ve ağ kablolarına alçak geçiren (low-pass) filtreler eklenerek, iç kısımdaki yüksek frekanslı gürültülerin kablolar üzerinden dış dünyaya taşınması önlenir.
*   **Bölgeleme (Kırmızı/Siyah Yalıtımı)**: Şifrelenmemiş gizli verileri işleyen cihazlar (Kırmızı bölge) ile dış dünyaya bağlı veya şifreli veri taşıyan hatlar (Siyah bölge) arasına fiziksel mesafe konulmasıdır.
*   **Gürültü Karıştırma (Jamming)**: Çalışma ortamında kasıtlı olarak rastgele elektromanyetik gürültü üreterek, gerçek cihazlardan sızan sinyalleri bastırmak ve saldırganın veriyi çözmesini imkansız kılmaktır.

---

## English (EN)

### Introduction
Every active electronic device is a miniature radio transmitter. As current flows through integrated circuits, transistors switch state, and signals travel along copper traces, they generate unintentional physical side-effects. These side-effects—ranging from electromagnetic waves to acoustic vibrations and subtle light flickers—often correlate directly with the data being processed. If an attacker captures these "compromising emanations" and knows how to decode them, they can reconstruct sensitive information, such as cryptographic keys, typed keystrokes, or screen displays, from a distance. The study of these leaks and the standards designed to shield against them is widely referred to by the US military codename **TEMPEST**.

### How Data Leaks Physically: The Categories
Compromising emanations manifest in several physical mediums:

1. **Electromagnetic (EM) Radiation**: The most prominent vector. Rapid changes in current within a computer's CPU, GPU, or video cable emit radio-frequency radiation. A classic exploit is **Van Eck Phreaking**, where an adversary captures the EM radiation emitted by a monitor or its HDMI/VGA cable to reconstruct the screen image in real-time on a remote display.
2. **Acoustic Emissions**: Many electronic components make subtle, high-frequency sounds. For example, voltage regulator capacitors on motherboards squeal depending on CPU load. In some cases, this "capacitor squeal" can leak cryptographic operations (like RSA decryption) because different computations consume power differently. Keyboard acoustics are another risk; microphones can capture the unique click sound of each key to determine what is being typed.
3. **Optical Leakage**: Computers also leak data visually. Status LEDs on hard drives and routers flicker rapidly in response to data processing. By pointing a high-speed photodiode at these LEDs, an attacker can extract data packets. Even screen reflections off nearby spoons, bottles, or the user's retina can be analyzed with telescopic cameras to reconstruct display outputs.

### The Attack Flow
The following architecture diagram visualizes how compromising emanations escape a system and are captured by a passive observer:

![Diyagram / Diagram](/img/mermaid-compromising-emanations-tempest-2-ee356e46.svg)

### Defense and Mitigation (TEMPEST Shielding)
Securing against TEMPEST attacks requires physical-layer countermeasures:
*   **Faraday Cages**: Enclosing sensitive hardware in grounded metallic enclosures blocks outbound EM waves.
*   **Signal Filtering**: Placing low-pass filters on power supply lines and network lines prevents internal high-frequency noise from traveling out through copper wires.
*   **Zoning**: Establishing a physical distance (red/black isolation) between equipment that processes unencrypted data (red) and lines carrying encrypted data or connected to the outside world (black).
*   **Jamming**: Generating intentional EM noise in the immediate environment to drown out any genuine compromising emanations, making reconstruction mathematically impossible.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / compromising-emanations-tempest]]*
