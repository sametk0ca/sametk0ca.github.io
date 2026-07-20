+++
title = "Cloud Key Management Service (KMS)"
date = "2026-05-19"
draft = false
categories = ["Cloud"]
type = "cyberwiki"
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

---

## English Version

KMS is a service offered by cloud providers that enables the creation, storage and management of cryptographic keys used to encrypt data.

### Summary
Encryption keys, which are the basis of data security, are difficult to manage. KMS protects and controls access to these keys using hardware security modules (HSM).

### Technical Details
- **CMK (Customer Master Keys):** Master keys that encrypt data keys.
- **Envelope Encryption:** The technique of encrypting data with a data key, and that data key with a master key.
- **Rotation:** Periodic automatic renewal of keys.

### Security Approach and Best Practices
- **Separation of Duties:** Separate the person managing the key and the person (service) using the key.
- **KMS Policy:** Restrict access to keys directly with key policies, not through IAM.
- **Audit Logging:** Log each use (encrypt/decrypt) of the key with CloudTrail or similar tools.
