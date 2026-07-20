+++
title = "Sınırlama (Containment) Stratejileri | Containment Strategies"
date = "2026-05-19"
draft = false
categories = ["IncidentResponse"]
type = "cyberwiki"
+++

Sınırlama, bir güvenlik olayı tespit edildikten hemen sonra saldırganın daha fazla zarar vermesini ve ağ içerisinde yayılmasını (lateral movement) durdurma sürecidir.

### Özet
Olay müdahalenin (Incident Response) en kritik aşamalarından biridir. Amaç, kanıtları yok etmeden saldırganı izole etmek ve sistemi korumaya almaktır.

### Teknik Detaylar
- **Short-term Containment:** Saldırganın erişimini anlık kesme (örn: port kapatma, kullanıcıyı askıya alma).
- **Long-term Containment:** Sistemin daha temiz bir bölgeye taşınması veya tamamen izole edilmesi.
- **Evidence Preservation:** Kısıtlama yaparken disk ve bellek (RAM) imajlarının bozulmamasına dikkat edilmesi.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Automated Containment:** SOAR araçları ile kritik saldırılara milisaniyeler içinde tepki verin.
- **VLAN Isolation:** Şüpheli sunucuyu anında "Karantina VLAN"ına taşıyın.
- **Forensics First:** Sunucuyu formatlamadan veya kapatmadan önce adli bilişim analizi için gerekli verileri toplayın.

---

## English Version

Containment is the process of stopping an attacker from causing further damage and spreading within the network (lateral movement) immediately after a security incident is detected.

### Summary
It is one of the most critical stages of Incident Response. The aim is to isolate the attacker and protect the system without destroying the evidence.

### Technical Details
- **Short-term Containment:** Instantly cutting off the attacker's access (e.g. closing the port, suspending the user).
- **Long-term Containment:** Moving the system to a cleaner area or isolating it completely.
- **Evidence Preservation:** When restricting, be careful not to corrupt disk and memory (RAM) images.

### Security Approach and Best Practices
- **Automated Containment:** React to critical attacks within milliseconds with SOAR tools.
- **VLAN Isolation:** Instantly move the suspect server to the "Quarantine VLAN".
- **Forensics First:** Collect necessary data for forensic analysis before formatting or shutting down the server.
