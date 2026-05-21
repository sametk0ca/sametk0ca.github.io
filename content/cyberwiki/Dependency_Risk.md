+++
title = "Bağımlılık Riski Yönetimi (Dependency Risk) | Dependency Risk Management"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Bağımlılık riski yönetimi, uygulamada kullanılan açık kaynaklı veya üçüncü taraf kütüphanelerin oluşturabileceği güvenlik, lisans ve sürdürülebilirlik risklerinin yönetilmesidir.

### Özet
Modern yazılımların %80'inden fazlası açık kaynaklı bağımlılıklardan oluşur. Bu durum, başkasının yazdığı kodun zafiyetlerini ve risklerini de kendi uygulamanıza taşımanız anlamına gelir.

### Teknik Detaylar
- **Direct vs Transitive Dependencies:** Sizin eklediğiniz kütüphaneler (direct) ve onların da kullandığı alt kütüphaneler (transitive).
- **SCA (Software Composition Analysis):** Bağımlılıkları otomatik tarayan teknoloji.
- **License Compliance:** Kullanılan kütüphanelerin kurum politikasına uygun lisanslara (MIT, Apache, GPL vb.) sahip olduğunun kontrolü.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Dependency Pinning:** Kütüphane sürümlerini sabitleyin (örn: `package-lock.json`), böylece her build'de beklenmedik bir sürüm yüklenmez.
- **Vulnerability Scanning:** Kritik zafiyet içeren kütüphaneler tespit edildiğinde build işlemini durdurun.
- **Regular Updates:** "Çalışıyorsa dokunma" mantığını bırakıp, güvenlik güncellemelerini düzenli olarak uygulayın.

---

## English Version

Dependency risk management is the management of security, licensing and maintainability risks that may be created by open source or third-party libraries used in the application.

### Summary
More than 80% of modern software consists of open source dependencies. This means that you carry the vulnerabilities and risks of the code written by someone else into your own application.

### Technical Details
- **Direct vs Transitive Dependencies:** The libraries you added (direct) and the sub-libraries they use (transitive).
- **SCA (Software Composition Analysis):** Technology that automatically scans dependencies.
- **License Compliance:** Checking that the libraries used have licenses (MIT, Apache, GPL, etc.) in accordance with the institutional policy.

### Security Approach and Best Practices
- **Dependency Pinning:** Pin library versions (eg: `package-lock.json`) so that an unexpected version is not loaded with every build.
- **Vulnerability Scanning:** Stop the build process when libraries containing critical vulnerabilities are detected.
- **Regular Updates:** Abandon the "if it's working, don't touch it" mentality and apply security updates regularly.
