# Key Derivation Functions (KDF) & XOFs

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #keys #kdf

## Overview
Key Derivation Functions (KDFs) and Extendable Output Functions (XOFs) are used to derive long (or fixed-length) pseudorandom strings from initial random bits (entropy).

## KDF vs. XOF
- **KDF:** Produces a fixed-length output (usually a key for a symmetric algorithm).
- **XOF:** Produces an arbitrary-length output (used for padding or extending a key).

## Key Construction Approaches

### 1. Block Cipher-based
- **Mechanism:** Uses a block cipher (e.g., AES) in CBC-MAC mode to compress the input into a key, then uses CTR mode to produce output bits.
- **Example:** $k \leftarrow CBC-MAC(m, 0)$ then $o_i \leftarrow Enc(i, k)$.

### 2. Hash-based
- **Merkle-Damgård:** Using multiple hash applications like $o_i \leftarrow H(m \| i)$.
- **Sponge-based:** SHA-3/Keccak is naturally an XOF; one simply inputs the padded message and "squeezes" as many bits as needed.

## Password-based KDFs (PBKDF)
Specialized KDFs designed for low-entropy inputs like passwords or PINs.
- **Design Goal:** Computationally expensive to mitigate brute-force attacks (e.g., PBKDF2, Argon2).
- **Security:** Use salt and many iterations to slow down an adversary.

## Related Concepts
- [[symmetric-primitives]]
- [[message-authentication-codes]]
- [[digital-signatures]]
