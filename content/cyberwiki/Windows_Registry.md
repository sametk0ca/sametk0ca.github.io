+++
title = "Windows Registry Mantığı | Windows Registry Logic"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
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

---

## English Version

Windows Registry is a huge database where all the settings of the operating system, hardware and software are kept. For cybersecurity, Registry is both an attack surface (Persistence) and a source of evidence.

### 1. Hierarchical Structure (Hives)
The Registry consists of 5 main branches (Hives):
- **HKEY_LOCAL_MACHINE (HKLM):** Settings that concern the entire system.
- **HKEY_CURRENT_USER (HKCU):** Settings specific to the currently logged in user.
- **HKEY_CLASSES_ROOT (HKCR):** File associations (Which file opens with which program?).

### 2. Persistence Attacks
Attackers use the Registry to run their malware every time the system boots:
- **Run/RunOnce Switches:** A record added under `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` will run on every startup.
- **Service Creation:** Creating a new service means creating a record in the Registry.

### 3. Forensic Value (Artifacts)
Whatever a user does on the system leaves a trace in the Registry:
- **UserAssist:** Keeps track of which program the user ran, how many times and when it was last run.
- **ShellBags:** Shows which folders the user has accessed (even if they have been deleted).
- **USBStor:** Stores the serial number and insertion time of each USB device plugged into the system.

### 4. Registry Manipulation
Malware manipulates Registry settings to turn off the firewall, change antivirus settings, or create backdoors such as "Sticky Keys" (opening CMD by pressing the Shift key 5 times).
