+++
title = "Brute Force vs Password Spraying"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

Şifre kırma saldırıları, en temel ama hala en etkili yöntemler arasındadır. Aralarındaki fark, saldırganın ne kadar "gürültü" çıkardığıdır.

### 1. Brute Force (Kaba Kuvvet)
Bir saldırganın, tek bir kullanıcı hesabını ele geçirmek için binlerce, milyonlarca şifre denemesi yapmasıdır.
- **Mantık:** Kullanıcı adı bellidir (Örn: `admin`), şifre deneme yanılma ile bulunur.
- **Sorun:** Eğer sistemde "5 kez yanlış girince hesabı kilitle" kuralı varsa, bu saldırı hemen fark edilir ve hesap kilitlenir.

### 2. Password Spraying (Şifre Püskürtme)
Brute Force'un daha akıllıca halidir. Saldırgan, binlerce kullanıcı adı toplar ve hepsine sadece **tek bir popüler şifre** (Örn: `Sifre123!`, `Kış2024`) dener.
- **Mantık:** Her hesapta sadece 1-2 kez deneme yapıldığı için sistem hesapları kilitlemez (gürültü azdır).
- **Sonuç:** Binlerce kullanıcıdan mutlaka 3-5 tanesi o basit şifreyi kullanıyordur. Saldırgan sessizce içeri sızmış olur.

### 3. Bilmen Gereken Bazı Terimler
- **Dictionary Attack:** İçinde binlerce gerçek şifrenin olduğu bir "sözlük" listesi kullanarak yapılan denemeler.
- **Account Lockout:** Üst üste hatalı girişlerde hesabın dondurulması koruması.
- **Credential Stuffing:** Başka bir siteden çalınan şifre listelerinin (Örn: LinkedIn sızıntısı) başka sitelerde otomatik olarak denenmesi.

### 4. Korunma Yolları
- **Güçlü Şifre Politikası:** Harf, rakam ve sembol içeren uzun şifreler.
- **MFA:** Şifre doğru olsa bile telefona gelen onay olmadan giriş yapılamaz.
- **IP Bloklama:** Belirli bir IP'den çok fazla hatalı giriş gelirse o IP'yi tamamen yasaklamak.

### Gerçek Dünya Analojisi
- **Brute Force:** Bir evin kapısına gelip, elinizdeki 1 milyon farklı anahtarı tek tek denemeye başlamanızdır. Çok gürültü çıkar ve komşular (Sistem) hemen polisi (Firewall) arar.
- **Password Spraying:** Bir mahalledeki 1000 tane evin kapısını gezmeniz ve her birinde sadece elinizdeki tek bir "standart" anahtarı denemenizdir. Kimse sizi fark etmez ama mahalledeki 3-4 evin kilidi mutlaka o anahtarla açılacaktır.

---

## English Version

Password cracking attacks are among the most basic but still most effective methods. The difference between them is how much "noise" the attacker makes.

### 1. Brute Force
An attacker tries thousands or millions of passwords to take over a single user account.
- **Logic:** The username is clear (Ex: `admin`), the password is found by trial and error.
- **Problem:** If there is a rule in the system "Lock the account after entering it incorrectly 5 times", this attack will be noticed immediately and the account will be locked.

### 2. Password Spraying
It is a smarter version of Brute Force. The attacker collects thousands of usernames and tries all of them with just **one popular password** (Ex: `Password123!`, `Winter2024`).
- **Logic:** Since only 1-2 attempts are made on each account, the system does not lock accounts (low noise).
- **Result:** Out of thousands of users, 3-5 are definitely using that simple password. The attacker sneaks in silently.

### 3. Some Terms You Should Know
- **Dictionary Attack:** Attempts made using a "dictionary" list containing thousands of real passwords.
- **Account Lockout:** Account freezing protection in case of repeated incorrect logins.
- **Credential Stuffing:** Automatically testing password lists stolen from another site (e.g. LinkedIn leak) on other sites.

### 4. Ways of Protection
- **Strong Password Policy:** Long passwords containing letters, numbers and symbols.
- **MFA:** Even if the password is correct, login cannot be made without the confirmation received on the phone.
- **IP Blocking:** If too many incorrect entries come from a particular IP, banning that IP completely.

### Real World Analogy
- **Brute Force:** It is when you come to the door of a house and start trying 1 million different keys one by one. There is a lot of noise and the neighbors (System) immediately call the police (Firewall).
- **Password Spraying:** It means visiting 1000 doors of houses in a neighborhood and trying only one "standard" key in each of them. No one will notice you, but 3-4 houses in the neighborhood will definitely be unlocked with that key.
