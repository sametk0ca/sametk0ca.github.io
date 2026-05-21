+++
title = "Tehdit Modelleme İş Akışları (Threat Modeling Workflows) | Threat Modeling Workflows"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
+++

Tehdit modelleme iş akışı, bir uygulamanın güvenliğini sağlamak için izlenen sistematik ve tekrarlanabilir adımlar bütünüdür.

### Özet
Sürekli teslimat (CI/CD) dünyasında tehdit modelleme, sadece tek seferlik bir aktivite değil, yazılım geliştirme yaşam döngüsüne (SDLC) entegre edilmiş dinamik bir süreç olmalıdır.

### Teknik Detaylar
- **Hazırlık:** Uygulamanın mimarisini anlama ve dokümantasyon toplama.
- **Diyagram Oluşturma:** Veri akış diyagramları (DFD) veya Trust Boundary çizimleri.
- **Tehdit Belirleme:** STRIDE veya PASTA gibi metodolojilerle tehditleri bulma.
- **Hafifletme (Mitigation):** Tehditlere karşı kontroller tasarlama.
- **Doğrulama:** Kontrollerin doğru uygulandığını test etme (Unit/Integration tests).

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **TM-as-Code:** Tehdit modellerini YAML/JSON formatında kod olarak tutun ve Git üzerinden yönetin.
- **Incremental Modeling:** Sadece yapılan yeni değişiklikler için tehdit modelini güncelleyin.
- **Developer-Centric:** Tehdit modellemeyi geliştiricilerin kendi araçlarıyla (örn: IDE eklentileri) yapabilmesini sağlayın.

---

## English Version

A threat modeling workflow is a systematic and repeatable set of steps followed to secure an application.

### Summary
In the world of continuous delivery (CI/CD), threat modeling should not just be a one-time activity but a dynamic process integrated into the software development lifecycle (SDLC).

### Technical Details
- **Preparation:** Understanding the architecture of the application and gathering documentation.
- **Diagramming:** Data flow diagrams (DFD) or Trust Boundary drawings.
- **Threat Identification:** Finding threats with methodologies such as STRIDE or PASTA.
- **Mitigation:** Designing controls against threats.
- **Verification:** Testing that controls are implemented correctly (Unit/Integration tests).

### Security Approach and Best Practices
- **TM-as-Code:** Keep threat models as code in YAML/JSON format and manage them via Git.
- **Incremental Modeling:** Only update the threat model for new changes made.
- **Developer-Centric:** Enable developers to do threat modeling with their own tools (e.g. IDE plugins).
