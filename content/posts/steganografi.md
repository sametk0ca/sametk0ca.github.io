---
title: "Steganography"
date: 2026-01-04
draft: false
tags: ["Cryptography", "Steganography"]
categories: ["Writeups"]
cover:
    image: "https://miro.medium.com/v2/resize:fit:700/1*p3tvvzQk7A6tDtmDc9uIxA.jpeg"
    alt: "Steganography"
    relative: false
---

## Steganografi Nedir?

Steganografi, bir bilginin başka bir verinin içine gizlenerek iletilmesi sanatıdır. Kriptografi gibi siber güvenlikte bilgi koruma yöntemleri arasında yer alsa da, farklı bir yaklaşımı vardır. Kriptografide mesajın içeriği şifrelenerek koruma sağlanırken, steganografide mesajın varlığı gizlenir. Yani üçüncü kişiler mesajın varlığından bile haberdar olmaz.

Bu teknik özellikle dijital dosyalar üzerinden yürütülür; örneğin, bir resim, ses dosyası, video ya da yazı dosyasının içine bilgi saklanabilir. Günümüzde çeşitli yazılımlar sayesinde, bilgi, bu tür dosyaların içine gömülerek gizlice iletilebilir.

## Steganografinin Tarihi

Steganografi, aslında dijital çağdan çok daha eski bir tarihe sahiptir. Eski Yunan’da, mesajlar kölelerin kafasına kazınır ve saçları uzayana kadar beklenirdi. Bu, düşmanlardan bilgi saklama amacı taşıyan ilk örneklerden biridir. Ortaçağ Avrupa’sında ise mesajlar görünmez mürekkeplerle yazılırdı. Dijital çağda ise steganografi, daha çok dijital dosyaların içine gizlenen verilerle yapılır.

## Steganografinin Çeşitleri ve Teknikleri

Steganografi farklı medya türleri aracılığıyla yapılabilir:

1. **Görüntü Steganografisi:** Dijital resimler, steganografinin en sık kullanıldığı medya türlerinden biridir. Bir resmin piksel renklerinin en düşük bitleri değiştirilerek mesaj gizlenebilir. Bu yöntem LSB (Least Significant Bit) olarak bilinir ve insan gözüyle algılanamayacak kadar küçük değişiklikler yapılır.
2. **Ses Steganografisi:** Ses dosyalarında frekanslar ve amplitüdler gibi özellikler değiştirilerek veri saklanabilir. Örneğin, bir ses dosyasının belirli kısımlarındaki düşük frekanslar modifiye edilerek veri gömülür.
3. **Video Steganografisi:** Görüntü steganografisinin bir genişletmesi olarak video dosyalarında da kullanılabilir. Videonun her bir karesindeki renk değerleri değiştirilerek veri gizlenebilir. Bu yöntem, büyük miktarda veri saklayabilmesi açısından oldukça etkilidir.
4. **Metin Steganografisi:** İlk bakışta fark edilmeyen harfler ya da boşluklar kullanılarak, metin dosyalarında bilgi saklanabilir. Bu yöntem, eski bir tekniktir ve daha çok düşük hacimli bilgi saklama için uygundur.


![](https://miro.medium.com/v2/resize:fit:700/1*p3tvvzQk7A6tDtmDc9uIxA.jpeg)

## Steganografinin Kullanım Alanları

1. **Güvenli İletişim:** Özellikle gizli servisler veya hassas verileri iletmek isteyen bireyler, steganografi sayesinde mesajların görünürlüğünü azaltarak iletişim kurabilirler. Bilgi, gözle algılanamayacak bir şekilde saklanarak yalnızca ilgili alıcı tarafından çözülebilir.
2. **Dijital Suçlarla Mücadele:** Steganografi teknikleri siber suçlarla mücadelede hem avantaj hem de dezavantaj sağlar. Bazı zararlı yazılımlar komut dosyalarını veya verilerini yaymak için steganografi kullanabilir. Bu da güvenlik araştırmacılarının steganografi tespitine önem vermelerini gerektirir.
3. **Dijital Telif Hakkı Koruma:** Dijital dosyaların içine gömülen gizli işaretler, telif hakkı ihlallerini engellemek için kullanılır. Örneğin, bir fotoğraf veya videonun içine yerleştirilen dijital bir imza, izinsiz çoğaltılmasını engelleyebilir.
4. **Gizli Veri Depolama:** Bazı durumlarda hassas verilerin görünürlüğünü en aza indirgemek için steganografi tercih edilir. Bu, kişisel verilerin güvenliğini sağlama veya veri sızmalarını önleme amacı taşır.

## Steganografi Nasıl Çalışır?

Steganografi, verinin bir medya dosyasına “gizlenmesi” için algoritmalar kullanır. En yaygın kullanılan yöntemlerden biri olan LSB tekniğinde, veriler bir resmin en az anlamlı bitlerine (LSB) gizlenir. Örneğin, RGB formatında bir resimde her bir piksel 24 bit bilgi içerir; bu bitlerden en az anlamlı olanları değiştirilerek, veri gizlenir. Ses dosyalarında ise veriler, duyulamayan düşük frekanslarda saklanır.

En az anlamlı bit (Least Significant Bit — LSB), bir veri biriminde değeri en az etkileyen bit anlamına gelir. Bu bit, sayısal veri içinde en sağda bulunan ve bir sayının en düşük seviyeli kısmını temsil eden bittir. LSB steganografisinde, dijital bir dosyada (genellikle bir resim ya da ses dosyasında) bu bitler değiştirilerek veriler saklanır, çünkü değişiklikler gözle veya kulakla fark edilemeyecek kadar küçüktür.

Örneğin, bir resimde her piksel genellikle kırmızı, yeşil ve mavi (RGB) bileşenleriyle tanımlanır. Her bir bileşen 8 bit (1 byte) ile gösterilir, yani toplamda 24 bit ile bir pikselin rengi belirlenir. Bu 8 bitin en sağdaki bitini (en az anlamlı bitini) değiştirmek, rengin tonunu çok az değiştirir. İnsanın bu küçük değişiklikleri algılayamaması sayesinde de veriler gizlenebilir.

Bir örnekle açıklayalım:

- Bir resmin bir pikselinin kırmızı bileşeni `11101110` olsun.
- Eğer biz bu bileşende en sağdaki biti `0` yerine `1` olarak değiştirirsek, yeni değer `11101111` olur.

Bu küçük değişiklik, pikselin rengini neredeyse fark edilmeyecek kadar az değiştirir. Bu sayede LSB yöntemiyle çok sayıda bit gizlenebilir. Steganografi işlemi boyunca, her pikselin LSB’si değiştirilerek, büyük bir mesajı küçük değişikliklerle saklamak mümkün olur.



![](https://miro.medium.com/v2/resize:fit:700/1*XI3yGfKYW35GkI1VCXaX6w.jpeg)

LSB

## Steganografi ve Kriptografi Farkı

Kriptografi, veriyi şifreleyerek koruma altına alırken, steganografi verinin varlığını gizler. Kriptografik bir mesaj ele geçirildiğinde, şifreleme algoritmasına dayanarak mesajın içeriği anlaşılabilir. Steganografide ise mesajın varlığı fark edilmediğinden, yakalanması daha zordur. Bu iki yöntem bir arada kullanılarak, güvenlik iki katına çıkarılabilir. Önce mesaj şifrelenip sonra bir dosyanın içine gömülerek iletilir.

## What is Steganography?

Steganography is the art of concealing information within other data. In contrast to cryptography, which encrypts the content of a message, steganography hides the existence of the message itself, making it a discreet and undetectable form of secure communication.


This technique is often applied to digital files, such as images, audio files, videos, or text documents, which can carry hidden information without arousing suspicion. Modern software tools enable data embedding within these files, allowing the safe transmission of sensitive information.

## A Brief History of Steganography

Steganography dates back to ancient times, long before the digital age. In Ancient Greece, messages were tattooed on the heads of slaves, who would grow their hair back before delivering the message to the intended recipient. During medieval Europe, invisible ink was used to hide information in letters. In the digital era, steganography has evolved to include concealing data within digital files.

## Types and Techniques of Steganography

Steganography can be applied to various media types:

1. **Image Steganography:** Digital images are the most common medium for steganography. A technique called LSB (Least Significant Bit) modifies the least significant bits of an image’s pixels to embed data, which is undetectable by the human eye.
2. **Audio Steganography:** In audio files, frequencies and amplitudes can be adjusted to conceal data. Specific portions of an audio file may be modified to contain hidden information at low, nearly inaudible frequencies.
3. **Video Steganography:** This technique extends image steganography to video files. Data can be embedded in individual frames of a video, which is effective for storing large amounts of data.
4. **Text Steganography:** By using small changes like hidden letters or spaces, data can be embedded within a text file. Though an older method, it’s suitable for small data volumes.



![](https://miro.medium.com/v2/resize:fit:700/1*p3tvvzQk7A6tDtmDc9uIxA.jpeg)

## Applications of Steganography

1. **Secure Communication:** Steganography allows secure communication by reducing the visibility of messages. Information can be concealed and decrypted only by the intended receiver, making it useful for sensitive communications.
2. **Cybercrime Investigation:** While steganography aids secure communication, it can also be used maliciously. Some malware programs use steganography to propagate code or hidden data, which is why security experts focus on detecting steganographic methods.
3. **Digital Copyright Protection:** Hidden markers within digital files help prevent copyright infringement. For example, a digital watermark within an image or video enables tracking and proves ownership.
4. **Hidden Data Storage:** In cases where data privacy is paramount, steganography can reduce data visibility, minimizing the risk of data breaches.

## How Does Steganography Work?

Steganography algorithms embed data within a media file without affecting its visible content. The commonly used LSB method hides data in the least significant bits of an image (LSB). For instance, a 24-bit RGB image can have its least significant bits altered slightly without noticeable color changes. In audio files, data is embedded in frequencies that are inaudible to the human ear.

The **Least Significant Bit (LSB)** is the bit in a data unit that has the smallest effect on its overall value. Located on the far right of a binary number, it represents the lowest-value part of that number. In LSB steganography, this bit is modified in digital files (usually an image or audio file) to embed hidden data because such small changes are almost undetectable by human perception.

For example, in an image, each pixel is typically represented by three color components: red, green, and blue (RGB). Each color component is stored in 8 bits (1 byte), resulting in a total of 24 bits for one pixel. By modifying the LSB of each 8-bit color component, we can change the color by a tiny amount, which is visually imperceptible to the human eye.

Here’s a quick example:

- Suppose the red component of a pixel has a binary value of `11101110`.
- If we change the LSB from `0` to `1`, the new value becomes `11101111`.

This small change slightly alters the pixel’s color, but it’s hardly noticeable. By modifying the LSB of many pixels, a significant amount of data can be hidden within the image.


![](https://miro.medium.com/v2/resize:fit:700/1*XI3yGfKYW35GkI1VCXaX6w.jpeg)

LSB

## Steganography vs. Cryptography

While cryptography secures data by encrypting it, steganography hides the existence of the data itself. A cryptographic message can be intercepted and decrypted, but a steganographic message, if unnoticed, is difficult to capture. Combining both techniques offers enhanced security; the message is first encrypted, then embedded within a file, making it nearly undetectable.