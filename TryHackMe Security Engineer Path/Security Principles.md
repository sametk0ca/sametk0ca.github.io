Security has become a buzzword; every company wants to claim its product or service is secure. But is it?

Before we start discussing the different security principles, it is vital to know the adversary against whom we are protecting our assets. Are you trying to stop a toddler from accessing your laptop? Or are you trying to protect a laptop that contains technical designs worth millions of dollars? Using the exact protection mechanisms against toddlers and industrial espionage actors would be ludicrous. Consequently, knowing our adversary is a must so we can learn about their attacks and start implementing appropriate security controls.

It is impossible to achieve perfect security; ==no solution is 100% secure.== Therefore, we try to improve our security posture to make it more difficult for our adversaries to gain access.

The objective of this room is to:

- Explain the security functions: Confidentiality, Integrity and Availability (CIA).
- Present the opposite of the security triad, CIA: Disclosure, Alteration, and Destruction/Denial (DAD).
- Introduce the fundamental concepts of security models, such as the Bell-LaPadula model.
- Explain security principles such as Defence-in-Depth, Zero Trust, and Trust but Verify.
- Introduce ISO/IEC 19249.
- Explain the difference between Vulnerability, Threat, and Risk.

![[Pasted image 20260310133405.png]]
- **Confidentiality** ensures that only the intended persons or recipients can access the data.
- **Integrity** aims to ensure that the data cannot be altered; moreover, we can detect any alteration if it occurs.
- **Availability** aims to ensure that the system or service is available when needed.

![[Pasted image 20260310134056.png]]

The security of a system is attacked through one of several means. It can be via the disclosure of secret data, alteration of data, or destruction of data.

- **Disclosure** is the opposite of confidentiality. In other words, disclosure of confidential data would be an attack on confidentiality.
- **Alteration** is the opposite of Integrity. For example, the integrity of a cheque is indispensable.
- **Destruction/Denial** is the opposite of Availability.

The opposite of the CIA Triad would be the DAD Triad: Disclosure, Alteration, and Destruction.

# Fundamental Concepts of Security Models

### Bell-LaPadula Model

Siber güvenlikte (ve özellikle güvenli işletim sistemlerinde) **Bell-LaPadula (BLP)** modeli, gizliliği korumak için tasarlanmış en temel formal erişim kontrol modelidir. 1970'lerde ABD Savunma Bakanlığı için geliştirilmiştir.

Bu modelin ana felsefesi şudur: **Verinin sızmasını engellemek.**

### 1. Temel Kavramlar

BLP modeli iki ana unsur üzerine kuruludur:

- **Subject (Özne):** Dosyaya erişmek isteyen kullanıcı veya süreç.
    
- **Object (Nesne):** Veri içeren dosya, veritabanı veya cihaz.
    

Sistemdeki her özne ve nesneye bir **Güvenlik Seviyesi** (Gizli, Çok Gizli vb.) atanır.

---

### 2. İki Altın Kural

BLP modelini "aşılmaz" kılan iki temel kural vardır. Bu kurallar verinin düşük güvenlik seviyesinden yüksek seviyeye çıkmasına izin verirken, yüksekten düşüğe inmesini yasaklar.

#### A. Basit Güvenlik Özelliği (Simple Security Property)

**Kural:** "Yukarıyı okuma" (No Read Up).

Bir kullanıcı, kendi güvenlik seviyesinden daha yüksek bir seviyedeki dosyayı okuyamaz.

- _Örnek:_ "Gizli" yetkisi olan bir personel, "Çok Gizli" bir dosyayı açamaz.
    

#### B. Yıldız (*) Özelliği (Star Property)

**Kural:** "Aşağıyı yazma" (No Write Down).

Yüksek güvenlik seviyesindeki bir kullanıcı, alt seviyedeki bir dosyaya veri yazamaz.

- **Neden?** Bu kural, "Çok Gizli" bilgilere erişimi olan birinin, bu bilgileri yanlışlıkla veya kasıtlı olarak "Genel" bir dosyaya kopyalayıp sızdırmasını önlemek içindir.
    

---

### 3. Güçlü Yönleri ve Zafiyetleri

|**Özellik**|**Açıklama**|
|---|---|
|**Odak Noktası**|Sadece **Gizlilik (Confidentiality)** üzerine kuruludur.|
|**Veri Bütünlüğü**|Verinin değiştirilip değiştirilmediğiyle (Integrity) ilgilenmez.|
|**Kullanım Alanı**|Genellikle askeri sistemler ve devlet kurumları.|

> **Önemli Not:** Eğer amacın verinin doğruluğunu korumaksa (örneğin bankacılık verileri), Bell-LaPadula yetersiz kalır. Bu durumda tam tersi mantıkla çalışan **Biba Modeli** kullanılır.

---

### 4. Özet Mantık

Bu modeli bir binadaki yetkilendirme gibi düşünebilirsin:

- En üst kattaki (Çok Gizli) belgeleri alt kattakiler göremez (**No Read Up**).
    
- En üst kattakiler, ellerindeki gizli belgeleri alt kattaki herkesin görebileceği panolara asamaz (**No Write Down**).

### Biba Model

Bell-LaPadula modelinin tam tersi olarak düşünebileceğin **Biba Modeli**, gizliliğe değil **Bütünlüğe (Integrity)** odaklanır. 1977 yılında Ken Biba tarafından geliştirilmiştir.

Eğer Bell-LaPadula "Sır saklamak" içinse, Biba "Verinin bozulmasını veya manipüle edilmesini engellemek" içindir.
### 1. Temel Felsefesi

Biba modelinde en önemli kural şudur: **Düşük güvenilirlikteki bir kaynak, yüksek güvenilirlikteki bir kaynağı kirletemez.** Bu modelde nesnelerin (dosyaların) ve öznelerin (kullanıcıların) bir "Bütünlük Seviyesi" vardır. Seviye ne kadar yüksekse, verinin o kadar doğru ve güvenilir olduğu varsayılır.

---

### 2. İki Temel Kural

Biba modelini ayakta tutan iki ana kural, Bell-LaPadula'nın tam simetriğidir:

#### A. Basit Bütünlük Özelliği (Simple Integrity Property)

**Kural:** "Aşağıyı okuma" (No Read Down).

Bir kullanıcı, kendi bütünlük seviyesinden daha düşük seviyedeki bir veriyi okuyamaz.

- **Neden?** Çünkü alt seviyedeki veri "kirli" veya "güvenilmez" olabilir. Eğer yüksek seviyeli bir süreç (örneğin bir sistem çekirdeği), düşük seviyeli (güvenilmeyen) bir dosyayı okursa, kendi bütünlüğü bozulabilir.
    

#### B. Yıldız (*) Bütünlük Özelliği (Star Integrity Property)

**Kural:** "Yukarıyı yazma" (No Write Up).

Bir kullanıcı, kendi seviyesinden daha yüksek bir seviyedeki dosyaya veri yazamaz veya onu değiştiremez.

- **Neden?** Düşük yetkili veya daha az güvenilen birinin, sistemin kritik ve yüksek bütünlüklü dosyalarını bozmasını engellemek içindir.
    

---

### 3. Bell-LaPadula vs. Biba Karşılaştırması

SOC analisti olarak bu ikisi arasındaki farkı bilmek, bir sistemin neden belirli bir kısıtlamaya sahip olduğunu anlamanı sağlar.

|**Özellik**|**Bell-LaPadula**|**Biba**|
|---|---|---|
|**Öncelik**|Gizlilik (Confidentiality)|Bütünlük (Integrity)|
|**Okuma Kuralı**|Yukarıyı Okuma Yok (No Read Up)|Aşağıyı Okuma Yok (No Read Down)|
|**Yazma Kuralı**|Aşağıyı Yazma Yok (No Write Down)|Yukarıyı Yazma Yok (No Write Up)|
|**Slogan**|Sırları koru.|Kirlenmeyi önle.|


### Clark-Wilson Model

Bell-LaPadula ve Biba modelleri askeri kökenli ve daha teorik modellerken, **Clark-Wilson Modeli** tamamen ticari dünyadaki "Bütünlük" (Integrity) ihtiyacını karşılamak için 1987 yılında geliştirilmiştir.

Biba modelinden en büyük farkı, sadece "kimin neyi değiştirebileceğine" değil, verinin **nasıl** değiştirildiğine ve değişim sürecinin ne kadar **doğru** olduğuna odaklanmasıdır.

---

### 1. Temel Bileşenler

Clark-Wilson modeli, veriyi ve bu veriye erişim yöntemlerini üç ana gruba ayırır:

- **CDI (Constrained Data Items):** Bütünlüğü korunması gereken kritik verilerdir. (Örn: Banka bakiyesi, envanter kayıtları).
    
- **UDI (Unconstrained Data Items):** Bütünlüğü kritik olmayan veya dış dünyadan gelen işlenmemiş verilerdir. (Örn: Kullanıcı girişleri, geçici dosyalar).
    
- **TP (Transformation Procedures):** Veriyi (CDI) değiştirebilen tek yasal yoldur. Kullanıcı veriye doğrudan dokunamaz; sadece bir TP (yazılım/program) aracılığıyla müdahale edebilir.
    

---

### 2. İki Ana Mekanizma

Bu model, bütünlüğü sağlamak için şu iki süreci şart koşar:

#### A. Doğrulama (Integrity Verification Procedures - IVP)

Sistemdeki verilerin (CDI) o anki durumunun doğru olup olmadığını kontrol eden prosedürdür. Örneğin, gün sonunda bankadaki tüm hesapların toplamının, bankanın kasasındaki paraya eşit olup olmadığını kontrol eden bir denetim mekanizmasıdır.

#### B. Dönüşüm (Transformation Procedures - TP)

Veriyi bir geçerli durumdan diğerine taşıyan işlemlerdir. Bir kullanıcı bir CDI'yı değiştirmek isterse, bunu doğrudan yapamaz. Önce bir TP çağırır, TP veriyi doğrular, işlemi yapar ve veriyi tekrar "güvenli" halde bırakır.

---

### 3. Clark-Wilson'ın 3 Temel İlkesi

Bu modeli gerçek dünyada (özellikle finans sektöründe) vazgeçilmez kılan prensipler şunlardır:

1. **Yetkilendirme (Authorization):** Sadece belirli kullanıcılar belirli TP'leri çalıştırabilir.
    
2. **Görevler Ayrılığı (Separation of Duties):** Bir işlemi başlatan kişi ile o işlemi onaylayan kişi aynı olamaz. (Örn: Bir muhasebeci faturayı girer, müdür onaylar. Hiç kimse tek başına para çıkışı yapamaz).
    
3. **Denetim (Auditing):** Yapılan her işlem (TP kullanımı) mutlaka kayıt altına alınmalıdır.
    

---

### 4. Özet Karşılaştırma

|**Model**|**Odak Noktası**|**Mekanizma**|
|---|---|---|
|**Biba**|Hiyerarşik Bütünlük|No Read Down / No Write Up|
|**Clark-Wilson**|Ticari Bütünlük|TP ve IVP (Yazılım aracılı erişim)|

> **Analiz Notu:** Bell-LaPadula ve Biba modellerinde kullanıcı veriye doğrudan erişebilirken, Clark-Wilson modelinde kullanıcı ile veri arasında bir **"Yazılım/Program (TP)"** katmanı vardır. Bu, günümüzdeki modern uygulama mimarilerine (Database <-> Backend <-> User) en yakın modeldir.


**Defence-in-Depth** refers to creating a security system of multiple levels; hence it is also called Multi-Level Security.

Consider the following analogy: you have a locked drawer where you keep your important documents and pricey stuff. The drawer is locked; however, do you want this drawer lock to be the only thing standing between a thief and your expensive items? If we think of multi-level security, we would prefer that the drawer be locked, the relevant room be locked, the main door of the apartment be locked, the building gate be locked, and you might even want to throw in a few security cameras along the way. Although these multiple levels of security cannot stop every thief, they would block most of them and slow down the others.

### ISO/IEC 19249

ISO/IEC 19249, siber güvenlik dünyasında teorik modelleri (Bell-LaPadula, Biba vb.) alıp bunları modern bilgi işlem sistemlerine nasıl entegre edeceğimizi söyleyen bir **"Mimari Tasarım İlkeleri"** standartıdır.

Özetle; "Güvenli bir sistem inşa etmek istiyorsan, şu 5 prensibi uygulamalısın" diyen bir rehberdir.

---

### 1. ISO/IEC 19249'un 5 Temel Tasarım İlkesi

Bu standart, güvenli bir mimari oluşturmak için aşağıdaki beş ana ilkeyi zorunlu kılar:

#### I. Alan Ayrımı (Domain Separation)

Sistemi farklı güvenlik seviyelerine sahip bölgelere ayırmaktır. Bir bölgedeki sızma veya hata, diğer bölgeyi etkilememelidir.

- **Örnek:** Kullanıcı modunun (User Mode) çekirdek modundan (Kernel Mode) ayrı tutulması veya ağın VLAN'lar ile bölümlenmesi.
    

#### II. Katmanlandırma (Layering)

"Derinlemesine Savunma" (Defense in Depth) stratejisidir. Bir saldırganın hedefe ulaşmak için birden fazla güvenlik katmanını aşması gerekir.

- **Örnek:** Güvenlik duvarı -> IPS -> Antivirüs -> Veri Şifreleme.
    

#### III. Kapsülleme (Encapsulation)

Veriye ve süreçlere yalnızca belirlenmiş arayüzler (API'ler) üzerinden erişilmesini sağlar. Verinin doğrudan manipüle edilmesini engeller (Clark-Wilson modelindeki TP mantığı gibi).

- **Örnek:** Bir veritabanına doğrudan SQL sorgusu atmak yerine, sadece yetkili bir web servisi üzerinden erişmek.
    

#### IV. Gereksizliğin Azaltılması (Redundancy Elimination / Minimization)

Sistem ne kadar karmaşıksa, o kadar çok açık verir. Gereksiz servisleri, portları ve kod bloklarını kaldırarak saldırı yüzeyini küçültmeyi hedefler.

- **Örnek:** Bir sunucuda kullanılmayan "Print Spooler" servisini kapatmak.
    

#### V. En Az Ayrıcalık (Least Privilege)

Bir kullanıcıya veya sürece, görevini yerine getirmesi için gereken **minimum** yetkinin verilmesidir.

- **Örnek:** Bir stajyere sistemde "Admin" yetkisi değil, sadece okuma yetkisi verilmesi.
    

---

### 2. Neden Önemli?

Önceki sorularda konuştuğumuz Bell-LaPadula veya Biba gibi modeller "ne yapılacağını" (Gizlilik veya Bütünlük korunsun) söylerken; **ISO/IEC 19249**, bu modellerin fiziksel ve yazılımsal olarak "nasıl" hayata geçirileceğinin mühendislik reçetesini sunar.

### 3. SOC Analisti İçin Kritik Nokta

Log analizi yaparken veya bir sistemin zafiyetini incelerken şu soruyu sorarsın: _"Bu sistemde ISO 19249'un hangi ilkesi ihlal edilmiş?"_

- Eğer bir kullanıcı tüm sisteme erişebiliyorsa: **Least Privilege** ihlali.
    
- Eğer bir saldırgan web sunucusundan doğrudan veritabanına zıplayabiliyorsa: **Domain Separation** veya **Layering** eksikliği.
    

---


### Zero Trust vs Trust but Verify

Trust is a very complex topic; in reality, we cannot function without trust. If one were to think that the laptop vendor has installed spyware on the laptop, they would most likely end up rebuilding the system. If one were to mistrust the hardware vendor, they would stop using it completely. If we think of trust on a business level, things only become more sophisticated; however, we need some guiding security principles. Two security principles that are of interest to us regarding trust:

- Trust but Verify
- Zero Trust

**Trust but Verify**: This principle teaches that we should always verify even when we trust an entity and its behaviour. An entity might be a user or a system. Verifying usually requires setting up proper logging mechanisms; verifying indicates going through the logs to ensure everything is normal. In reality, it is not feasible to verify everything; just think of the work it takes to review all the actions taken by a single entity, such as Internet pages browsed by a single user. This requires automated security mechanisms, such as proxy, intrusion detection, and intrusion prevention systems.

**Zero Trust**: This principle treats trust as a vulnerability, and consequently, it caters to insider-related threats. After considering trust as a vulnerability, zero trust tries to eliminate it. It is teaching indirectly, “never trust, always verify.” In other words, every entity is considered adversarial until proven otherwise. Zero trust does not grant trust to a device based on its location or ownership. This approach contrasts with older models that would trust internal networks or enterprise-owned devices. Authentication and authorization are required before accessing any resource. As a result, if any breach occurs, the damage would be more contained if a zero trust architecture had been implemented.

Microsegmentation is one of the implementations used for Zero Trust. It refers to the design where a network segment can be as small as a single host. Moreover, communication between segments requires authentication, access control list checks, and other security requirements.  

There is a limit to how much we can apply zero trust without negatively impacting a business; however, this does not mean that we should not apply it as long as it is feasible.

---
## 🔗 Bağlantılar
- [[TryHackMe Security Engineer Path/index|🎓 TryHackMe: Security Engineer Path]]
- [[index|🏠 Ana İndeks]]
