+++
title = "SIEM (Security Information and Event Management)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
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

---

## English Version

SIEM is a huge "brain" that collects and analyzes digital traces (logs) from a company's entire IT infrastructure (servers, network devices, firewalls) in a single center and raises an alarm when there is a suspicious situation.

### 1. How Does SIEM Work?
1. **Data Collection:** Every device on the network produces records such as "Today at 10:00, the following user logged in." SIEM collects them.
2. **Normalization:** It converts the logs written by different devices in different languages ​​into a common language.
3. **Correlation:** This is the smartest part. It combines seemingly unrelated events from different places. (Ex: "Someone entered from the outside door" + "The server room light turned on" = Alarm!).
4. **Alarm Generation:** When it finds a suspicious situation, it notifies the security team (SOC).

### 2. Some Terms You Should Know
- **Log:** A digital history of any event that occurs in a system.
- **SOC (Security Operations Center):** Security center team that monitors SIEM screens and responds to alarms.
- **False Positive (False Alarm):** An event that is actually harmless is mistaken for an "attack" by the SIEM. (Ex: An employee who forgets his password makes many attempts).
- **Splunk & ELK:** The two most popular SIEM/Log analysis platforms in the world.

### 3. Why is it necessary?
Imagine there are thousands of computers in a bank. You can't check every computer individually to find out if an attacker has infiltrated just one computer. SIEM lets you see the whole picture on a single screen.

### Real World Analogy
SIEM is like a monitoring room to which all security cameras (Logs) in a giant shopping mall (Company network) are connected. The system doesn't just look at a camera; Combining the information "Someone sneaked in from the parking lot" and then immediately saying "The alarm went off on the floor where the safe was located", he told the security "There is a robbery!" He instantly sends a message.
