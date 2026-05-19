+++
title = "LDAP (Lightweight Directory Access Protocol)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Networking"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

LDAP, ağ üzerindeki kullanıcılar, gruplar, cihazlar ve diğer kaynaklar hakkında bilgi depolayan ve bu bilgilere erişim sağlayan bir dizin hizmeti (Directory Service) protokolüdür.

### 1. Dizin vs Veritabanı
Dizinler, çok sık okunan ancak seyrek güncellenen veriler için optimize edilmiştir. LDAP, bu verileri hiyerarşik bir ağaç yapısında (DIT - Directory Information Tree) tutar.
- **Örnek Yapı:** `cn=User, ou=Security, dc=digital-samet, dc=local`
    - `cn` (Common Name): Kullanıcı adı.
    - `ou` (Organizational Unit): Departman.
    - `dc` (Domain Component): Domain parçası.

### 2. LDAP ve Güvenlik
- **LDAPS (LDAP over SSL/TLS) - Port 636:** Standart LDAP (Port 389) verileri açık metin olarak gönderir. Güvenlik için mutlaka şifreli olan LDAPS kullanılmalıdır.
- **Anonymous Bind:** Bazı LDAP sunucuları kimlik doğrulaması yapmadan sorgu yapılmasına izin verir. Bu, ağdaki tüm kullanıcı listesinin (Information Gathering) sızmasına neden olabilir.
- **LDAP Injection:** Web uygulamalarında kullanıcı girişlerinin temizlenmemesi sonucu, saldırganın LDAP sorgusunu manipüle ederek yetkisiz erişim kazanmasıdır.

### 3. Kullanım Alanları
En yaygın kullanım alanı **Microsoft Active Directory**'dir. Ayrıca uygulamalarda (Örn: Jenkins, GitLab, VPN) kullanıcıların tek bir merkezden doğrulanması (SSO temeli) için kullanılır.

### Gerçek Dünya Analojisi
LDAP, dev bir şirketin insan kaynakları klasörü gibidir. Kimin hangi masada oturduğu, hangi yetkilere sahip olduğu ve hangi departmanda çalıştığı bu hiyerarşik klasörde yazılıdır. Bir güvenlik görevlisi (Uygulama), birinin içeri girmesine izin vermeden önce bu klasöre bakıp doğrular.