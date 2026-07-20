+++
title = "Snapshot ve Klonlama Yönetimi | Snapshot and Cloning Management"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "cyberwiki"
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

---

## English Version

The biggest advantage of virtual machines is that their state can be "frozen" and stored.

### 1. Snapshot
It is to take a photo of the current RAM and disk status of a virtual machine.
- **Area of ​​Use:** A snapshot is taken before performing a system update. If the update corrupts the system, "Revert to Snapshot" can be used to restore the old state within seconds.
- **Forensics/Analysis:** A snapshot is taken just before running the malware. When the analysis is finished, the snapshot is returned to prevent the system from remaining infected.

### 2. Cloning
It is to create an exact copy of a virtual machine.
- **Full Clone:** Creates a copy completely independent of the original VM. It takes up a lot of disk space.
- **Linked Clone:** Reads the disk of the original VM, just writing the changes made to a new file. It takes up little space, but if the original VM is deleted, the clone will also be corrupted.

### Security Risk 3: Accumulation of Snapshots
Snapshots take up a lot of disk space and reduce system performance. 
- **Data Leak:** If you do not clear the snapshots when giving a virtual machine to someone, the other party can access the past states of the system (maybe the passwords you deleted at that moment) through the snapshots.

### 4. Golden Image
It is a "master" virtual machine with hardened security and all updates. When a new server is to be established, this "Golden Image" is cloned and used instead of establishing it from scratch; This ensures that all systems meet the same security standards.
