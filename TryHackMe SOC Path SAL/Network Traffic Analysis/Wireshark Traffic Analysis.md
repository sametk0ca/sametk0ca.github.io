
# Nmap Scans

Bu bölüm, bir ağ analistinin Wireshark kullanarak **Nmap** ile yapılan taramaları ağ trafiğinde nasıl tespit edip ayırt edebileceğini anlatmaktadır.


### 1. Temel TCP Bayrakları ve Filtreleri

Analiz yapabilmek için öncelikle Wireshark'ta TCP bayraklarını (flags) nasıl filtreleyeceğinizi bilmeniz gerekir:

- **SYN Bayrağı:** Bağlantı başlatmak için kullanılır. (`tcp.flags.syn == 1`)
    
- **ACK Bayrağı:** Onaylamak için kullanılır. (`tcp.flags.ack == 1`)
    
- **RST Bayrağı:** Bağlantıyı sıfırlamak/kesmek için kullanılır. (`tcp.flags.reset == 1`)
    
- **FIN Bayrağı:** Bağlantıyı sonlandırmak için kullanılır. (`tcp.flags.fin == 1`)
    

---

### 2. TCP Connect Taramaları (`nmap -sT`)

Bu tarama türü genellikle yetkili olmayan (root olmayan) kullanıcılar tarafından yapılır.

- **Özelliği:** 3'lü el sıkışma (3-way handshake) sürecini **tamamlar**.
    
- ==**Ayırt Edici Özellik:** Genellikle **Window Size (Pencere Boyutu) 1024 bayttan büyüktür**. Çünkü protokol doğası gereği veri almayı bekler.==
    
- **Açık Port Davranışı:**
    
    1. Saldırgan: SYN gönderir.
        
    2. Hedef: SYN, ACK gönderir.
        
    3. Saldırgan: ACK gönderir (Bağlantı kurulur).
        
- **Kapalı Port Davranışı:** Hedef, RST/ACK döner.
    
- Wireshark Filtresi:
    
    ==tcp.flags.syn 1 and tcp.flags.ack == 0 and tcp.window_size > 1024==
    

---

### 3. SYN Taramaları (`nmap -sS`)

Bu tarama türü, "Stealth" (gizli) tarama olarak da bilinir ve yetkili (root) kullanıcılar tarafından yapılır.

- **Özelliği:** 3'lü el sıkışma sürecini **tamamlamaz**. Yarı açık taramadır.
    
- **Ayırt Edici Özellik:** Genellikle **Window Size (Pencere Boyutu) 1024 bayta eşit veya küçüktür**. Çünkü bağlantı tamamlanmadığı için veri almayı beklemez.
    
- **Açık Port Davranışı:**
    
    1. Saldırgan: SYN gönderir.
        
    2. Hedef: SYN, ACK gönderir.
        
    3. Saldırgan: **RST** gönderir (Bağlantıyı hemen keser).
        
- Wireshark Filtresi:
    
    tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size <= 1024
    

---

### 4. UDP Taramaları (`nmap -sU`)

UDP bağlantısız (connectionless) bir protokoldür, bu yüzden el sıkışma yoktur.

- **Açık Port Davranışı:** Genellikle sunucudan hiçbir cevap gelmez (paket düşer veya kabul edilir ama yanıt dönmez).
    
- **Kapalı Port Davranışı:** Hedef sunucu, **ICMP Type 3, Code 3 (Destination Unreachable: Port Unreachable)** hatası döner. Bu, portun kapalı olduğunu kanıtlar.
    
- **Analiz İpucu:** Wireshark'ta dönen ICMP hata paketinin içine bakıldığında, hataya sebep olan orijinal UDP isteği (saldırganın paketi) görülebilir.
    
- Wireshark Filtresi:
    
    icmp.type==3 and icmp.code==3
    

### Özet

Bu döküman, bir siber güvenlik analistinin Wireshark üzerinde;

1. Tam bağlantı kuran taramaları (**TCP Connect** - Büyük window size),
    
2. Yarı açık taramaları (**SYN Scan** - Küçük window size),
    
3. Ve **UDP** taramalarını (ICMP hata mesajları ile)
    

nasıl tespit edebileceğini filtrelerle birlikte öğretmektedir.



---


---

### 1. ARP Nedir ve Neden Zayıftır?

Sayfa, ARP'nin (Address Resolution Protocol) çalışma mantığını anlatarak başlıyor.

- **Görevi:** IP adreslerini (mantıksal adres) MAC adreslerine (fiziksel adres) çevirmektir.
    
- **Zafiyeti:** ARP "stateless" (durumsuz) bir protokoldür. Yani bir cihaz, hiç istek göndermemiş olsa bile kendisine gelen "Benim MAC adresim bu!" (ARP Reply) mesajına **sorgusuz sualsiz güvenir**.
    
- **Sonuç:** Bu güveni kötüye kullanan saldırgan, kurbana sürekli yalan söyleyerek kendini "Modem" (Gateway) gibi tanıtabilir.
    

### 2. Saldırı Mantığı (MITM)

Saldırgan (Attacker), kurban (Victim) ile modem (Gateway) arasına girer.

- Saldırgan, Kurban'a der ki: "192.168.1.1 (Modem) benim."
    
- Saldırgan, Modem'e der ki: "192.168.1.10 (Kurban) benim."
    
- Böylece tüm trafik saldırganın üzerinden akar (**Man-in-the-Middle**). Wireshark'ta bu durumu, normalde doğrudan modeme gitmesi gereken paketlerin saldırganın MAC adresine yönelmesinden anlarız.
    

### 3. Wireshark ile Tespit ve Analiz

Döküman, bu saldırıyı tespit etmek için şu adımları ve ipuçlarını veriyor:

- **Filtre:** `arp` filtresi ile trafiği daraltın.
    
- **Opcode Kontrolü:**
    
    - `arp.opcode == 1`: İstek (Request - "Kimde?")
        
    - **`arp.opcode == 2`**: Cevap (Reply - "Bende!") — _Saldırının ana silahı budur._
        
- **Gürültü (Spam):** Saldırgan, kurbanın "doğruyu" hatırlamaması için sürekli (spam şeklinde) ARP Reply paketleri gönderir. Kırmızıya boyanmış yoğun bir ARP trafiği görürsen şüphelenmelisin.
    
- **Wireshark Uyarısı (Duplicate IP):** Wireshark akıllıdır; eğer aynı IP adresi kısa süre içinde iki farklı MAC adresiyle görülürse, "Info" sütununda veya paket detaylarında **"Duplicate IP address detected"** (Çift IP adresi tespit edildi) uyarısı verir. Bu, saldırının "sigara dumanıdır" (kesin kanıtıdır).
    

Bu metin, bir siber güvenlik analistinin ağ trafiğini incelerken sadece IP veya MAC adreslerine bağlı kalmayıp, **cihazların isimlerini (Hostname)** ve **kullanıcı adlarını (Username)** nasıl tespit edebileceğini anlatmaktadır.

Kurumsal ağlarda cihazlar ve kullanıcılar genellikle belirli bir isimlendirme standardına göre adlandırılır. Bu isimleri bulmak, saldırının kaynağını veya kurbanı tespit etmek için kritik bir adımdır.

Metinde bu tespit işlemi için kullanılan üç ana protokol ve Wireshark filtreleri açıklanmaktadır:

### 1. DHCP Analizi (Otomatik IP Dağıtımı)

DHCP, cihazlara otomatik IP adresi atayan protokoldür. Cihazlar IP adresi talep ederken genellikle kendi isimlerini (Hostname) de pakete eklerler, bu da analist için en kolay bilgi toplama yöntemlerinden biridir.

- **Mantık:** Cihaz IP ister (Request), sunucu kabul eder (ACK) veya reddeder (NAK).
    
- **Önemli Paket:** **DHCP Request** paketleri (Option 53 = 3). Bu paketler cihazın ismini içerir.
    
- **Wireshark Filtreleri:**
    
    - Genel arama: `dhcp` veya `bootp`.
        
    - İstek paketleri (Hostname içerir): `dhcp.option.dhcp == 3`.
        
    - Hostname içinde kelime arama: `dhcp.option.hostname contains "keyword"`.
        
    - Diğer önemli bilgiler: Option 12 (Hostname), Option 50 (İstenen IP), Option 61 (MAC adresi).
        

### 2. NetBIOS (NBNS) Analizi

NetBIOS, yerel ağdaki cihazların ve uygulamaların birbirleriyle isimleri üzerinden iletişim kurmasını sağlayan eski bir teknolojidir.

- **Mantık:** Cihazlar ağda birbirlerini bulmak için isim sorguları gönderir.
    
- **Önemli Bilgi:** Sorgular (Queries) cihazın ismini, IP adresini ve TTL değerini içerebilir.
    
- **Wireshark Filtreleri:**
    
    - Genel arama: `nbns`.
        
    - İsim arama: `nbns.name contains "keyword"`.
        

### 3. Kerberos Analizi (Windows Kimlik Doğrulama)

Kerberos, Windows domain ortamlarında kullanılan varsayılan kimlik doğrulama protokolüdür. Kullanıcıların ve hizmetlerin kimliğini doğrulamak için kullanılır.

- **Mantık:** Bir kullanıcı veya bilgisayar sisteme giriş yaparken kimlik kanıtı sunar. Bu trafik, **kullanıcı adlarını** tespit etmek için mükemmeldir.
    
- **Kritik Ayrım:** Kerberos trafiğinde hem kullanıcı adları hem de bilgisayar isimleri (Hostname) görünebilir.
    
    - **Bilgisayar İsimleri:** Genellikle sonu **$** işaretiyle biter (Örn: `DESKTOP-123$`).
        
    - **Kullanıcı Adları:** $ işareti içermez (Örn: `samet.kocats`).
        
- **Wireshark Filtreleri:**
    
    - Genel arama: `kerberos`.
        
    - Kullanıcı adı arama (CNameString): `kerberos.CNameString contains "keyword"`.
        
    - Sadece Kullanıcıları Bulmak İçin (Bilgisayarları Eler):
        
        kerberos.CNameString and !(kerberos.CNameString contains "$").
        

### Özet

Bu döküman sana diyor ki: "Sadece IP adresine bakıp geçme."

1. **DHCP** paketlerine bakarak cihazın ismini (**Hostname**) bul.
    
2. **NetBIOS** sorgularına bakarak yerel ağdaki isimlendirmeyi gör.
    
3. **Kerberos** trafiğine bakarak o cihazda hangi **kullanıcının** (Username) oturum açtığını tespit et.



---

---

### 1. Trafik Tünelleme (Traffic Tunnelling) Nedir?

Tünelleme, veriyi başka bir protokolün içine gizleyerek taşıma işlemidir.

- **Analoji:** Hani filmlerde kaçakçılar değerli mücevherleri sıradan bir oyuncak ayının içine saklayıp gümrükten geçirirler ya? Tünelleme tam olarak budur.
    
- **Siber Dünyada:** Saldırgan, yasaklı verileri (mücevherleri), güvenlik duvarının güvendiği ve izin verdiği protokollerin (oyuncak ayıların) içine gizler. En çok kullanılan "güvenilir" kılıflar **ICMP** ve **DNS**'tir.
    

---

### 2. ICMP Analizi (Ping'in İçine Veri Saklamak)

ICMP normalde ağdaki hataları raporlamak ve cihazların erişilebilirliğini test etmek (Ping atmak) için kullanılır.

- **Saldırı Yöntemi:** Saldırgan, Ping paketlerinin veri taşıyabilme özelliğini kötüye kullanır. Normalde boş olması gereken veya standart veri taşıyan Ping paketinin içine çaldığı verileri (SSH, HTTP verisi vb.) koyar.
    
- **C2 (Command & Control):** Saldırgan, zararlı yazılımla haberleşmek için bu kanalı kullanır.
    
- **Nasıl Tespit Edilir?**
    
    - **Paket Boyutu:** Normal bir Ping paketi genellikle küçüktür (standart 64 byte civarı). Eğer ağda **devasa boyutlu Ping paketleri** görüyorsan, içinde bir şeyler kaçırılıyor olabilir.
        
- **Wireshark Filtresi:**
    
    - `data.len > 64 and icmp` -> (Veri boyutu 64 bayttan büyük olan ICMP paketlerini göster).
        

---

### 3. DNS Analizi (Adres Defterini Kötüye Kullanmak)

DNS, internetin telefon rehberidir (Domain adını IP'ye çevirir). Her ağda DNS trafiğine izin verilir, bu yüzden saldırganlar için mükemmel bir kaçış yoludur.

- **Saldırı Yöntemi:** Saldırgan kendine ait bir domain (örn: `kotu-site.com`) alır. Kurban bilgisayardaki virüs, saldırgana veri göndermek istediğinde bunu DNS sorgusu gibi yapar.
    
- **Örnek:** `sifreleriniz-burada.kotu-site.com` diye bir adresi sorgular.
    
    - DNS sunucusu bu sorguyu alır ve saldırganın sunucusuna iletir. Saldırgan, "sifreleriniz-burada" kısmını okur ve veriyi almış olur.
        
- **Nasıl Tespit Edilir?**
    
    - **Sorgu Uzunluğu:** Normalde `google.com` gibi kısa adresler sorgulanır. Çok uzun ve anlamsız harflerden oluşan subdomain sorguları (örn: `a1b2c3d4e5f6...g7.site.com`) şüphelidir.
        
    - **Hacim:** Bir bilgisayar durmaksızın aynı domaine yüzlerce garip sorgu gönderiyorsa, bu bir tünellemedir.
        
- **Wireshark Filtreleri:**
    
    - `dns contains "dnscat"` -> (Bilinen bir DNS tünelleme aracı olan dnscat'i arar).
        
    - `dns.qry.name.len > 15 and !mdns` -> (Yerel ağ trafiği hariç, ismi 15 karakterden uzun olan DNS sorgularını göster).
        

### Özetle

Saldırganlar, güvenlik sistemlerinin "Bu Ping paketidir, zararsızdır" veya "Bu DNS sorgusudur, internete girmek için lazımdır" diyerek kapıyı açtığı anı bekler ve veriyi bu paketlerin içine gizleyerek kaçırır. Senin görevin, paketlerin boyutlarına ve isimlerin garipliğine bakarak bu "truva atlarını" yakalamaktır.


---


---

### 1. FTP Nedir ve Neden Risklidir?

FTP, dosya transferi için tasarlanmış çok eski ve basit bir protokoldür. En büyük zafiyeti **şifreleme kullanmamasıdır**.

- **Risk:** Ağdaki trafiği dinleyen herhangi biri (Man-in-the-Middle), gönderilen dosyaları, **kullanıcı adlarını ve şifreleri** olduğu gibi (cleartext) okuyabilir.
    
- **Olası Saldırılar:** Kimlik hırsızlığı, yetkisiz erişim, veri kaçırma ve zararlı yazılım yükleme.
    

### 2. Wireshark ile FTP Analizi Nasıl Yapılır?

Analist olarak amacın "kolay hedefleri" (low-hanging fruits) toplamak. Bunun için **Komutlar (Client'tan giden)** ve **Cevap Kodları (Server'dan gelen)** izlenir.

#### A. FTP İstekleri (Client -> Server)

Kullanıcının ne yapmaya çalıştığını gösterir.

- **Filtre:** `ftp.request.command`
    
- **Önemli Komutlar:**
    
    - `USER`: Kullanıcı adını gönderir.
        
    - `PASS`: **Şifreyi gönderir.** (En kritik kısım burasıdır, şifre açıkça görülür).
        
    - `CWD`: Klasör değiştirme (Current Work Directory).
        
    - `LIST`: Dosyaları listeleme.
        

#### B. FTP Cevap Kodları (Server -> Client)

Sunucunun kullanıcının isteğine ne cevap verdiğini gösterir. Kodlar serilere ayrılır:

- **x2x Serisi (Bağlantı Mesajları - Başarılı):**
    
    - **200:** Komut başarılı.
        
    - **220:** Servis hazır (Bağlantı kuruldu).
        
        
    - _Filtre:_ `ftp.response.code == 220
        
- **x3x Serisi (Kimlik Doğrulama):**

    - ==**230:** **Kullanıcı girişi başarılı.** (Bir saldırganın içeri sızıp sızmadığını anlamak için en kritik koddur).==
    - **331:** Kullanıcı adı geçerli, şimdi şifreyi gir.
    
    - **430:** Geçersiz kullanıcı adı veya şifre.
        
    - ==**530:** **Giriş başarısız** (Hatalı şifre vb.).==
        
    - ==_Filtre:_ `ftp.response.code == 530`==
        

### 3. Saldırı Tespiti (Advanced Usage)

Wireshark filtrelerini birleştirerek saldırı türlerini tespit edebilirsin:

1. **Kaba Kuvvet (Brute-Force) Saldırısı:**
    
    - Bir kullanıcı adına sürekli yanlış şifre denenmesi durumudur.
        
    - **Belirtisi:** Arka arkaya gelen çok sayıda **530 (Login Failed)** hatası.
        
    - _Filtre:_ `ftp.response.code == 530` (Bunu kullanıcı adına göre daraltabilirsin).
        
2. **Parola Püskürtme (Password Spraying):**
    
    - Saldırganın tek bir şifreyi (örn: "Password123") birçok farklı kullanıcı adı üzerinde denemesidir (Hesap kilitlenmesini önlemek için).
        
    - _Filtre:_ `(ftp.request.command == "PASS") and (ftp.request.arg == "password")`
        

### Özet Strateji

Eğer bir FTP trafiğini inceliyorsan:

1. Önce `ftp` yazıp genel trafiğe bak.
    
2. `ftp.response.code == 230` yazıp başarılı giriş yapanları bul.
    
3. Eğer şüpheli bir giriş varsa, ilgili akışı takip et (`Follow TCP Stream`) ve `PASS` komutuna bakarak saldırganın çaldığı veya kullandığı şifreyi gör.
    
4. `ftp.response.code == 530` ile başarısız denemeleri kontrol et (Brute-force var mı?).
    



---

### 1. HTTP Analizine Giriş

HTTP (Hypertext Transfer Protocol), internetin temel iletişim dilidir. İstemci (senin tarayıcın) bir istekte bulunur, sunucu da cevap verir.

- **Özelliği:** "Cleartext" yani şifresizdir. Trafik içerisindeki her şey (parolalar, sayfalar, komutlar) okunabilir.
    
- **Önemi:** Şifresiz olduğu ve hemen hemen hiçbir güvenlik duvarı tarafından engellenmediği için (çünkü internete girmek zorundayız), saldırganlar için ana oyun alanıdır.
    
- **Tespit Edilebilen Saldırılar:**
    
    - Phishing (Oltalama) sayfaları.
        
    - Web saldırıları (SQLi, XSS vb.).
        
    - Veri kaçırma (Data Exfiltration).
        
    - C2 (Komuta Kontrol) trafiği.
        

_(Not: HTTP2 daha yeni, hızlı ve güvenli bir versiyondur ancak analiz mantığı benzerdir.)_

---

### 2. Wireshark ile "Kolay Hedefleri" (Low-Hanging Fruits) Toplamak

Analiz yaparken milyonlarca paket arasından işimize yarayanları cımbızla çekmemiz gerekir. İşte bakılması gereken 3 ana bölge:

#### A. İstek Metotları (Request Methods)

Saldırganın ne yapmaya çalıştığını gösterir.

- **GET:** Bilgi/Sayfa istemek için kullanılır. (Genel gezinme).
    
- **POST:** Sunucuya veri göndermek için kullanılır. (Giriş yapma, dosya yükleme, form doldurma). **Veri kaçırma** veya **zararlı yükleme** genellikle burada olur.
    
- _Filtre:_ `http.request.method == "POST"`
    

#### B. Cevap Kodları (Response Status Codes)

Sunucunun bu isteklere ne cevap verdiğini gösterir.

- **200 (OK):** Saldırı başarılı olmuş olabilir (İstek kabul edildi).
    
- **301/302 (Moved):** Yönlendirme. Phishing saldırılarında kurbanı sahte siteye yönlendirmek için sıkça kullanılır.
    
- **401/403 (Unauthorized/Forbidden):** Saldırgan yetkisiz bir yere (Admin paneli vb.) girmeye çalışıyor demektir.
    
- **404 (Not Found):** Tarama (Scan) belirtisidir. Saldırgan rastgele dosyalar arıyordur (örn: `admin.php`, `backup.zip`).
    
- **500 (Internal Error):** Saldırgan sunucuyu bozmuş veya bir zafiyeti (SQL Injection gibi) tetiklemiş olabilir.
    

#### C. HTTP Parametreleri

İsteğin detaylarında gizlenen ipuçlarıdır.

- **URI (Uniform Resource Identifier):** Hangi dosyanın istendiği. (Örn: `/admin/login.php`). Filtre: `http.request.uri contains "admin"`.
    
- **Host:** İsteğin hangi siteye gittiği. (Örn: `malicious-site.com`).
    
- **HTML Form URL Encoded:** Bir POST işleminde gönderilen verilerdir (Kullanıcı adı, Parola burada görünür).
    

---

### 3. User Agent (Kullanıcı Aracısı) Analizi

User Agent (UA), tarayıcının web sitesine girerken gösterdiği "Kimlik Kartı"dır. (Örn: "Ben Chrome kullanıyorum, Windows 10 üzerindeyim").

- **Saldırganın Taktığı Maske:** Saldırganlar dikkat çekmemek için bu kimliği taklit ederler. Ancak bazen hatalar yaparlar.
    
- **Tespit Yöntemleri:**
    
    1. **Tutarsızlık:** Aynı IP adresinden kısa süre içinde farklı User Agent'lar geliyorsa şüphelidir.
        
    2. **Yazım Hataları:** Saldırgan sahte kimlik oluştururken "Mozilla" yerine "Mozlilla" yazabilir.
        
    3. **Saldırı Araçları:** Bazı araçlar (Nmap, Sqlmap, Nikto) varsayılan olarak kendi isimlerini User Agent kısmında açıkça söylerler.
        
    4. **Zararlı Kod:** Bazen saldırganlar (Log4j örneğindeki gibi) saldırı kodunu User Agent satırının içine gizlerler.
        
- _Altın Kural:_ User Agent'ı asla güvenilir olarak işaretleme (whitelist), çünkü değiştirilmesi en kolay veridir.
    

---

### 4. Log4j Zafiyet Analizi (Örnek Vaka)

Metin, ünlü **Log4j** zafiyetinin Wireshark'ta nasıl tespit edileceğini bir vaka çalışması olarak anlatıyor.

- **Saldırı Doğası:** Saldırgan sunucuya özel bir komut dizisi gönderir ve sunucu bu komutu işlemeye çalışırken saldırganın sunucusuna bağlanır.
    
- **İmzalar (Signatures):**
    
    1. Genellikle **POST** isteği ile başlar.
        
    2. Paket içinde **`jndi:ldap`** veya **`Exploit.class`** gibi ifadeler geçer.
        
    3. User Agent veya diğer başlıklarda **`${...}`** gibi değişken karakterleri bulunur.
        
- _Wireshark Filtreleri:_
    
    - `http.request.method == "POST"`
        
    - `ip contains "jndi"` (Paket içinde jndi kelimesini arar).
        
    - `http.user_agent contains "$"` (User agent içinde $ işareti arar).
        

### Özet

Bu bölüm sana şunu öğretiyor: HTTP trafiği şifresiz olduğu için, bir dedektif gibi paketlerin içine girip; kimin ne istediğini (**Method**), sunucunun ne dediğini (**Status Code**), kimlik kartlarını (**User Agent**) ve gizlenmiş sinsi komutları (**Log4j, JNDI**) okuyarak saldırıyı çözebilirsin.


---

---

### 1. Sorun: HTTPS "Karanlık Oda"dır

Normal HTTP trafiği şeffaftır, her şey okunabilir. Ancak HTTPS, **TLS (Transport Layer Security)** protokolünü kullanarak iletişimi şifreler.

- **Analist İçin Sorun:** Paketleri yakalasanız bile, içeriği (hangi URL'ye gidildiği, hangi verinin indirildiği) göremezsiniz. Sadece anlamsız, şifreli veriler (Application Data) görürsünüz.
    
- **Risk:** Saldırganlar da gizlenmek için HTTPS kullanır. Bu yüzden "şifreli trafik güvenlidir" deyip geçemeyiz, içine bakmamız gerekir.
    

### 2. Şifreyi Çözmeden Neleri Görebiliriz? (Handshake)

Şifreli veri akışı başlamadan önce, istemci (tarayıcı) ve sunucu arasında bir **"El Sıkışma" (Handshake)** gerçekleşir. Bu aşama şifresizdir ve bazı temel bilgileri sızdırır.

![TLS Handshake Diagram resmi](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcT9nBhn_a1mr3S1rxIidDJnFUKvs86ZQqKmV0Qids5gklYl9Kd88LnvQA7v8Fd_hkhYmfHhQyKzoPnxH3wjw7h2AmwRl4-v5YxSNAN_IVY1IuJcq84)



- **Client Hello (İstemci Merhaba):** Tarayıcı, sunucuya "Benimle güvenli konuş" der.
    
    - _Filtre:_ `tls.handshake.type == 1`
        
- **Server Hello (Sunucu Merhaba):** Sunucu, "Tamam, şu şifreleme yöntemini kullanacağız" der.
    
    - _Filtre:_ `tls.handshake.type == 2`
        

Bu paketler sayesinde en azından **kimin (IP adresi)** şifreli bağlantı kurmaya çalıştığını görebiliriz.

### 3. Şifreyi Çözmek: Anahtar Dosyası (Key Log File)

Şifreli trafiğin içini (HTTP verisini) görebilmek için şifreleme anahtarlarına ihtiyacınız vardır. Wireshark bu şifreyi kendi başına kıramaz, anahtarı sizin vermeniz gerekir.

- **SSLKEYLOGFILE:** Tarayıcılar (Chrome, Firefox), bir ortam değişkeni (Environment Variable) ayarlandığında, her oturum için ürettikleri şifreleme anahtarlarını bir metin dosyasına (log) kaydedebilirler.
    
- **Kritik Kural:** Anahtarlar, bağlantı kurulduğu an üretilir. Trafiği kaydettikten _sonra_ anahtar oluşturamazsınız. **Trafik kaydı (pcap) alınırken anahtar kaydı da eş zamanlı yapılmalıdır**.
    

### 4. Wireshark'ta Şifre Çözme İşlemi

Elinizde hem `.pcap` dosyası hem de o oturuma ait `.log` (anahtar) dosyası varsa, Wireshark'ta şifreyi şöyle çözersiniz:

1. **Menü:** `Edit` --> `Preferences` --> `Protocols` --> `TLS` yolunu izleyin.
    
2. **Dosyayı Yükle:** "(Pre)-Master-Secret log filename" kısmına elinizdeki anahtar dosyasını (key log file) ekleyin.
    
3. **Sonuç:** Wireshark ekranı değişecektir. Daha önce "TLS Encrypted Alert" veya "Application Data" olarak görünen satırlar, artık **HTTP** veya **HTTP2** olarak açık bir şekilde görünecek ve URL'ler, dosyalar okunabilir hale gelecektir.
    

### Özetle

Bu görev sana şunu öğretiyor: "Şifreli trafiği (HTTPS) analiz etmek imkansız değildir, sadece doğru anahtara (Key Log File) ihtiyacın vardır." Anahtarı Wireshark'a verdiğin an, şifreli trafik şeffaf bir HTTP trafiğine dönüşür.