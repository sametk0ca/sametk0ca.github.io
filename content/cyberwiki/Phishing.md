+++
title = "Phishing (Oltalama) Teknikleri | Phishing Techniques"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

Phishing is the act of cyber attackers deceiving users by pretending to be a reliable institution (Bank, social media, workplace) and stealing sensitive information such as passwords and credit cards.

### 1. How Does Phishing Work?
It usually follows these steps:
1. **Baiting:** The attacker sends a compelling email such as “There is suspicious activity on your account” or “Salary raise list.”
2. **Hook:** The email contains a link to a fake website.
3. **Phishing:** When the user enters his password on the fake site, this information falls directly into the attacker's hands.

### 2. Common Types of Phishing
- **Spear Phishing:** It is an attack specifically prepared for a specific person or group (e.g. the accounting department of a company), not for everyone. The attacker does research on the victim beforehand.
- **Whaling:** It is an attack targeting "big fish" such as the CEO or senior executives of the company.
- **Pharming:** It is a method of redirecting the user to a fake site not by linking it, but by corrupting the DNS settings. Even if you type 'banka.com' into the browser, it will take you to the fake site.

### 3. Some Terms You Should Know
- **Spoofing:** The act of misleading the user by making the e-mail address or website very similar to the real one.
- **Urgency:** A panic-inducing tactic such as "If you do not do it immediately, your account will be closed", which is frequently used in phishing e-mails.
- **Typosquatting:** Trapping users by purchasing misspelled versions of known domains (e.g. `google.com` instead of `gogle.com`).

### 4. Ways of Protection
- Carefully check the sender address of the incoming e-mail (For example, it may be `destek@banka-onay.com` instead of `destek@banka.com`).
- Check where the links actually go by hovering over them without clicking on them.
- **Most Important:** Always use **MFA** to ensure that your passwords are useless even if stolen.

### Real World Analogy
Phishing is like real fishing. The attacker throws thousands of hooks (E-mail) into the sea (Internet). There is a delicious bait (Salary raise news) on the hook. When a fish (User) bites the bait, it is caught.
