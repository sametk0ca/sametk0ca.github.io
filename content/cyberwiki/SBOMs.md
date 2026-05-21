+++
title = "SBOM (Software Bill of Materials)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

SBOM, bir yazılım paketinin içindeki tüm bileşenlerin, kütüphanelerin, modüllerin ve bunların bağımlılıklarının detaylı ve makine tarafından okunabilir bir listesidir.

### Özet
Gıda ürünlerinin arkasındaki "içindekiler" listesi gibi, SBOM da yazılımın içinde ne olduğunu şeffaf hale getirir. Bu sayede yeni bir zafiyet (örn: Log4j) çıktığında, hangi uygulamaların etkilendiği anında tespit edilebilir.

### Teknik Detaylar
- **Formats:** CycloneDX ve SPDX en yaygın kullanılan SBOM formatlarıdır.
- **Generation:** Kod analiz araçları (SCA) veya derleme araçları ile otomatik olarak üretilir.
- **Vulnerability Mapping:** SBOM listesinin CVE veritabanları ile otomatik olarak eşleştirilmesi.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Continuous Generation:** Her yeni sürümde (build) güncel bir SBOM dosyası üretin.
- **Supplier Transparency:** Satın alınan veya kullanılan yazılımlar için tedarikçilerden SBOM talep edin.
- **Automated Analysis:** SBOM dökümanlarını manuel incelemek yerine otomatik zafiyet takip araçlarına (Dependency-Track vb.) aktarın.

---

## English Version

SBOM is a detailed and machine-readable list of all components, libraries, modules and their dependencies within a software package.

### Summary
Like the "ingredients" list on the back of food products, SBOM makes software transparent about what's inside. In this way, when a new vulnerability (e.g. Log4j) emerges, it can be immediately determined which applications are affected.

### Technical Details
- **Formats:** CycloneDX and SPDX are the most commonly used SBOM formats.
- **Generation:** Generated automatically with code analysis tools (SCA) or compilation tools.
- **Vulnerability Mapping:** Automatic mapping of the SBOM list with CVE databases.

### Security Approach and Best Practices
- **Continuous Generation:** Generate an updated SBOM file with each new version (build).
- **Supplier Transparency:** Request SBOM from suppliers for software purchased or used.
- **Automated Analysis:** Transfer SBOM documents to automatic vulnerability tracking tools (Dependency-Track etc.) instead of manually reviewing them.
