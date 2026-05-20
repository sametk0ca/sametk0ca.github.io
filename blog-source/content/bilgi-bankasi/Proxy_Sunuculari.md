+++
title = "Proxy Sunucuları (Forward vs Reverse Proxy)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
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