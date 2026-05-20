The purpose of this room is to introduce users to basic cryptography concepts such as:

- Symmetric encryption, such as
- Asymmetric encryption, such as
- Diffie-Hellman Key Exchange
- Hashing
- PKI

Suppose you want to send a message that no one can understand except the intended recipient. How would you do that?


One of the simplest ciphers is the Caesar cipher, used more than 2000 years ago. Caesar Cipher shifts the letter by a fixed number of places to the left or to the right.

![[Pasted image 20260501161830.png]]

![[Pasted image 20260501161836.png]]

quipqiup.com (Decypher website)


# **Symmetric Encryption**

A symmetric encryption algorithm uses the same key for encryption and decryption. Consequently, the communicating parties need to agree on a secret key before being able to exchange any messages.

![[Pasted image 20260501163556.png]]
![[Pasted image 20260501163605.png]]
National Institute of Standard and Technology (NIST) published the Data Encryption Standard (DES) in 1977. DES is a symmetric encryption algorithm that uses a key size of 56 bits. In 1997, a challenge to break a message encrypted using DES was solved. Consequently, it was demonstrated that it had become feasible to use a brute-force search to find the key and break a message encrypted using DES . In 1998, a DES key was broken in 56 hours. These cases indicated that DES could no longer be considered secure.

NIST published the Advanced Encryption Standard (AES) in 2001. Like DES, it is a symmetric encryption algorithm; however, it uses a key size of 128, 192, or 256 bits, and it is still considered secure and in use today. AES repeats the following four transformations multiple times:

1. `SubBytes(state)`: This transformation looks up each byte in a given substitution table (S-box) and substitutes it with the respective value. The `state` is 16 bytes, i.e., 128 bits, saved in a 4 by 4 array.
2. `ShiftRows(state)`: The second row is shifted by one place, the third row is shifted by two places, and the fourth row is shifted by three places. This is shown in the figure below.
3. `MixColumns(state)`: Each column is multiplied by a fixed matrix (4 by 4 array).
4. `AddRoundKey(state)`: A round key is added to the state using the XOR operation.

---
## 🔗 Bağlantılar
- [[TryHackMe Security Engineer Path/index|🎓 TryHackMe: Security Engineer Path]]
- [[index|🏠 Ana İndeks]]
