---
title: "Software Supply Chain Security | Yazılım Tedarik Zinciri Güvenliği"
date: 2026-07-02
description: "Understanding software supply chain attacks, how to protect CI/CD pipelines, and implementing frameworks like SLSA and SBOM. / Yazılım tedarik zinciri saldırılarını anlama, CI/CD süreçlerini koruma, SLSA çerçevesi ve SBOM gibi standartları uygulama rehberi."
tags: ["Supply Chain Security", "SLSA", "SBOM", "DevSecOps", "CI/CD Security", "Application Security"]
categories: ["Security"]
ShowToc: true
math: false
mermaid: true
cover:
    image: "/img/cover-1618401471353-b98aedd07871.jpg"
    alt: "Software development code and repository management visualization"
    relative: false
---

## Türkçe (TR)

### 1. Giriş: Modern Yazılımların İnşa Blokları
Modern yazılımlar artık sıfırdan yazılmıyor. Bugün yazılan bir uygulamanın büyük bir kısmı, açık kaynaklı kütüphaneler, hazır paketler, üçüncü taraf bağımlılıklar ve otomatik çalışan CI/CD (Sürekli Entegrasyon / Sürekli Dağıtım) boru hatlarından oluşmaktadır. Bu durum geliştirme sürecini inanılmaz derecede hızlandırsa da, beraberinde devasa bir güvenlik zayıflığı getirir: **Yazılım Tedarik Zinciri**.

Saldırganlar, hedefledikleri şirketin korunaklı üretim sunucularına saldırmak yerine, şirketin kullandığı küçük bir açık kaynak kütüphaneyi veya yazılım derleme (build) sunucusunu ele geçirerek çok daha büyük bir etki yaratabilirler. Yakın geçmişteki **SolarWinds** ve **XZ Utils** olayları, yazılım tedarik zincirinin ne kadar kritik ve tehlikeli bir saldırı vektörü haline geldiğini acı bir şekilde göstermiştir.

---

### 2. Tedarik Zinciri Saldırılarının Anatomisi
Saldırganların yazılım tedarik zincirine sızmak için kullandığı en yaygın yöntemlerden bazıları şunlardır:

1.  **Bağımlılık Karışıklığı (Dependency Confusion):** Şirketlerin kendi iç ağlarında kullandığı özel paket isimlerinin (örneğin `şirket-odeme-sistemi`), npm veya PyPI gibi herkese açık havuzlarda sahte ve daha yüksek sürüm numarasıyla yayınlanarak derleme sistemlerinin yanlışlıkla bu sahte paketi indirmesinin sağlanmasıdır.
2.  **Yazım Hatası Suistimali (Typosquatting):** Popüler kütüphanelerin isimlerinin harf hatalı versiyonlarının (örneğin `requests` yerine `requesst`) oluşturulup içine zararlı kod yerleştirilerek kütüphaneyi yanlış yazan yazılımcıların ağa düşürülmesidir.
3.  **CI/CD Boru Hattı Ele Geçirme:** Geliştiricilerin kodlarını derleyen sunucularda veya kod havuzlarında (GitHub, GitLab vb.) zafiyet bulunarak derleme aşamasında araya sızılması ve yazılıma zararlı kod enjekte edilmesidir.

#### Yazılım Tedarik Zinciri Akışı ve Saldırı Noktaları
Aşağıdaki şema, yazılımın geliştirilmesinden son kullanıcıya ulaşmasına kadar geçen süreçteki saldırı noktalarını göstermektedir:

![Diyagram / Diagram](/img/mermaid-software-supply-chain-security-1-86382df6.svg)

---

### 3. SLSA Çerçevesi (Supply Chain Levels for Software Artifacts)
Tedarik zinciri güvenliğini sistematik hale getirmek için geliştirilen en önemli çerçevelerden biri **SLSA (Supply Chain Levels for Software Artifacts - Yazılım Bileşenleri için Tedarik Zinciri Seviyeleri)**'dır. Google ve OpenSSF öncülüğünde geliştirilen SLSA, yazılımın güvenli bir şekilde derlendiğini ve yol boyunca değiştirilmediğini doğrulamayı amaçlar.

SLSA'nın temelinde **Provenans (Provenance - Kaynak Belgesi)** kavramı yatar. Provenans, yazılımın tam olarak hangi kaynak koddan, nerede, hangi araçlarla ve ne zaman derlendiğini gösteren, kriptografik olarak imzalanmış bir tür "üretim etiketidir".

#### SLSA Derleme Seviyeleri (Build Track)
*   **Seviye 1 (Level 1):** Derleme süreci belgelenmiştir ve basit bir provenans raporu oluşturulur.
*   **Seviye 2 (Level 2):** Provenans raporu, derleme servisi tarafından kriptografik olarak imzalanmıştır. Bu sayede raporun sonradan değiştirilmesi engellenir.
*   **Seviye 3 (Level 3):** Derleme ortamı tamamen izole edilmiştir. Farklı projelerin derleme süreçlerinin birbirini kirletmesi (cross-contamination) engellenir ve derleme sürecinin tekrar üretilebilir (reproducible) olması garanti altına alınır.

---

### 4. SBOM (Software Bill of Materials): Yazılımın İçerik Reçetesi
Bir gıda paketinin arkasındaki "içindekiler" tablosu gibi, **SBOM (Software Bill of Materials)** da bir yazılım paketinin içindeki tüm bileşenleri, kütüphaneleri, bunların sürümlerini ve lisans bilgilerini listeleyen standartlaştırılmış bir makinece okunabilir belgedir (CycloneDX veya SPDX formatlarında).

SBOM, özellikle yeni bir güvenlik açığı (CVE) çıktığında hayati önem taşır. Örneğin, 2021 yılındaki **Log4Shell** krizinde şirketlerin en büyük sorunu, hangi uygulamalarının içinde Log4j kütüphanesinin kullanıldığını bilmemesiydi. SBOM envanterine sahip olan organizasyonlar, tek bir sorguyla hangi yazılımlarının savunmasız olduğunu saniyeler içinde tespit edebilmişlerdir.

---

## English (EN)

### 1. Introduction: The Building Blocks of Modern Software
Modern software is rarely constructed from scratch. Today, the vast majority of an application's codebase consists of open-source libraries, package dependencies, and automated CI/CD (Continuous Integration / Continuous Deployment) pipelines. While this component-based development dramatically accelerates release cycles, it introduces a significant attack vector: the **Software Supply Chain**.

Instead of trying to break through hardened enterprise perimeters or production systems, modern adversaries compromise a minor, trusted open-source dependency or breach the build environment. High-profile incidents like the **SolarWinds** compromise and the near-miss **XZ Utils** backdoor have made software supply chain security a top priority for cybersecurity professionals worldwide.

---

### 2. Anatomy of Software Supply Chain Attacks
Adversaries target different links in the supply chain to inject malicious payloads into trusted software:

1.  **Dependency Confusion:** Attackers identify internal private package names used by a company (e.g., `company-auth-module`) and register the exact same name on a public registry (like npm or PyPI) with a much higher version number. When the company's build system runs, it pulls the malicious public version instead of the internal one.
2.  **Typosquatting:** Creating packages with names very similar to popular open-source libraries (e.g., `reqeusts` instead of `requests`). Gaining entry when developers make typographical errors during installation.
3.  **CI/CD Pipeline Compromise:** Hijacking developer credentials, compromising code repositories (GitHub, GitLab), or exploiting vulnerabilities in build servers to inject unauthorized code during the build process before the final binary is compiled.

#### The Software Supply Chain and Attack Vectors
The diagram below illustrates the path code takes from development to deployment and highlights where attackers typically intervene:

![Diyagram / Diagram](/img/mermaid-software-supply-chain-security-2-bb700d0e.svg)

---

### 3. The SLSA Framework (Supply Chain Levels for Software Artifacts)
To systematize software supply chain security, the industry introduced **SLSA (Supply Chain Levels for Software Artifacts)**. Led by Google and the OpenSSF, SLSA provides a set of standards and controls to ensure that software artifacts are built securely and haven't been tampered with.

The cornerstone of the SLSA framework is **Provenance**. Provenance is cryptographically signed metadata that describes how, when, and where an artifact was built. It serves as a digital "birth certificate" for the software.

#### SLSA Build Track Levels
*   **Level 1:** The build process is fully scripted, and basic provenance data is generated.
*   **Level 2:** The build service cryptographically signs the provenance, preventing tampering after the build is completed.
*   **Level 3:** The build environment is completely isolated, preventing cross-build contamination. The build process must be reproducible, ensuring that the same source code always yields the same binary under the same build configuration.

---

### 4. SBOM (Software Bill of Materials): The Ingredients List
Similar to the nutrition label on packaged food, a **SBOM (Software Bill of Materials)** is a formal, machine-readable inventory (typically in SPDX or CycloneDX format) of all the ingredients, libraries, transitive dependencies, and licenses contained within a software package.

The value of an SBOM becomes apparent when a new zero-day vulnerability is announced. During the **Log4Shell** crisis in late 2021, organizations struggled to identify which of their systems contained the vulnerable Log4j library. With an SBOM-indexed software inventory, IT and security teams can query their database and pinpoint vulnerable systems in seconds, dramatically reducing response and mitigation times.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / software-supply-chain-security]]*
