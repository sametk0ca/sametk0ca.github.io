+++
title = "Anakart (Motherboard)  Chipset | Motherboard Chipset"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "cyberwiki"
+++

Anakart, bir bilgisayarın tüm bileşenlerinin birbiriyle iletişim kurmasını sağlayan ana sinir sistemidir. Siber güvenlik uzmanı için anakart, sadece bir "kart" değil, güvenliğin donanım seviyesinde başladığı (Hardware Root of Trust) yerdir.

### 1. Chipset (Yonga Seti) Rolü
Chipset, CPU ile bellek ve çevre birimleri (USB, Diskler, Ağ) arasındaki veri akışını yönetir. 
- **Güvenlik Perspektifi:** Modern chipsetler, **Intel ME (Management Engine)** veya **AMD PSP (Platform Security Processor)** gibi işlemciler içerir. Bu yapılar işletim sisteminden bağımsız çalışır ve ağ üzerinden erişilebilirler. Eğer bu seviyede bir zafiyet varsa, işletim sistemi ne kadar güvenli olursa olsun saldırgan tam kontrol sağlayabilir.

### 2. BIOS ve UEFI
Eski BIOS yerini UEFI'ye bırakmıştır. 
- **Secure Boot:** Sadece imzalı ve güvenilir işletim sistemi çekirdeklerinin yüklenmesine izin vererek **Bootkit** saldırılarını engeller.
- **TPM (Trusted Platform Module):** Anakart üzerinde bulunan bu çip, şifreleme anahtarlarını saklar. BitLocker gibi disk şifreleme teknolojileri anahtarlarını burada tutar; bu da diski başka bir bilgisayara takıp içini okumayı imkansız kılar.

### 3. Otobüsler (Bus) ve DMA Saldırıları
Bileşenler arasındaki veri yolları (PCIe gibi) üzerinden **DMA (Direct Memory Access)** saldırıları gerçekleştirilebilir. Bir saldırgan, örneğin Thunderbolt portu üzerinden cihazı takıp doğrudan RAM içeriğini okuyabilir. Modern anakartlarda bu, **IOMMU** teknolojisi ile kısıtlanmaktadır.

---

## English Version

The motherboard is the main nervous system that allows all components of a computer to communicate with each other. For the cyber security expert, the motherboard is not just a "card", it is the place where security begins at the hardware level (Hardware Root of Trust).

### 1. Chipset Role
The chipset manages the flow of data between the CPU and memory and peripherals (USB, Disks, Network). 
- **Security Perspective:** Modern chipsets include processors such as **Intel ME (Management Engine)** or **AMD PSP (Platform Security Processor)**. These structures work independently of the operating system and can be accessed over the network. If this level of vulnerability exists, the attacker can gain full control, no matter how secure the operating system is.

### 2. BIOS and UEFI
Legacy BIOS has been replaced by UEFI. 
- **Secure Boot:** Prevents **Bootkit** attacks by only allowing signed and trusted operating system kernels to be loaded.
- **TPM (Trusted Platform Module):** This chip on the motherboard stores the encryption keys. Disk encryption technologies like BitLocker keep their keys here; This makes it impossible to insert the disk into another computer and read its contents.

### 3. Buses and DMA Attacks
**DMA (Direct Memory Access)** attacks can be carried out over data paths (such as PCIe) between components. An attacker can, for example, plug in the device via the Thunderbolt port and directly read the contents of the RAM. On modern motherboards this is restricted by **IOMMU** technology.
