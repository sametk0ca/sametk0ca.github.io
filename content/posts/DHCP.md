---
title: "DHCP"
date: 2026-01-04
description: "How DHCP hands out IP addresses automatically: the four-step DORA exchange and lease renewal. / DHCP'nin IP adreslerini otomatik dağıtma süreci: DORA adımları ve kira yenileme."
draft: false
tags: ["Networking", "Protocols"]
categories: ["Writeups"]
related:
  - "[[DHCP_DORA|DHCP (Dynamic Host Configuration Protocol) - DORA Süreci]]"
---

## 🇹🇷 Türkçe (TR)

**DHCP (Dynamic Host Configuration Protocol)**, bir cihazın ağa bağlandığında IP adresini ve diğer ağ ayarlarını (alt ağ maskesi, varsayılan ağ geçidi, DNS sunucuları) otomatik olarak almasını sağlayan protokoldür. Manuel IP ataması gerekmez, ağ yönetimi kolaylaşır.

Atama süreci dört adımdan oluşur ve baş harflerinden **DORA** olarak bilinir: **Discover**, **Offer**, **Request**, **Acknowledge**.

### DORA Adımları

| Adım | Mesaj | Yön | Ne yapar? |
|---|---|---|---|
| 1 | **Discover** (Keşif) | İstemci → yayın (broadcast) | "Ağda DHCP sunucusu var mı?" |
| 2 | **Offer** (Teklif) | Sunucu → istemci | Kullanılabilecek bir IP adresi ve ağ ayarlarını önerir |
| 3 | **Request** (İstek) | İstemci → yayın (broadcast) | Seçtiği teklifi kabul eder |
| 4 | **Acknowledge** (Onay) | Sunucu → istemci | Atamayı onaylar |

DHCP, UDP üzerinde çalışır: sunucu **67**, istemci **68** numaralı portu kullanır.

#### 1. Discover (Keşif)

- Ağa yeni bağlanan cihazın henüz bir IP adresi yoktur.
- Cihaz, DHCP sunucusunu bulmak için ağdaki herkese yayın yapan bir **Discover** paketi gönderir.
- Paket, cihazın MAC adresi gibi kimlik bilgilerini taşır; sunucu cihazı bu sayede tanır.

#### 2. Offer (Teklif)

- DHCP sunucusu Discover paketine **Offer** ile yanıt verir.
- Teklif; bir IP adresi, alt ağ maskesi, varsayılan ağ geçidi, DNS sunucuları ve kira süresini (lease time) içerir.
- Ağda birden fazla DHCP sunucusu varsa cihaz birden fazla teklif alabilir. Genellikle ilk gelen teklif kabul edilir.

#### 3. Request (İstek)

- Cihaz tekliflerden birini seçer ve **Request** paketi gönderir. Paket, seçilen IP adresini ve teklifi veren sunucunun kimliğini içerir.
- Request yayın olarak gönderildiği için diğer sunucular da tekliflerinin kabul edilmediğini öğrenir ve önerdikleri adresi başkasına verebilir.

#### 4. Acknowledge (Onay)

- Sunucu, **ACK** paketiyle IP adresinin cihaza atandığını doğrular.
- ACK; IP adresi, ağ ayarları ve kira süresini içerir. Cihaz artık adresi kullanabilir.

### Kira Süresi (Lease Time)

- DHCP ile atanan adres kalıcı değildir, belirli bir süre için kiralanır. Süreyi sunucu belirler; saatler veya günler olabilir.
- Cihaz, kira süresi dolmadan adresini yenilemek (renew) için sunucuya istek gönderir. Sunucu onaylarsa cihaz aynı adresi kullanmaya devam eder.
- Yenileme yapılmazsa süre dolunca adres serbest kalır ve başka bir cihaza verilebilir.

### Özet

Süreç, cihazın Discover ile sunucuyu aramasıyla başlar; sunucunun Offer ile adres önermesi, cihazın Request ile bu adresi istemesi ve sunucunun ACK ile atamayı onaylamasıyla tamamlanır. Bu otomatik süreç, adres çakışmalarını büyük ölçüde önler ve özellikle büyük ağlarda yönetimi kolaylaştırır.

---

## 🇬🇧 English (EN)

**DHCP (Dynamic Host Configuration Protocol)** lets a device automatically obtain an IP address and other network settings (subnet mask, default gateway, DNS servers) when it joins a network. There is no need for manual IP assignment, which makes network management easier.

The assignment takes four steps, known by their initials as **DORA**: **Discover**, **Offer**, **Request**, **Acknowledge**.

### The DORA Steps

| Step | Message | Direction | Purpose |
|---|---|---|---|
| 1 | **Discover** | Client → broadcast | "Is there a DHCP server on this network?" |
| 2 | **Offer** | Server → client | Proposes an IP address and network settings |
| 3 | **Request** | Client → broadcast | Accepts the chosen offer |
| 4 | **Acknowledge** | Server → client | Confirms the assignment |

DHCP runs over UDP: the server listens on port **67** and the client uses port **68**.

#### 1. Discover

- A device that has just joined the network does not have an IP address yet.
- It broadcasts a **Discover** packet to find a DHCP server.
- The packet carries identifying information such as the device's MAC address, so the server can recognize it.

#### 2. Offer

- A DHCP server answers the Discover with an **Offer**.
- The offer contains an IP address, subnet mask, default gateway, DNS servers, and the lease time.
- If there are several DHCP servers, the device may receive several offers. It usually accepts the first one.

#### 3. Request

- The device picks one offer and sends a **Request** containing the chosen IP address and the identity of the server that made the offer.
- Because the Request is broadcast, the other servers learn their offers were declined and can hand those addresses to someone else.

#### 4. Acknowledge

- The server confirms the assignment with an **ACK** packet.
- The ACK contains the IP address, network settings, and lease time. The device can now use the address.

### Lease Time

- An address assigned by DHCP is not permanent; it is leased for a limited time set by the server, which can be hours or days.
- Before the lease expires, the device asks the server to renew it. If the server agrees, the device keeps the same address.
- If the lease is not renewed, the address is released when it expires and can be assigned to another device.

### Summary

The process starts with the device looking for a server with Discover, continues with the server proposing an address with Offer and the device asking for it with Request, and ends with the server confirming it with ACK. This automatic process largely prevents address conflicts and makes management easier, especially in large networks.
