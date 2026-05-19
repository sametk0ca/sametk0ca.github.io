+++
title = "Windows Dosya Sistemi (NTFS)  İzinler - Teknik Detay"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "OS"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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