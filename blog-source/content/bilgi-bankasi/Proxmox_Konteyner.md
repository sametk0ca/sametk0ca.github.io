+++
title = "Proxmox  Konteyner Sanallaştırma"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "bilgi-bankasi"
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