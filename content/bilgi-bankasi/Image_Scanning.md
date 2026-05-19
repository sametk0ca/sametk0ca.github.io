+++
title = "Container Image Scanning"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

İmaj tarama, konteyner imajlarındaki bilinen zafiyetleri (CVE), hatalı yapılandırmaları ve gömülü sırları (secrets) tespit etme işlemidir.

### Özet
Tedarik zinciri güvenliğinin en kritik adımlarından biridir. Üretim ortamına alınan her imajın, güvenli olduğu kanıtlanmış bir kaynaktan gelmesi ve taranmış olması gerekir.

### Teknik Detaylar
- **SCA (Software Composition Analysis):** İmaj içindeki kütüphane ve paketlerin zafiyetlerini bulur.
- **Tools:** Trivy, Grype, Clair, Snyk veya Docker Scout.
- **Registry Integration:** İmajlar bir registry'ye (örn: Harbor, ECR) yüklendiğinde otomatik olarak taranması.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Shift-Left Scanning:** İmajları daha geliştirici bilgisayarında veya CI aşamasında tarayın.
- **Deny-by-Policy:** Belirli bir kritiklik seviyesinin (örn: High/Critical) üzerindeki imajların deploy edilmesini otomatik olarak engelleyin.
- **Base Image Updates:** Temel imajlarınızı düzenli olarak güncelleyerek "zero-day" olmayan açıklardan korunun.