+++
title = "CLI (Komut Satırı) Navigasyonu - Teknik Detaylar"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "bilgi-bankasi"
+++

Komut satırı, bir bilgisayarla grafiksel arayüz (fare, ikonlar) olmadan, sadece metin tabanlı komutlarla konuşma yöntemidir.

### 1. Shell (Kabuk) Nedir?
**Shell**, kullanıcıdan gelen komutları alıp, bunları işletim sisteminin kalbi olan **Kernel**'e (Çekirdek) ileten bir "çevirmendir". 
- **Neden Kabuk Denir?** Çekirdeği (Kernel) dışarıdan gelen doğrudan müdahalelerden koruyan bir kabuk görevi gördüğü için bu isim verilmiştir.
- **Yaygın Sheller:**
    - **Bash (Bourne Again Shell):** Linux'ta en yaygın standart.
    - **Zsh:** Modern Linux ve macOS (varsayılan) kabuğu.
    - **PowerShell:** Windows'un gelişmiş kabuğu (.NET tabanlıdır, sadece metin değil nesne tabanlı çalışır).

---

### 2. Temel Komutlar ve Güvenlikteki Rolleri

#### A. Listeleme ve Navigasyon
- **`ls` (List):** Bulunduğun klasördeki dosyaları listeler. 
    - `ls -la`: Gizli dosyaları (nokta ile başlayan) ve izinleri gösterir. Siber güvenlikte `.ssh` veya `.bash_history` gibi gizli klasörleri bulmak için ilk adımdır.
- **`cd` (Change Directory):** Klasör değiştirir. `cd ..` bir üst klasöre çıkar.
- **`pwd` (Print Working Directory):** "Ben şu an tam olarak neredeyim?" sorusunun cevabıdır. Dosya sistemindeki tam yolunu (path) gösterir.

#### B. Dosya Okuma ve Analiz
- **`cat` (Concatenate):** Dosyanın içeriğini ekrana basar. Küçük dosyaları okumak için kullanılır.
- **`grep` (Global Regular Expression Print):** Metin içinde arama yapar. 
    - *Güvenlik Örneği:* Binlerce satırlık bir log dosyasında sadece "error" veya "failed login" kelimelerini bulmak için `grep "failed" auth.log` kullanılır.
- **`awk` (Metin İşleme):** Satır ve sütun bazlı karmaşık analizler yapar.
    - *Güvenlik Örneği:* Bir log dosyasının sadece 3. sütunundaki IP adreslerini çekmek istiyorsan `awk '{print $3}' log.txt` kullanırsın.
- **`sed` (Stream Editor):** Metin üzerinde toplu değişiklikler veya filtrelemeler yapar.

#### C. Arama ve Tespit
- **`find`:** Dosya sisteminde isim, boyut veya izin tipine göre dosya arar.
    - *Güvenlik Örneği:* Sistemdeki "SUID" bitine sahip (tehlikeli yetki) dosyaları bulmak için kullanılır.

---

### 3. Borulama (Piping) ve Yönlendirme (Redirection)
Siber güvenlik uzmanının en büyük gücü komutları birleştirmektir.
- **`|` (Pipe):** Soldaki komutun çıktısını, sağdaki komuta girdi olarak "fırlatır".
    - `ls -la /var/www | grep "config.php"`: Web sunucusundaki config dosyalarını bulur.
- **`>` (Yönlendirme):** Komut çıktısını bir dosyaya yazar (mevcut içeriği siler).
- **`>>` (Ekleme):** Çıktıyı mevcut dosyanın sonuna ekler (log tutmak için idealdir).

### 4. Neden Bilmelisin?
Saldırganlar sisteme sızdığında (örneğin bir web açığıyla), ellerinde bir grafik arayüz olmaz. Sadece bir metin satırı (shell) olur. Bu shell üzerinde ne kadar hakim olursan, sistemde o kadar derinlere inebilir veya analist olarak saldırganın ne yaptığını o kadar hızlı anlayabilirsin.