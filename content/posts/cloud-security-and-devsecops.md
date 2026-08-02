---
title: "A'dan Z'ye Bulut Bilişim, Bulut Güvenliği ve DevSecOps Rehberi / End-to-End Cloud, Cloud Security, and DevSecOps Guide"
date: 2026-08-02
description: "Bulut bilişim mimarilerinden başlayarak, bulut güvenliği yapılandırmalarına ve CI/CD süreçlerine güvenliği entegre eden DevSecOps pratiklerine kadar uzanan kapsamlı başucu rehberi. / A comprehensive guide spanning from cloud computing architectures and security configurations to DevSecOps practices integrating security into CI/CD pipelines."
tags: ["Cloud Security", "DevSecOps", "AWS", "Terraform", "Docker", "Kubernetes", "IAM", "CI-CD"]
categories: ["Blog"]
math: false
mermaid: true
---

# (TR) Bulut Bilişim, Bulut Güvenliği ve DevSecOps: Kapsamlı Başucu Rehberi

Günümüz modern yazılım dünyasında uygulamaları hızlıca canlıya almak kadar, bu uygulamaların üzerinde çalıştığı altyapıyı korumak ve geliştirme süreçlerinin her aşamasına güvenliği entegre etmek de kritik bir zorunluluktur. Bu rehber; **Bulut Bilişim**, **Bulut Güvenliği** ve **DevSecOps** disiplinlerini kavramsal temellerden pratik kod örneklerine kadar en ince detaylarıyla ele almaktadır.

---

## 1. Bulut Bilişim (Cloud Computing) Temelleri

Bulut bilişim, bilişim kaynaklarının (sunucular, depolama alanları, veritabanları, ağ bileşenleri ve yazılımlar) internet üzerinden, talep doğrultusunda ve kullandığın kadar öde (Pay-as-you-go) modeliyle sunulmasıdır.

### 1.1 Hizmet Modelleri (Service Models)
Bulut sağlayıcıları (AWS, Azure, GCP) sorumluluğun kimde olduğuna bağlı olarak hizmetleri üç ana kategoride sunar:

1. **IaaS (Infrastructure as a Service - Altyapı Hizmeti):** 
   * **Açıklama:** En esnek modeldir. Bulut sağlayıcı size fiziksel veya sanal sunucuları, ağı ve depolama alanını kiralar. İşletim sistemini kurmak, yamamak ve güvenliğini sağlamak tamamen sizin sorumluluğunuzdadır.
   * **Örnekler:** AWS EC2, Azure VM, Google Compute Engine.
2. **PaaS (Platform as a Service - Platform Hizmeti):** 
   * **Açıklama:** Altyapı ve işletim sistemi yönetimi bulut sağlayıcıdadır. Siz sadece yazdığınız kodu yüklersiniz. Ölçekleme ve sunucu güncellemeleri otomatik yapılır.
   * **Örnekler:** AWS Elastic Beanstalk, Heroku, Google App Engine.
3. **SaaS (Software as a Service - Yazılım Hizmeti):** 
   * **Açıklama:** Son kullanıcının doğrudan tarayıcı üzerinden eriştiği hazır yazılımlardır. Hiçbir teknik altyapı yönetimine gerek yoktur.
   * **Örnekler:** Office 365, Gmail, Salesforce, Slack.

### 1.2 Sanallaştırma (Virtualization) vs Konteynerizasyon (Containerization)
* **Sanallaştırma (VM):** Donanım seviyesinde sanallaştırmadır. Her Sanal Makine (VM) kendi işletim sistemine (Guest OS) sahiptir. Bu durum yüksek izolasyon sağlasa da fazla kaynak (CPU, RAM) tüketimine ve yavaş açılış sürelerine neden olur.
* **Konteynerizasyon (Docker/Podman):** İşletim sistemi çekirdeği (Kernel) seviyesinde sanallaştırmadır. Tüm konteynerler aynı ana bilgisayarın (Host OS) işletim sistemi çekirdeğini paylaşır. Hafiftirler, saniyeler içinde başlarlar ve kaynak tüketimleri oldukça düşüktür.

### 1.3 Paylaşımlı Sorumluluk Modeli (Shared Responsibility Model)
Bulutta güvenlik, bulut sağlayıcısı ile müşteri arasında paylaşılan bir sorumluluktur:
* **Bulutun Güvenliği (Security OF the Cloud):** Altyapıyı sağlayan kurumun (örn: AWS) fiziksel veri merkezlerini, donanımları, kablolamayı ve hipervizör katmanını koruma sorumluluğudur.
* **Bulutun İçindeki Güvenlik (Security IN the Cloud):** Müşterinin (yani sizin) verileri şifreleme, ağ erişim kurallarını (Firewall) yönetme, kimlik ve erişim yetkilerini (IAM) düzenleme sorumluluğudur.

---

## 2. Bulut Güvenliği (Cloud Security) Derin İnceleme

Geleneksel veri merkezlerindeki fiziksel duvarlar bulut dünyasında yerini tamamen mantıksal sınırlara ve kimlik denetimlerine bırakmıştır.

### 2.1 Kimlik ve Erişim Yönetimi (IAM)
IAM, buluttaki kaynaklara kimlerin hangi şartlar altında erişebileceğini belirleyen güvenlik mekanizmasıdır.
* **Least Privilege (En Az Yetki) İlkesi:** Bir kullanıcıya veya servise sadece yapacağı iş için zorunlu olan en dar yetki seti verilmelidir.
* **Rol Tabanlı Erişim Kontrolü (RBAC):** Yetkiler doğrudan kişilere değil, rollere atanır. Kullanıcılar bu rolleri üstlenerek işlem yaparlar.

**Örnek Hatalı AWS IAM Politikası (Aşırı Yetkili):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

**Güvenli AWS IAM Politikası (Sadece Belirli S3 Bucket Okuma Yetkisi):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::sirket-raporlari",
        "arn:aws:s3:::sirket-raporlari/*"
      ]
    }
  ]
}
```

### 2.2 Bulut Ağ Güvenliği
* **VPC (Virtual Private Cloud):** Bulutta size özel yalıtılmış sanal ağ alanıdır.
* **Security Groups (Güvenlik Grupları):** Sunucu (örneğin EC2) seviyesinde çalışan durum bilgili (stateful) firewall'dur. Gelen ve giden trafiği kontrol eder.
* **NACL (Network Access Control List):** Alt ağ (Subnet) seviyesinde çalışan durum bilgisiz (stateless) firewall'dur. Trafiği hem giriş hem çıkış yönünde açıkça engellemek (Deny) veya izin vermek (Allow) için kullanılır.

### 2.3 CSPM ve CWPP Kavramları
* **CSPM (Cloud Security Posture Management):** Bulut altyapısının güvenlik duruşunu izler. Dışa açık S3 bucket'lar, açık SSH portları gibi yanlış yapılandırmaları (misconfiguration) otomatik tespit eder ve uyumluluk standartlarına (CIS, ISO 27001) göre raporlar.
* **CWPP (Cloud Workload Protection Platform):** Bulutta çalışan sanal makineler, konteynerler ve serverless fonksiyonlar gibi iş yüklerini çalışma zamanında (runtime) malware ve zafiyetlere karşı korur.

---

## 3. DevSecOps: Yazılım Yaşam Döngüsünde Güvenlik

DevSecOps; geliştirme (Dev), güvenlik (Sec) ve operasyon (Ops) ekiplerinin ortak sorumluluk alarak, güvenlik süreçlerini yazılım yaşam döngüsünün en başına çekmesini (**Shift-Left**) hedefler.

```text
       [ Plan ] ➔ [ Code ] ➔ [ Build ] ➔ [ Test ]
          ▲                                 │
          │                                 ▼
       [ Monitor ] ◀ [ Deploy ] ◀ [ Release ]
          (Her aşamada Güvenlik Taramaları entegre edilir)
```

### 3.1 CI/CD Sürecinde Güvenlik Taramaları
Bir DevSecOps boru hattında aşağıdaki güvenlik testleri otomatik olarak koşulmalıdır:
1. **SAST (Static Application Security Testing):** Yazılım henüz derlenmeden veya çalıştırılmadan kod analiz edilerek olası güvenlik açıkları (SQL Injection, XSS) tespit edilir. (Örn: SonarQube, Semgrep).
2. **DAST (Dynamic Application Security Testing):** Çalışan uygulama dışarıdan taklit edilen siber saldırılarla taranır. (Örn: OWASP ZAP).
3. **SCA (Software Composition Analysis):** Uygulamanın kullandığı üçüncü parti kütüphanelerin (bağımlılıkların) zafiyet barındırıp barındırmadığı ve lisans uyumlulukları kontrol edilir. (Örn: Snyk, Dependency-Check).
4. **SBOM (Software Bill of Materials):** Uygulamanın içerdiği tüm bileşenlerin envanteridir. Tedarik zinciri güvenliği için kritik öneme sahiptir.

### 3.2 Kod Olarak Altyapı Güvenliği (IaC Security)
Modern sistemlerde sunucular ve ağ yapılandırmaları Terraform, Ansible veya CloudFormation gibi kodlarla yönetilir. Bu kodların canlıya çıkmadan taranması gerekir.

**Örnek Güvensiz Terraform Kodu (Dışa Açık SSH Portu):**
```hcl
resource "aws_security_group" "guvensiz_sg" {
  name        = "guvensiz-sg"
  description = "Herkese acik SSH portu"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # BÜYÜK RİSK: Herkes erişebilir!
  }
}
```

**Güvenli Terraform Kodu (Sadece Şirket IP Adresine Açık):**
```hcl
resource "aws_security_group" "guvenli_sg" {
  name        = "guvenli-sg"
  description = "Sadece ofis IP adresine acik SSH portu"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["195.175.20.40/32"] # Sadece şirket dış IP'si
  }
}
```

**Tfsec veya Checkov ile Analiz:**
Yukarıdaki güvensiz kod CI/CD aşamasında `checkov -f main.tf` veya `tfsec` aracıyla taranarak otomatik olarak reddedilir ve canlıya alınması engellenir.

### 3.3 Konteyner ve Orkestrasyon (Kubernetes) Güvenliği
* **Konteyner İmaj Taraması (Image Scanning):** Docker imajları oluşturulurken içerisindeki paketlerin zafiyetleri `trivy` veya `grype` gibi araçlarla taranmalıdır.
* **Kubernetes Güvenliği (Hardening):**
  * Konteynerler asla `root` yetkisiyle çalıştırılmamalıdır (`runAsNonRoot: true`).
  * Pod'ların dosya sistemleri salt okunur olmalıdır (`readOnlyRootFilesystem: true`).
  * Ağ politikaları (NetworkPolicies) ile mikroservisler arasındaki erişim en aza indirgenmelidir.

---

## 📋 Özet ve Son Söz
Bulut güvenliği ve DevSecOps, statik bir durum değil dinamik bir süreçtir. Güvenliğin hızı engellememesi, aksine otomasyon araçlarıyla geliştirme sürecini desteklemesi hedeflenmelidir. Her satır altyapı kodunun denetlenmesi ve yetkilendirmelerin en küçük yetki prensibine uygun yapılması modern bulut mimarisinin temel anahtarıdır.

---

# (EN) Cloud Computing, Cloud Security, and DevSecOps: A Comprehensive Guide

In the modern software ecosystem, deploying applications rapidly is as critical as securing the underlying infrastructure and integrating security into every step of the development pipeline. This guide covers the foundations of **Cloud Computing**, **Cloud Security**, and **DevSecOps** from concepts to practical code implementations.

---

## 1. Cloud Computing Foundations

Cloud computing is the on-demand delivery of compute power, database storage, applications, and other IT resources through the internet with a pay-as-you-go pricing model.

### 1.1 Cloud Service Models
Cloud service providers (AWS, Azure, GCP) offer services grouped into three primary models depending on the scope of customer responsibility:

1. **IaaS (Infrastructure as a Service):**
   * **Description:** The most flexible model where the provider rents you physical or virtual servers, networking, and storage. Operating system management, patching, and security are fully your responsibility.
   * **Examples:** AWS EC2, Azure VMs, Google Compute Engine.
2. **PaaS (Platform as a Service):**
   * **Description:** The underlying hardware and OS are managed by the provider. You only upload your application code. Scaling and server updates are managed automatically.
   * **Examples:** AWS Elastic Beanstalk, Heroku, Google App Engine.
3. **SaaS (Software as a Service):**
   * **Description:** End-user applications accessed directly via a web browser. No infrastructure management or technical overhead is required.
   * **Examples:** Office 365, Gmail, Salesforce, Slack.

### 1.2 Virtualization vs Containerization
* **Virtualization (VM):** Hardware-level virtualization. Each VM runs a full guest operating system (Guest OS). This provides high isolation but incurs significant compute overhead (CPU, RAM) and slow startup times.
* **Containerization (Docker/Podman):** OS-level virtualization. Containers share the host OS kernel. They are lightweight, pack tightly, and spin up in milliseconds.

### 1.3 The Shared Responsibility Model
Security in the cloud is shared between the provider and the customer:
* **Security OF the Cloud:** The provider (e.g., AWS) is responsible for securing physical facilities, compute, storage, networking, and the virtualization layer.
* **Security IN the Cloud:** The customer is responsible for encrypting data, managing network traffic policies (Firewalls), and configuring Identity and Access Management (IAM).

---

## 2. Cloud Security Deep Dive

Physical perimeters of on-premises data centers are replaced by logical perimeters and identity-centric controls in the cloud.

### 2.1 Identity and Access Management (IAM)
IAM governs who can access what resources under which conditions.
* **Principle of Least Privilege:** Users and services must only be granted the minimum permissions necessary to perform their specific tasks.
* **Role-Based Access Control (RBAC):** Permissions are assigned to roles, not individual users. Users assume these roles as needed.

**Example Insecure AWS IAM Policy (Over-privileged):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

**Secure AWS IAM Policy (ReadOnly access to a specific S3 bucket):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::sirket-raporlari",
        "arn:aws:s3:::sirket-raporlari/*"
      ]
    }
  ]
}
```

### 2.2 Cloud Network Security
* **VPC (Virtual Private Cloud):** An isolated virtual network dedicated to your cloud account.
* **Security Groups:** Stateful virtual firewalls at the instance (e.g., VM) level controlling inbound and outbound traffic.
* **Network ACLs (NACL):** Stateless firewalls at the subnet level that can explicitly permit or deny traffic in both directions.

### 2.3 CSPM and CWPP Concepts
* **CSPM (Cloud Security Posture Management):** Continuously scans cloud configurations for posture weaknesses (e.g., public S3 buckets, open port 22) and ensures compliance with frameworks like CIS or ISO 27001.
* **CWPP (Cloud Workload Protection Platform):** Protects active workloads (VMs, containers, serverless functions) from runtime exploits, vulnerabilities, and malware.

---

## 3. DevSecOps: Integrating Security Into CI/CD

DevSecOps bridges the gap between development, security, and operations. The core goal is to shift security left (**Shift-Left**), incorporating automated security guardrails early in the Software Development Life Cycle (SDLC).

```text
       [ Plan ] ➔ [ Code ] ➔ [ Build ] ➔ [ Test ]
          ▲                                 │
          │                                 ▼
       [ Monitor ] ◀ [ Deploy ] ◀ [ Release ]
          (Automated Security Scans integrated at every phase)
```

### 3.1 Security Testing in the Pipeline
An automated DevSecOps pipeline should execute the following tools:
1. **SAST (Static Application Security Testing):** Scans source code for potential vulnerabilities (like SQLi or XSS) without running the code (e.g., Semgrep, SonarQube).
2. **DAST (Dynamic Application Security Testing):** Tests the running application from the outside by mimicking cyber attacks (e.g., OWASP ZAP).
3. **SCA (Software Composition Analysis):** Scans third-party open-source dependencies for known CVEs and license compliance (e.g., Snyk).
4. **SBOM (Software Bill of Materials):** Generates a machine-readable list of all components inside your software, essential for securing the software supply chain.

### 3.2 Infrastructure as Code (IaC) Security
Modern cloud assets are defined via code templates (e.g., Terraform). These templates should be scanned for security flaws before provisioning.

**Example Insecure Terraform Code (Open SSH Port):**
```hcl
resource "aws_security_group" "guvensiz_sg" {
  name        = "insecure-sg"
  description = "Open SSH access to the world"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # CRITICAL RISK: Open to everyone!
  }
}
```

**Secure Terraform Code (Restricted to corporate IP Range):**
```hcl
resource "aws_security_group" "guvenli_sg" {
  name        = "secure-sg"
  description = "SSH access restricted to office IP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["195.175.20.40/32"] # Corporate IP only
  }
}
```

**Pipeline Scan with Checkov or Tfsec:**
By adding tools like `checkov` or `tfsec` to your workflow, insecure configurations will trigger a build failure and prevent deployment.

### 3.3 Container & Kubernetes Security
* **Container Image Scanning:** Scan Docker base images during the build phase for vulnerabilities using tools like `trivy` or `grype`.
* **Kubernetes Hardening:**
  * Configure pods with `runAsNonRoot: true` to prevent root-privilege execution.
  * Mount root filesystems as read-only (`readOnlyRootFilesystem: true`).
  * Implement `NetworkPolicies` to enforce microsegmentation and restrict unauthorized pod-to-pod communication.

---

## Conclusion
Cloud security and DevSecOps are continuous processes, not one-time objectives. Security should act as an enabler rather than a barrier to deployment. Enforcing IaC scanning, practicing least privilege, and automating response mechanisms are the cornerstones of a resilient cloud architecture.

---

*This post is linked to the Knowledge Base: [[Bulut_Guvenligi]]*
