+++
title = "Pass the Hash  Golden Ticket"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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