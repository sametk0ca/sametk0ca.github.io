+++
title = "Depolama Birimleri (HDD, SSD, NVMe) | Storage Units (HDD, SSD, NVMe)"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
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

---

## English Version

Knowing where and how data is stored is critical both to prevent data leaks and to recover deleted data (Forensics).

### 1. HDD etc. SSD: The Computer Forensics Difference
- **HDD (Hard Disk Drive):** Data is written on magnetic plates. When data is deleted, only the "address table" is deleted, the data is physically there (until new data is written over it). It can be easily recovered with recovery tools.
- **SSD (Solid State Drive):** Thanks to the **TRIM** command, when the operating system deletes a file, the SSD immediately empties those cells. This makes data recovery in a forensic investigation very difficult.

### 2. NVMe (Non-Volatile Memory express)
It is the fastest storage standard using the PCIe bus. Since it talks directly to the CPU, performance is high, but it may introduce memory security (DMA) risks.

### 3. Data Destruction (Data Sanitization)
Just formatting does not destroy data.
- **Disk Wiping:** Randomly writing "0" and "1" to each cell of the disk.
- **Degaussing:** Destroying data by disrupting the magnetic field for HDDs (does not work on SSD).
- **Physical Destruction:** Physically destroying disks at the enterprise level is the safest way.

### 4. SMART Data
These are reports showing the health status of the disks. An attacker can damage the system by deliberately corrupting the disk (DoS) or pushing data write limits.
