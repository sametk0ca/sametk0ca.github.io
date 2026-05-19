+++
title = "Güvenli Girdi Doğrulama (Input Validation)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Input Validation, bir uygulamaya giren tüm verilerin, uygulamanın beklediği format, uzunluk ve karakter türüne uygun olup olmadığını kontrol etme sürecidir.

### Özet
"Asla kullanıcıya güvenme" (Never trust user input) prensibinin en temel uygulamasıdır. Sadece kötü niyetli verileri engellemek değil, sadece iyi niyetli verilerin geçmesine izin vermek hedeflenir.

### Teknik Detaylar
- **Allow-listing (Positive Validation):** Sadece beklenen karakterlere/formatlara izin verin (örn: yaş alanı sadece rakam içermeli).
- **Type Checking:** Verinin beklenen veri tipinde (string, integer, boolean) olduğunu doğrulayın.
- **Range & Length Checks:** Verinin uzunluğunu ve değer aralığını kontrol edin.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Sunucu Taraflı Doğrulama:** İstemci taraflı (browser) kontroller kolayca atlatılabilir, bu yüzden doğrulamayı her zaman sunucu tarafında yapın.
- **Regex Kullanımı:** Karmaşık desenleri (e-posta, telefon) doğrulamak için güvenli ve optimize edilmiş düzenli ifadeler kullanın.
- **Fail Fast:** Geçersiz bir veri tespit edildiğinde işlemi anında durdurun ve hata döndürün.