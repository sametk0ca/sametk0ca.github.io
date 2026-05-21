+++
title = "Windows Dosya Sistemi (NTFS)  İzinler - Teknik Detay | Windows File System (NTFS) Permissions - Technical Details"
date = "2026-05-19"
draft = false
categories = ["OS"]
type = "cyberwiki"
+++

NTFS, hiyerarşik bir yapıdan ziyade, her şeyin bir **"Nitelik" (Attribute)** olarak tanımlandığı veritabanı benzeri bir sistemdir.

### 1. MFT (Master File Table) Kayıtları
NTFS'de her dosyanın bir MFT kaydı vardır. Bu kayıtta siber güvenlik için hayati olan nitelikler bulunur:
- **$STANDARD_INFORMATION:** Dosyanın MAC (Modified, Accessed, Created) zamanlarını tutar. Windows Explorer'da gördüğünüz tarihler budur.
- **$FILE_NAME:** Dosyanın adını ve klasör içindeki yerini tutar. Bu nitelikteki zaman damgaları, $STANDARD_INFORMATION'dan farklıdır.
- **Forensics (Timestomping):** Bir saldırgan dosyanın oluşturulma tarihini değiştirebilir ($STANDARD_INFORMATION'ı manipüle eder). Ancak $FILE_NAME içindeki zaman damgaları genellikle orijinal kalır. Bu çelişki, saldırganın izini sürmemizi sağlar.

### 2. İzinler: Read vs. Read & Execute
Bir siber güvenlik uzmanı için aradaki fark kritiktir:
- **Read:** Dosyayı açıp içindeki metni okumaya izin verir (Örn: Bir script dosyasının içeriğini görmek).
- **Read & Execute:** Dosyanın bir program gibi işlemci tarafından çalıştırılmasına izin verir. Zararlı yazılımlar genellikle bu yetkiye ihtiyaç duyar.
- **Modify vs. Write:** `Modify` yetkisi, dosyanın silinmesine de izin verirken, `Write` sadece üzerine yazmaya veya ekleme yapmaya izin verir.

### 3. ADS (Alternate Data Streams) Teknik Detay
NTFS, dosyaları `Veri:Akış` formatında saklar. Varsayılan akış `$DATA`'dır.
- **Analiz:** Bir dosyayı `dir /r` komutuyla incelemezseniz, dosyanın arkasına gizlenmiş olan diğer veri akışlarını göremezsiniz.
- **Zone.Identifier:** İnternetten indirdiğiniz dosyalara Windows tarafından otomatik olarak eklenen bir ADS'dir. Adli incelemede bir dosyanın internetten geldiğinin en net kanıtıdır.

### 4. Disk Şifreleme (EFS vs. BitLocker)
- **EFS (Encrypting File System):** Dosya bazlı şifrelemedir. Kullanıcının oturum açma şifresine bağlıdır. Kullanıcı şifresi sıfırlanırsa (admin tarafından bile olsa), veriye erişim kaybolabilir.
- **BitLocker:** Tüm disk bölüntüsünü şifreler. Bilgisayar çalındığında diski söküp başka yere takarak veriye erişmeyi engeller (TPM ile birlikte çalışır).

---

## English Version

Rather than a hierarchical structure, NTFS is a database-like system where everything is defined as an "Attribute"**.

### 1. MFT (Master File Table) Records
In NTFS, every file has an MFT record. This registry contains attributes vital to cybersecurity:
- **$STANDARD_INFORMATION:** Keeps the MAC (Modified, Accessed, Created) times of the file. These are the dates you see in Windows Explorer.
- **$FILE_NAME:** Holds the name of the file and its location in the folder. Timestamps with this attribute are different from $STANDARD_INFORMATION.
- **Forensics (Timestomping):** An attacker can change the creation date of the file (manipulates $STANDARD_INFORMATION). However, timestamps in $FILE_NAME usually remain original. This contradiction allows us to track down the attacker.

### 2. Permissions: Read etc. Read & Execute
For a cybersecurity professional, the difference is critical:
- **Read:** Allows opening the file and reading the text inside it (Ex: Seeing the content of a script file).
- **Read & Execute:** Allows the file to be executed by the processor like a program. Malware often needs this authorization.
- **Modify vs. Write:** The `Modify` privilege also allows deletion of the file, while `Write` only allows overwriting or appending.

### 3. ADS (Alternate Data Streams) Technical Details
NTFS stores files in `Data:Stream` format. The default stream is `$DATA`.
- **Analysis:** If you do not examine a file with the `dir /r` command, you cannot see other data streams hidden behind the file.
- **Zone.Identifier:** It is an ADS that is automatically added by Windows to the files you download from the internet. In forensic examination, it is the clearest evidence that a file came from the internet.

### 4. Disk Encryption (EFS vs. BitLocker)
- **EFS (Encrypting File System):** It is file-based encryption. It depends on the user's login password. If the user password is reset (even by the admin), access to data may be lost.
- **BitLocker:** Encrypts the entire disk partition. When the computer is stolen, it prevents access to data by removing the disk and inserting it elsewhere (works with TPM).
