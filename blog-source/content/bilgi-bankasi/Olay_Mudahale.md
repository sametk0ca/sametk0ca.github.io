+++
title = "Olay Müdahale Süreci (Incident Response)"
date = "2026-05-19"
draft = false
categories = ["IncidentResponse"]
type = "bilgi-bankasi"
+++

Bir siber güvenlik olayı gerçekleştiğinde izlenmesi gereken adımlar ve temel kavramlar.

## Olay Müdahale Aşamaları (NIST/SANS)

1. **Preparation (Hazırlık):** Araçların ve süreçlerin hazır hale getirilmesi.
2. **Identification (Tanımlama):** Bir olayın gerçekleştiğinin saptanması.
3. **Containment (Sınırlandırma):** Saldırının yayılmasının önlenmesi.
4. **Eradication (Yok Etme):** Tehdidin sistemden tamamen temizlenmesi.
5. **Recovery (Kurtarma):** Sistemlerin normale döndürülmesi.
6. **Lessons Learned (Alınan Dersler):** Gelecekteki olayları önlemek için analizin yapılması.

## Tehdit Avcılığı ve Analizi

### 🔍 Threat Hunting
Sistemlerde henüz tespit edilmemiş tehditleri proaktif olarak arama süreci.

### 🕵️ OSINT (Open Source Intelligence)
Açık kaynaklı istihbarat toplama süreci.

### 🏺 Honeypots
Saldırganları şaşırtmak ve bilgi toplamak için kurulan sahte sistemler (Yem).

## Önemli Kavramlar
- **Zero-Day (Sıfırıncı Gün):** Henüz yaması çıkmamış veya bilinmeyen zafiyet.
- **APT (Advanced Persistent Threat):** Gelişmiş kalıcı tehdit (Genellikle devlet destekli gruplar).
- **Vulnerability Management:** Zafiyetlerin düzenli olarak taranması ve giderilmesi süreci.
- **Runbooks:** Belirli olay türleri için önceden tanımlanmış müdahale adımları.
- **False Positive / Negative:** Yanlış alarm veya alarmın tetiklenmemesi durumları.