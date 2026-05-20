+++
title = "ACLs (Access Control Lists)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "bilgi-bankasi"
+++

ACL'ler, bir nesneye (dosya, dizin veya ağ kaynağı) kimlerin ve hangi yetkilerle erişebileceğini belirleyen kurallar listesidir.

### Özet
Erişim Kontrol Listeleri, sistem güvenliğinin temel yapı taşlarından biridir. Hem dosya sistemlerinde (dosya izinleri) hem de ağ cihazlarında (trafik filtreleme) yaygın olarak kullanılır.

### Teknik Detaylar
- **Ağ ACL'leri:** IP adresi, port numarası ve protokol temelinde trafiğe izin verir veya engeller (stateless).
- **Dosya Sistemi ACL'leri:** Kullanıcı ve gruplara okuma, yazma ve yürütme yetkileri atar.
- **Standard vs. Extended:** Standart ACL'ler sadece kaynak IP'ye bakarken, Genişletilmiş ACL'ler kaynak/hedef IP ve portlara bakabilir.

### Güvenlik Yaklaşımı ve En İyi Uygulamalar
- **Implicit Deny:** Listenin sonunda her zaman "her şeyi engelle" kuralı bulunmalıdır.
- **Least Privilege:** Sadece ihtiyaç duyulan erişime izin verin.
- **Düzenli Denetim:** Kullanılmayan veya gereğinden fazla yetki veren kuralları periyodik olarak temizleyin.