+++
title = "Memory Leak (Bellek Sızıntısı)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
+++

Memory Leak, bir bilgisayar programının ihtiyaç duyduğu belleği (RAM) aldıktan sonra, işlemini bitirdiğinde bu belleği sisteme geri vermeyi "unutması" durumudur.

### 1. Saldırı ve Güvenlik Mantığı
Memory Leak genellikle bir yazılım hatasıdır, ancak siber güvenlikte bir saldırı aracı olarak da kullanılabilir. Program sürekli yeni bellek alanları işgal eder ama bırakmaz. Sonuçta bilgisayarın tüm RAM'i dolar ve sistem kilitlenir (DoS).

### 2. Nasıl Gerçekleşir?
Özellikle C ve C++ gibi dillerde geliştirici belleği manuel olarak yönetir. `malloc()` ile yer ayırıp `free()` ile bırakmazsa sızıntı başlar. Bir saldırgan, sızıntıya neden olan bir özelliği milyonlarca kez tetikleyerek sunucuyu çökertmeye çalışabilir.

### 3. Bilmen Gereken Bazı Terimler
- **Garbage Collection (Çöp Toplama):** Bazı dillerin (Java, Python, C#) belleği otomatik olarak temizleme özelliğidir. Bu dillerde bellek sızıntısı riski çok daha düşüktür.
- **Out of Memory (OOM):** Bilgisayarın artık yeni hiçbir işlem için yerinin kalmaması durumu.
- **Resource Exhaustion:** Sistemin kaynaklarının (İşlemci, RAM, Disk) tamamen tüketilmesi saldırısı.

### 4. Korunma Yolları
- **Kod Analizi:** Statik kod analiz araçları kullanarak potansiyel sızıntıları önceden tespit etmek.
- **Modern Diller:** Bellek yönetimini otomatik yapan veya Rust gibi bu konuda çok katı kuralları olan diller kullanmak.
- **İzleme:** Sunucu performansını sürekli izleyerek (Monitoring), RAM kullanımındaki anormal artışları fark etmek.

### Gerçek Dünya Analojisi
Bir kütüphaneden kitap aldığınızı düşünün. Kitabı okuyup bitirince rafa geri koymazsanız (Belleği bırakmazsanız) ve sürekli yeni kitaplar alırsanız, bir süre sonra kütüphanede (RAM) kimsenin okuyabileceği kitap kalmaz. Kütüphane işlevsiz hale gelir.