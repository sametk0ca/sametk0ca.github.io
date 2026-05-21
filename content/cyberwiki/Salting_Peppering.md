+++
title = "Salting ve Peppering (Şifre Güvenliği) | Salting and Peppering (Password Security)"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
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

---

## English Version

Storing passwords simply by hashing them is not sufficient against modern attack methods (Rainbow Tables, Brute Force). **Salting** and **Peppering** are additional methods used to increase password security.

### 1. What is Salting?
Salting is a randomly generated unique string of characters that is added to each user's password before hashing it.
- **How ​​Does It Work?** User's password: `123456`, Random Salt (Salt): `x9f!2`. The value hashed by the system: `123456x9f!2`.
- **Why Used?** 
  - **Same Passwords Different Hashes:** Even if two users use the same password, the hash values in the database look completely different because their salts are different.
  - **Prevents Rainbow Table Attacks:** It renders millions of previously calculated password-hash tables (Rainbow Tables) useless.
- **Where Is It Stored?** Salt is unique to each user and is stored openly in the database alongside the user's hashed password.

### 2. What is Peppering?
Peppering is a value added to a password, similar to salting, but with two key differences:
1. **Confidential:** Pepper is not stored in the database, usually within the application code or in a secure hardware module (HSM).
2. **Common:** Usually the same pepper value is used for all users (or for specific groups).

### 3. Salting vs Peppering
| Feature | Salting | Peppering |
| :--- | :--- | :--- |
| **Location** | In Database (Open) | Application Code / HSM (Confidential) |
| **Uniqueness** | Different for each user | Same for everyone |
| **Purpose** | Rainbow Table blocking | Protecting password even if database is leaked |

### 4. Security Scenario
If an attacker only takes over the database (SQL Injection, etc.), it becomes almost impossible to brute force it because he knows the salts to crack the passwords but does not know the "pepper". To find out the pepper, he must also infiltrate the application server.

### Real World Analogy
Let your password be "Food" (Data).
- **Hashing:** It means putting the food through the blender. You cannot understand what is happening.
- **Salting:** Adding a different "Salt" to each dish. Even the same dishes (Passwords) give different tastes (Hashes).
- **Peppering:** It is the "Secret Pepper" that the chef keeps in his secret cupboard in the kitchen. Even if the attacker steals the food from the table, he can never imitate the original taste of the food (Password) without knowing what that secret pepper in the kitchen is.
