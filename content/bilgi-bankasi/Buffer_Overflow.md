+++
title = "Buffer Overflow (Tampon Bellek Taşması)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Buffer Overflow, bir programa kapasitesinden daha fazla veri gönderilerek, bu verinin kendisine ayrılan alanı (tampon bölgeyi) aşması ve bellekteki (RAM) diğer kritik alanların üzerine yazılmasıdır.

### 1. Saldırı Mantığı
Bilgisayar programları verileri saklamak için RAM'de belirli kutular (Buffer) ayırır. Eğer saldırgan bu kutuya sığmayacak kadar çok veri gönderirse, taşan veri yandaki kutuların (Örn: Programın bir sonraki komutunun ne olacağını tutan kutu) üzerine yazar. Saldırgan bu taşan kısma kendi zararlı komutlarını koyarak programın kontrolünü ele geçirebilir.

### 2. Nasıl Gerçekleşir?
Özellikle C ve C++ gibi dillerde bellek yönetimi geliştiriciye bırakılmıştır. Eğer geliştirici "Kullanıcıdan gelen veri 10 karakterden fazlaysa kabul etme" diye bir kontrol koymazsa, saldırgan 1000 karakter göndererek belleği taşırabilir.

### 3. Bilmen Gereken Bazı Terimler
- **Stack & Heap:** Belleğin (RAM) verileri saklamak için kullandığı iki farklı bölge. Taşmalar genellikle "Stack" üzerinde olur.
- **Return Address:** Programın bir işi bitirdikten sonra hangi komuta geri döneceğini bildiren adres. Saldırgan en çok bu adresi kendi zararlı koduna yönlendirmeye çalışır.
- **Shellcode:** Saldırganın belleğe sızdırdığı ve çalıştırılmasını istediği küçük kod parçası (Örn: Bir komut satırı - shell açan kod).
- **ASLR (Address Space Layout Randomization):** Bellekteki adreslerin her seferinde rastgele yerleştirilmesi. Saldırganın hedefi bulmasını zorlaştıran bir savunma mekanizmasıdır.

### 4. Korunma Yolları
- **Güvenli Diller:** Bellek yönetimini otomatik yapan diller (Python, Java, Go, Rust) kullanmak.
- **Bounds Checking:** Kullanıcıdan gelen her verinin boyutunu mutlaka kontrol etmek.
- **DEP (Data Execution Prevention):** Belleğin veri saklanan kısımlarında kod çalıştırılmasını engellemek.

### Gerçek Dünya Analojisi
Bir bardağa (Buffer) su doldurduğunuzu düşünün. Bardak dolunca su taşar ve masadaki önemli bir evrakın (Bellekteki diğer veriler) üzerine dökülüp onu okunmaz hale getirir. Eğer dökülen su sihirli olsaydı ve evrakın üzerine yeni (ve kötü) emirler yazsaydı, bu tam bir Buffer Overflow olurdu.