+++
title = "RAM"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
+++

**RAM (Random Access Memory - Rastgele Erişilebilir Bellek)**, bilgisayarların, akıllı telefonların ve diğer akıllı cihazların **"kısa süreli hafızası"** olarak görev yapan son derece hızlı bir donanım bileşenidir. İşlemcinin (CPU) o an üzerinde çalıştığı işletim sistemi verilerini, aktif uygulamaları ve işlemleri geçici olarak depolar. "Rastgele erişim" (Random Access) terimi, bellekteki herhangi bir veri hücresine, verinin fiziksel konumundan bağımsız olarak doğrudan ve neredeyse aynı hızda ulaşılabileceği anlamına gelir. RAM, işlemcinin ihtiyaç duyduğu verilere, sabit disk (HDD) veya SSD gibi kalıcı sürücülere kıyasla onlarca kat daha hızlı erişmesini sağlayarak sistemin hızını ve çoklu görev performansını artırır.

**RAM Nasıl Çalışır?** RAM modülleri, mikroskobik düzeyde "0" ve "1" değerlerini temsil eden elektriksel yükleri yöneterek çalışır. Bir programı çalıştırdığınızda veriler yavaş olan depolama biriminden alınıp hızlı olan RAM'e kopyalanır. Veri yazma ve okuma süreci şu aşamalardan oluşur:

- **Adresleme:** İşlemci bir veriyi talep ettiğinde veya yeni bir veri yazmak istediğinde, bellek kontrolcüsü (memory controller) üzerinden bir adres sinyali gönderir.
- **Sinyal İletimi ve Anahtarlama:** RAM üzerinde belirlenmiş adresteki transistörler açılarak, o veri hücresine giden elektriksel kapıları kontrol eder.
- **Kapasitör Etkileşimi:** Özellikle yaygın olan DRAM hücrelerinde veri, bir kapasitör üzerindeki elektrik yükü olarak depolanır. "Sense amplifier" (duyarlı yükseltici) adı verilen devreler bu çok küçük elektriksel yükü algılayıp okur ve sistemin anlayabileceği voltaj seviyelerine (0 veya 1) çeker. İşlem bittiğinde veya uygulama kapatıldığında veri RAM'den silinir ve yerini yeni işlemlere bırakır.

**Volatility (Uçuculuk) Nedir?** **Volatility (Uçuculuk)**, RAM'in içindeki verileri tutabilmesi için **sürekli ve kesintisiz bir güç kaynağına (elektriğe) ihtiyaç duymasıdır**. Sisteme giden elektrik akımı kesildiği anda veya cihaz kapatıldığında, bellek hücrelerindeki tüm veriler kalıcı olarak silinir. Bu fiziksel durumun temel nedeni şarj sızıntısıdır: Dinamik RAM (DRAM) kapasitörleri mükemmel yalıtkan değildir ve içerdikleri yük zamanla sızarak kaybolur. Verinin kaybolmaması için kapasitörlerin milisaniyeler içinde sürekli olarak yeniden şarj edilmesi (refresh - tazeleme) gerekir. Elektrik kesildiğinde bu tazeleme işlemi durduğu için veri anında yok olur. Uçucu yapı bir dezavantaj gibi görünse de, verilerin kalıcı olarak mühürlenmesi gerekmediğinden okuma ve yazma işlemlerinin inanılmaz derecede yüksek hızlarda ve düşük voltajlarda gerçekleştirilmesini sağlar.

**RAM Türleri Nelerdir?** Yarı iletken bellek dünyası, veriyi saklama yöntemlerine ve mimarilerine göre farklı RAM türlerine ayrılır:

**1. SRAM (Statik RAM):** Veriyi tutmak için kapasitör yerine "flip-flop" devreleri (genellikle bir hücrede 6 transistör) kullanır. Bu yapı sayesinde sürekli güç sağlandığı sürece veriyi **tazelemeye (refresh) ihtiyaç duymaz**. DRAM'den çok daha hızlı ve daha düşük gecikme sürelerine sahiptir. Ancak yapısı gereği üretimi çok daha pahalıdır ve yoğunluğu düşüktür (az kapasite sunar). Bu nedenle ana bellek yerine işlemcilerin içindeki **çok yüksek hızlı önbelleklerde (Cache - L1, L2, L3)** kullanılır.

**2. DRAM (Dinamik RAM):** Her bir veri biti, bir transistör ve bir kapasitörden oluşan mikroskobik hücrelerde saklanır. Kapasitörler sürekli yük sızdırdığı için verinin silinmemesi adına her milisaniyede bir **tazelenmesi (refresh)** gerekir. SRAM'e kıyasla daha yavaştır fakat tek bir çip üzerine çok yüksek kapasitede veri sığdırılabilir ve üretimi oldukça ucuzdur. Bilgisayarlarımızın **ana belleği** olarak kullanılan RAM türüdür.

**3. SDRAM (Eş Zamanlı Dinamik RAM):** DRAM teknolojisinin işlemci saat döngüsüyle senkronize çalışarak veri transfer hızını optimize eden türüdür.

**4. DDR SDRAM Nesilleri (Double Data Rate):** SDR teknolojisinin saat döngüsünün hem yükselen hem de alçalan kenarında veri aktarımı yaparak bant genişliğini iki katına çıkaran neslidir. Masaüstü ve dizüstü bilgisayarlarda temel standarttır. Yıllar içinde gelişerek farklı nesillere ayrılmıştır:

- **DDR3:** Eski nesil cihazlarda kullanılır (1.5V, ~2133 MT/s hıza kadar).
- **DDR4:** Uzun süredir standart olarak kullanılan, 1.2V voltaj seviyesinde çalışan ve uygun maliyet ile yeterli performansı sunan belleklerdir (3200 MT/s'ye kadar standart).
- **DDR5:** Günümüzün en modern standartlarından biridir. 1.1V çalışma voltajıyla daha az güç tüketirken 8400 MT/s ve üzerine kadar ulaşabilen hızlar sunar. En büyük yeniliği voltaj regülasyonunu (PMIC) doğrudan bellek modülünün üzerine taşımasıdır.

**Özel Kullanım Alanlarına Göre Diğer RAM Türleri:**

- **LPDDR (Low Power DDR):** Akıllı telefonlar, tabletler ve ince dizüstü bilgisayarlar için tasarlanmış, performanstan ödün vermeden son derece düşük güç tüketen ve anakarta doğrudan lehimlenen belleklerdir (Örn. LPDDR5X).
- **GDDR (Graphics DDR):** Ekran kartlarında (GPU) kullanılan, yüksek bant genişliği ve grafik işleme için özel optimize edilmiş bellek türüdür (Örn. GDDR6).
- **ECC RAM (Error Correcting Code):** Veri bütünlüğünün kritik olduğu sunucularda ve iş istasyonlarında kullanılan, kozmik ışınlar gibi nedenlerle oluşan anlık tek bitlik veri hatalarını tespit edip düzeltebilen RAM türüdür.

---

## English Version

**RAM (Random Access Memory)** is an extremely fast hardware component that serves as the **"short-term memory"** of computers, smartphones and other smart devices. It temporarily stores operating system data, active applications and processes that the processor (CPU) is currently running on. The term "Random Access" means that any cell of data in memory can be accessed directly and at nearly the same speed, regardless of the physical location of the data. RAM increases system speed and multitasking performance by allowing the processor to access the data it needs dozens of times faster than permanent drives such as hard disk (HDD) or SSD.

**How ​​Does RAM Work?** RAM modules work by managing electrical charges that represent "0" and "1" values ​​at the microscopic level. When you run a program, data is taken from the slower storage and copied to the faster RAM. The process of writing and reading data consists of the following stages:

- **Addressing:** When the processor requests data or wants to write new data, it sends an address signal through the memory controller.
- **Signal Transmission and Switching:** The transistors at the specified address on the RAM are opened and control the electrical gates leading to that data cell.
- **Capacitor Interaction:** Particularly common in DRAM cells, data is stored as an electrical charge on a capacitor. Circuits called "sense amplifier" detect and read this very small electrical charge and draw it to voltage levels (0 or 1) that the system can understand. When the process is finished or the application is closed, the data is deleted from RAM and replaced by new processes.

**What is Volatility?** **Volatility** is the fact that RAM needs a constant and uninterrupted power supply (electricity) to hold the data in it**. As soon as the electrical current to the system is cut off or the device is turned off, all data in the memory cells is permanently deleted. The primary cause of this physical condition is charge leakage: Dynamic RAM (DRAM) capacitors are not perfect insulators, and the charge they contain leaks away over time. To prevent data from being lost, capacitors must be constantly recharged (refreshed) within milliseconds. When the power is cut off, this refresh process stops and the data is instantly destroyed. While the volatile nature may seem like a disadvantage, it allows reads and writes to be performed at incredibly high speeds and low voltages because data does not need to be permanently sealed.

**What are the Types of RAM?** The world of semiconductor memory is divided into different types of RAM according to their data storage methods and architectures:

**1. SRAM (Static RAM):** Uses "flip-flop" circuits (usually 6 transistors in a cell) instead of capacitors to hold data. Thanks to this structure, there is no need to refresh the data as long as continuous power is provided. It is much faster and has lower latency than DRAM. However, due to its structure, it is much more expensive to produce and has low density (offers little capacity). For this reason, it is used in very high-speed caches (Cache - L1, L2, L3)** inside the processors instead of main memory.

**2. DRAM (Dynamic RAM):** Each bit of data is stored in microscopic cells consisting of a transistor and a capacitor. Since capacitors constantly leak charge, they must be refreshed every millisecond to prevent data from being deleted. It is slower than SRAM, but a very high capacity of data can be placed on a single chip and its production is quite cheap. It is the type of RAM used as the **main memory** of our computers.

**3. SDRAM (Synchronous Dynamic RAM):** It is a type of DRAM technology that optimizes data transfer speed by working synchronously with the processor clock cycle.

**4. DDR SDRAM Generations (Double Data Rate):** It is the generation of SDR technology that doubles the bandwidth by transferring data on both the rising and falling edges of the clock cycle. It is the basic standard on desktop and laptop computers. It has evolved over the years and is divided into different generations:

- **DDR3:** Used in older generation devices (1.5V, up to ~2133 MT/s).
- **DDR4:** These are memories that have been used as standard for a long time, operate at 1.2V voltage level and offer sufficient performance at an affordable cost (standard up to 3200 MT/s).
- **DDR5:** It is one of the most modern standards of today. With its 1.1V operating voltage, it offers speeds of up to 8400 MT/s and above while consuming less power. Its biggest innovation is that it moves the voltage regulation (PMIC) directly onto the memory module.

**Other RAM Types According to Specific Usage Areas:**

- **LPDDR (Low Power DDR):** These are memories designed for smartphones, tablets and thin laptops, that consume extremely low power without compromising performance and are soldered directly to the motherboard (e.g. LPDDR5X).
- **GDDR (Graphics DDR):** It is a type of memory used in graphics cards (GPU), specially optimized for high bandwidth and graphics processing (e.g. GDDR6).
- **ECC RAM (Error Correcting Code):** It is a type of RAM that is used in servers and workstations where data integrity is critical and can detect and correct instantaneous single-bit data errors caused by reasons such as cosmic rays.
