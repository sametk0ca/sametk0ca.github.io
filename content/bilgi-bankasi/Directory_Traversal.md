+++
title = "Directory Traversal (Path Traversal)"
date = "2026-05-19"
draft = false
categories = ["Attacks"]
type = "bilgi-bankasi"
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