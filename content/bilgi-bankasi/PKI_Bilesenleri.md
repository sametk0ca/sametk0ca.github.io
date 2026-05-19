+++
title = "PKI (Public Key Infrastructure) Bileşenleri"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "bilgi-bankasi"
+++

**PKI (Kamu Anahtarı Altyapısı)**, dijital dünyada kimlikleri doğrulamak, verileri şifrelemek ve güvenli iletişim kurmak için kullanılan bir "güven ekosistemi"dir. PKI, açık anahtarlı kriptografinin (asimetrik şifreleme) gerçek hayatta güvenli bir şekilde uygulanmasını sağlar.

### 1. PKI'nın Temel Amacı
İnternette konuştuğunuz kişinin gerçekten o kişi olduğundan nasıl emin olabilirsiniz? PKI, dijital sertifikalar kullanarak "Bu anahtar gerçekten bu kişiye/kuruma aittir" garantisini verir.

### 2. PKI'nın Temel Bileşenleri
1. **Sertifika Otoritesi (CA - Certificate Authority):** Güvenin merkezidir. Dijital sertifikaları düzenleyen, imzalayan ve yayınlayan güvenilir üçüncü taraftır (Örn: Let's Encrypt, DigiCert).
2. **Kayıt Otoritesi (RA - Registration Authority):** CA adına kullanıcıların kimliklerini doğrulayan birimdir. "Başvuran kişi gerçekten kimliğini iddia ettiği kişi mi?" kontrolünü yapar.
3. **Sertifika Veritabanı:** CA tarafından düzenlenen aktif sertifikaların saklandığı yerdir.
4. **Sertifika İptal Listesi (CRL - Certificate Revocation List):** Süresi dolmadan iptal edilen (çalınan, güvenliği sarsılan) sertifikaların listesidir.
5. **Dijital Sertifikalar:** Bir açık anahtarı ve o anahtarın sahibinin kimlik bilgilerini içeren, CA tarafından imzalanmış elektronik belgedir (Genellikle X.509 formatında).

### 3. PKI Nasıl Çalışır?
- **Adım 1:** Bir web sitesi sahibi (Örn: `google.com`), bir anahtar çifti (Açık ve Gizli) oluşturur.
- **Adım 2:** Açık anahtarını ve kimlik bilgilerini bir "Sertifika İmza İsteği" (CSR) ile CA'ya gönderir.
- **Adım 3:** CA, kimliği doğrular ve google.com'un açık anahtarını kendi gizli anahtarı ile imzalayarak bir **Sertifika** oluşturur.
- **Adım 4:** Sizin tarayıcınız bu sertifikayı gördüğünde, CA'nın imzasını kontrol eder ve siteye güvenir.

### 4. PKI'nın Önemi
PKI olmasaydı:
- İnternet bankacılığı güvenli olamazdı (Aradaki biri bankaymış gibi davranabilirdi).
- E-imza kullanılamazdı.
- Yazılım güncellemelerinin gerçekten üreticiden gelip gelmediğini anlayamazdık.

### Gerçek Dünya Analojisi
PKI, bir "Nüfus Müdürlüğü" ve "Kimlik Kartı" sistemi gibidir.
- **Dijital Sertifika:** T.C. Kimlik Kartınızdır. Üzerinde fotoğrafınız (Açık Anahtar) ve bilgileriniz vardır.
- **CA (Sertifika Otoritesi):** Devlettir (Nüfus Müdürlüğü). Kimlik kartını o basar ve üzerine mühür vurur.
- **Güven:** Siz birinin kimliğini gördüğünüzde, o kişiye değil, kartın üzerindeki devlet mührüne (CA imzası) güvendiğiniz için o kişinin o olduğunu kabul edersiniz.