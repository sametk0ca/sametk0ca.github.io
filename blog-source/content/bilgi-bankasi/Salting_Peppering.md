+++
title = "Salting ve Peppering (Şifre Güvenliği)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "bilgi-bankasi"
+++

Şifrelerin sadece hashlenerek saklanması, modern saldırı yöntemlerine karşı (Rainbow Tables, Brute Force) yeterli değildir. **Salting** ve **Peppering**, şifre güvenliğini artırmak için kullanılan ek yöntemlerdir.

### 1. Salting (Tuzlama) Nedir?
Salting, her kullanıcının şifresine hashleme işleminden önce eklenen, rastgele oluşturulmuş benzersiz bir karakter dizisidir.
- **Nasıl Çalışır?** Kullanıcının şifresi: `123456`, Rastgele Tuz (Salt): `x9f!2`. Sistemin hashlediği değer: `123456x9f!2`.
- **Neden Kullanılır?** 
  - **Aynı Şifreler Farklı Hashler:** İki kullanıcı aynı şifreyi kullansa bile, tuzları farklı olduğu için veritabanındaki hash değerleri tamamen farklı görünür.
  - **Rainbow Table Saldırılarını Engeller:** Önceden hesaplanmış milyonlarca şifre-hash tablosunu (Rainbow Tables) işe yaramaz hale getirir.
- **Nerede Saklanır?** Salt, her kullanıcı için özeldir ve veritabanında kullanıcının hashlenmiş şifresinin yanında açık olarak saklanır.

### 2. Peppering (Biberleme) Nedir?
Peppering, salting'e benzer şekilde şifreye eklenen bir değerdir, ancak iki temel farkı vardır:
1. **Gizlidir:** Pepper, veritabanında değil, genellikle uygulama kodunun içinde veya güvenli bir donanım modülünde (HSM) saklanır.
2. **Ortaktır:** Genellikle tüm kullanıcılar için aynı pepper değeri kullanılır (veya belirli gruplar için).

### 3. Salting vs Peppering
| Özellik | Salting (Tuz) | Peppering (Biber) |
| :--- | :--- | :--- |
| **Konum** | Veritabanında (Açık) | Uygulama Kodu / HSM (Gizli) |
| **Benzersizlik** | Her kullanıcı için farklı | Herkes için aynı |
| **Amacı** | Rainbow Table engelleme | Veritabanı sızsa bile şifreyi koruma |

### 4. Güvenlik Senaryosu
Eğer bir saldırgan sadece veritabanını ele geçirirse (SQL Injection vb.), şifreleri kırmak için tuzları bilse de "biberi" (pepper) bilmediği için brute force yapması neredeyse imkansız hale gelir. Biberi öğrenmek için uygulama sunucusuna da sızması gerekir.

### Gerçek Dünya Analojisi
Şifreniz bir "Yemek" (Veri) olsun.
- **Hashing:** Yemeği blenderdan geçirmektir. Ne olduğunu anlayamazsınız.
- **Salting:** Her yemeğe farklı bir "Tuz" katmaktır. Aynı yemekler (Şifreler) bile farklı tatlar (Hashler) verir.
- **Peppering:** Şefin mutfaktaki gizli dolabında sakladığı "Gizli Biber"dir. Saldırgan yemeği masadan çalsa bile, mutfaktaki o gizli biberin ne olduğunu bilmeden yemeğin orijinal tadını (Şifreyi) asla taklit edemez.