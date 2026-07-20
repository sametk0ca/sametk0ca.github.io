+++
title = "Directory Traversal (Path Traversal)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "cyberwiki"
+++

Directory Traversal, bir saldırganın web uygulaması üzerinden sunucudaki kısıtlı dosya yollarına (klasörlere) erişmesi ve sistem dosyalarını (Örn: `/etc/passwd`) okuması saldırısıdır.

### 1. Saldırı Mantığı
Uygulama size bir resmi göstermek için şöyle çalışıyor olabilir: `site.com/indir?dosya=resim.jpg`. Saldırgan bu dosya adını değiştirerek üst klasörlere çıkmaya çalışır: `site.com/indir?dosya=../../../../etc/passwd`. Eğer uygulama "dur" demezse, sunucudaki gizli sistem dosyalarını saldırgana gönderir.

### 2. Nasıl Gerçekleşir?
İşletim sistemlerinde `..` (iki nokta) bir üst klasöre çıkmak anlamına gelir. Saldırgan arka arkaya `../` yazarak uygulamanın hapsedildiği klasörden dışarı çıkar ve sunucunun kök (root) dizinine kadar ulaşabilir.

### 3. Bilmen Gereken Bazı Terimler
- **Dot-Dot-Slash (../):** Bir üst dizine çıkma komutu. Saldırının ana aracıdır.
- **Root Directory:** Sunucunun en üst klasörü. Tüm sistem dosyaları buradadır.
- **Local File Inclusion (LFI):** Directory Traversal ile çok benzerdir; sunucudaki yerel bir dosyanın uygulama içine dahil edilip çalıştırılmasıdır.

### 4. Korunma Yolları
- **Input Validation:** Kullanıcıdan gelen dosya adının içinde `..` veya `/` gibi karakterlerin olmamasını sağlayın.
- **Chroot Jail:** Uygulamayı işletim sistemi içinde sanki sadece kendi klasörü varmış gibi kısıtlı bir alanda (hapiste) çalıştırın.
- **İzinler:** Web uygulamasını çalıştıran kullanıcının sistem dosyalarını okuma yetkisini elinden alın.

### Gerçek Dünya Analojisi
Bir kütüphanedesiniz. Görevliye "Bana 5. raftaki kitabı getir" diyorsunuz. Ama aslında şöyle diyorsunuz: "5. raftan 10 adım geri git, depoya gir, oradaki gizli personel kayıtlarını getir." Eğer görevli (Uygulama) sadece raftaki kitaplara bakmak yerine kütüphanenin her yerine gidebiliyorsa bu bir Directory Traversal'dır.

---

## English Version

Directory Traversal is an attack where an attacker accesses restricted file paths (folders) on the server through a web application and reads system files (e.g. `/etc/passwd`).

### 1. Attack Logic
The application may be trying to show you an image like this: `site.com/indir?dosya=image.jpg`. The attacker tries to go to the upper folders by changing this file name: `site.com/indir?dosya=../../../../etc/passwd`. If the application does not say "stop", it sends hidden system files on the server to the attacker.

### 2. How Does It Happen?
In operating systems, `..` (colon) means going up a folder. By typing `../` repeatedly, the attacker can get out of the folder where the application is locked and reach the root directory of the server.

### 3. Some Terms You Should Know
- **Dot-Dot-Slash (../):** Command to go up one directory. It is the main tool of attack.
- **Root Directory:** The top folder of the server. All system files are here.
- **Local File Inclusion (LFI):** Very similar to Directory Traversal; It is the inclusion and running of a local file on the server into the application.

### 4. Ways of Protection
- **Input Validation:** Make sure that the file name received from the user does not contain characters such as `..` or `/`.
- **Chroot Jail:** Run the application in a restricted area (jail) within the operating system as if it only had its own folder.
- **Permissions:** Deprive the user running the web application of the ability to read system files.

### Real World Analogy
You are in a library. You say to the clerk, "Bring me the book on shelf 5." But what you're actually saying is: "Take 10 steps back from shelf 5, go into the warehouse, bring up the confidential personnel records there." If the attendant (Application) can go all over the library instead of just looking at the books on the shelf, this is a Directory Traversal.
