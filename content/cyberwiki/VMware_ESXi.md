+++
title = "VMware Workstation  ESXi | VMware Workstation ESXi"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "cyberwiki"
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

---

## English Version

VMware is one of the leading and most widely used platforms in the virtualization world.

### 1. VMware Workstation (Pro/Player)
For individual users, Type 2 is a Hypervisor.
- **Snapshot Feature:** Records the current status of the system. While performing malware analysis, it enables you to run a virus and restore it to a clean state with a single click after the system is corrupted.
- **VM Encryption:** Encrypts the disk files of the virtual machine, preventing the data inside from being read even if these files are stolen.

### 2. VMware ESXi (vSphere)
It is an enterprise-level Type 1 Hypervisor.
- **Management Plane:** ESXi servers are usually managed centrally via vCenter.
- **VLAN Tagging:** ESXi supports 802.1Q (VLAN) tagging for network isolation between virtual machines. Virtual machines on a server can be prevented from seeing each other.

### 3. VMware Tools
It is a driver package that is installed inside the virtual machine. It provides features such as screen resolution, mouse synchronization and file sharing.
- **Security:** Since VMware Tools provides "Guest-to-Host" communication, attackers can sometimes perform VM Escape attacks by using vulnerabilities in this driver.
