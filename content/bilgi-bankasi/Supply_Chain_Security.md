+++
title = "Yazılım Tedarik Zinciri Güvenliği (Supply Chain Security)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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