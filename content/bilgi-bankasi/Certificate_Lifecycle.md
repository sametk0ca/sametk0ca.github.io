+++
title = "Sertifika Yaşam Döngüsü Yönetimi (Certificate Lifecycle)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cryptography"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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