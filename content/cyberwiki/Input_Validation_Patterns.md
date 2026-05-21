+++
title = "Güvenli Girdi Doğrulama (Input Validation) | Secure Input Validation"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

Input Validation is the process of checking whether all data entering an application conforms to the format, length and character type that the application expects.

### Summary
It is the most basic application of the "Never trust user input" principle. The aim is not to just block malicious data, but to allow only benign data to pass through.

### Technical Details
- **Allow-listing (Positive Validation):** Allow only expected characters/formats (eg: age field should only contain numbers).
- **Type Checking:** Verify that the data is of the expected data type (string, integer, boolean).
- **Range & Length Checks:** Check the length and value range of the data.

### Security Approach and Best Practices
- **Server-Side Authentication:** Client-side (browser) checks can be easily bypassed, so always perform validation on the server side.
- **Regex Usage:** Use safe and optimized regular expressions to validate complex patterns (email, phone).
- **Fail Fast:** Immediately stop the process and return an error when invalid data is detected.
