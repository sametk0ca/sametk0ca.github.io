+++
title = "PKI (Public Key Infrastructure) Bileşenleri | PKI (Public Key Infrastructure) Components"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
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

---

## English Version

**PKI (Public Key Infrastructure)** is a "trust ecosystem" used to verify identities, encrypt data, and communicate securely in the digital world. PKI enables secure implementation of public key cryptography (asymmetric encryption) in real life.

### 1. Main Purpose of PKI
How can you be sure that the person you are talking to online is really that person? By using digital certificates, PKI guarantees that "This key really belongs to this person/entity."

### 2. Key Components of PKI
1. **Certificate Authority (CA):** It is the center of trust. A trusted third party that issues, signs and issues digital certificates (Ex: Let's Encrypt, DigiCert).
2. **Registration Authority (RA):** It is the unit that verifies the identities of users on behalf of the CA. "Is the applicant really the person he claims to be?" performs the control.
3. **Certificate Database:** It is where active certificates issued by the CA are stored.
4. **Certificate Revocation List (CRL - Certificate Revocation List):** It is the list of certificates that were canceled (stolen, compromised) before their expiration.
5. **Digital Certificates:** It is an electronic document signed by the CA (Usually in X.509 format) that contains a public key and the identification information of the owner of that key.

### 3. How Does PKI Work?
- **Step 1:** A website owner (Ex: `google.com`) creates a key pair (Public and Private).
- **Step 2:** Sends its public key and credentials to the CA via a "Certificate Signing Request" (CSR).
- **Step 3:** The CA verifies the identity and creates a **Certificate** by signing google.com's public key with its private key.
- **Step 4:** When your browser sees this certificate, it checks the signature of the CA and trusts the site.

### 4. Importance of PKI
Without PKI:
- Internet banking could not be secure (someone in between could pretend to be a bank).
- E-signature could not be used.
- We wouldn't be able to tell if the software updates actually came from the manufacturer.

### Real World Analogy
PKI is like a "Census Directorate" and "ID Card" system.
- **Digital Certificate:** T.R. It is your ID Card. It has your photo (Public Key) and information on it.
- **CA (Certificate Authority):** State (Census Directorate). He prints the ID card and stamps it.
- **Trust:** When you see someone's ID, you accept that person because you trust the government seal (CA signature) on the card, not the person.
