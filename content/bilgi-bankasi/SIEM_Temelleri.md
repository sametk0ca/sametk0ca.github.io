+++
title = "SIEM (Security Information and Event Management)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

SIEM, bir şirketin tüm bilişim altyapısından (sunucular, ağ cihazları, firewall'lar) gelen dijital izleri (logları) tek bir merkezde toplayan, analiz eden ve şüpheli bir durum olduğunda alarm veren devasa bir "beyin"dir.

### 1. SIEM Nasıl Çalışır?
1. **Veri Toplama:** Ağdaki her cihaz "Bugün saat 10:00'da şu kullanıcı giriş yaptı" gibi kayıtlar üretir. SIEM bunları toplar.
2. **Normalleştirme:** Farklı cihazların farklı dillerde yazdığı logları ortak bir dile çevirir.
3. **Korelasyon (İlişkilendirme):** En zeki kısmıdır. Farklı yerlerden gelen alakasız görünen olayları birleştirir. (Örn: "Dış kapıdan biri girdi" + "Server odasının ışığı yandı" = Alarm!).
4. **Alarm Üretme:** Şüpheli bir durum bulduğunda güvenlik ekibine (SOC) haber verir.

### 2. Bilmen Gereken Bazı Terimler
- **Log (Günlük Kaydı):** Bir sistemde gerçekleşen her türlü olayın dijital tarihçesi.
- **SOC (Security Operations Center):** SIEM ekranlarını izleyen ve alarmlara müdahale eden güvenlik merkezi ekibi.
- **False Positive (Hatalı Alarm):** Aslında zararsız olan bir olayın SIEM tarafından "saldırı" sanılması. (Örn: Şifresini unutan bir çalışanın çok deneme yapması).
- **Splunk & ELK:** Dünyanın en popüler iki SIEM/Log analiz platformudur.

### 3. Neden Gereklidir?
Bir bankada binlerce bilgisayar olduğunu düşünün. Bir saldırganın sadece bir bilgisayara sızdığını anlamak için her bilgisayarı tek tek kontrol edemezsiniz. SIEM, tüm resmi tek bir ekranda görmenizi sağlar.

### Gerçek Dünya Analojisi
SIEM, dev bir alışveriş merkezindeki (Şirket ağı) tüm güvenlik kameralarının (Loglar) bağlı olduğu bir izleme odası gibidir. Sistem, sadece bir kameraya bakmaz; "Birisi otoparktan gizlice girdi" ve hemen ardından "Kasanın olduğu katın alarmı çaldı" bilgisini birleştirip güvenliğe "Soygun var!" diye anında mesaj atar.