+++
title = "CSPM (Cloud Security Posture Management)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Cloud"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

CSPM, bulut altyapılarındaki yanlış yapılandırmaları (misconfigurations) ve uyumluluk risklerini sürekli olarak izleyen ve raporlayan bir güvenlik çözümüdür.

### Özet
Bulut ortamlarındaki en büyük güvenlik riski, insan hatası kaynaklı yanlış yapılandırmalardır (örn: açık bir S3 bucket). CSPM araçları bu riskleri otomatik olarak tespit eder.

### Teknik Detaylar
- **Misconfiguration Detection:** Açık portlar, şifrelenmemiş diskler, yetersiz loglama gibi durumların tespiti.
- **Compliance Mapping:** Altyapının CIS, SOC2, PCI-DSS gibi standartlara uygunluğunun kontrolü.
- **Auto-Remediation:** Tespit edilen bir hatanın (örn: açık bir SSH portu) otomatik olarak kapatılması.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Continuous Monitoring:** Bulut ortamı dinamiktir; taramaları anlık veya çok kısa aralıklarla yapın.
- **Multi-Cloud Visibility:** Tüm bulut sağlayıcılarınızı (AWS, Azure, GCP) tek bir panelden izleyin.
- **Drift Detection:** Onaylı altyapı kodundan (IaC) sapmaları anında tespit edin.