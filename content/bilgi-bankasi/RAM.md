+++
title = "RAM"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
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