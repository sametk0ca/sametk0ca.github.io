Phishing remains one of the most common and effective ways for attackers to gain initial access to target systems. To counter this, defenders can deploy a variety of tools and controls designed to protect users from malicious emails.

The MITRE ATT&CK Framework describes [Phishing for Information](https://attack.mitre.org/techniques/T1598) as the attempt to trick targets into divulging information.

# SPF ( Sender Policy Framework )

“Sender Policy Framework (SPF) is used to authenticate the sender of an email. With an SPF record in place, Internet Service Providers can verify that a mail server is authorized to send email for a specific domain. An SPF record is a DNS TXT record containing a list of the IP addresses that are allowed to send email on behalf of your domain.”

![[616945d482ef350052080da1-1759814016781.svg]]

# DKIM ( Domain Keys Identified Mail )

“DKIM stands for DomainKeys Identified Mail and is used for the authentication of an email that’s being sent. Like SPF, DKIM is an open standard for email authentication that is used for DMARC alignment. A DKIM record exists in the DNS, but it is more complex than SPF. DKIM’s advantage is that it can survive forwarding, which makes it superior to SPF and a foundation for securing your email.”

Let's break it down. When an email is sent, the sending mail server uses a private key to add a digital signature to the email. The receiving server retrieves the public key from the domain's DKIM record to verify that the message truly came from the domain. If the signature matches, the email is authentic; otherwise, it may be flagged or rejected.

![[616945d482ef350052080da1-1759815078151.svg]]Harika bir seçim! Teknik detaylarda kaybolmadan, mantığını **"Dijital İmza ve Parmak İzi"** benzetmesiyle adım adım inceleyelim.

DKIM'in çalışma prensibi aslında iki ana oyuncuya dayanır: **Özel Anahtar (Private Key)** ve **Genel Anahtar (Public Key)**.

İşleyişi şöyle düşünebilirsin:

### 1. Gönderen Tarafı (İmzalama) 

Sen bir e-posta gönderdiğinde, sunucun arka planda şu işlemleri yapar:

- **Parmak İzi Alma:** Önce e-postanın içeriğinin (metin ve ekler) matematiksel bir özetini çıkarır. Buna "hash" denir ama biz buna **"dijital parmak izi"** diyelim. Bu parmak izi e-postaya özeldir; e-postada tek bir harf bile değişse, bu parmak izi tamamen değişir.
    
- **Mühürleme:** Sunucun, sadece kendisinde bulunan **"Özel Anahtar"**ı kullanarak bu parmak izini şifreler. İşte e-postanın başlığına (header) eklenen o karmaşık kod yığını, yani **DKIM İmzası** budur.
    

### 2. İletim Süreci 📨

E-posta internet üzerinden alıcıya doğru yola çıkar. Bu esnada e-postanın üzerinde senin sunucunun attığı o dijital mühür (DKIM imzası) yapışıktır.

### 3. Alıcı Tarafı (Doğrulama) 

E-posta karşı tarafın sunucusuna (örneğin Gmail veya Outlook) ulaştığında, alıcı sunucu şüpheci bir dedektif gibi davranır:

- **Anahtarı Bulma:** "Bu e-posta `ornek.com` adresinden geldiğini iddia ediyor" der ve `ornek.com`'un DNS kayıtlarına (herkese açık telefon rehberi gibi) bakar. Orada senin daha önce yayınladığın **"Genel Anahtar"**ı bulur.
    
- **Mühürü Açma:** Bulduğu bu Genel Anahtar ile e-postanın üzerindeki mühürü (DKIM imzasını) açmaya çalışır. Eğer anahtar kilide uyarsa, bu imzanın gerçekten senin Özel Anahtarınla atıldığı kanıtlanmış olur. Kimlik doğrulandı! ✅
    
- **İçerik Kontrolü:** Mühürü açınca içinden gönderirken oluşturulan **"dijital parmak izi"** çıkar. Alıcı sunucu, kendisine gelen e-postanın parmak izini de o an hesaplar. Eğer mührün içinden çıkan parmak izi ile kendi hesapladığı parmak izi birebir aynıysa, e-posta yolda değiştirilmemiş demektir. Bütünlük doğrulandı! ✅
    

Özetle; **Özel Anahtar** ile atılan imzayı, herkes **Genel Anahtar** ile kontrol edebilir ama o imzayı **sadece** sen (yani sunucun) atabilirsin.,

# DMARC ( Domain-Based Message Authentication, Reporting, and Conformance)

“DMARC, an open source standard, uses a concept called alignment to tie the result of two other open source standards,  SPF (a published list of servers that are authorized to send email on behalf of a domain) and DKIM (a tamper-evident domain seal associated with a piece of email), to the content of an email.”

This means that DMARC ensures the sender's domain matches the domains verified by SPF and DKIM. If the alignment fails, DMARC instructs the recipient server on how to handle the email based on a policy specified in the record.

# How Organizations Stop Phishing?

Modern email systems employ various technical controls to help detect and block phishing messages before they reach users.

- [**Email Filtering**](https://www.spamhaus.org/resource-hub/ip-domain-reputation/): Provides filtering based on IP and domain reputation, allowing for blocking or quarantining of suspicious messages.
- [**Secure Email Gateways**](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/) (SEGs): Scan messages to detect impersonation attempts, spoofing, and other phishing techniques that other filters might miss.
- [**Link Rewriting**](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about): Replaces suspicious or unknown URLs with safe, redirected ones, giving the system time to scan and verify the link.
- [**Sandboxing**](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about): Isolates and tests suspicious links or attachments in a secure, virtual environment to check for malicious behavior.


- **Trust & Warning Indicators**: Modern email platforms display visual cues to help users understand if a message is safe. A banner may read “External Sender,” “Suspicious Link,” or signify that a message is from a trusted organization or sender. 
- **Phishing Reporting**: Easy, in-email reporting options that let users quickly report suspicious messages.
- **User Awareness Training**: Train employees on identifying phishing attempts, social engineering tactics, and safe email practices.
- **Phishing Simulation Exercises**: Run controlled phishing campaigns to test and reinforce employee training.