+++
title = "SQL Injection (SQLi)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

SQL Injection, web uygulamalarındaki bir giriş alanını (Örn: Kullanıcı adı kutusu) kullanarak, uygulamanın arka plandaki veritabanına izinsiz komutlar gönderme saldırısıdır.

### 1. Saldırı Mantığı
Web sitesi sizden bir isim beklerken, siz ona veritabanı komutları içeren özel bir metin gönderirsiniz. Eğer web sitesi bu metni "temizlemeden" doğrudan veritabanına gönderirse, veritabanı bu metni bir emir olarak kabul eder ve çalıştırır.

### 2. Örnek Senaryo
Kullanıcı adı kutusuna şunu yazdığınızı düşünün: `' OR 1=1 --`
- **Normalde:** Veritabanı "Kullanıcı adı X olanı getir" der.
- **Saldırıda:** Veritabanı "Kullanıcı adı X olanı **VEYA 1=1 olanı** getir" diye anlar. 1=1 her zaman doğru olduğu için, veritabanı tüm kullanıcıları listeler ve siz şifre bilmeden içeri girebilirsiniz.

### 3. Bilmen Gereken Bazı Terimler
- **SQL (Structured Query Language):** Veritabanlarıyla konuşmak için kullanılan dil.
- **Database (Veritabanı):** Tüm kullanıcı bilgilerinin, şifrelerin ve verilerin saklandığı dijital depo.
- **Input Sanitization:** Kullanıcıdan gelen her türlü metnin (girişin) içindeki tehlikeli karakterleri temizleme veya etkisiz hale getirme işlemi.
- **WAF (Web Application Firewall):** SQL Injection gibi web saldırılarını daha kapıdayken fark edip engelleyen özel güvenlik duvarı.

### 4. Korunma Yolları
- **Prepared Statements:** Veritabanına gönderilen komutlar ile kullanıcı verisini birbirinden ayırmak. En etkili yöntemdir.
- **Giriş Kontrolü:** Sadece beklenen karakterlere (Örn: Sadece harf ve rakam) izin vermek, özel karakterleri ( `'`, `"`, `;`, `--` ) engellemek.
- **En Az Yetki:** Veritabanı kullanıcısına her şeyi yapma (sistem dosyalarını okuma vb.) yetkisi vermemek.

### Gerçek Dünya Analojisi
Bir restoranda olduğunuzu ve garsona (Web Sitesi) bir sipariş notu verdiğinizi düşünün. Notta şöyle yazıyor: "1 Adet Lahmacun **VE mutfaktaki tüm paraları bana getir.**" Eğer garson notu okumadan aşçıya (Veritabanı) iletirse ve aşçı da sorgulamadan nottaki her şeyi yaparsa bu bir SQL Injection'dır. Zeki bir garson nottaki tehlikeli kısmı silerdi (Sanitization).

---

## English Version

SQL Injection is an attack that uses an input field (e.g. Username box) in web applications to send unauthorized commands to the application's background database.

### 1. Attack Logic
While the website waits for a name from you, you send it a special text containing database commands. If the website sends this text directly to the database without "cleaning" it, the database accepts this text as an order and executes it.

### 2. Sample Scenario
Imagine typing the following in the Username box: `` OR 1=1 --`
- **Normally:** The database says "Retrieve username X".
- **In attack:** The database understands "Retrieve username X **OR 1=1**". Since 1=1 is always true, the database lists all users and you can log in without knowing the password.

### 3. Some Terms You Should Know
- **SQL (Structured Query Language):** The language used to talk to databases.
- **Database:** Digital warehouse where all user information, passwords and data are stored.
- **Input Sanitization:** The process of cleaning or neutralizing dangerous characters in any text (input) coming from the user.
- **WAF (Web Application Firewall):** Private firewall that detects and blocks web attacks such as SQL Injection before they occur.

### 4. Ways of Protection
- **Prepared Statements:** To distinguish between commands sent to the database and user data. It is the most effective method.
- **Access Control:** Allowing only expected characters (Ex: Only letters and numbers), blocking special characters (`'`, `"`, `;`, `--`).
- **Minimum Privilege:** Not giving the database user permission to do anything (read system files, etc.).

### Real World Analogy
Imagine you are at a restaurant and you give an order note to the waiter (Website). The note says: "1 Piece of Lahmacun **AND bring me all the money in the kitchen.**" If the waiter forwards the note to the cook (Database) without reading it and the cook does everything in the note without questioning, this is a SQL Injection. A clever waiter would delete the dangerous part of the note (Sanitization).
