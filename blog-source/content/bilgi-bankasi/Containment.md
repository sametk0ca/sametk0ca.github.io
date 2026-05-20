+++
title = "Sınırlama (Containment) Stratejileri"
date = "2026-05-19"
draft = false
categories = ["IncidentResponse"]
type = "bilgi-bankasi"
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