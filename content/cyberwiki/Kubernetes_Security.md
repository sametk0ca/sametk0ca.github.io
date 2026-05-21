+++
title = "Kubernetes Güvenliği ve RBAC | Kubernetes Security and RBAC"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

Kubernetes (K8s) security is the process of protecting the components, network traffic, and workloads of a large and complex orchestration platform.

### Summary
In Kubernetes, security is handled with the "4C" model (Cloud, Cluster, Container, Code). The flexibility of the platform comes with the risk of misconfiguration.

### Technical Details
- **RBAC (Role-Based Access Control):** Determines who can access which K8s API resources.
- **Network Policies:** Restricts inter-pod network traffic at layer 3/4 level.
- **Admission Controllers:** Mechanisms that control and modify requests entering the Cluster (eg: OPA, Kyverno).

### Security Approach and Best Practices
- **API Server Hardening:** Shut off the K8s API server from the internet and use strong authentication.
- **Secret Management:** Manage K8s Secrets by encrypting them with tools like HashiCorp Vault instead of the default `base64`.
- **Pod Security Admission:** Apply standards (`Baseline`, `Restricted`) that prevent pods from operating in privileged mode.
