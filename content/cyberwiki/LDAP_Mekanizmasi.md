+++
title = "LDAP (Lightweight Directory Access Protocol)"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

LDAP is a directory service protocol that stores and provides access to information about users, groups, devices, and other resources on the network.

### 1. Directory vs Database
Indexes are optimized for data that is read very frequently but updated infrequently. LDAP keeps this data in a hierarchical tree structure (DIT - Directory Information Tree).
- **Sample Structure:** `cn=User, ou=Security, dc=digital-samet, dc=local`
    - `cn` (Common Name): Username.
    - `ou` (Organizational Unit): Department.
    - `dc` (Domain Component): Domain part.

### 2. LDAP and Security
- **LDAPS (LDAP over SSL/TLS) - Port 636:** Standard LDAP (Port 389) sends data in cleartext. For security, encrypted LDAPS must be used.
- **Anonymous Bind:** Some LDAP servers allow queries without authentication. This may cause the entire user list (Information Gathering) on ​​the network to be leaked.
- **LDAP Injection:** As a result of not clearing user inputs in web applications, the attacker gains unauthorized access by manipulating the LDAP query.

### 3. Areas of Use
The most common usage area is **Microsoft Active Directory**. It is also used to authenticate users from a single center (SSO basis) in applications (e.g. Jenkins, GitLab, VPN).

### Real World Analogy
LDAP is like the human resources folder of a giant company. Who sits at which table, what authority they have and in which department they work are written in this hierarchical folder. A security guard (App) looks at this folder and verifies it before allowing anyone in.
