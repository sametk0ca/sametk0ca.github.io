---
title: "Steganography"
date: 2026-01-04
description: "How steganography hides the very existence of a message in images, audio and text, how LSB embedding works, and how it differs from cryptography. / Steganografinin mesajın varlığını görüntü, ses ve metin içinde nasıl gizlediği, LSB yönteminin işleyişi ve kriptografiden farkı."
draft: false
tags: ["Cryptography", "Steganography"]
categories: ["Writeups"]
---

## 🇹🇷 Türkçe (TR)

### Steganografi Nedir?

Steganografi, bir bilginin başka bir verinin içine gizlenerek iletilmesi sanatıdır. Kriptografi gibi siber güvenlikte bilgi koruma yöntemleri arasında yer alsa da, farklı bir yaklaşımı vardır. Kriptografide mesajın içeriği şifrelenerek koruma sağlanırken, steganografide mesajın varlığı gizlenir. Yani üçüncü kişiler mesajın varlığından bile haberdar olmaz.

Bu teknik özellikle dijital dosyalar üzerinden yürütülür; örneğin, bir resim, ses dosyası, video ya da yazı dosyasının içine bilgi saklanabilir. Günümüzde çeşitli yazılımlar sayesinde, bilgi, bu tür dosyaların içine gömülerek gizlice iletilebilir.

### Steganografinin Tarihi

Steganografi, aslında dijital çağdan çok daha eski bir tarihe sahiptir. Eski Yunan’da, mesajlar kölelerin kafasına kazınır ve saçları uzayana kadar beklenirdi. Bu, düşmanlardan bilgi saklama amacı taşıyan ilk örneklerden biridir. Ortaçağ Avrupa’sında ise mesajlar görünmez mürekkeplerle yazılırdı. Dijital çağda ise steganografi, daha çok dijital dosyaların içine gizlenen verilerle yapılır.

### Steganografinin Çeşitleri ve Teknikleri

Steganografi farklı medya türleri aracılığıyla yapılabilir:

1. **Görüntü Steganografisi:** Dijital resimler, steganografinin en sık kullanıldığı medya türlerinden biridir. Bir resmin piksel renklerinin en düşük bitleri değiştirilerek mesaj gizlenebilir. Bu yöntem LSB (Least Significant Bit) olarak bilinir ve insan gözüyle algılanamayacak kadar küçük değişiklikler yapılır.
2. **Ses Steganografisi:** Ses örneklerinin en az anlamlı bitleri, faz veya yankı gibi kulağın algılayamayacağı özellikler hafifçe değiştirilerek veri saklanabilir.
3. **Video Steganografisi:** Görüntü steganografisinin bir genişletmesi olarak video dosyalarında da kullanılabilir. Videonun her bir karesindeki renk değerleri değiştirilerek veri gizlenebilir. Bu yöntem, büyük miktarda veri saklayabilmesi açısından oldukça etkilidir.
4. **Metin Steganografisi:** İlk bakışta fark edilmeyen harfler ya da boşluklar kullanılarak, metin dosyalarında bilgi saklanabilir. Bu yöntem, eski bir tekniktir ve daha çok düşük hacimli bilgi saklama için uygundur.

### Steganografinin Kullanım Alanları

1. **Güvenli İletişim:** Özellikle gizli servisler veya hassas verileri iletmek isteyen bireyler, steganografi sayesinde mesajların görünürlüğünü azaltarak iletişim kurabilirler. Bilgi, gözle algılanamayacak bir şekilde saklanarak yalnızca ilgili alıcı tarafından çözülebilir.
2. **Siber Suçlar ve Savunma:** Steganografi hem savunmacılar hem de saldırganlar tarafından kullanılabilir. Bazı zararlı yazılımlar, komutlarını veya yüklerini görüntü dosyalarının içine gizleyerek ağ denetimlerinden kaçar (örneğin Stegoloader, yükünü PNG görüntülerinin içine saklamıştır). Bu da güvenlik araştırmacılarının steganografi tespitine (steganaliz) önem vermesini gerektirir.
3. **Dijital Telif Hakkı Koruma:** Dijital dosyaların içine gömülen görünmez filigranlar, sahipliği kanıtlamaya ve içeriğin nereden sızdığını izlemeye yardımcı olur. Örneğin, bir fotoğraf veya videonun içine yerleştirilen dijital bir imza, izinsiz çoğaltmayı engellemez ama izlenebilir kılar.
4. **Gizli Veri Depolama:** Bazı durumlarda hassas verilerin varlığını gizlemek için steganografi tercih edilir. Aynı yöntem, saldırganlar tarafından veri sızdırmak (exfiltration) için de kullanılabilir.

### Steganografi Nasıl Çalışır?

Steganografi, verinin bir medya dosyasına “gizlenmesi” için algoritmalar kullanır. En yaygın kullanılan yöntemlerden biri olan LSB tekniğinde, veriler bir resmin en az anlamlı bitlerine (LSB) gizlenir. Örneğin, RGB formatında bir resimde her bir piksel 24 bit bilgi içerir; bu bitlerden en az anlamlı olanları değiştirilerek, veri gizlenir. Ses dosyalarında ise veriler, örneklerin en az anlamlı bitlerinde veya faz ve yankı gibi duyulamayan özelliklerde saklanır.

En az anlamlı bit (Least Significant Bit — LSB), bir veri biriminde değeri en az etkileyen bit anlamına gelir. Bu bit, sayısal veri içinde en sağda bulunan ve bir sayının en düşük seviyeli kısmını temsil eden bittir. LSB steganografisinde, dijital bir dosyada (genellikle bir resim ya da ses dosyasında) bu bitler değiştirilerek veriler saklanır, çünkü değişiklikler gözle veya kulakla fark edilemeyecek kadar küçüktür.

Örneğin, bir resimde her piksel genellikle kırmızı, yeşil ve mavi (RGB) bileşenleriyle tanımlanır. Her bir bileşen 8 bit (1 byte) ile gösterilir, yani toplamda 24 bit ile bir pikselin rengi belirlenir. Bu 8 bitin en sağdaki bitini (en az anlamlı bitini) değiştirmek, rengin tonunu çok az değiştirir. İnsanın bu küçük değişiklikleri algılayamaması sayesinde de veriler gizlenebilir.

Bir örnekle açıklayalım:

- Bir resmin bir pikselinin kırmızı bileşeni `11101110` olsun.
- Eğer biz bu bileşende en sağdaki biti `0` yerine `1` olarak değiştirirsek, yeni değer `11101111` olur.

Bu küçük değişiklik, pikselin rengini neredeyse fark edilmeyecek kadar az değiştirir. Bu sayede LSB yöntemiyle çok sayıda bit gizlenebilir. Steganografi işlemi boyunca, her pikselin LSB’si değiştirilerek, büyük bir mesajı küçük değişikliklerle saklamak mümkün olur. Ancak istatistiksel yöntemlerle (steganaliz; örneğin histogram ve ki-kare analizi) bu tür değişiklikler tespit edilebilir.

### Steganografi ve Kriptografi Farkı

Kriptografi, veriyi şifreleyerek koruma altına alırken, steganografi verinin varlığını gizler. Kriptografik bir mesaj ele geçirildiğinde, mesajın içeriği okunamaz olsa da bir gizli mesaj olduğu belli olur. Steganografide ise mesajın varlığı fark edilmediğinden, dikkat çekmez. Bu iki yöntem birbirini tamamlar: önce mesaj şifrelenir, sonra bir dosyanın içine gömülerek iletilir. Böylece mesaj bulunsa bile içeriği okunamaz.

---

## 🇬🇧 English (EN)

### What is Steganography?

Steganography is the art of concealing information within other data. In contrast to cryptography, which encrypts the content of a message, steganography hides the existence of the message itself, making it a discreet and undetectable form of secure communication.

This technique is often applied to digital files, such as images, audio files, videos, or text documents, which can carry hidden information without arousing suspicion. Modern software tools enable data embedding within these files, allowing the safe transmission of sensitive information.

### A Brief History of Steganography

Steganography dates back to ancient times, long before the digital age. In Ancient Greece, messages were tattooed on the heads of slaves, who would grow their hair back before delivering the message to the intended recipient. During medieval Europe, invisible ink was used to hide information in letters. In the digital era, steganography has evolved to include concealing data within digital files.

### Types and Techniques of Steganography

Steganography can be applied to various media types:

1. **Image Steganography:** Digital images are the most common medium for steganography. A technique called LSB (Least Significant Bit) modifies the least significant bits of an image’s pixels to embed data, which is undetectable by the human eye.
2. **Audio Steganography:** Data can be concealed by slightly altering the least significant bits of audio samples, or properties the ear cannot perceive, such as phase or echo.
3. **Video Steganography:** This technique extends image steganography to video files. Data can be embedded in individual frames of a video, which is effective for storing large amounts of data.
4. **Text Steganography:** By using small changes like hidden letters or spaces, data can be embedded within a text file. Though an older method, it’s suitable for small data volumes.

### Applications of Steganography

1. **Secure Communication:** Steganography allows secure communication by reducing the visibility of messages. Information can be concealed and decrypted only by the intended receiver, making it useful for sensitive communications.
2. **Cybercrime and Defense:** Steganography can be used by defenders and attackers alike. Some malware hides its commands or payloads inside image files to evade network inspection (for example, Stegoloader hid its payload inside PNG images). This is why security experts focus on detecting steganographic methods (steganalysis).
3. **Digital Copyright Protection:** Invisible watermarks within digital files help prove ownership and trace where content leaked from. For example, a digital watermark within an image or video does not prevent copying, but makes it traceable.
4. **Hidden Data Storage:** In some cases steganography is used to hide the very existence of sensitive data. Attackers can use the same method to exfiltrate data.

### How Does Steganography Work?

Steganography algorithms embed data within a media file without affecting its visible content. The commonly used LSB method hides data in the least significant bits of an image (LSB). For instance, a 24-bit RGB image can have its least significant bits altered slightly without noticeable color changes. In audio files, data is embedded in the least significant bits of samples or in properties such as phase and echo that are inaudible to the human ear.

The **Least Significant Bit (LSB)** is the bit in a data unit that has the smallest effect on its overall value. Located on the far right of a binary number, it represents the lowest-value part of that number. In LSB steganography, this bit is modified in digital files (usually an image or audio file) to embed hidden data because such small changes are almost undetectable by human perception.

For example, in an image, each pixel is typically represented by three color components: red, green, and blue (RGB). Each color component is stored in 8 bits (1 byte), resulting in a total of 24 bits for one pixel. By modifying the LSB of each 8-bit color component, we can change the color by a tiny amount, which is visually imperceptible to the human eye.

Here’s a quick example:

- Suppose the red component of a pixel has a binary value of `11101110`.
- If we change the LSB from `0` to `1`, the new value becomes `11101111`.

This small change slightly alters the pixel’s color, but it’s hardly noticeable. By modifying the LSB of many pixels, a significant amount of data can be hidden within the image. However, statistical methods (steganalysis, such as histogram and chi-square analysis) can detect such changes.

### Steganography vs. Cryptography

While cryptography secures data by encrypting it, steganography hides the existence of the data itself. An intercepted cryptographic message may be unreadable, but it is obvious that a secret message exists; a steganographic message, if unnoticed, draws no attention. The two techniques complement each other: the message is first encrypted, then embedded within a file, so even if it is found, its content stays unreadable.
