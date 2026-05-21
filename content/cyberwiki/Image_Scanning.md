+++
title = "Container Image Scanning"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

Image scanning is the process of detecting known vulnerabilities (CVEs), misconfigurations and buried secrets in container images.

### Summary
It is one of the most critical steps in supply chain security. Every image introduced into the production environment must come from a proven secure source and must be scanned.

### Technical Details
- **SCA (Software Composition Analysis):** Finds vulnerabilities of libraries and packages in the image.
- **Tools:** Trivy, Grype, Clair, Snyk or Docker Scout.
- **Registry Integration:** Automatic scanning of images when they are uploaded to a registry (eg: Harbor, ECR).

### Security Approach and Best Practices
- **Shift-Left Scanning:** Scan images on the developer computer or at the CI stage.
- **Deny-by-Policy:** Automatically prevent images above a certain criticality level (e.g. High/Critical) from being deployed.
- **Base Image Updates:** Protect yourself from non-zero-day vulnerabilities by regularly updating your base images.
