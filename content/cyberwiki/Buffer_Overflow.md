+++
title = "Buffer Overflow (Tampon Bellek Taşması) | Buffer Overflow"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

Buffer Overflow is when more data is sent to a program than its capacity, exceeding the allocated space (buffer zone) and overwriting other critical areas in the memory (RAM).

### 1. Attack Logic
Computer programs allocate certain boxes (Buffers) in RAM to store data. If the attacker sends more data than can fit into this box, the overflowing data overwrites the adjacent boxes (e.g. the box that holds what the program's next command will be). The attacker can take control of the program by placing his own malicious commands in this overflowing section.

### 2. How Does It Happen?
Especially in languages ​​such as C and C++, memory management is left to the developer. If the developer does not set a check saying "Do not accept data from the user if it is more than 10 characters", the attacker can overflow the memory by sending 1000 characters.

### 3. Some Terms You Should Know
- **Stack & Heap:** Two different regions that memory (RAM) uses to store data. Overflows usually occur on the "Stack".
- **Return Address:** The address that tells the program which command to return to after finishing a job. The attacker mostly tries to redirect this address to his own malicious code.
- **Shellcode:** A small piece of code that the attacker leaks into memory and wants to be executed (Ex: Code that opens a command line - shell).
- **ASLR (Address Space Layout Randomization):** Random placement of addresses in memory each time. It is a defense mechanism that makes it difficult for the attacker to find the target.

### 4. Ways of Protection
- **Safe Languages:** Using languages that automate memory management (Python, Java, Go, Rust).
- **Bounds Checking:** To check the size of every data coming from the user.
- **DEP (Data Execution Prevention):** Preventing code execution in the parts of the memory where data is stored.

### Real World Analogy
Imagine filling a glass (Buffer) with water. When the glass is full, the water overflows and spills onto an important document (other data in memory) on the table, making it unreadable. If the spilled water were magical and wrote new (and evil) orders onto the paperwork, this would be a complete Buffer Overflow.
