+++
title = "RDP (Remote Desktop Protocol) Güvenliği"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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