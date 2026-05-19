+++
title = "Digital Forensics (Adli Bilişim)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Digital Forensics, dijital cihazlarda (bilgisayar, telefon, sunucu) meydana gelen olayların kanuni olarak kabul edilebilir kanıtlarını toplama, koruma, analiz etme ve raporlama sürecidir. Siber güvenlikte bir saldırının "nasıl" ve "ne zaman" gerçekleştiğini anlamak için kullanılır.

### 1. Adli Bilişimin Temel Aşamaları
1. **Muhafaza (Preservation):** Kanıtların bozulmaması için cihazın imajı alınır. Orijinal disk üzerinde asla çalışma yapılmaz.
2. **Tanımlama (Identification):** Hangi cihazların ve verilerin inceleneceği belirlenir.
3. **Analiz (Analysis):** Silinmiş dosyalar, internet geçmişi, kayıt defteri girdileri ve bellek dökümleri incelenir.
4. **Raporlama (Reporting):** Bulguların teknik olmayan bir dille, kanıtlarıyla birlikte sunulması.

### 2. Disk Forensics (Disk Analizi)
Sabit diskler, SSD'ler veya USB bellekler üzerindeki verilerin incelenmesidir.
- **Write Blocker:** Diske veri yazılmasını fiziksel olarak engelleyen cihazdır. Kanıt bütünlüğünü korur.
- **Disk İmajı (Bit-stream Image):** Diskin her bir sektörünün (boş alanlar dahil) birebir kopyasıdır. `.ad1`, `.e01` veya `.raw` formatlarında olabilir.
- **Timeline Analizi:** Dosyaların ne zaman oluşturulduğu, değiştirildiği veya erişildiği kronolojik olarak dizilir (MAC times: Modification, Access, Creation).

### 3. Memory Forensics (Bellek Analizi)
Bilgisayarın RAM'indeki verilerin incelenmesidir. RAM, bilgisayar kapandığında silindiği için (volatile) canlı müdahale sırasında ilk toplanması gereken kanıttır.
- **Neden Önemlidir?** Bazı gelişmiş zararlı yazılımlar sadece RAM'de çalışır (fileless malware). Şifreli disklerin anahtarları veya aktif ağ bağlantıları sadece RAM'den okunabilir.
- **Araçlar:** Bellek analizinde dünya standardı **Volatility** aracıdır.

### 4. Temel Kavramlar
- **Chain of Custody (Zapturapt Altında Tutma):** Kanıtın ele geçirildiği andan mahkemeye kadar kimlerin elinden geçtiğinin belgelenmesidir.
- **Hash Değeri:** Bir dosyanın veya disk imajının dijital parmak izidir (MD5, SHA-1). İmaj alındıktan sonra hash değeri hesaplanır; eğer analiz sırasında bu değer değişirse kanıt geçersiz sayılır.

### Gerçek Dünya Analojisi
Digital Forensics, bir cinayet mahalline gelen olay yeri inceleme ekibi gibidir. Polisler (Adli Bilişim Uzmanları), yerdeki parmak izlerini (Loglar), kurbanın son aradığı kişileri (Bellek) ve katilin düşürdüğü eşyaları (Silinmiş dosyalar) toplar. En önemli kural şudur: "Olay yerindeki hiçbir şeye çıplak elle dokunma" (Yani orijinal diske müdahale etme, imajını al).