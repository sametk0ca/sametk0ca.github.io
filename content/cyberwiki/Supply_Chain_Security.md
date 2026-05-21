+++
title = "Yazılım Tedarik Zinciri Güvenliği (Supply Chain Security) | Software Supply Chain Security"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Yazılım tedarik zinciri güvenliği, bir yazılımın geliştirilmesinden dağıtımına kadar geçen süreçte kullanılan tüm bileşenlerin (kod, kütüphane, araç, altyapı) güvenliğini sağlama sürecidir.

### Özet
Saldırganlar artık doğrudan hedefi vurmak yerine, hedefin kullandığı açık kaynaklı kütüphanelere veya CI/CD araçlarına sızarak (SolarWinds örneği gibi) daha geniş çaplı etki yaratmayı amaçlamaktadır.

### Teknik Detaylar
- **Upstream Security:** Kullanılan üçüncü taraf kütüphanelerin güvenilirliğinin denetlenmesi.
- **Build Integrity:** Yazılımın derlendiği ortamın (CI/CD) izole ve güvenli olması.
- **Provenance:** Bir yazılım paketinin gerçekten iddia edilen kaynak tarafından üretildiğinin kanıtlanması.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **SBOM Kullanımı:** Yazılımın tüm bileşenlerini içeren bir "malzeme listesi" (SBOM) tutun.
- **Code Signing:** Derlenen paketleri (binary, imaj) dijital olarak imzalayarak bütünlüğünü koruyun.
- **Vetting Process:** Yeni bir kütüphane eklemeden önce zafiyet geçmişini ve topluluk desteğini kontrol edin.

---

## English Version

Software supply chain security is the process of ensuring the security of all components (code, library, tools, infrastructure) used in the process from development to distribution of a software.

### Summary
Instead of hitting the target directly, attackers now aim to have a broader impact by infiltrating open source libraries or CI/CD tools used by the target (such as the SolarWinds example).

### Technical Details
- **Upstream Security:** Checking the reliability of third-party libraries used.
- **Build Integrity:** The environment (CI/CD) in which the software is compiled is isolated and secure.
- **Provenance:** Proving that a software package was actually produced by the claimed source.

### Security Approach and Best Practices
- **SBOM Usage:** Maintain a "bill of materials" (SBOM) containing all components of the software.
- **Code Signing:** Protect the integrity of compiled packages (binary, image) by digitally signing them.
- **Vetting Process:** Check vulnerability history and community support before adding a new library.
