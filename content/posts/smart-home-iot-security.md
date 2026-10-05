---
title: "Smart Home and IoT Device Security"
slug: "smart-home-iot-security"
date: 2026-10-05
description: "How smart fridges, thermostats and other IoT devices get hacked, what attackers do with them, and how to protect your home network. / Akıllı buzdolabı, termostat gibi IoT cihazlar nasıl hacklenir, saldırganlar bunlarla neler yapar ve ev ağınızı nasıl korursunuz."
draft: false
tags: ["IoT", "Smart Home", "Network Security", "Botnet", "Privacy", "Blue Team"]
categories: ["Blog"]
ShowToc: true
related:
  - "[[ip-camera-vulnerabilities|IP Camera Vulnerabilities]]"
  - "[[Network_Segmentation|Network Segmentation]]"
  - "[[DoS_DDoS|DoS / DDoS]]"
---

## 🇹🇷 Türkçe (TR)

### Giriş

Akıllı buzdolabı, termostat, ampul, priz, robot süpürge, kapı zili... Evdeki bu cihazların hepsi aslında ağa bağlı küçük bilgisayarlardır. Çoğu ucuza üretilir, güvenlik ikinci planda kalır, güncelleme alması beklenmez ve kurulduktan sonra bir daha ilgilenilmez. Saldırgan açısından bu, kolay ve çok sayıda hedef demektir. Aynı konunun IP kamera tarafını [IP Camera Vulnerabilities](/posts/ip-camera-vulnerabilities/) yazısında anlatmıştım. Burada akıllı ev cihazlarının geneline bakıyoruz.

### Neden Bu Kadar Savunmasızlar?

- **Zayıf veya varsayılan parolalar:** Fabrika çıkışı kullanıcı adı ve parola değiştirilmez.
- **Güncelleme eksikliği:** Üretici bellenimi (firmware) güncellemez, güncelleme varsa kullanıcı farkında değildir. Bir buzdolabı 10-15 yıl kullanılır, yazılım desteği çoğu zaman bundan çok daha kısadır.
- **Gereksiz açık servisler:** Telnet, UPnP, açık yönetim panelleri.
- **Sınırlı kaynaklar:** Küçük işlemci ve bellek, güçlü şifreleme ve güvenlik kontrollerini zorlaştırır.
- **Güvenliğin son sırada olması:** Fiyat ve pazara çıkış hızı öncelik olur.

### Saldırı Yüzeyi: Nasıl Hacklenirler?

1. **Varsayılan kimlik bilgileri ve internete açık cihazlar:** Shodan gibi arama motorları internete açık cihazları listeler. Saldırgan kısa bir varsayılan parola listesiyle binlerce cihazı dener. 2016'daki **Mirai** botneti tam olarak bunu yaptı: Telnet'i açık, varsayılan parolalı kamera ve yönlendiriciler ele geçirildi.
2. **Eski bellenimdeki bilinen açıklar:** Yamasız bir RCE (uzaktan kod çalıştırma) açığı, kimlik doğrulama olmadan cihazı ele geçirmeye yeter.
3. **Şifreleme hataları:** Cihaz sunucu sertifikasını doğrulamazsa ortadaki adam (MitM) saldırısıyla trafik okunabilir. Araştırmacılar, bir akıllı buzdolabının bu hata yüzünden Google hesap bilgilerini sızdırabildiğini bildirdi (2015).
4. **Bulut ve mobil uygulama zafiyetleri:** Cihaz kadar, onu yöneten bulut API'si ve uygulaması da hedeftir. Yetkilendirme hatası (IDOR gibi) başkasının cihazına erişime yol açabilir.
5. **Kablosuz protokoller:** Zayıf eşleştirme (pairing) kullanan Bluetooth, Zigbee gibi protokoller yakındaki bir saldırgana kapı açabilir.
6. **Fiziksel erişim:** Cihaz üzerindeki UART/JTAG gibi hata ayıklama portlarından bellenim çıkarılıp incelenir. Bellenimin içine gömülü parola veya anahtar bulunması sık rastlanan bir durumdur.

### Ele Geçirilen Cihazla Ne Yapılabilir?

- **Botnet ve DDoS:** Cihaz bir "zombi" olur ve toplu saldırılarda kullanılır. Mirai, 2016'da Dyn DNS'ine yapılan saldırıda birçok büyük servisi erişilemez kıldı.
- **Ağda yatay hareket (pivot):** Akıllı ampul gibi zayıf bir cihaz, aynı ağdaki bilgisayar ve telefonlara geçiş noktası olabilir.
- **Gizlilik ihlali:** Kamera, mikrofon ve kullanım verileri (evde ne zaman olduğunuz) izlenebilir.
- **Fiziksel etki:** Isıtma sistemi, kilit veya priz gibi cihazlar kontrol edilebilir. Araştırmacılar, akıllı termostatı fidye yazılımıyla ele geçirip kullanıcıdan para istemenin mümkün olduğunu gösterdi (kavram kanıtı, 2016).
- **Veri hırsızlığı:** Cihazda saklı Wi-Fi parolası, hesap bilgisi veya API anahtarı çalınabilir.

### Nasıl Korunuruz?

- **Varsayılan parolayı değiştirin**, her cihaz için benzersiz ve uzun bir parola kullanın. Bulut hesabında MFA açın.
- **Güncellemeleri uygulayın.** Otomatik güncelleme varsa açın. Satın almadan önce üreticinin destek süresine bakın.
- **Ağı ayırın:** IoT cihazlarını misafir ağına veya ayrı bir VLAN'a koyun. Böylece ele geçirilen bir ampul bilgisayarınıza ulaşamaz.
- **UPnP'yi kapatın** ve gerekmedikçe cihazı internete açmayın (port yönlendirme yok).
- **Kullanmadığınız özellikleri kapatın:** uzaktan erişim, mikrofon, gereksiz bulut bağlantıları.
- **Satın alırken seçici olun:** Güvenlik güncelleme politikası olan, tanınmış üreticileri tercih edin. Varsayılan parolayı yasaklayan düzenlemeler var (örneğin İngiltere'nin PSTI yasası), bu da standart haline geliyor.
- **Elden çıkarırken fabrika ayarlarına döndürün.**

### Savunmacı (SOC) Gözüyle

Evde veya kurumda IoT cihazlarını izlemek için şunlara bakılır:
- Cihazın normalde konuşmadığı yerlere **yeni giden bağlantılar**
- Beklenmedik **DNS sorguları** ve yüksek hacimli giden trafik (botnet göstergesi)
- Cihazdan **ağdaki diğer makinelere** yapılan tarama veya bağlantı denemeleri
- IoT ağından iç ağa gelen, kurala aykırı trafik (segmentasyonun işlediğini doğrular)

Bunun için bir DNS günlüğü, güvenlik duvarı kayıtları veya Zeek/Suricata gibi araçlar yeterlidir.

---

## 🇬🇧 English (EN)

### Introduction

Smart fridges, thermostats, bulbs, plugs, robot vacuums, video doorbells... Every one of these home devices is a small networked computer. Most are built cheaply, security comes second, they aren't expected to get updates, and nobody looks at them after setup. For an attacker this means many easy targets. I covered the IP camera side in [IP Camera Vulnerabilities](/posts/ip-camera-vulnerabilities/). Here I look at smart home devices more broadly.

### Why Are They So Vulnerable?

- **Weak or default passwords:** The factory username and password are never changed.
- **Missing updates:** The vendor doesn't patch the firmware, or the user never learns an update exists. A fridge lasts 10-15 years, while software support is often far shorter.
- **Unnecessary exposed services:** Telnet, UPnP, open admin panels.
- **Limited resources:** Small CPUs and memory make strong crypto and security controls harder.
- **Security comes last:** Price and time to market win.

### Attack Surface: How Do They Get Hacked?

1. **Default credentials and internet-exposed devices:** Search engines like Shodan list devices exposed to the internet. An attacker tries a short list of default passwords against thousands of them. The 2016 **Mirai** botnet did exactly this: cameras and routers with Telnet open and default passwords were taken over.
2. **Known flaws in old firmware:** An unpatched RCE (remote code execution) bug is enough to take over a device without authentication.
3. **Crypto mistakes:** If a device doesn't validate the server certificate, a man-in-the-middle (MitM) attacker can read its traffic. Researchers reported that a smart fridge could leak Google account credentials this way (2015).
4. **Cloud and mobile app weaknesses:** The cloud API and app that manage the device are targets too. An authorization flaw (like an IDOR) can give access to someone else's device.
5. **Wireless protocols:** Bluetooth, Zigbee and similar protocols with weak pairing can let a nearby attacker in.
6. **Physical access:** Debug ports such as UART/JTAG let an attacker dump and analyse the firmware. Hardcoded passwords or keys inside firmware are a common finding.

### What Can an Attacker Do with a Compromised Device?

- **Botnet and DDoS:** The device becomes a "zombie" used in large attacks. In 2016, Mirai took part in the attack on Dyn DNS that made many major services unreachable.
- **Pivot into the network:** A weak device like a smart bulb can be a stepping stone to the computers and phones on the same network.
- **Privacy violations:** Cameras, microphones and usage data (when you're home) can be watched.
- **Physical effects:** Heating, locks and plugs can be controlled. Researchers demonstrated that a smart thermostat could be taken over with ransomware and the user asked to pay (proof of concept, 2016).
- **Data theft:** Stored Wi-Fi passwords, account details or API keys can be stolen.

### How Do We Protect Ourselves?

- **Change the default password**, and use a unique, long password for each device. Enable MFA on the cloud account.
- **Apply updates.** Turn on automatic updates if available. Check the vendor's support period before buying.
- **Segment the network:** Put IoT devices on a guest network or a separate VLAN so a compromised bulb can't reach your computer.
- **Disable UPnP** and don't expose devices to the internet unless needed (no port forwarding).
- **Turn off unused features:** remote access, microphone, unnecessary cloud connections.
- **Buy carefully:** Prefer established vendors with a published security update policy. Regulations banning default passwords exist (for example the UK's PSTI law), and this is becoming the standard.
- **Factory reset before selling or discarding.**

### From a Defender's (SOC) View

To monitor IoT devices at home or in an organisation, look for:
- **New outbound connections** to places the device doesn't normally talk to
- Unexpected **DNS queries** and high-volume outbound traffic (a botnet indicator)
- **Scanning or connection attempts** from the device to other hosts on the network
- Traffic from the IoT network to the internal network that breaks the rules (confirms segmentation works)

DNS logs, firewall logs, or tools like Zeek and Suricata are enough for this.
