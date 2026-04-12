---
title: "Yan Kanal Saldırıları ve Maskeleme: Donanım Düzeyinde Güvenlik"
date: 2026-04-11
draft: true
tags: ["Hardware Security", "Cryptography", "Side-Channel", "CyBOK"]
categories: ["Advanced Security"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:900/1*P9O8I7U6Y5T4R3E2W1.png"
    alt: "Side-Channel Attack"
    relative: false
---

![](https://miro.medium.com/v2/resize:fit:900/1*P9O8I7U6Y5T4R3E2W1.png)

Kriptografik algoritmaların matematiksel güvenliği, bu algoritmaların fiziksel donanımlar üzerindeki uygulamalarının güvenliğini her zaman garanti etmez. **Yan Kanal Saldırıları (Side-Channel Attacks - SCA)**, bir cihazın şifreleme işlemi sırasında sızdırdığı fiziksel bilgileri (güç tüketimi, elektromanyetik radyasyon, zamanlama) analiz ederek gizli anahtarları ele geçirmeyi amaçlar. Bu saldırılar, algoritmanın kendisini değil, fiziksel gerçeklemesini hedef alır.

### Teknik Analiz ve Saldırı Vektörleri

CyBOK "Hardware Security" bilgi alanı çerçevesinde, yan kanal saldırıları temel olarak iki ana kategoriye ayrılır:

1. **Güç Analizi Saldırıları (Power Analysis):** İşlemcinin tükettiği elektrik akımındaki dalgalanmaların izlenmesidir.
    * **Basit Güç Analizi (SPA):** Tek bir güç izinin (power trace) doğrudan gözlemlenmesidir.
    * **Diferansiyel Güç Analizi (DPA):** Çok sayıda güç izi üzerinde istatistiksel yöntemler kullanılarak anahtarın tahmin edilmesidir.
    * **Korelasyon Güç Analizi (CPA):** Güç tüketimi ile varsayımsal bir güç modeli (Örn: Hamming Weight) arasındaki korelasyonun hesaplanmasıdır.
2. **Elektromanyetik (EM) Analizi:** Cihazın üzerinden yayılan radyo dalgalarının dinlenmesidir. Temassız (non-invasive) olması nedeniyle tespiti oldukça zordur.
3. **Zamanlama Analizi (Timing Attacks):** Operasyonların tamamlanma sürelerindeki mikro farklılıkların ölçülmesidir.

### Korunma Mekanizmaları ve Standartlar

ISO/IEC 17825 standardı, non-invasive saldırı sınıflarına karşı koruma yöntemlerinin test edilmesi için bir metodoloji sunar. En etkili savunma tekniklerinden biri olan **Maskeleme (Masking)**, veriyi rastgele parçalara (shares) bölerek işleme prensibine dayanır. "Boolean Masking" (XOR tabanlı) ve "Arithmetic Masking" gibi yöntemler, güç tüketimi ile gizli veri arasındaki korelasyonu koparmayı hedefler. Ayrıca, "Threshold Implementation" gibi teknikler, donanım düzeyinde (glitch'lere karşı dirençli) güvenli tasarım sağlamak için kullanılır.

---

### Side-Channel Attacks and Masking: Security at the Hardware Level

The mathematical security of cryptographic algorithms does not always guarantee the security of their implementations on physical hardware. **Side-Channel Attacks (SCA)** aim to recover secret keys by analyzing physical information (power consumption, electromagnetic radiation, timing) leaked by a device during encryption. These attacks target the physical implementation rather than the algorithm itself.

### Technical Analysis and Attack Vectors

Within the framework of the CyBOK "Hardware Security" knowledge area, side-channel attacks are primarily divided into two main categories:

1. **Power Analysis Attacks:** Monitoring fluctuations in the electric current consumed by the processor.
    * **Simple Power Analysis (SPA):** Direct observation of a single power trace.
    * **Differential Power Analysis (DPA):** Estimating the key using statistical methods over a large number of power traces.
    * **Correlation Power Analysis (CPA):** Calculating the correlation between power consumption and a hypothetical power model (e.g., Hamming Weight).
2. **Electromagnetic (EM) Analysis:** Monitoring radio waves emitted by the device. Since it is non-invasive, detection is highly challenging.
3. **Timing Attacks:** Measuring micro-differences in the duration of operations.

### Countermeasures and Standards

The ISO/IEC 17825 standard provides a methodology for testing protection methods against non-invasive attack classes. **Masking**, one of the most effective defense techniques, is based on the principle of processing data by splitting it into random shares. Methods such as "Boolean Masking" (XOR-based) and "Arithmetic Masking" aim to break the correlation between power consumption and secret data. Additionally, techniques like "Threshold Implementation" are utilized to ensure secure design at the hardware level, resilient against glitches.
