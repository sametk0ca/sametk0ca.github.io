+++
title = "VPN (Virtual Private Network) Türleri ve Güvenlik"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

VPN, internet gibi güvensiz bir ağ üzerinde iki nokta arasında şifreli ve güvenli bir "tünel" oluşturma teknolojisidir. Uzaktan çalışma ve şubeler arası güvenli bağlantı için vazgeçilmezdir.

### 1. Temel Çalışma Mantığı
Veriler orijinal haliyle internete çıkmadan önce VPN protokolü tarafından şifrelenir ve bir paket içine (encapsulation) konur. Bu sayede servis sağlayıcılar veya ağdaki saldırganlar verinin içeriğini göremez.

### 2. Yaygın VPN Türleri
- **Remote Access VPN (İstemciden Ağa):** Tek bir kullanıcının (Örn: Evden çalışan personel) kurum ağına bağlanması. Genellikle SSL/TLS veya IPsec kullanılır.
- **Site-to-Site VPN (Ağdan Ağa):** İki farklı fiziksel konumun (Örn: İstanbul ve Ankara ofisleri) internet üzerinden tek bir ağmış gibi bağlanması. IPsec standarttır.

### 3. Kullanılan Protokoller
- **IPsec (Internet Protocol Security):** Ağ katmanında (Layer 3) çalışır. Çok güçlü şifreleme sunar. Genellikle Site-to-Site bağlantılarda tercih edilir.
- **SSL/TLS VPN:** Uygulama katmanında çalışır. Web tarayıcısı üzerinden bile bağlanılabilir (AnyConnect, OpenVPN). Esnekliği nedeniyle Remote Access için idealdir.
- **WireGuard:** Çok daha modern, hızlı ve basit kod yapısına sahip, yüksek güvenlikli yeni nesil bir protokoldür.

### 4. Kritik Kavramlar ve Güvenlik
- **Split Tunneling:** İnternet trafiğinin (Örn: YouTube) normal internetten, şirket trafiğinin ise VPN'den gitmesi. Performans sağlar ama risklidir (Kullanıcı cihazı üzerinden iç ağa sızıntı olabilir).
- **Full Tunneling:** Tüm trafiğin VPN üzerinden geçmesi. En güvenli yöntemdir; kurum tüm trafiği denetleyebilir.
- **MFA (Multi-Factor Authentication):** VPN girişlerinde sadece şifre yetmez; mutlaka SMS veya uygulama onayı (MFA) eklenmelidir.

### Gerçek Dünya Analojisi
VPN, kalabalık bir şehirde (İnternet) size özel, görünmez ve zırhlı bir yer altı tüneli kazmak gibidir. Dışarıdakiler tünelin giriş ve çıkışını görebilir ama içinden ne geçtiğini asla bilemezler.