+++
title = "Diamond Model of Intrusion Analysis"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

Diamond Model (Elmas Modeli), bir siber saldırıyı veya olayı analiz etmek için kullanılan, saldırının dört temel bileşeni arasındaki ilişkiyi gösteren bir çerçevedir.

### 1. Elmasın Dört Köşesi
Bir saldırıyı tam olarak anlamak için şu dört soruyu sormalıyız:
1. **Adversary (Saldırgan):** Bu saldırıyı kim yapıyor? (Bir grup, devlet, bireysel hacker?).
2. **Infrastructure (Altyapı):** Saldırgan hangi yolları kullanıyor? (IP adresleri, sahte alan adları, sunucular).
3. **Capability (Yetenek):** Saldırgan hangi araçları veya yöntemleri kullanıyor? (Virüsler, zafiyetler, sosyal mühendislik).
4. **Victim (Kurban):** Kurban kim? (Bir şirket, bir banka, belirli bir ülke?).

### 2. Neden "Elmas"?
Bu dört bileşen birbirine çizgilerle bağlıdır ve bir elmas şekli oluşturur. Örneğin; saldırganın (Adversary) elindeki virüs (Capability), bir sunucu (Infrastructure) üzerinden kurbana (Victim) ulaştırılır. Bu bağlantıları kurmak, saldırganın profilini çıkarmayı sağlar.

### 3. Bilmen Gereken Bazı Terimler
- **TTP (Tactics, Techniques, and Procedures):** Saldırganların kullandığı yöntemlerin genel adı. Elmasın "Capability" köşesiyle ilgilidir.
- **Attribution:** Bir saldırının kimin tarafından yapıldığını kesin olarak belirleme işlemi. Elmasın "Adversary" köşesinin amacıdır.

### Gerçek Dünya Analojisi
Bir hırsızlık olayını çözen bir dedektif olduğunuzu düşünün:
- **Kurban:** Soyulan ev sahibi.
- **Saldırgan:** Hırsız (Belki bir çete).
- **Yetenek:** Kapıyı açmak için kullandığı maymuncuk.
- **Altyapı:** Hırsızın olay yerine geldiği çalıntı araba.
Eğer bu dört köşeyi birleştirirseniz, hırsızın kim olduğunu ve bir sonraki sefer nereye saldırabileceğini bulabilirsiniz.

---

## English Version

The Diamond Model is a framework used to analyze a cyber attack or incident, showing the relationship between four key components of the attack.

### 1. Four Corners of the Diamond
To fully understand an attack, we must ask these four questions:
1. **Adversary:** Who is making this attack? (A group, government, individual hacker?).
2. **Infrastructure:** What ways does the attacker use? (IP addresses, fake domain names, servers).
3. **Capability:** What tools or methods does the attacker use? (Viruses, vulnerabilities, social engineering).
4. **Victim (Sacrifice):** Who is the victim? (A company, a bank, a particular country?).

### 2. Why "Diamond"?
These four components are connected to each other by lines and form a diamond shape. For example; The virus (Capability) in the hands of the attacker (Adversary) is delivered to the victim (Victim) through a server (Infrastructure). Establishing these connections allows profiling the attacker.

### 3. Some Terms You Should Know
- **TTP (Tactics, Techniques, and Procedures):** The general name of the methods used by attackers. It is related to the "Capability" corner of the diamond.
- **Attribution:** The process of determining precisely who committed an attack. It is the purpose of the "Adversary" corner of the diamond.

### Real World Analogy
Imagine you are a detective solving a burglary:
- **Victim:** The homeowner who was robbed.
- **Aggressor:** Thief (Maybe a gang).
- **Ability:** The lock pick he uses to open the door.
- **Infrastructure:** The stolen car in which the thief arrived at the scene.
If you connect these four corners, you can find out who the thief is and where he might attack next.
