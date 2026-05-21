+++
title = "Uyarı Türleri ve Eşik Değerleri (Alert Types) | Alert Types and Threshold Values ​​(Alert Types)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Uyarı türleri ve eşik değerleri, güvenlik izleme sistemlerinin (SIEM, EDR, IDS) hangi olayları "şüpheli" veya "tehlikeli" olarak işaretleyeceğini belirleyen parametrelerdir.

### Özet
Her olaya alarm kurmak "analist yorgunluğuna" (alert fatigue) yol açar. Doğru yapılandırılmış eşik değerleri, gürültüyü azaltarak gerçek tehditlere odaklanmayı sağlar.

### Teknik Detaylar
- **Threshold-based Alerts:** Belirli bir sürede yapılan hatalı giriş sayısı gibi sayısal sınırlar (örn: 5 dk'da 50 hatalı login).
- **Anomaly-based Alerts:** Normal kullanıcı davranışından sapmaların tespiti (örn: kullanıcının gece 3'te büyük veri indirmesi).
- **Signature-based Alerts:** Bilinen bir saldırı imzasının (örn: SQLi payload) tespiti.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Severity Levels:** Uyarıları Kritik, Yüksek, Orta ve Düşük olarak sınıflandırın.
- **Contextual Alerts:** Alarmları sadece teknik veriyle değil, varlık bilgisiyle (örn: "Kritik Veritabanı Sunucusu") zenginleştirin.
- **Regular Tuning:** Sahte pozitifleri (False Positives) azaltmak için alarm kurallarını düzenli olarak güncelleyin.

---

## English Version

Alert types and thresholds are parameters that determine which events security monitoring systems (SIEM, EDR, IDS) will mark as "suspicious" or "dangerous".

### Summary
Setting an alert for every event causes "analyst fatigue". Properly configured threshold values ​​reduce noise, allowing you to focus on real threats.

### Technical Details
- **Threshold-based Alerts:** Numerical limits such as the number of incorrect logins made in a certain period of time (e.g. 50 incorrect logins in 5 minutes).
- **Anomaly-based Alerts:** Detection of deviations from normal user behavior (e.g. user downloading large data at 3 am).
- **Signature-based Alerts:** Detection of a known attack signature (e.g. SQLi payload).

### Security Approach and Best Practices
- **Severity Levels:** Classify alerts as Critical, High, Medium and Low.
- **Contextual Alerts:** Enrich alerts with asset information (e.g. "Critical Database Server"), not just technical data.
- **Regular Tuning:** Update alarm rules regularly to reduce false positives.
