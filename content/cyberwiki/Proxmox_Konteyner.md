+++
title = "Proxmox  Konteyner Sanallaştırma | Proxmox Container Virtualization"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "cyberwiki"
+++

Proxmox, KVM ve LXC (Linux Containers) teknolojilerini birleştiren kurumsal bir sanallaştırma platformudur.

### 1. VM (Sanal Makine) vs. Container (Konteyner)
Siber güvenlik uzmanı bu ikisi arasındaki izolasyon farkını bilmelidir:
- **VM (KVM):** Kendi çekirdeğine (Kernel) sahiptir. Donanımı taklit eder. Daha ağır ama daha güvenlidir (İzolasyon tamdır).
- **Container (LXC/Docker):** Ana sistemin çekirdeğini (Host Kernel) paylaşır. Sadece uygulama katmanını izole eder. Çok hızlıdır ama eğer kernel'de bir açık varsa, bir konteynerden diğerine veya ana sisteme sızmak çok daha kolaydır.

### 2. Proxmox Firewall
Proxmox, hem ana sunucu hem de her bir sanal makine bazında kurallar yazılabilen gelişmiş bir dahili güvenlik duvarına sahiptir. "Datacenter -> Node -> VM" hiyerarşisi ile siber güvenlik kuralları merkezi olarak yönetilebilir.

### 3. ZFS Dosya Sistemi
Proxmox genellikle ZFS kullanır.
- **Data Integrity:** ZFS, verinin bozulup bozulmadığını sürekli kontrol eder ve otomatik onarır. 
- **Snapshot Hızı:** ZFS sayesinde saniyeler içinde binlerce sanal makinenin yedeği alınabilir.

### 4. Cluster Güvenliği
Birden fazla Proxmox sunucusu birbirine bağlanarak bir "küme" (cluster) oluşturabilir. Bu durumda yönetim trafiği şifrelenmeli ve özel bir ağdan (Management LAN) geçirilmelidir.

---

## English Version

Proxmox is an enterprise virtualization platform combining KVM and LXC (Linux Containers) technologies.

### 1. VM (Virtual Machine) etc. Container
The cybersecurity professional should know the isolation difference between these two:
- **VM (KVM):** It has its own kernel. It emulates hardware. It is heavier but safer (Isolation is complete).
- **Container (LXC/Docker):** Shares the host system's kernel. It only isolates the application layer. It is very fast, but if there is a vulnerability in the kernel, it is much easier to infiltrate from one container to another or to the host system.

### 2. Proxmox Firewall
Proxmox has an advanced internal firewall where rules can be written on both the host server and each virtual machine basis. Cyber ​​security rules can be managed centrally with the "Datacenter -> Node -> VM" hierarchy.

### 3. ZFS File System
Proxmox generally uses ZFS.
- **Data Integrity:** ZFS constantly checks whether the data is corrupted and repairs it automatically. 
- **Snapshot Speed:** Thanks to ZFS, thousands of virtual machines can be backed up in seconds.

### 4. Cluster Security
Multiple Proxmox servers can be connected to each other to form a "cluster". In this case, management traffic must be encrypted and passed through a private network (Management LAN).
