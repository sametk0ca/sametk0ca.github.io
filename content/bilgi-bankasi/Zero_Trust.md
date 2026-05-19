+++
title = "Zero Trust Architecture (Sıfır Güven Mimarisi)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Principles"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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