+++
title = "Windows Event Logs Analizi"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "bilgi-bankasi"
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