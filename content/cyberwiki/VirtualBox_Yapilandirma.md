+++
title = "VirtualBox Yapılandırması ve Ağ Modları | VirtualBox Configuration and Network Modes"
date = "2026-05-19"
draft = false
categories = ["Virtualization"]
type = "cyberwiki"
+++

VirtualBox, açık kaynak kodlu ve ücretsiz bir sanallaştırma yazılımıdır. Siber güvenlik lab ortamı kurarken en önemli konu **Ağ Yapılandırmasıdır**.

### 1. Ağ Bağlantı Türleri (Kritik)
Sanal makinenin dış dünyayla nasıl iletişim kuracağını belirler:
- **NAT (Network Address Translation):** Sanal makine internete çıkabilir ama dışarıdan kimse ona erişemez. Varsayılan ayardır.
- **Bridged Adapter (Köprü Bağdaştırıcısı):** Sanal makine, fiziksel bilgisayarınızla aynı modeme bağlıymış gibi davranır. Kendi IP'sini modemden alır. Güvenlik riski taşır çünkü sanal makine evdeki diğer tüm cihazlarla doğrudan iletişim kurabilir.
- **Internal Network (Dahili Ağ):** Sadece sanal makineler kendi arasında konuşur. Ana bilgisayar (Host) bile bu ağı göremez. Malware analizi için en güvenli yoldur.
- **Host-Only Adapter:** Sanal makine sadece ana bilgisayarla konuşabilir. İnternet erişimi yoktur.

### 2. Guest Additions
VMware Tools'un VirtualBox karşılığıdır. 
- **Shared Clipboard (Paylaşılan Pano):** Eğer "Kopyala-Yapıştır" özelliği açıksa, sanal makinedeki bir zararlı, ana bilgisayarınızın panosuna (clipboard) veri yazabilir veya oradaki şifrelerinizi okuyabilir.

### 3. USB Passthrough
Ana bilgisayara takılan bir USB cihazını doğrudan sanal makineye atama özelliğidir.
- **Analiz:** Bir USB'yi analiz etmek istiyorsanız, onu ana bilgisayara hiç "değdirmeden" (mount etmeden) doğrudan sanal makineye atayarak ana bilgisayarınızı virüsten koruyabilirsiniz.

---

## English Version

VirtualBox is an open source and free virtualization software. The most important issue when setting up a cyber security lab environment is **Network Configuration**.

### 1. Network Connection Types (Critical)
Determines how the virtual machine communicates with the outside world:
- **NAT (Network Address Translation):** The virtual machine can access the internet, but no one from the outside can access it. It is the default setting.
- **Bridged Adapter:** The virtual machine behaves as if it were connected to the same modem as your physical computer. It gets its own IP from the modem. It poses a security risk because the virtual machine can communicate directly with every other device in the home.
- **Internal Network:** Only virtual machines talk among themselves. Even the host cannot see this network. It is the safest way for malware analysis.
- **Host-Only Adapter:** The virtual machine can only talk to the host computer. There is no internet access.

### 2. Guest Additions
It is the VirtualBox equivalent of VMware Tools. 
- **Shared Clipboard:** If the "Copy-Paste" feature is turned on, a malware in the virtual machine can write data to the clipboard of your host computer or read your passwords there.

### 3. USB Passthrough
It is the feature of assigning a USB device plugged into the host computer directly to the virtual machine.
- **Analysis:** If you want to analyze a USB, you can protect your host from viruses by assigning it directly to the virtual machine without ever "touching" (mounting) it to the host.
