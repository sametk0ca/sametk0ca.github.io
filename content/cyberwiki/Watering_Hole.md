+++
title = "Watering Hole Attack"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
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

---

## English Version

A Watering Hole attack is an indirect and insidious cyber attack method that targets users in a specific group or institution.

### 1. How Does It Work?
Rather than attacking the victim directly, the attacker preemptively hacks a trusted website that the victim (or target group) frequently visits (e.g., a news site, professional forum, or a favorite restaurant site).
1. **Observation:** The attacker learns which sites the victims visit.
2. **Poisoning:** Infects this site with harmful software (Malware).
3. **Hunting:** The victim enters the site he trusts as usual. While the site is opening, the victim's computer is infected in the background.

### 2. Why "Watering Hole"?
The name comes from nature: Instead of chasing gazelles (Victims), a lion (Aggressor) waits by the only waterhole where gazelles (Victims) come to drink (Website). When gazelles come to drink water, they attack.

### 3. Some Terms You Should Know
- **Drive-by Download:** The virus is automatically downloaded to the user's computer as soon as he visits the website, without having to click anywhere.
- **Exploit Kit:** A software package placed on the website that automatically scans the visitor's computer for vulnerabilities (e.g. old browser version) and infects the appropriate virus.
- **Strategic Web Compromise:** It is another name for watering hole attack; It refers to the takeover of a strategic website.

### 4. Ways of Protection
- Always keep your browser and all your plugins (Java, Adobe, etc. - although most are now gone) up to date.
- Use advanced endpoint protection (EDR) software.
- Restrict access to suspicious or low-security sites by using "Web Filtering" in corporate networks.

### Real World Analogy
Imagine there is a bakery that everyone in the neighborhood visits every morning. The thief hacks (poisons) the bakery and secretly places a tracking device inside each loaf of bread. People buy their bread and take it home with the usual confidence. The thief now knows the location of everyone's house.
