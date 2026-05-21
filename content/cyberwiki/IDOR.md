+++
title = "IDOR (Insecure Direct Object Reference)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

IDOR, bir web uygulamasının kullanıcıdan gelen bir "ID" veya "dosya adı" bilgisini, yetki kontrolü yapmadan doğrudan veritabanından çekip getirmesi sonucu oluşan bir güvenlik açığıdır.

### 1. Saldırı Mantığı
Uygulama size kendi faturanızı göstermek için şöyle bir adres kullanıyor olabilir: `site.com/fatura?id=123`. Eğer siz bu `123` sayısını `124` yaparsanız ve uygulama size başkasının faturasını gösterirse, işte bu bir IDOR açığıdır.

### 2. Nasıl Gerçekleşir?
Saldırgan, URL'deki veya istekteki parametreleri (sayıları) değiştirerek ("Parameter Tampering") sistemdeki diğer tüm verilere (kullanıcılar, siparişler, mesajlar) erişmeye çalışır.

### 3. Bilmen Gereken Bazı Terimler
- **Parameter Tampering (Parametre Değiştirme):** Web sitesine giden verileri (URL'deki sayılar gibi) el ile değiştirme eylemi.
- **Object Reference:** Veritabanındaki bir veriyi işaret eden numara veya isim.
- **Broken Access Control:** Yetkilendirme sisteminin bozuk olması. IDOR bunun en yaygın örneğidir.

### 4. Korunma Yolları
- **Yetki Kontrolü:** Her istekte "Bu veri (ID=124) gerçekten bu kullanıcıya mı (User) ait?" diye kontrol edin.
- **Tahmin Edilemez ID'ler (UUID):** `123`, `124` gibi ardışık sayılar yerine `550e8400-e29b-41d4-a716-446655440000` gibi tahmin edilmesi imkansız uzun kodlar kullanın.

### Gerçek Dünya Analojisi
Bir emanetçiye gittiğinizi düşünün. Elinizde 10 numaralı anahtar var. Anahtarı verip 10 numaralı dolabı açıyorsunuz. Ancak dolaplar yan yana ve kilitleri bozuk. Siz elinizle 11 numaralı dolabı da açabiliyorsunuz ve emanetçi sizi durdurmuyor. İşte bu IDOR'dur. Emanetçinin (Uygulama) sadece sizin numaranızdaki dolabı açmanıza izin vermesi gerekirdi.

---

## English Version

IDOR is a security vulnerability that occurs when a web application retrieves "ID" or "file name" information from the user directly from the database without checking for authorization.

### 1. Attack Logic
The application may be using an address like this to show you your own bill: `site.com/fatura?id=123`. If you change this number '123' to '124' and the application shows you someone else's invoice, this is an IDOR vulnerability.

### 2. How Does It Happen?
The attacker tries to access all other data in the system (users, orders, messages) by changing the parameters (numbers) in the URL or request ("Parameter Tampering").

### 3. Some Terms You Should Know
- **Parameter Tampering:** The act of manually altering data (such as numbers in the URL) going to the website.
- **Object Reference:** A number or name that points to a data in the database.
- **Broken Access Control:** The authorization system is broken. IDOR is the most common example of this.

### 4. Ways of Protection
- **Authority Check:** In every request, "Does this data (ID=124) really belong to this user?" Check it out.
- **Unpredictable IDs (UUID):** Use long codes that are impossible to guess, such as `550e8400-e29b-41d4-a716-446655440000`, instead of consecutive numbers such as `123`, `124`.

### Real World Analogy
Imagine going to a depository. You have key number 10 in your hand. You give the key and open locker number 10. However, the cabinets are side by side and their locks are broken. You can also open locker number 11 with your hand and the custodian does not stop you. This is IDOR. The escrow agent (Application) should only allow you to open the locker with your number.
