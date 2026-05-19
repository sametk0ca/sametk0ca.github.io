+++
title = "Uyarı Türleri ve Eşik Değerleri (Alert Types)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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