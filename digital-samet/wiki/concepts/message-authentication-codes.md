# Message Authentication Codes (MAC)

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #authentication #integrity

## Overview
A Message Authentication Code (MAC) is a deterministic tag generated from a message and a secret key. It provides both integrity and data origin authentication (but not non-repudiation, unlike digital signatures).

## Key Constructions

### 1. HMAC (Hash-based MAC)
Specifically designed for use with Merkle-Damgård hash functions (e.g., MD5, SHA-1, SHA-2) to prevent length extension attacks.
- **Formula:** $HMAC(m, k) = H((k \oplus opad) \| H((k \oplus ipad) \| m))$
- **Efficiency:** Requires two applications of the underlying hash function.

### 2. KMAC (Keccak-based MAC)
The standardized MAC for SHA-3 (Keccak).
- **Benefit:** More efficient than HMAC because SHA-3's sponge construction is not vulnerable to length extension.
- **Operation:** Uses the absorb phase for the padded message and squeezes the desired tag length.

### 3. Block Cipher MACs
Block ciphers can also produce MACs (e.g., CBC-MAC, GMAC).
- **CBC-MAC:** Uses the final ciphertext block as the tag. Secure only for fixed-length messages unless post-processing is applied.
- **GMAC:** The MAC component of the GCM mode of operation, based on universal hashing over a Galois field.

## Security Requirements
The standard security goal for a MAC is **UF-CMA** (Unforgeability under Chosen Message Attack), meaning an adversary cannot create a valid message-tag pair without the key, even with access to a tagging oracle.

## Related Concepts
- [[symmetric-primitives]]
- [[digital-signatures]]
- [[key-derivation-functions]]
