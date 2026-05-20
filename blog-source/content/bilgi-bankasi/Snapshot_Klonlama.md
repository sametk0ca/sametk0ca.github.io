+++
title = "Snapshot ve Klonlama Yönetimi"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "bilgi-bankasi"
+++

Sanal makinelerin en büyük avantajı, durumlarının "dondurulup" saklanabilmesidir.

### 1. Snapshot (Anlık Görüntü)
Bir sanal makinenin o anki RAM ve disk durumunun fotoğrafını çekmektir.
- **Kullanım Alanı:** Bir sistem güncellemesi yapmadan önce snapshot alınır. Eğer güncelleme sistemi bozarsa "Revert to Snapshot" denilerek saniyeler içinde eski hale dönülür.
- **Forensics/Analiz:** Zararlı yazılımı çalıştırmadan hemen önce snapshot alınır. Analiz bittiğinde, sistem virüslü kalmasın diye snapshot'a geri dönülür.

### 2. Klonlama (Cloning)
Bir sanal makinenin birebir kopyasını oluşturmaktır.
- **Full Clone:** Orijinal VM'den tamamen bağımsız bir kopya oluşturur. Çok disk alanı kaplar.
- **Linked Clone:** Orijinal VM'in diskini okur, sadece yapılan değişiklikleri yeni bir dosyaya yazar. Az yer kaplar ama orijinal VM silinirse klon da bozulur.

### 3. Güvenlik Riski: Snapshotların Birikmesi
Snapshotlar diskte çok yer kaplar ve sistem performansını düşürür. 
- **Veri Sızıntısı:** Bir sanal makineyi birine verirken snapshotlarını temizlemezseniz, karşı taraf sistemin geçmişteki hallerine (belki o an sildiğiniz şifrelere) snapshotlar üzerinden ulaşabilir.

### 4. Golden Image (Altın Kalıp)
Güvenliği sıkılaştırılmış (hardened), tüm güncellemeleri yapılmış bir "ana" sanal makinedir. Yeni bir sunucu kurulacağı zaman sıfırdan kurmak yerine bu "Golden Image" klonlanarak kullanılır; böylece tüm sistemlerin aynı güvenlik standartlarında olması sağlanır.