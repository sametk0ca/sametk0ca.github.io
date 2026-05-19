+++
title = "Cloud Key Management Service (KMS)"
date = "2026-05-19"
draft = false
categories = ["Cloud"]
type = "bilgi-bankasi"
+++

KMS, bulut sağlayıcıları tarafından sunulan, verileri şifrelemek için kullanılan kriptografik anahtarların oluşturulmasını, saklanmasını ve yönetilmesini sağlayan servistir.

### Özet
Veri güvenliğinin temeli olan şifreleme anahtarlarının yönetimi zordur. KMS, bu anahtarları donanımsal güvenlik modülleri (HSM) kullanarak korur ve erişimini denetler.

### Teknik Detaylar
- **CMK (Customer Master Keys):** Veri anahtarlarını şifreleyen ana anahtarlar.
- **Envelope Encryption:** Verinin bir veri anahtarıyla, o veri anahtarının da bir master anahtarla şifrelenmesi tekniği.
- **Rotation:** Anahtarların periyodik olarak otomatik yenilenmesi.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Separation of Duties:** Anahtarı yöneten kişi ile anahtarı kullanan kişiyi (servisi) ayırın.
- **KMS Policy:** Anahtarlara erişimi IAM üzerinden değil, doğrudan anahtar politikaları (Key Policies) ile kısıtlayın.
- **Audit Logging:** Anahtarın her kullanımını (encrypt/decrypt) CloudTrail veya benzeri araçlarla loglayın.