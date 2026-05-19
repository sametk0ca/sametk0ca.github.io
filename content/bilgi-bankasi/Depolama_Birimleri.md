+++
title = "Depolama Birimleri (HDD, SSD, NVMe)"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
+++

Verinin nerede ve nasıl saklandığını bilmek, hem veri sızıntılarını önlemek hem de silinen verileri geri getirmek (Forensics) için kritiktir.

### 1. HDD vs. SSD: Adli Bilişim Farkı
- **HDD (Hard Disk Drive):** Veriler manyetik plakalara yazılır. Veri silindiğinde sadece "adres tablosu" silinir, veri fiziksel olarak oradadır (üzerine yeni veri yazılana kadar). Recovery araçlarıyla kolayca kurtarılabilir.
- **SSD (Solid State Drive):** **TRIM** komutu sayesinde işletim sistemi bir dosyayı sildiğinde, SSD o hücreleri hemen boşaltır. Bu, adli incelemede veri kurtarmayı çok zorlaştırır.

### 2. NVMe (Non-Volatile Memory express)
PCIe veri yolunu kullanan en hızlı depolama standardıdır. Doğrudan CPU ile konuştuğu için performans yüksektir ancak bellek güvenliği (DMA) risklerini beraberinde getirebilir.

### 3. Veri İmhası (Data Sanitization)
Sadece format atmak veriyi yok etmez.
- **Disk Wiping:** Diskin her hücresine rastgele "0" ve "1" yazma işlemi.
- **Degaussing:** HDD'ler için manyetik alanı bozarak veriyi yok etme (SSD'de çalışmaz).
- **Physical Destruction:** Kurumsal seviyede diskleri fiziksel olarak parçalamak en güvenli yoldur.

### 4. SMART Verileri
Disklerin sağlık durumunu gösteren raporlardır. Bir saldırgan diski kasten bozarak (DoS) veya veri yazma limitlerini zorlayarak sisteme zarar verebilir.