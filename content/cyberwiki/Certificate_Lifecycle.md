+++
title = "Sertifika Yaşam Döngüsü Yönetimi (Certificate Lifecycle) | Certificate Lifecycle Management"
date = "2026-05-19"
draft = false
categories = ["Cryptography"]
type = "cyberwiki"
+++

Sertifika yaşam döngüsü yönetimi, dijital sertifikaların (SSL/TLS) oluşturulmasından geçerlilik süresinin dolmasına veya iptal edilmesine kadar geçen tüm sürecin planlanması ve izlenmesidir.

### Özet
Yönetilmeyen sertifikalar, beklenmedik hizmet kesintilerine (expiration) veya sızdırılmış anahtarlar nedeniyle güvenlik zafiyetlerine yol açar. Otomasyon bu sürecin en kritik parçasıdır.

### Teknik Detaylar
- **Enrollment:** Sertifika talebinin yapılması ve imzalanması (CA).
- **Inventory:** Tüm sertifikaların nerede olduğunu ve ne zaman sona ereceğini takip etme.
- **Renewal:** Sertifikanın süresi dolmadan otomatik yenilenmesi (örn: Let's Encrypt / ACME).
- **Revocation:** Çalınan veya geçersiz kalan sertifikaların iptali (CRL/OCSP).

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Short-lived Certificates:** Sertifika ömrünü kısa tutarak risk süresini azaltın.
- **Monitoring:** Sertifika sürelerini izleyen otomatik uyarı sistemleri kurun.
- **Private Key Protection:** Sertifika anahtarlarını asla düz metin olarak saklamayın; HSM veya güvenli anahtar depoları kullanın.

---

## English Version

Certificate lifecycle management is the planning and monitoring of the entire process from the creation of digital certificates (SSL/TLS) to their expiration or revocation.

### Summary
Unmanaged certificates lead to unexpected service interruptions (expiration) or security vulnerabilities due to leaked keys. Automation is the most critical part of this process.

### Technical Details
- **Enrollment:** Making and signing the certificate request (CA).
- **Inventory:** Keep track of where all certificates are and when they will expire.
- **Renewal:** Automatic renewal of the certificate before it expires (eg: Let's Encrypt / ACME).
- **Revocation:** Revocation of stolen or invalid certificates (CRL/OCSP).

### Security Approach and Best Practices
- **Short-lived Certificates:** Reduce risk by keeping certificate life short.
- **Monitoring:** Set up automatic alert systems that monitor certificate expirations.
- **Private Key Protection:** Never store certificate keys in plain text; Use HSM or secure keystores.
