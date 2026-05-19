+++
title = "SQL Injection (SQLi)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
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