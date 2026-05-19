+++
title = "Hypervisor Türleri (Type 1 vs Type 2)"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Virtualization"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
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