---
title: "Everything About DHCP"
date: 2026-01-04
draft: false
tags: ["Networking", "Protocols"]
categories: ["Writeups"]
---
DHCP Hakkında Her Şey | Everything About DHCP

**DHCP (Dynamic Host Configuration Protocol)**, bir cihazın ağa bağlandığında otomatik olarak IP adresi ve diğer ağ ayarlarını almasını sağlayan bir protokoldür. Bu sayede manuel IP ataması yapmaya gerek kalmaz ve ağ yönetimi kolaylaşır. DHCP’nin bir cihaza IP adresi atama süreci, dört temel adımdan oluşur: **_Discover_**, **_Offer_**, **_Request_** ve **_Acknowledge_**.

**1. DHCP Discover (Keşif)**  
- Bir cihaz (örneğin, bir bilgisayar veya telefon) ağa bağlandığında, henüz bir IP adresine sahip olmadığını fark eder.  
- Cihaz, ağdaki DHCP sunucusunu bulmak için bir **DHCP Discover** paketi gönderir. Bu paket, ağdaki tüm cihazlara yayınlanır (broadcast) ve “DHCP sunucusu var mı?” diye sorar.  
- Discover paketi, cihazın MAC adresi gibi benzersiz kimlik bilgilerini içerir, böylece sunucu cihazı tanıyabilir.

**2. DHCP Offer (Teklif)**  
- Ağdaki DHCP sunucusu, Discover paketini alır ve buna yanıt olarak bir **DHCP Offer** paketi gönderir.  
- Offer paketi, cihazın kullanabileceği bir IP adresi, alt ağ maskesi (subnet mask), varsayılan ağ geçidi (default gateway), DNS sunucuları ve kira süresi (lease time) gibi bilgileri içerir.  
- Eğer ağda birden fazla DHCP sunucusu varsa, cihaz birden fazla Offer paketi alabilir. Genellikle cihaz, ilk gelen teklifi kabul eder.

**3. DHCP Request (İstek)**  
- Cihaz, aldığı Offer paketlerinden birini seçer ve bu teklifi kabul etmek için bir **DHCP Request** paketi gönderir.  
- Request paketi, seçilen IP adresini ve sunucunun kimliğini içerir. Bu, sunucuya “Bu IP adresini kullanmak istiyorum” mesajını iletir.  
- Aynı zamanda, diğer sunuculara (eğer varsa) bu IP adresini kullanmayacağını bildirir, böylece o adres başka bir cihaza atanabilir.

**4. DHCP Acknowledge (Onay)**  
- DHCP sunucusu, cihazın isteğini onaylamak için bir **DHCP Acknowledge** (ACK) paketi gönderir.  
- ACK paketi, IP adresinin cihaza resmi olarak atandığını doğrular ve cihazın bu adresi kullanabileceğini bildirir.  
- Bu pakette, IP adresinin yanı sıra ağ ayarları (subnet mask, default gateway, DNS vb.) ve kira süresi de yer alır.

**Kira Süresi (Lease Time) Hakkında**  
- DHCP tarafından atanan IP adresi kalıcı değildir; belirli bir kira süresi için geçerlidir. Bu süre, sunucu tarafından belirlenir ve saatler veya günler sürebilir.  
- Cihaz, kira süresi dolmadan önce IP adresini yenilemek (renew) için sunucuya bir istek gönderir. Sunucu bu isteği onaylarsa, cihaz aynı IP adresini kullanmaya devam eder.  
- Eğer yenileme yapılmazsa, kira süresi dolduğunda IP adresi serbest kalır ve başka bir cihaza atanabilir.


**Özet**  
DHCP, bir cihazın ağa bağlandığında IP adresini otomatik olarak almasını sağlayan pratik bir protokoldür. Süreç, cihazın Discover paketiyle sunucuyu aramasıyla başlar, sunucunun Offer paketiyle bir IP adresi önermesiyle devam eder, cihazın Request paketiyle bu adresi istemesi ve son olarak sunucunun ACK paketiyle atamayı onaylamasıyla tamamlanır. Bu otomatik süreç, IP çakışmalarını önler ve özellikle büyük ağlarda yönetimi kolaylaştırır.

**DHCP (Dynamic Host Configuration Protocol)** is a protocol that allows a device to automatically obtain an IP address and other network settings when it connects to a network. This eliminates the need for manual IP assignment and makes network management easier. The process of DHCP assigning an IP address to a device consists of four basic steps: **_Discover_**, **_Offer_**, **_Request_**, and **Acknowledge**. Below, I explain these steps step by step:

**1. DHCP Discover (Discovery)**  
- When a device (e.g., a computer or phone) connects to the network, it realizes that it does not yet have an IP address.  
- The device sends a **DHCP Discover** packet to find the DHCP server on the network. This packet is broadcast to all devices on the network and asks, “Is there a DHCP server?”  
- The Discover packet contains unique identification information such as the device’s MAC address, so the server can recognize the device.

**2. DHCP Offer (Offer)**  
- The DHCP server on the network receives the Discover packet and responds with a **DHCP Offer** packet.  
- The Offer packet contains an IP address that the device can use, subnet mask, default gateway, DNS servers, and lease time.  
- If there are multiple DHCP servers on the network, the device may receive multiple Offer packets. Usually, the device accepts the first offer it receives.

**3. DHCP Request (Request)**  
- The device selects one of the Offer packets it received and sends a **DHCP Request** packet to accept that offer.  
- The Request packet contains the selected IP address and the server’s identity. This tells the server, “I want to use this IP address.”  
- At the same time, it notifies other servers (if any) that it will not use that IP address, so that address can be assigned to another device.

**4. DHCP Acknowledge (Acknowledgment)**  
- The DHCP server sends a **DHCP Acknowledge** (ACK) packet to confirm the device’s request.  
- The ACK packet confirms that the IP address has been officially assigned to the device and notifies the device that it can use this address.  
- This packet includes the IP address, network settings (subnet mask, default gateway, DNS, etc.), and the lease time.

**About Lease Time**  
- The IP address assigned by DHCP is not permanent; it is valid for a specific lease time. This duration is determined by the server and can last for hours or days.  
- Before the lease time expires, the device sends a request to the server to renew the IP address. If the server approves this request, the device continues to use the same IP address.  
- If the renewal is not made, the IP address becomes free when the lease time expires and can be assigned to another device.

**Summary**  
DHCP is a practical protocol that allows a device to automatically obtain an IP address when it connects to the network. The process starts with the device searching for the server with a Discover packet, continues with the server suggesting an IP address with an Offer packet, the device requesting this address with a Request packet, and finally, the server confirming the assignment with an ACK packet. This automatic process prevents IP conflicts and makes management easier, especially in large networks.