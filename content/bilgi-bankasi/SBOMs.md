+++
title = "SBOM (Software Bill of Materials)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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