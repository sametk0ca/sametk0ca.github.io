+++
title = "Kubernetes Güvenliği ve RBAC"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "DevSecOps"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Kubernetes (K8s) güvenliği, geniş ve karmaşık bir orkestrasyon platformunun bileşenlerini, ağ trafiğini ve iş yüklerini koruma sürecidir.

### Özet
Kubernetes'te güvenlik, "4C" modeliyle (Cloud, Cluster, Container, Code) ele alınır. Platformun esnekliği, yanlış yapılandırma riskini de beraberinde getirir.

### Teknik Detaylar
- **RBAC (Role-Based Access Control):** Kimin hangi K8s API kaynaklarına erişebileceğini belirler.
- **Network Policies:** Podlar arası ağ trafiğini katman 3/4 seviyesinde kısıtlar.
- **Admission Controllers:** Cluster'a giren istekleri denetleyen ve değiştiren mekanizmalar (örn: OPA, Kyverno).

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **API Server Hardening:** K8s API sunucusunu internete kapatın ve güçlü kimlik doğrulaması kullanın.
- **Secret Management:** K8s Secret'larını varsayılan `base64` yerine HashiCorp Vault gibi araçlarla şifreleyerek yönetin.
- **Pod Security Admission:** Podların privileged modda çalışmasını engelleyen standartları (`Baseline`, `Restricted`) uygulayın.