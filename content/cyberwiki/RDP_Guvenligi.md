+++
title = "RDP (Remote Desktop Protocol) Güvenliği | RDP (Remote Desktop Protocol) Security"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

RDP, Windows sistemlere grafik arayüzü (GUI) üzerinden uzaktan erişim sağlayan bir protokoldür. Varsayılan olarak TCP/UDP 3389 portunu kullanır.

### 1. Neden RDP Hedef Tahtasında?
RDP, saldırganların "en sevdiği" giriş noktalarından biridir. Sisteme girildiğinde doğrudan masaüstü erişimi sağladığı için ransomware (fidye yazılımı) saldırılarında sıkça kullanılır.

### 2. Kritik Güvenlik Özellikleri
- **NLA (Network Level Authentication):** Kullanıcı adı ve şifre doğrulanmadan oturum açma ekranının bile gösterilmemesini sağlar. Bu, kaynak tüketimini ve belirli exploit risklerini azaltır.
- **Şifreleme:** Modern RDP sürümleri TLS kullanarak trafiği şifreler.

### 3. En İyi Uygulamalar (Best Practices)
- **Asla İnternete Açmayın:** RDP'yi doğrudan internete açmak (Port forwarding) intihar gibidir. Uzaktan erişim için mutlaka **VPN** kullanılmalıdır.
- **Port Değişikliği:** 3389'u değiştirmek botları yavaşlatır ancak uzman bir saldırganı durdurmaz.
- **MFA Şartı:** Microsoft Duo veya RD Gateway üzerinden Çok Faktörlü Kimlik Doğrulama (MFA) eklenmelidir.
- **Hesap Kilitleme Politikası:** Ardışık yanlış girişlerde hesabı dondurmak kaba kuvvet saldırılarını önler.

### 4. Tarihi Bir Örnek: BlueKeep (CVE-2019-0708)
BlueKeep, RDP üzerinden kullanıcı müdahalesi olmadan sistemin ele geçirilmesine (Wormable) izin veren çok kritik bir açıktı. Bu tür açıklar, sistemlerin güncel tutulmasının ne kadar hayati olduğunu gösterir.

### Gerçek Dünya Analojisi
RDP, evinizin ön kapısı gibidir. Eğer kapıyı internete açarsanız, dünyadaki her hırsız kapı kolunu zorlayabilir. VPN kullanmak, önce evin bahçe kapısından (güvenli alan) girmeyi şart koşmak gibidir.

---

## English Version

RDP is a protocol that provides remote access to Windows systems via a graphical interface (GUI). By default it uses TCP/UDP port 3389.

### 1. Why is RDP in the Target?
RDP is one of attackers' favorite entry points. It is frequently used in ransomware attacks because it provides direct desktop access when entered into the system.

### 2. Critical Security Features
- **NLA (Network Level Authentication):** Ensures that the login screen is not even shown unless the username and password are verified. This reduces resource consumption and certain exploit risks.
- **Encryption:** Modern RDP versions encrypt traffic using TLS.

### 3. Best Practices
- **Never Open to the Internet:** Opening RDP directly to the Internet (Port forwarding) is like suicide. **VPN** must be used for remote access.
- **Port Change:** Changing 3389 will slow down bots but won't stop an expert attacker.
- **MFA Requirement:** Multi-Factor Authentication (MFA) must be added via Microsoft Duo or RD Gateway.
- **Account Locking Policy:** Freezing the account for consecutive incorrect logins prevents brute force attacks.

### 4. A Historical Example: BlueKeep (CVE-2019-0708)
BlueKeep was a critical vulnerability that allowed system takeover (Wormable) via RDP without user intervention. These types of vulnerabilities show how vital it is to keep systems updated.

### Real World Analogy
RDP is like the front door to your home. If you open the door to the internet, every thief in the world can pry the door handle. Using a VPN is like requiring you to enter the garden gate (secure area) of the house first.
