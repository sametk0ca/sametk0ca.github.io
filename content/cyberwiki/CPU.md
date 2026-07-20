+++
title = "CPU"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
+++

Türkçe adıyla **Merkezi İşlem Birimi**, bilgisayarların, akıllı telefonların, tabletlerin ve diğer tüm akıllı cihazların **"beyni"** olarak kabul edilen en temel donanım bileşenidir. Genellikle anakart üzerinde özel bir yuvaya (sokete) yerleştirilen bu aygıt, tek bir mikroçip üzerinde bir araya getirilmiş milyarlarca mikroskobik transistörden oluşur.

**CPU Ne İşe Yarar?** İşlemciler, bir sistem içindeki tüm donanım ve yazılım etkileşimlerini yönetir, komutları yorumlar ve bilgisayardaki tüm veri akışını koordine eder.

- **Talimatları Yürütür:** Bilgisayar programlarından ve işletim sisteminden gelen yazılım komutlarını alır, çalıştırır ve klavye, fare, ekran kartı gibi diğer bileşenlerin ne yapması gerektiğini kontrol eder.
- **Dijital Çeviri Yapar:** İnternette gezinmek, oyun oynamak veya bir video açmak gibi gerçekleştirdiğiniz tüm işlemleri "0" ve "1"lerden oluşan ikili (binary) koda dönüştürerek cihazın anlayabileceği formata çevirir ve ardından görsel bir çıktı oluşturur.
- **Hesaplama Yapar:** Sistem için gerekli olan tüm aritmetik (toplama, çıkarma, çarpma, bölme) ve mantıksal (VE, VEYA, eşittir, büyüktür vb.) işlemleri saniyenin milyarda biri hızında gerçekleştirir.

**CPU Nasıl Çalışır?** İşlemci, cihaz açıldığı andan kapanana kadar sürekli devam eden ve **"Komut Döngüsü" (Instruction Cycle)** olarak adlandırılan üç temel aşamalı bir sistemle çalışır. Bu döngü saniyede milyarlarca kez tekrarlanır:

1. **Arama/Getirme (Fetch):** CPU, çalıştırılacak olan bir sonraki komutu veya veriyi ana bellekten (RAM) alır. Bu aşamada Program Sayacı (PC) adı verilen yapı, alınacak komutun hafızadaki adresini gösterir ve bu komut CPU içerisindeki özel yazmaçlara (IR) getirilir.
2. **Kod Çözme (Decode):** İşlemcinin kontrol birimi, bellekten gelen ikili formdaki komutun ne anlama geldiğini deşifre eder. Talimatın bir matematiksel işlem mi yoksa veri taşıma mı olduğunu belirler ve bu işlem için hangi donanım parçalarının gerektiğini koordine ederek ilgili sinyalleri üretir.
3. **Yürütme (Execute):** Şifresi çözülen talimat, ilgili işlemci birimleri (genellikle ALU) tarafından yerine getirilir. Elde edilen sonuç, ya CPU içindeki geçici belleklere (yazmaçlara) ya da ana belleğe geri yazılarak kaydedilir (Write-back) ve işlemci hızla bir sonraki döngüye geçer.

**CPU'nun Ana Bileşenleri Nelerdir?** Bu döngünün kusursuz çalışabilmesi için işlemcinin içinde farklı uzmanlıklara sahip kritik alt birimler bulunur:

- **Aritmetik Mantık Birimi (ALU):** İşlemcinin kalbi ve hesap makinesidir. Tüm matematiksel hesaplamaları ve mantıksal karşılaştırmaları bu bölüm gerçekleştirir.
- **Kontrol Birimi (CU):** İşlemcinin "orkestra şefi" olarak görev yapar. Komutların kodunu çözer, bileşenlerin ne zaman ve nasıl çalışacağını belirleyen zamanlama sinyallerini üretir ve birimler arasındaki veri akışının senkronizasyonunu yönetir.
- **Yazmaçlar (Registers):** İşlemcinin o an doğrudan üzerinde çalıştığı verileri ve işlem sırasını tutan, RAM veya önbellekten çok daha hızlı olan CPU içindeki en küçük depolama alanlarıdır.
- **Önbellek (Cache):** CPU'nun sık ihtiyaç duyduğu verilere, yavaş olan RAM'e gitmeden çok hızlı bir şekilde ulaşabilmesini sağlayan CPU içi özel yüksek hızlı bellektir.
- **Veri Yolları (BUS):** Bilgisayar içindeki farklı bileşenler ve işlemcinin alt birimleri arasındaki bilgi iletimini sağlayan köprü ve kanallardır.

---

## English Version

**Central Processing Unit**, as it is known in Turkish, is the most basic hardware component that is considered the **"brain"** of computers, smartphones, tablets and all other smart devices. This device, usually placed in a special slot (socket) on the motherboard, consists of billions of microscopic transistors assembled on a single microchip.

**What Does a CPU Do?** Processors manage all hardware and software interactions within a system, interpret commands, and coordinate the entire flow of data in the computer.

- **Executes Instructions:** It receives software commands from computer programs and the operating system, executes them, and controls what other components such as keyboard, mouse, and video card should do.
- **Does Digital Translation:** It converts all the operations you perform, such as surfing the Internet, playing games or opening a video, into binary code consisting of "0" and "1" into a format that the device can understand, and then creates a visual output.
- **Performs Calculation:** It performs all arithmetic (addition, subtraction, multiplication, division) and logical (AND, OR, equals, greater than, etc.) operations required for the system at a speed of one billionth of a second.

**How ​​Does the CPU Work?** The processor works with a three basic stage system called **Instruction Cycle**, which continues from the moment the device is turned on until it is turned off. This cycle repeats billions of times per second:

1. **Search/Fetch:** The CPU retrieves the next command or data to be executed from the main memory (RAM). At this stage, the structure called Program Counter (PC) shows the address of the command to be received in memory, and this command is brought to special registers (IR) in the CPU.
2. **Decode:** The processor's control unit deciphers what the binary command coming from memory means. It determines whether the instruction is a mathematical operation or a data transfer and produces the relevant signals by coordinating which pieces of hardware are required for this operation.
3. **Execute:** The decrypted instruction is executed by the relevant processor units (usually ALU). The result obtained is recorded either in temporary memories (registers) within the CPU or by writing back to the main memory (Write-back), and the processor quickly moves on to the next cycle.

**What are the Main Components of the CPU?** In order for this cycle to work flawlessly, there are critical subunits with different specializations inside the processor:

- **Arithmetic Logic Unit (ALU):** It is the heart of the processor and the calculator. This section performs all mathematical calculations and logical comparisons.
- **Control Unit (CU):** Acts as the "conductor" of the processor. It decodes commands, generates timing signals that determine when and how components operate, and manages the synchronization of data flow between units.
- **Registers:** These are the smallest storage areas within the CPU that hold the data and processing sequence that the processor is currently working on directly, and are much faster than RAM or cache.
- **Cache:** It is a special high-speed memory within the CPU that allows the CPU to access frequently needed data very quickly without going to the slower RAM.
- **Data Buses (BUS):** These are bridges and channels that provide information transmission between different components within the computer and subunits of the processor.
