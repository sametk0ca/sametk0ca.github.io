+++
title = "Pass the Hash  Golden Ticket | Pass the Hash Golden Ticket"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

Bu saldırılar, bir ağa sızan saldırganın şifrelerin kendisini bilmesine gerek kalmadan, sistemde yetki yükseltmek ve diğer bilgisayarlara yayılmak için kullandığı ileri seviye yöntemlerdir.

### 1. Pass the Hash (Hash'i Geçir)
Windows sistemlerde şifreler açık metin olarak değil, "Hash" (karma) denilen matematiksel halleriyle tutulur.
- **Saldırı Mantığı:** Saldırgan şifreyi kırmakla uğraşmaz. Bilgisayarın hafızasından bu Hash değerini çalar ve giriş yapmak istediği yere bu Hash'i sunar. Sistem "Hah, doğru anahtar geldi" diyerek saldırganı içeri alır.

### 2. Golden Ticket (Altın Bilet)
Active Directory (Kurumsal ağ yönetimi) ortamlarındaki en tehlikeli saldırıdır.
- **Saldırı Mantığı:** Saldırgan, Kerberos sisteminin en tepesindeki anahtarı (KRBTGT şifresini) ele geçirir. Bu anahtarla, kendisini istediği kişi (Örn: En yetkili Admin) olarak gösteren ve hiçbir zaman süresi dolmayan sahte bir "Altın Bilet" oluşturur. Artık o ağın tanrısı olmuştur.

### 3. Bilmen Gereken Bazı Terimler
- **Hash:** Şifrenin matematiksel bir algoritma (Örn: NTLM) ile geri döndürülemez bir koda çevrilmiş hali.
- **Active Directory (AD):** Şirketlerdeki tüm kullanıcıları ve bilgisayarları tek bir merkezden yöneten sistem.
- **Domain Admin:** Bir ağdaki en yüksek yetkili kullanıcı. Golden Ticket ile bu yetkiye ulaşılır.
- **Kerberos:** Ağda "bilet" kullanarak kimlik doğrulayan protokol.

### 4. Korunma Yolları
- **Privileged Access Management (PAM):** Admin yetkilerini çok sıkı denetlemek ve kısıtlamak.
- **LAPS:** Her bilgisayarın yerel admin şifresini farklı ve rastgele yapmak.
- **Kerberos Güvenliği:** KRBTGT şifresini periyodik olarak (yılda 2 kez gibi) değiştirmek.

### Gerçek Dünya Analojisi
- **Pass the Hash:** Bir otel odasının anahtarını çalmak yerine, anahtarın içindeki dijital kodu (Hash) kopyalayıp sahte bir kart oluşturmak gibidir. Kilidi açmak için gerçek anahtara ihtiyacınız yoktur, kopya kod yeterlidir.
- **Golden Ticket:** Oteldeki tüm odaları, kasaları ve kapıları açan "Master Key" (Ana Anahtar) yapma makinesini ele geçirmek gibidir. Artık otelin sahibi sizsiniz.

---

## English Version

These attacks are advanced methods that an attacker who infiltrates a network uses to increase authority in the system and spread to other computers, without needing to know the passwords themselves.

### 1. Pass the Hash
In Windows systems, passwords are not kept in clear text, but in their mathematical form called "Hash" (hash).
- **Attack Logic:** The attacker does not bother to crack the password. It steals this Hash value from the computer's memory and presents this Hash to the place where it wants to log in. The system lets the attacker in by saying "Hah, the right key has arrived."

### 2. Golden Ticket
It is the most dangerous attack in Active Directory (Enterprise network management) environments.
- **Attack Logic:** The attacker obtains the key (KRBTGT password) at the top of the Kerberos system. With this key, he creates a fake "Golden Ticket" that portrays himself as the person he wants (E.g. the most competent Admin) and never expires. He has now become the god of the network.

### 3. Some Terms You Should Know
- **Hash:** The password is converted into an irreversible code by a mathematical algorithm (Ex: NTLM).
- **Active Directory (AD):** The system that manages all users and computers in companies from a single center.
- **Domain Admin:** The highest authority user on a network. This authority is achieved with the Golden Ticket.
- **Kerberos:** Protocol that authenticates to the network using "tickets".

### 4. Ways of Protection
- **Privileged Access Management (PAM):** Strictly controlling and restricting admin privileges.
- **LAPS:** Making the local admin password of each computer different and random.
- **Kerberos Security:** Changing the KRBTGT password periodically (like twice a year).

### Real World Analogy
- **Pass the Hash:** Instead of stealing a hotel room key, it is like creating a fake card by copying the digital code (Hash) in the key. You don't need the real key to open the lock, a copy code is enough.
- **Golden Ticket:** It is like getting hold of the "Master Key" making machine that opens all rooms, safes and doors in the hotel. You are now the owner of the hotel.
