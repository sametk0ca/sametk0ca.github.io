# Attribute-Based Encryption (ABE)

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #cryptography #access-control #abe

## Overview
Attribute-Based Encryption (ABE) is a type of public-key encryption where the decryption of a ciphertext depends on the attributes of the user and the access policy.

## Key Types

### 1. Key-Policy ABE (KP-ABE)
- **Policy Location:** The policy is embedded in the user's **private key**.
- **Ciphertext:** Encrypted with a set of attributes.
- **Access:** The user can decrypt if the attributes of the ciphertext satisfy the policy in their key.

### 2. Ciphertext-Policy ABE (CP-ABE)
- **Policy Location:** The policy is embedded in the **ciphertext**.
- **User Key:** Associated with a set of user attributes.
- **Access:** Decryption is possible if the user's attributes satisfy the policy in the ciphertext.
- **Significance:** Most useful for cloud storage, as the data owner defines the policy during encryption.

## Role of the Trusted Third Party
A Key Generator (TTP) issues private keys based on a user's attributes or policy. 
- **Limitation:** The TTP has the power to recreate any private key (key escrow).

## Challenges
- **Complexity:** High computational overhead compared to standard symmetric/asymmetric encryption.
- **Efficiency:** Not yet widely feasible for large-scale, highly dynamic environments.

## Related Concepts
- [[abac-and-ucon]]
- [[aaa-fundamental-concepts]]
- [[computational-cryptographic-proofs]]
