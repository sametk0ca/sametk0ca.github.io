+++
title = "IDOR (Insecure Direct Object Reference)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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