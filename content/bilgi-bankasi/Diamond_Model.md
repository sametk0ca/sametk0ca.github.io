+++
title = "Diamond Model of Intrusion Analysis"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Attacks"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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