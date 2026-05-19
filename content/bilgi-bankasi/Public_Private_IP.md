+++
title = "Public vs Private IP Farkları ve NAT Mekanizması"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

İnternet dünyasında her cihazın bir kimliği (IP adresi) vardır. Ancak bu kimlikler "evrensel" ve "yerel" olmak üzere ikiye ayrılır.

### 1. Public IP (Genel IP)
İnternet servis sağlayıcınız (ISP) tarafından modeminize atanan, tüm dünyada benzersiz olan adrestir.
- **Karakteristik:** İnternet üzerindeki herhangi bir yerden bu adrese ulaşılabilir.
- **Güvenlik:** Public IP'niz doğrudan saldırı alabilir. Firewall (Güvenlik Duvarı) bu noktada ilk savunma hattıdır.

### 2. Private IP (Özel IP) - RFC 1918
Yerel ağınızda (ev, ofis) cihazların birbirleriyle konuşması için kullanılan adreslerdir.
- **Bloklar:**
    - `10.0.0.0 /8` (Büyük kurumsal ağlar)
    - `172.16.0.0 /12` (Orta ölçekli ağlar)
    - `192.168.0.0 /16` (Ev ve küçük ofisler)
- **Karakteristik:** İnternet üzerinden doğrudan bu adreslere ulaşılamaz. Bu durum, iç ağdaki cihazlar için doğal bir koruma sağlar.

### 3. NAT (Network Address Translation) Nedir?
Onlarca cihazın tek bir Public IP üzerinden internete çıkmasını sağlayan teknolojidir.
- **Nasıl Çalışır?** İç ağdaki bir cihaz (Örn: 192.168.1.10) internete bir istek gönderdiğinde, Router bu isteğin kaynağını kendi Public IP'si ile değiştirir ve hangi cihazın hangi isteği yaptığını bir tabloda (NAT Table) tutar. Yanıt geldiğinde, tabloya bakarak paketi içerdeki doğru cihaza iletir.
- **Güvenlik Avantajı:** Dışarıdaki bir saldırgan, iç ağdaki cihazın Private IP'sini bilse bile NAT tablosunda bir kayıt (istek) olmadığı sürece içeri sızamaz.

### 4. Statik IP ve Dinamik IP
- **Dinamik IP:** Çoğu ev kullanıcısında olduğu gibi, modem her açıldığında değişen IP'dir. Takibi biraz daha zordur.
- **Statik IP:** Hiç değişmeyen adrestir. Sunucular ve VPN ağları için gereklidir. Saldırganlar için "sabit bir hedef" oluşturduğu için ekstra koruma gerektirir.

### Gerçek Dünya Analojisi
Bir siteyi (apartman kompleksini) düşünün. Sitenin tek bir posta adresi vardır (Public IP). Ancak sitenin içinde yüzlerce daire (Private IP) bulunur. Postacı kargoyu site girişindeki güvenliğe (Router/NAT) bırakır. Güvenlik, paketin hangi daireye ait olduğunu kontrol edip içeri dağıtır. Dışarıdan kimse daire kapılarını doğrudan göremez.