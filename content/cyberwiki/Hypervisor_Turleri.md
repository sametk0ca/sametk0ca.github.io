+++
title = "Hypervisor Türleri (Type 1 vs Type 2) | Hypervisor Types (Type 1 vs Type 2)"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "cyberwiki"
+++

Sanallaştırma, fiziksel bir donanımın kaynaklarını (CPU, RAM, Disk) birden fazla sanal makineye (VM) paylaştırma teknolojisidir. Bu işlemi yöneten yazılıma **Hypervisor** (Sanal Makine Monitörü) denir.

### 1. Type 1 Hypervisor (Bare-Metal)
Bu tür, doğrudan fiziksel donanım üzerine kurulur. Arada bir işletim sistemi (Windows/Linux) yoktur.
- **Örnekler:** VMware ESXi, Microsoft Hyper-V (Server sürümü), Proxmox (KVM tabanlı).
- **Security:** Arada genel amaçlı bir işletim sistemi olmadığı için saldırı yüzeyi çok dardır. Daha performanslı ve güvenlidir. Veri merkezlerinde ve bulut sistemlerinde standarttır.

### 2. Type 2 Hypervisor (Hosted)
Mevcut bir işletim sisteminin (Windows 10, macOS vb.) üzerine bir uygulama olarak kurulur.
- **Örnekler:** VMware Workstation, Oracle VirtualBox.
- **Security:** Eğer ana işletim sisteminiz (Host) hacklenirse, içindeki tüm sanal makineler de tehlikeye girer. Genellikle test ve kişisel kullanım/öğrenme amaçlıdır.

### 3. Sanallaştırma Terimleri
- **Host (Ev Sahibi):** Fiziksel bilgisayarın kendisi.
- **Guest (Misafir):** Sanallaştırılmış işletim sistemi (VM).
- **VM Escape (Sanal Makineden Kaçış):** Bir saldırganın sanal makine içindeki bir açıktan faydalanarak ana işletim sistemine (Host) veya diğer sanal makinelere sızmasıdır. Bu, siber güvenlikteki en kritik sanallaştırma açıklarından biridir.

---

## English Version

Virtualization is the technology of sharing the resources (CPU, RAM, Disk) of a physical hardware across multiple virtual machines (VMs). The software that manages this process is called **Hypervisor** (Virtual Machine Monitor).

### 1. Type 1 Hypervisor (Bare-Metal)
This type is built directly on physical hardware. There is no operating system (Windows/Linux) in between.
- **Examples:** VMware ESXi, Microsoft Hyper-V (Server edition), Proxmox (KVM based).
- **Security:** Since there is no general purpose operating system, the attack surface is very narrow. It is more performant and safer. It is standard in data centers and cloud systems.

### 2. Type 2 Hypervisor (Hosted)
It installs as an application on top of an existing operating system (Windows 10, macOS, etc.).
- **Examples:** VMware Workstation, Oracle VirtualBox.
- **Security:** If your main operating system (Host) is hacked, all virtual machines in it are also compromised. Generally for testing and personal use/learning purposes.

### 3. Virtualization Terms
- **Host:** The physical computer itself.
- **Guest:** Virtualized operating system (VM).
- **VM Escape:** An attacker infiltrates the main operating system (Host) or other virtual machines by exploiting a vulnerability in the virtual machine. This is one of the most critical virtualization vulnerabilities in cybersecurity.
