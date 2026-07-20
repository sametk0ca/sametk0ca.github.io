+++
title = "Firewall (Güvenlik Duvarı) Çalışma Prensipleri | Firewall Working Principles"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Firewall, ağınızın kapısındaki "güvenlik görevlisi"dir. Gelen ve giden ağ trafiğini önceden belirlenmiş güvenlik kurallarına göre denetler ve ya izin verir ya da engeller.

### 1. Temel Mantık: İzin Verilmeyen Her Şey Yasaktır
Güvenlik dünyasında iki yaklaşım vardır:
- **Blacklisting (Kara Liste):** Her şeye izin ver, sadece kötüleri engelle. (Çok risklidir).
- **Whitelisting (Beyaz Liste):** Her şeyi engelle, sadece güvenli olduğunu bildiklerine izin ver. (Firewall'lar genellikle bu mantıkla, yani **Implicit Deny** kuralı ile çalışır).

### 2. Firewall Türleri
- **Packet Filtering (Paket Filtreleme):** En temel seviyedir. Sadece IP adresine ve porta bakar. "Hangi mektup nereden geliyor?" diye bakar ama mektubun içini okumaz.
- **Stateful Inspection (Durumsal Denetim):** Daha zekidir. Bağlantının durumunu (state) takip eder. Eğer siz bir web sitesine istek gönderdiyseniz, o siteden gelen yanıtın "beklenen bir yanıt" olduğunu anlar ve izin verir. Dışarıdan durup dururken gelen bağlantıları engeller.
- **Next-Gen Firewall (NGFW):** Günümüzün modern duvarlarıdır. Sadece porta değil, uygulamanın kendisine de bakar. Örneğin, 80 portundan (HTTP) geçen trafiğin Facebook mu yoksa bir virüs mü olduğunu ayırt edebilir.

### 3. Bilmen Gereken Bazı Terimler
- **IDS (Intrusion Detection System):** Saldırı Tespit Sistemi. Sadece "Hırsız var!" diye bağırır ama müdahale etmez.
- **IPS (Intrusion Prevention System):** Saldırı Önleme Sistemi. Hırsızı görür ve kapıyı kilitleyerek girmesini engeller.
- **Teardrop Saldırısı:** Bir saldırganın, hedef bilgisayara bilerek "parçalanmış ve üst üste binen" (overlapping fragments) IP paketleri göndermesidir. Bilgisayar bu paketleri birleştirmeye çalışırken kafası karışır ve sistemi çöker. Modern firewall'lar bu paketleri temizleyerek içeri sokmaz.

### Gerçek Dünya Analojisi
Firewall, bir sitenin girişindeki güvenlik kulübesi gibidir. Görevli, gelen arabanın plakasına (IP) ve kime geldiğine (Port) bakar. Eğer listede varsanız (Rules) kapıyı açar. Next-Gen bir görevli ise arabanın bagajını da açtırıp (DPI - Deep Packet Inspection) içinde tehlikeli bir madde olup olmadığına bakar.

---

## English Version

Firewall is the "security guard" at the gate of your network. It inspects incoming and outgoing network traffic according to predefined security rules and either allows or blocks it.

### 1. Basic Logic: Whatever is Not Allowed is Prohibited
There are two approaches in the security world:
- **Blacklisting:** Allow everything, block only the bad ones. (It is very risky).
- **Whitelisting:** Block everything, only allow what you know is safe. (Firewalls generally work with this logic, that is, the **Implicit Deny** rule).

### 2. Firewall Types
- **Packet Filtering:** It is the most basic level. It only looks at the IP address and port. "Which letter comes from where?" He looks at it but doesn't read the inside of the letter.
- **Stateful Inspection:** It is more intelligent. It keeps track of the state of the connection. If you send a request to a website, it understands that the response from that site is an "expected response" and allows it. It blocks incoming connections from outside out of the blue.
- **Next-Gen Firewall (NGFW):** These are today's modern walls. It looks not just at the port but also at the application itself. For example, it can distinguish whether traffic passing through port 80 (HTTP) is from Facebook or a virus.

### 3. Some Terms You Should Know
- **IDS (Intrusion Detection System):** Intrusion Detection System. Just "There's a thief!" He shouts but does not intervene.
- **IPS (Intrusion Prevention System):** Intrusion Prevention System. He sees the thief and locks the door, preventing him from entering.
- **Teardrop Attack:** An attacker knowingly sends "fragmented and overlapping" IP packets to the target computer. As the computer tries to combine these packets, it gets confused and crashes the system. Modern firewalls do not clear these packets and do not let them in.

### Real World Analogy
Firewall is like a security booth at the entrance of a site. The officer looks at the license plate (IP) of the incoming car and who it is coming from (Port). If you are on the list (Rules) it opens the door. A Next-Gen officer also opens the trunk of the car (DPI - Deep Packet Inspection) to see if there is a dangerous substance inside.
