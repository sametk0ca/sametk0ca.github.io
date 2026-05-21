+++
title = "DoS vs DDoS (Denial of Service)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

DoS ve DDoS saldırıları, bir web sitesini veya internet servisini "meşgul ederek" gerçek kullanıcıların erişememesini sağlamayı hedefler. Amaç bilgi çalmak değil, sistemi iş göremez hale getirmektir.

### 1. DoS (Denial of Service - Servis Dışı Bırakma)
Saldırının tek bir kaynaktan (bir bilgisayar) yapılmasıdır.
- **Mantık:** Hedef sunucuya, kapasitesinin üzerinde istek göndererek onu yormak ve dondurmaktır.

### 2. DDoS (Distributed Denial of Service - Dağıtık Servis Dışı Bırakma)
Saldırının dünya geneline yayılmış binlerce, hatta milyonlarca bilgisayardan aynı anda yapılmasıdır.
- **Neden Durdurulamaz?** Saldırı tek bir IP adresinden gelmediği için engellenmesi çok zordur. Gerçek kullanıcı ile saldırganı ayırt etmek imkansıza yakındır.

### 3. Bilmen Gereken Bazı Terimler
- **Botnet:** Saldırganın ele geçirdiği ve köle gibi kullandığı binlerce bilgisayar/cihaz (Kamera, buzdolabı vb.) ordusu. Bu ordudaki her bir cihaza **"Zombie"** denir.
- **Amplification (Yükseltme):** Küçük bir istekle karşı taraftan devasa bir yanıt dönmesini sağlayarak (Örn: DNS üzerinden) hedefi paket yağmuruna tutma tekniği.
- **Volume-based Attacks:** Hattı tamamen paketlerle doldurup tıkama saldırıları.
- **Application Layer Attacks:** Web sitesinin belirli bir özelliğini (Örn: Arama butonu) milyonlarca kez çalıştırarak sunucunun işlemcisini kilitleme saldırıları.

### 4. Korunma Yolları
- **DDoS Mitigation Servisleri:** Cloudflare veya Akamai gibi servisler trafiği temizleyerek sadece gerçek kullanıcıları içeri alır.
- **Rate Limiting:** Aynı IP adresinden gelen saniyelik istek sayısını kısıtlamak.
- **Load Balancer:** Trafiği birden fazla sunucuya dağıtmak.

### Gerçek Dünya Analojisi
Bir bakkal dükkanınız olduğunu düşünün.
- **DoS:** Bir kişinin dükkana girip sürekli saçma sapan sorular sorarak diğer müşterilerle ilgilenmenizi engellemesi.
- **DDoS:** Dükkanın önüne 5000 kişinin gelip kapıyı kapatması, içeri girmeye çalışması ve hiçbir şey almadan sadece kalabalık yapması. Gerçek müşteriler kapıdan bile giremez.

---

## English Version

DoS and DDoS attacks aim to "block" a website or internet service so that real users cannot access it. The aim is not to steal information, but to render the system inoperable.

### 1. DoS (Denial of Service)
The attack is made from a single source (one computer).
- **Logic:** By sending requests beyond the capacity of the target server, it will tire it out and freeze it.

### 2. DDoS (Distributed Denial of Service)
The attack is made simultaneously from thousands or even millions of computers spread around the world.
- **Why Can't It Be Stopped?** Since the attack does not come from a single IP address, it is very difficult to block it. It is almost impossible to distinguish between the real user and the attacker.

### 3. Some Terms You Should Know
- **Botnet:** An army of thousands of computers/devices (Camera, refrigerator, etc.) that the attacker has captured and uses like slaves. Each device in this army is called a **"Zombie"**.
- **Amplification:** A technique of showering the target with packets by causing a huge response from the other party with a small request (e.g. via DNS).
- **Volume-based Attacks:** Clogging attacks by filling the line completely with packets.
- **Application Layer Attacks:** Attacks that lock the server's processor by executing a certain feature of the website (Ex: Search button) millions of times.

### 4. Ways of Protection
- **DDoS Mitigation Services:** Services such as Cloudflare or Akamai clear the traffic and allow only real users in.
- **Rate Limiting:** Limiting the number of requests per second coming from the same IP address.
- **Load Balancer:** Distributing traffic across multiple servers.

### Real World Analogy
Imagine you own a grocery store.
- **DoS:** A person enters the shop and prevents you from dealing with other customers by constantly asking stupid questions.
- **DDoS:** 5000 people come to the front of the store, close the door, try to get in and just crowd the store without buying anything. Real customers can't even get through the door.
