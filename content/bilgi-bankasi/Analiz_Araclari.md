+++
title = "Analiz Araçları (VirusTotal, Any.run, WHOIS)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Defense"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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