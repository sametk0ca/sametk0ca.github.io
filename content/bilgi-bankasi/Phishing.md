+++
title = "Phishing (Oltalama) Teknikleri"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

Phishing, siber saldırganların kendilerini güvenilir bir kurum (Banka, sosyal medya, iş yeri) gibi göstererek kullanıcıları kandırması ve şifre, kredi kartı gibi hassas bilgileri çalması eylemidir.

### 1. Phishing Nasıl Çalışır?
Genellikle şu adımları izler:
1. **Yemleme:** Saldırgan, "Hesabınızda şüpheli işlem var" veya "Maaş zammı listesi" gibi ilgi çekici bir e-posta gönderir.
2. **Kanca:** E-postanın içinde sahte bir web sitesine giden bir link bulunur.
3. **Avlama:** Kullanıcı sahte siteye şifresini girdiğinde, bu bilgi doğrudan saldırganın eline geçer.

### 2. Yaygın Phishing Türleri
- **Spear Phishing (Zıpkınla Avlama):** Herkese değil, belirli bir kişiye veya gruba (Örn: Bir şirketin muhasebe departmanı) özel hazırlanan saldırıdır. Saldırgan kurban hakkında önceden araştırma yapar.
- **Whaling (Balina Avı):** Şirketin CEO'su veya üst düzey yöneticileri gibi "büyük balıkları" hedef alan saldırıdır.
- **Pharming:** Kullanıcıyı sahte siteye linkle değil, DNS ayarlarını bozarak yönlendirme yöntemidir. Siz tarayıcıya `banka.com` yazsanız bile sizi sahte siteye götürür.

### 3. Bilmen Gereken Bazı Terimler
- **Spoofing (Aldatma/Yanıltma):** E-posta adresini veya web sitesini gerçeğine çok benzer yaparak kullanıcıyı yanıltma eylemi.
- **Urgency (Aciliyet):** Phishing e-postalarında sıklıkla kullanılan "Hemen yapmazsanız hesabınız kapanacak" gibi panik yaratma taktiği.
- **Typosquatting:** Bilinen domainlerin yanlış yazılmış hallerini (Örn: `gogle.com` yerine `google.com`) satın alarak kullanıcıları tuzağa düşürmek.

### 4. Korunma Yolları
- Gelen e-postanın gönderici adresini dikkatlice kontrol edin (Örn: `destek@banka.com` yerine `destek@banka-onay.com` olabilir).
- Linklerin üzerine tıklamadan mouse ile bekleyerek (hover) gerçekte nereye gittiğini kontrol edin.
- **En Önemlisi:** Şifrelerinizin çalınsa bile işe yaramaması için her zaman **MFA** kullanın.

### Gerçek Dünya Analojisi
Phishing, gerçek bir balık avı gibidir. Saldırgan denize (İnternet) binlerce kanca (E-posta) atar. Kancanın ucunda lezzetli bir yem (Maaş zammı haberi) vardır. Bir balık (Kullanıcı) yemi ısırdığında avlanmış olur.