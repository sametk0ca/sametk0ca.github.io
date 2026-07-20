+++
title = "Proxy Sunucuları (Forward vs Reverse Proxy) | Proxy Servers (Forward vs Reverse Proxy)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
+++

Proxy (Vekil) sunucu, sizinle internet arasında duran bir "aracı"dır. İsteklerinizi sizin adınıza yapar veya dışarıdan gelen istekleri sizin adınıza karşılar.

### 1. Forward Proxy (İleri Proxy)
Kullanıcının (istemcinin) internete çıkarken kullandığı proxy'dir.
- **Kullanım Amacı:** 
    - **Kimlik Gizleme:** İnternet siteleri sizin IP adresinizi değil, proxy'nin IP adresini görür.
    - **Filtreleme:** Şirketlerde çalışanların "zararlı" veya "yasaklı" sitelere girmesini engellemek için kullanılır.
    - **Caching (Önbellekleme):** Çok sık girilen sitelerin bir kopyasını tutar, böylece internet daha hızlıymış gibi hissettirir.

### 2. Reverse Proxy (Ters Proxy)
Bir web sunucusunun (veya sunucu grubunun) önünde duran proxy'dir.
- **Kullanım Amacı:**
    - **Load Balancing (Yük Dengeleme):** Gelen binlerce isteği arkadaki 5-10 farklı sunucuya dağıtır ki sunucular çökmesin.
    - **Güvenlik:** Web sunucularının gerçek IP adresini gizler. Saldırgan doğrudan sunucuya değil, proxy'ye saldırır.
    - **SSL Termination:** Şifreleme (SSL/TLS) yükünü ana sunucunun üzerinden alıp kendi üzerinde çözer.

### 3. Bilmen Gereken Bazı Terimler
- **Latency (Gecikme):** Bir isteğin gönderilip yanıtın gelmesi arasında geçen süre. Proxy kullanmak bazen yolu uzattığı için gecikmeyi artırabilir.
- **Anonymity (Anonimlik):** İnternette kimliğinizin ne kadar gizli olduğu. Proxy'ler bu seviyeyi artırabilir.
- **Transparent Proxy:** Kullanıcının ruhu bile duymadan trafiğinin bir proxy üzerinden geçirilmesidir. Genellikle okul veya otel Wi-Fi ağlarında görülür.

### Gerçek Dünya Analojisi
- **Forward Proxy:** Sizin yerinize bakkala gidip alışveriş yapan bir arkadaşınız gibidir. Bakkal (İnternet) parayı kimin verdiğini bilir ama alışverişin aslında kimin için yapıldığını bilmez.
- **Reverse Proxy:** Büyük bir şirketin sekreteri gibidir. Kimse doğrudan müdürle (Web Sunucusu) konuşamaz. Önce sekretere (Proxy) gidersiniz, o sizi uygun olan odaya yönlendirir.

---

## English Version

A proxy server is an "intermediary" that stands between you and the internet. It makes your requests on your behalf or meets external requests on your behalf.

### 1. Forward Proxy
It is the proxy that the user (client) uses when accessing the internet.
- **Intended Use:** 
    - **Identity Hiding:** Websites see the proxy's IP address, not your IP address.
    - **Filtering:** It is used in companies to prevent employees from accessing "harmful" or "prohibited" sites.
    - **Caching:** Keeps a copy of frequently visited sites, so the internet feels faster.

### 2. Reverse Proxy
A proxy that sits in front of a web server (or farm of servers).
- **Intended Use:**
    - **Load Balancing:** Distributes thousands of incoming requests to 5-10 different servers in the background so that the servers do not crash.
    - **Security:** Hides the real IP address of web servers. The attacker attacks the proxy, not the server directly.
    - **SSL Termination:** It takes the encryption (SSL/TLS) load from the main server and solves it on itself.

### 3. Some Terms You Should Know
- **Latency:** The time between when a request is sent and the response arrives. Using a proxy can sometimes increase latency because it lengthens the path.
- **Anonymity:** How private your identity is on the Internet. Proxies can increase this level.
- **Transparent Proxy:** It is the passing of traffic through a proxy without the user even knowing it. It is often seen on school or hotel Wi-Fi networks.

### Real World Analogy
- **Forward Proxy:** It is like a friend who goes to the grocery store and does the shopping on your behalf. The grocery store (Internet) knows who gave the money, but does not know for whom the purchase was actually made.
- **Reverse Proxy:** It is like the secretary of a large company. No one can talk directly to the manager (Web Host). First you go to the secretary (Proxy), she will direct you to the appropriate room.
