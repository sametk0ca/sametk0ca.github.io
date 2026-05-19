+++
title = "Anakart (Motherboard)  Chipset"
date = "2026-05-19"
draft = false
categories = ["Hardware"]
type = "bilgi-bankasi"
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