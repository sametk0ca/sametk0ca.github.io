+++
title = "Windows Event Logs Analizi | Windows Event Logs Analysis"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Windows işletim sistemi, arka planda gerçekleşen her türlü önemli olayı (Giriş denemeleri, uygulama hataları, sistem değişiklikleri) "Event Log" adı verilen dosyalarda saklar. Bir siber güvenlik uzmanı için bu loglar, olay yerindeki parmak izleri gibidir.

### 1. Temel Log Kategorileri
Windows'ta üç ana log kanalı vardır:
- **System (Sistem):** Sürücülerin yüklenmesi veya donanım hataları gibi Windows'un kendi olayları.
- **Application (Uygulama):** Bilgisayardaki programların (Örn: Office, Tarayıcı) ürettiği hata veya bilgi mesajları.
- **Security (Güvenlik):** En kritik kısımdır. Kim giriş yaptı? Kim dosyayı sildi? Kim şifreyi yanlış girdi? Hepsi buradadır.

### 2. Bilmen Gereken Bazı Terimler
- **Event ID:** Her olay türünün benzersiz bir numarası vardır. (Örn: `4624` başarılı giriş, `4625` hatalı giriştir). Uzmanlar sadece bu numaralara bakarak ne olduğunu anlar.
- **Event Viewer:** Bu logları okumak için kullanılan Windows aracı.
- **Audit Policy (Denetim Politikası):** Windows'un neleri kaydedip neleri kaydetmeyeceğini belirleyen ayarlar. Eğer bu ayar kapalıysa, saldırgan sızsa bile log oluşmaz.
- **Artifact:** Sistemde bir olaydan sonra kalan dijital kalıntı (iz).

### 3. Kritik Event ID Örnekleri
- **4624:** Başarılı Oturum Açma (Sisteme kim girdi?).
- **4625:** Hatalı Oturum Açma (Saldırgan şifre mi deniyor?).
- **4720:** Yeni Kullanıcı Oluşturuldu (Saldırgan kendine gizli bir hesap mı açtı?).
- **1102:** Loglar Temizlendi (Saldırgan izlerini mi siliyor?).

### Gerçek Dünya Analojisi
Windows Event Logları, bir binanın girişindeki ziyaretçi defteri gibidir. Kimin saat kaçta geldiği, hangi anahtarı kullandığı ve ne zaman çıktığı bu deftere yazılır. Eğer defterde "Gece 03:00'te biri yanlış anahtar denedi" yazıyorsa, bu bir saldırı belirtisidir.

---

## English Version

The Windows operating system stores all kinds of important events that occur in the background (login attempts, application errors, system changes) in files called "Event Log". For a cybersecurity expert, these logs are like fingerprints at the crime scene.

### 1. Basic Log Categories
There are three main log channels in Windows:
- **System:** Windows' own events, such as drivers loading or hardware errors.
- **Application:** Error or information messages produced by programs on the computer (Ex: Office, Browser).
- **Security:** This is the most critical part. Who logged in? Who deleted the file? Who entered the wrong password? It's all here.

### 2. Some Terms You Should Know
- **Event ID:** Each event type has a unique number. (Ex: `4624` is successful entry, `4625` is incorrect entry). Experts figure out what's going on just by looking at these numbers.
- **Event Viewer:** The Windows tool used to read these logs.
- **Audit Policy:** Settings that determine what Windows will and will not record. If this setting is off, no logs will be created even if the attacker infiltrates.
- **Artifact:** Digital residue (trace) left in the system after an event.

### 3. Critical Event ID Examples
- **4624:** Successful Login (Who entered the system?).
- **4625:** Bad Login (Is an attacker trying a password?).
- **4720:** New User Created (Did the attacker create a secret account for himself?).
- **1102:** Logs Cleared (Is the attacker erasing his traces?).

### Real World Analogy
Windows Event Logs are like a guest book at the entrance of a building. Who arrived at what time, which key they used, and when they left are recorded in this book. If the notebook says "Someone tried the wrong key at 03:00 at night", this is a sign of an attack.
