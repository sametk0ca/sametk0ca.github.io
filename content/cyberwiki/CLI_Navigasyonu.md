+++
title = "CLI (Komut Satırı) Navigasyonu - Teknik Detaylar | CLI (Command Line) Navigation - Technical Details"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

Command line is a method of talking to a computer without a graphical interface (mouse, icons), just text-based commands.

### 1. What is Shell?
**Shell** is a "translator" that takes commands from the user and forwards them to the **Kernel**, the heart of the operating system. 
- **Why is it called Shell?** This name was given because it acts as a shell that protects the kernel from direct interventions from outside.
- **Common Sheller:**
    - **Bash (Bourne Again Shell):** The most common standard in Linux.
    - **Zsh:** Modern Linux and macOS (default) shell.
    - **PowerShell:** Advanced shell of Windows (.NET based, works object-oriented, not just text).

---

### 2. Basic Commands and Their Role in Security

#### A. Listing and Navigation
- **`ls` (List):** Lists the files in the current folder. 
    - `ls -la`: Shows hidden files (starting with a dot) and permissions. In cyber security, it is the first step to find hidden folders like `.ssh` or `.bash_history`.
- **`cd` (Change Directory):** Changes folder. `cd ..` extracts to a higher folder.
- **`pwd` (Print Working Directory):** "Where exactly am I right now?" is the answer to the question. Shows the full path in the file system.

#### B. File Reading and Analysis
- **`cat` (Concatenate):** Prints the content of the file to the screen. It is used to read small files.
- **`grep` (Global Regular Expression Print):** Searches within text. 
    - *Security Example:* `grep "failed" auth.log` is used to find only the words "error" or "failed login" in a log file with thousands of lines.
- **`awk` (Text Processing):** Performs complex row and column based analysis.
    - *Security Example:* If you only want to retrieve the IP addresses in the 3rd column of a log file, you would use `awk '{print $3}' log.txt`.
- **`sed` (Stream Editor):** Makes bulk changes or filters on the text.

#### C. Search and Detection
- **`find`:** Searches for files in the file system by name, size or permission type.
    - *Security Example:* It is used to find files with the "SUID" bit (dangerous authorization) in the system.

---

### 3. Piping and Redirection
The greatest power of a cyber security expert is combining commands.
- **`|` (Pipe):** "Pipes" the output of the left command as input to the right command.
    - `ls -la /var/www | grep "config.php"`: Finds config files on the web server.
- **`>` (Redirect):** Writes the command output to a file (deletes the current content).
- **`>>` (Append):** Appends the output to the end of the current file (ideal for logging).

### 4. Why Should You Know?
When attackers infiltrate the system (e.g. via a web exploit), they don't have a graphical interface at their disposal. It is just a line of text (shell). The more you master this shell, the deeper you can go into the system or the faster you can understand what the attacker is doing as an analyst.
