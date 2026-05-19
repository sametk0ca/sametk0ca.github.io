+++
title = "Bağımlılık Riski Yönetimi (Dependency Risk)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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