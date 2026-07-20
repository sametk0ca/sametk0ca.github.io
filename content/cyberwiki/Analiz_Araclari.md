+++
title = "Analiz Araçları (VirusTotal, Any.run, WHOIS) | Analysis Tools (VirusTotal, Any.run, WHOIS)"
date = "2026-05-19"
draft = false
categories = ["Defense"]
type = "cyberwiki"
+++

Siber güvenlik analizinde bir dosyanın, bir IP adresinin veya bir alan adının (domain) zararlı olup olmadığını hızlıca anlamak için kullanılan çeşitli çevrimiçi araçlar mevcuttur.

### 1. VirusTotal
Dünyanın en popüler dosya ve URL tarama servisidir.
- **Nasıl Çalışır?** Yüklediğiniz bir dosyayı veya girdiğiniz bir URL'yi 70'ten fazla farklı antivirüs motoru (Kaspersky, Bitdefender, Microsoft vb.) ile tarar.
- **Özellikleri:** Dosyanın "hash" değerini, davranış raporlarını (Sandbox sonuçları) ve topluluk yorumlarını sunar. Bir dosya VirusTotal'de 0/70 çıkıyorsa temiz olma ihtimali yüksektir, ancak "fud" (fully undetectable) bir zararlı da olabilir.

### 2. Any.run (Interactive Sandbox)
Zararlı yazılımları canlı olarak izleyebileceğiniz etkileşimli bir analiz platformudur.
- **Neden Farklıdır?** Sadece bir rapor sunmaz; size sanal bir masaüstü verir. Dosyayı kendi elinizle açabilir, tıklayabilir ve o an gerçekleşen ağ bağlantılarını, proses ağaçlarını (process tree) saniyelik olarak izleyebilirsiniz.
- **Kullanım Senaryosu:** Şüpheli bir e-posta ekini veya bir "phishing" linkini güvenli bir şekilde test etmek için idealdir.

### 3. WHOIS Sorgulaması
Bir alan adının (domain) veya IP adresinin kime ait olduğunu, ne zaman tescil edildiğini gösteren bir protokol ve araçtır.
- **Güvenlik Analizinde Kullanımı:**
  - **Yeni Kayıtlı Domainler:** Eğer bir domain sadece 1-2 gün önce alınmışsa ve size bankanızdan gelmiş gibi bir mail atıyorsa, bu büyük ihtimalle bir dolandırıcılıktır.
  - **İletişim Bilgileri:** Saldırganın kullandığı sunucunun hangi ülkede olduğunu veya hangi servis sağlayıcıda (hosting) barındığını bulmanızı sağlar.
- **Araçlar:** `whois` komutu (Linux/macOS) veya `whois.domaintools.com` gibi web siteleri.

### 4. Diğer Önemli Araçlar
- **Hybrid Analysis:** VirusTotal'e benzer şekilde kapsamlı sandbox raporları sunar.
- **Shodan:** İnternete bağlı cihazları (kameralar, sunucular, IoT cihazları) aramanızı sağlayan "hacker arama motoru".
- **AbuseIPDB:** Zararlı aktivitelerle ilişkilendirilmiş IP adreslerinin bildirildiği ve sorgulandığı bir veritabanı.

### Gerçek Dünya Analojisi
Bu araçlar bir dedektifin kullandığı "bilgi ağları" gibidir. VirusTotal, sabıka kaydı sorgulama sistemi; Any.run, şüpheliyi sorgu odasında izleme camı; WHOIS ise şüphelinin kimlik kartını ve ikametgah adresini kontrol etme aracıdır.

---

## English Version

There are various online tools used in cybersecurity analysis to quickly understand whether a file, an IP address, or a domain name is malicious.

### 1. VirusTotal
It is the world's most popular file and URL scanning service.
- **How ​​Does It Work?** It scans a file you upload or a URL you enter with more than 70 different antivirus engines (Kaspersky, Bitdefender, Microsoft, etc.).
- **Features:** Provides the "hash" value of the file, behavior reports (Sandbox results) and community comments. If a file shows 0/70 on VirusTotal, it is likely clean, but it may also be a "fud" (fully undetectable) malware.

### 2. Any.run (Interactive Sandbox)
It is an interactive analysis platform where you can monitor malware live.
- **Why Is It Different?** It doesn't just provide a report; gives you a virtual desktop. You can manually open the file, click on it, and monitor the network connections and process trees occurring at that moment in seconds.
- **Usage Scenario:** Ideal for securely testing a suspicious email attachment or a "phishing" link.

### 3. WHOIS Search
It is a protocol and tool that shows who owns a domain name or IP address and when it was registered.
- **Usage in Security Analysis:**
  - **Newly Registered Domains:** If a domain was purchased only 1-2 days ago and they send you an e-mail pretending to come from your bank, this is most likely a fraud.
  - **Contact Information:** It allows you to find out in which country the server used by the attacker is or which service provider (hosting) it hosts.
- **Tools:** `whois` command (Linux/macOS) or websites such as `whois.domaintools.com`.

### 4. Other Important Tools
- **Hybrid Analysis:** Provides comprehensive sandbox reports similar to VirusTotal.
- **Shodan:** "hacker search engine" that allows you to search for devices connected to the Internet (cameras, servers, IoT devices).
- **AbuseIPDB:** A database where IP addresses associated with malicious activities are reported and queried.

### Real World Analogy
These tools are like the "information networks" a detective uses. VirusTotal, criminal record check system; Any.run, viewing glass of the suspect in the interrogation room; WHOIS is a tool to check the identity card and residential address of the suspect.
