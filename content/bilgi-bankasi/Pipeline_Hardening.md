+++
title = "Build Pipeline Hardening"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

Build Pipeline Hardening, yazılımın derlendiği ve dağıtıldığı CI/CD hatlarının (Jenkins, GitHub Actions, GitLab CI) saldırılara karşı sıkılaştırılması ve güvenli hale getirilmesidir.

### Özet
Pipeline'lar, üretim ortamına (production) açılan doğrudan kapılardır. Buraya sızan bir saldırgan, koda zararlı yazılım enjekte edebilir veya tüm bulut şifrelerinizi ele geçirebilir.

### Teknik Detaylar
- **Runner Security:** Build işlemlerini yürüten sunucuların (Runners) her işlem sonrası sıfırlanması (ephemeral runners).
- **Secrets Management:** Şifrelerin ve API anahtarlarının pipeline kodunda düz metin olarak değil, güvenli "Secret" depolarından çekilmesi.
- **Least Privilege:** Pipeline'ın bulut ortamında sadece ihtiyacı olan yetkilere sahip olması.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **No Manual Intervention:** Üretim ortamına kod dağıtımını manuel değil, sadece onaylı pipeline'lar üzerinden yapın.
- **Branch Protection:** Ana kod dalına (main/master) doğrudan kod pushlanmasını engelleyin ve zorunlu kod incelemesi (Code Review) uygulayın.
- **Pipeline Monitoring:** Pipeline üzerindeki şüpheli aktiviteyi (örn: anormal bir script çalıştırılması) loglayın ve izleyin.