+++
title = "DoS vs DDoS (Denial of Service)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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