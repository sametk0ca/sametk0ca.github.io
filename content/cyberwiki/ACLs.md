+++
title = "ACLs (Access Control Lists)"
date = "2026-05-19"
draft = false
categories = ["DevSecOps"]
type = "cyberwiki"
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

---

## English Version

ACLs are lists of rules that determine who can access an object (file, directory, or network resource) and with what permissions.

### Summary
Access Control Lists are one of the fundamental building blocks of system security. It is widely used in both file systems (file permissions) and network devices (traffic filtering).

### Technical Details
- **Network ACLs:** Allows or blocks (stateless) traffic based on IP address, port number, and protocol.
- **File System ACLs:** Assigns read, write and execute permissions to users and groups.
- **Standard vs. Extended:** While standard ACLs only look at the source IP, Extended ACLs can look at source/destination IPs and ports.

### Security Approach and Best Practices
- **Implicit Deny:** There should always be a "block everything" rule at the end of the list.
- **Least Privilege:** Allow only needed access.
- **Regular Audit:** Periodically purge unused or overprovisioning rules.
