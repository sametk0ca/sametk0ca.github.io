---
title: "Kerberoasting"
date: 2026-10-05
description: "How Kerberoasting turns any domain user into an offline password cracker for service accounts, and how to detect it with Event 4769. / Kerberoasting saldırısı herhangi bir alan kullanıcısını servis hesaplarının parolalarını çevrimdışı kıran birine nasıl dönüştürür ve Event 4769 ile nasıl tespit edilir."
draft: false
tags: ["Kerberos", "Active Directory", "Blue Team", "Detection", "MITRE ATT&CK"]
categories: ["Blog"]
related:
  - "[[Kerberos_Mantigi|Kerberos - Bilet Tabanlı Kimlik Doğrulama Mekanizması]]"
  - "[[Pass_the_Hash_Ticket|Pass the Hash Golden Ticket]]"
  - "[[Windows_Logs|Windows Event Logs Analizi]]"
  - "[[Honeypot|Honeypot]]"
---

## 🇹🇷 Türkçe (TR)

Kerberoasting, Active Directory ortamlarında bir servis hesabının parolasını **çevrimdışı** kırmaya dayanan bir saldırıdır (MITRE ATT&CK T1558.003). Saldırganın başlangıçta yalnızca sıradan, yetkisiz bir alan (domain) kullanıcısı olması yeterlidir. Parola denemeleri hedef sisteme gitmediği için hesap kilitlenmesi olmaz ve ağda sınırlı iz kalır.

### Neden Çalışır?

Bir kullanıcı bir servise (SQL, IIS, dosya sunucusu vb.) erişmek istediğinde, Domain Controller'dan o servis için bir **servis bileti (TGS)** ister. Servis, bir **SPN (Service Principal Name)** ile tanımlanır. Bu bilet, **servis hesabının parola türevi (hash) ile şifrelenir**.

Kritik nokta: Domain Controller, bileti isteyen kullanıcının o servise erişim yetkisi olup olmadığına bakmaz. SPN'si olan herhangi bir hesap için, kimliği doğrulanmış herhangi bir kullanıcı bilet isteyebilir. Yetki kontrolünü servisin kendisi yapar.

### Saldırı Akışı

1. Saldırgan alan içinde SPN'si olan hesapları listeler (LDAP sorgusu).
2. Her SPN için bir TGS ister.
3. Biletleri hafızadan veya ağdan çıkarıp bir dosyaya yazar. Rubeus ve Impacket `GetUserSPNs.py` bu iş için yaygın araçlardır.
4. Biletleri kendi makinesinde Hashcat veya John ile kırar (Hashcat modları: RC4 için 13100, AES128 için 19600, AES256 için 19700).
5. Parola zayıfsa servis hesabının kimliğine bürünür. Bu hesap sıklıkla gereğinden fazla yetkiye sahiptir.

Servis hesaplarının parolaları genellikle insanlar tarafından belirlenir, nadiren değişir ve kolay hatırlanacak şekilde seçilir. Saldırının hedefi tam olarak bu zayıflıktır.

### RC4 ve AES Farkı

Bilet RC4 (şifre türü `0x17`) ile şifrelenmişse kırma çok daha hızlıdır. AES ile şifrelenmiş biletler de kırılabilir ama aynı parola için çok daha yavaştır. Bu fark hem önlemde hem tespitte işe yarar.

### Tespit

Kaynak: Domain Controller üzerindeki **Event ID 4769** (Kerberos servis bileti istendi).

- **RC4 bileti:** `Ticket Encryption Type = 0x17`. Domain'inizdeki hesaplar AES destekliyorsa RC4 isteği şüphelidir. Eski sistemler normal trafikte de RC4 üretebilir, bu yüzden önce ortamınızın normalini çıkarın.
- **Hacim:** Aynı kullanıcıdan kısa sürede çok sayıda **farklı** servis için bilet isteği.
- **Gürültüyü ele:** Servis adı `$` ile biten (bilgisayar hesapları) ve `krbtgt` kayıtlarını filtreleyin, yalnızca başarılı (`Status = 0x0`) istekleri inceleyin.

Başlangıç noktası olarak basit bir Sigma kuralı:

```yaml
title: Possible Kerberoasting (RC4 Service Ticket Request)
status: experimental
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4769
    TicketEncryptionType: '0x17'
    Status: '0x0'
  filter:
    ServiceName|endswith: '$'
  filter_krbtgt:
    ServiceName: 'krbtgt'
  condition: selection and not filter and not filter_krbtgt
level: medium
```

Bu kural ortamınıza göre ayarlanmadan çok fazla uyarı üretebilir. Hacim eşiği ekleyerek (örneğin 10 dakikada 5'ten fazla farklı servis) güvenilirliğini artırın.

### Honeypot Hesabı ile Tespit

Çok güvenilir bir yöntem: kimsenin kullanmadığı, **sahte bir SPN'si olan cazip bir servis hesabı** oluşturun (uzun ve rastgele parolalı). Hiçbir meşru kullanıcı bu servise bilet istemez. Bu SPN için gelen her 4769 olayı yüksek güvenilirlikli bir alarmdır.

### Önleme

- Servis hesapları için **gMSA** (Group Managed Service Account) kullanın: parola otomatik, uzun ve rastgele yönetilir.
- gMSA mümkün değilse **uzun (25+ karakter), rastgele** parolalar kullanın ve düzenli döndürün.
- Hesaplarda **AES'i zorunlu kılın** ve gereksiz yere RC4 desteğini kapatın (önce uyumluluğu test edin).
- Kullanılmayan **SPN'leri kaldırın** ve servis hesaplarına gereğinden fazla yetki (özellikle Domain Admin) vermeyin.
- 4769 olaylarını SIEM'de izleyin ve yukarıdaki tespit mantığını uygulayın.

### Kaynaklar

- [MITRE ATT&CK T1558.003: Kerberoasting](https://attack.mitre.org/techniques/T1558/003/)

---

## 🇬🇧 English (EN)

Kerberoasting is an attack on Active Directory environments that cracks a service account's password **offline** (MITRE ATT&CK T1558.003). The attacker only needs to start as an ordinary, unprivileged domain user. Because the password guesses never touch the target system, there are no account lockouts and little network noise.

### Why It Works

When a user wants to reach a service (SQL, IIS, a file server, etc.), they ask the Domain Controller for a **service ticket (TGS)** for it. The service is identified by an **SPN (Service Principal Name)**. That ticket is **encrypted with a key derived from the service account's password**.

The critical detail: the Domain Controller does not check whether the requesting user is allowed to use the service. Any authenticated user can request a ticket for any account that has an SPN. Authorization is left to the service itself.

### Attack Flow

1. The attacker lists accounts with SPNs in the domain (an LDAP query).
2. They request a TGS for each SPN.
3. They extract the tickets and save them to a file. Rubeus and Impacket's `GetUserSPNs.py` are common tools for this.
4. They crack the tickets on their own machine with Hashcat or John (Hashcat modes: 13100 for RC4, 19600 for AES128, 19700 for AES256).
5. If the password is weak, they impersonate the service account, which often has more privileges than it needs.

Service account passwords are often set by humans, rarely rotated, and chosen to be easy to remember. That is exactly the weakness this attack targets.

### RC4 vs. AES

Tickets encrypted with RC4 (encryption type `0x17`) crack much faster. AES tickets can still be cracked, but far more slowly for the same password. This difference helps with both prevention and detection.

### Detection

Source: **Event ID 4769** on the Domain Controller (a Kerberos service ticket was requested).

- **RC4 tickets:** `Ticket Encryption Type = 0x17`. If the accounts in your domain support AES, an RC4 request is suspicious. Legacy systems can produce RC4 in normal traffic too, so baseline your environment first.
- **Volume:** one user requesting tickets for many **different** services in a short time.
- **Cut the noise:** filter out service names ending in `$` (computer accounts) and `krbtgt`, and look only at successful requests (`Status = 0x0`).

A simple Sigma rule as a starting point:

```yaml
title: Possible Kerberoasting (RC4 Service Ticket Request)
status: experimental
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4769
    TicketEncryptionType: '0x17'
    Status: '0x0'
  filter:
    ServiceName|endswith: '$'
  filter_krbtgt:
    ServiceName: 'krbtgt'
  condition: selection and not filter and not filter_krbtgt
level: medium
```

Untuned, this rule can be noisy. Add a volume threshold (for example, more than 5 distinct services within 10 minutes) to make it more reliable.

### Detection with a Honeypot Account

A very reliable method: create an unused, **decoy service account with a fake SPN** (with a long, random password). No legitimate user ever requests a ticket for it, so every 4769 event for that SPN is a high-confidence alert.

### Prevention

- Use **gMSA** (Group Managed Service Accounts) for service accounts: passwords are long, random and managed automatically.
- If gMSA isn't possible, use **long (25+ characters), random** passwords and rotate them regularly.
- **Enforce AES** on accounts and disable RC4 support where it isn't needed (test compatibility first).
- Remove unused **SPNs** and don't give service accounts more privilege than they need, especially Domain Admin.
- Monitor 4769 events in your SIEM and apply the detection logic above.

### References

- [MITRE ATT&CK T1558.003: Kerberoasting](https://attack.mitre.org/techniques/T1558/003/)
