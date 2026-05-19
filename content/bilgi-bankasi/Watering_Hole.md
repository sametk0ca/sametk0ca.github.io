+++
title = "Watering Hole Attack"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
+++

Watering Hole (Su Birikintisi) saldırısı, belirli bir grup veya kurumdaki kullanıcıları hedef alan, dolaylı ve sinsi bir siber saldırı yöntemidir.

### 1. Nasıl Çalışır?
Saldırgan, kurbanın doğrudan üzerine gitmek yerine, kurbanın (veya hedef grubun) sık sık ziyaret ettiği güvenilir bir web sitesini (Örn: Bir haber sitesi, mesleki forum veya favori bir restoran sitesi) önceden hackler.
1. **Gözlem:** Saldırgan kurbanların hangi sitelere takıldığını öğrenir.
2. **Zehirleme:** Bu siteye zararlı bir yazılım (Malware) bulaştırır.
3. **Avlanma:** Kurban her zamanki gibi güvendiği siteye girer. Site açılırken arka planda kurbanın bilgisayarına virüs bulaşır.

### 2. Neden "Watering Hole"?
İsim doğadan gelir: Bir aslan (Saldırgan), ceylanları (Kurbanlar) kovalamak yerine, onların su içmeye geldiği tek su birikintisinin (Web sitesi) başında bekler. Ceylanlar su içmeye geldiğinde saldırıya geçer.

### 3. Bilmen Gereken Bazı Terimler
- **Drive-by Download:** Kullanıcının hiçbir yere tıklamasına gerek kalmadan, sadece web sitesini ziyaret ettiği anda bilgisayarına otomatik olarak virüs inmesi.
- **Exploit Kit:** Web sitesine yerleştirilen ve ziyaretçinin bilgisayarındaki açıkları (Örn: Eski tarayıcı versiyonu) otomatik olarak tarayıp uygun virüsü bulaştıran yazılım paketi.
- **Strategic Web Compromise:** Watering hole saldırısının diğer adıdır; stratejik bir web sitesinin ele geçirilmesini ifade eder.

### 4. Korunma Yolları
- Tarayıcınızı ve tüm eklentilerinizi (Java, Adobe vb. - gerçi artık çoğu kalktı) her zaman güncel tutun.
- Gelişmiş uç nokta koruma (EDR) yazılımları kullanın.
- Kurumsal ağlarda "Web Filtering" kullanarak, şüpheli veya düşük güvenliğe sahip sitelere erişimi kısıtlayın.

### Gerçek Dünya Analojisi
Mahalledeki herkesin her sabah uğradığı bir fırın olduğunu düşünün. Hırsız fırını hackleyip (zehirleyip) her ekmeğin içine gizlice bir takip cihazı yerleştirir. İnsanlar her zamanki güvenle ekmeklerini alıp eve götürürler. Hırsız artık herkesin evinin yerini biliyordur.