+++
title = "CPU"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
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