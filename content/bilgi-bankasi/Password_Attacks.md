+++
title = "Brute Force vs Password Spraying"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
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