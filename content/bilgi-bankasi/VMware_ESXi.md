+++
title = "VMware Workstation  ESXi"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Virtualization"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

VMware, sanallaştırma dünyasının öncü ve en yaygın kullanılan platformlarından biridir.

### 1. VMware Workstation (Pro/Player)
Bireysel kullanıcılar için Type 2 bir Hypervisor'dır.
- **Snapshot Özelliği:** Sistemin o anki durumunu kaydeder. Zararlı yazılım analizi yaparken bir virüsü çalıştırıp, sistem bozulduktan sonra tek tuşla temiz hale geri dönmeyi sağlar.
- **VM Encryption:** Sanal makinenin disk dosyalarını şifreleyerek, bu dosyalar çalınsa bile içindeki verinin okunmasını engeller.

### 2. VMware ESXi (vSphere)
Kurumsal seviyede Type 1 Hypervisor'dır.
- **Management Plane:** ESXi sunucuları genellikle vCenter üzerinden merkezi olarak yönetilir.
- **VLAN Tagging:** ESXi, sanal makineler arasında ağ izolasyonu yapmak için 802.1Q (VLAN) etiketlemesini destekler. Bir sunucu üzerindeki sanal makinelerin birbirini görmemesi sağlanabilir.

### 3. VMware Tools
Sanal makine içine yüklenen bir sürücü paketidir. Ekran çözünürlüğü, fare senkronizasyonu ve dosya paylaşımı gibi özellikleri sağlar.
- **Security:** VMware Tools, "Guest-to-Host" (Misafirden Ev Sahibine) iletişimi sağladığı için, saldırganlar bazen bu sürücüdeki açıkları kullanarak sanal makineden kaçış (VM Escape) saldırıları yapabilir.