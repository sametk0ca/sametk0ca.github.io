+++
title = "Zero Trust Architecture (Sıfır Güven Mimarisi) | Zero Trust Architecture"
date = "2026-05-19"
draft = false
categories = ["Principles"]
type = "cyberwiki"
+++

Zero Trust, "Asla güvenme, her zaman doğrula" (Never trust, always verify) prensibi üzerine kurulu modern bir güvenlik felsefesidir.

### 1. Eski vs Yeni Yaklaşım
- **Eski (Castle-and-Moat):** Ağın etrafına dev bir hendek (Firewall) kazılır. İçerideki herkese güvenilir, dışarıdaki herkese şüpheyle bakılır. Ancak bir saldırgan bir kez içeri sızarsa, tüm ağda özgürce hareket edebilir.
- **Yeni (Zero Trust):** Ağın içinde veya dışında olmanız fark etmez. Kim olursanız olun, hangi cihazı kullanırsanız kullanın, her bir kaynağa (dosya, uygulama) erişmek istediğinizde kimliğiniz tekrar doğrulanır.

### 2. Zero Trust'ın Üç Ana Prensibi
1. **Her Zaman Doğrula:** Kullanıcı kimliği, cihaz sağlığı, konum ve saat gibi tüm verileri her erişim isteğinde kontrol et.
2. **En Düşük Yetki (Least Privilege):** Bir kullanıcıya sadece işini yapması için gereken minimum yetkiyi ver. (Örn: Muhasebeci yazılım kodlarına erişememeli).
3. **İhlali Varsay (Assume Breach):** Sistemin zaten hacklendiğini varsayarak hareket et. Ağı küçük parçalara (Micro-segmentation) böl ki saldırgan içeri girse bile diğer odalara geçemesin.

### 3. Bilmen Gereken Bazı Terimler
- **Least Privilege:** "En az yetki" prensibi. Gereksiz verilen her yetki, saldırgan için bir fırsattır.
- **Micro-segmentation:** Bir ağı çok küçük parçalara ayırarak, parçalar arası geçişi sıkı denetleme işlemi.
- **Lateral Movement:** Bir saldırganın ağa girdikten sonra diğer bilgisayarlara ve sunuculara yayılma eylemi. Zero Trust bunu durdurmayı hedefler.
- **IAM (Identity and Access Management):** Kimlik ve erişim yönetimi. Zero Trust'ın kalbidir.

### Gerçek Dünya Analojisi
Eski sistem bir kaleye benzer; surları geçince içerideki her yere girebilirsiniz. Zero Trust ise çok sıkı korunan bir yüksek güvenlikli hapishane veya gizli laboratuvar gibidir. Her koridorda ayrı bir kapı, her kapıda parmak izi okuyucusu ve her odada ayrı bir kimlik kontrolü vardır. Bir odaya girmiş olmanız, yan odaya girebileceğiniz anlamına gelmez.

---

## English Version

Zero Trust is a modern security philosophy based on the principle of "Never trust, always verify".

### 1. Old vs New Approach
- **Old (Castle-and-Moat):** A giant moat (Firewall) is dug around the network. Everyone inside is trusted, everyone outside is viewed with suspicion. But once an attacker gets in, he can move freely across the entire network.
- **New (Zero Trust):** It doesn't matter whether you are inside or outside the network. No matter who you are, no matter what device you use, your identity is re-authenticated every time you want to access a resource (file, application).

### 2. Three Main Principles of Zero Trust
1. **Always Verify:** Check all data such as user ID, device health, location and time with every access request.
2. **Least Privilege:** Give a user only the minimum privilege required to do his job. (Ex: The accountant should not be able to access software codes).
3. **Assume Breach (Assume Breach):** Act assuming the system has already been hacked. Divide the network into small segments (Micro-segmentation) so that even if the attacker gets in, he cannot move to other rooms.

### 3. Some Terms You Should Know
- **Least Privilege:** "Least privilege" principle. Every unnecessary authority is an opportunity for the attacker.
- **Micro-segmentation:** The process of dividing a network into very small parts and tightly controlling the transition between parts.
- **Lateral Movement:** The act of an attacker spreading to other computers and servers after entering the network. Zero Trust aims to stop this.
- **IAM (Identity and Access Management):** Identity and access management. It is the heart of Zero Trust.

### Real World Analogy
The old system is like a castle; Once you pass the walls, you can enter anywhere inside. Zero Trust, on the other hand, is like a heavily guarded high security prison or secret laboratory. There is a separate door in each corridor, a fingerprint reader on each door, and a separate ID check in each room. Just because you've entered one room doesn't mean you can enter the next room.
