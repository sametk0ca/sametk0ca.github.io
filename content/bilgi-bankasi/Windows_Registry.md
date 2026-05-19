+++
title = "Windows Registry Mantığı"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "bilgi-bankasi"
+++

Windows Kayıt Defteri (Registry), işletim sisteminin, donanımın ve yazılımların tüm ayarlarının tutulduğu devasa bir veritabanıdır. Siber güvenlik için Registry, hem bir saldırı alanı (Kalıcılık) hem de bir kanıt kaynağıdır.

### 1. Hiyerarşik Yapı (Hives)
Registry 5 ana daldan (Hives) oluşur:
- **HKEY_LOCAL_MACHINE (HKLM):** Tüm sistemi ilgilendiren ayarlar.
- **HKEY_CURRENT_USER (HKCU):** O an oturumu açık olan kullanıcıya özel ayarlar.
- **HKEY_CLASSES_ROOT (HKCR):** Dosya ilişkilendirmeleri (Hangi dosya hangi programla açılır?).

### 2. Kalıcılık (Persistence) Saldırıları
Saldırganlar, sistem her açıldığında zararlı yazılımlarını çalıştırmak için Registry'yi kullanır:
- **Run/RunOnce Anahtarları:** `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` altına eklenen bir kayıt, her açılışta çalışır.
- **Service Creation:** Yeni bir servis oluşturmak Registry'de kayıt oluşturmaktır.

### 3. Forensic Değeri (Artifacts)
Bir kullanıcı sistemde ne yaptıysa Registry'de iz bırakır:
- **UserAssist:** Kullanıcının hangi programı kaç kez ve en son ne zaman çalıştırdığını tutar.
- **ShellBags:** Kullanıcının hangi klasörlere eriştiğini (silinmiş olsalar bile) gösterir.
- **USBStor:** Sisteme takılan her USB cihazın seri numarasını ve takılma zamanını saklar.

### 4. Registry Manipulation
Zararlı yazılımlar, güvenlik duvarını kapatmak, antivirüs ayarlarını değiştirmek veya "Sticky Keys" (Shift tuşuna 5 kez basınca CMD açılması) gibi arka kapılar oluşturmak için Registry ayarlarını manipüle eder.