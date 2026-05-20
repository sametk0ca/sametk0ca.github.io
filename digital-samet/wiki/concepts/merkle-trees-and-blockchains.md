# Merkle Trees & Blockchains

- **Source:** [[ka-cryptography]]
- **Tags:** #cryptography #hash-trees #blockchain #integrity

## Overview
Merkle Trees and Blockchains are structures used to provide data integrity and an unalterable history of operations (immutability).

## 1. Merkle Trees (Hash-Trees)
A hierarchical tree structure for data verification:
- **Leaf Nodes:** Contain individual data blocks.
- **Internal Nodes:** Contain the hash of their child nodes.
- **Root Node:** A single published hash (Merkle root) representing all the data in the tree.
- **Efficiency:** Verifying a single data block requires a path of hashes (Merkle proof) that is logarithmic $O(\log n)$ to the number of leaves.
- **Usage:** Version control (Git), backup systems, and verifying transaction sets in blocks.

## 2. Blockchains
A linear data structure providing an open distributed ledger:
- **Operation:** Each block in the chain contains data items and the hash of the previous block's header.
- **Security Goal:** If the head of the chain is trusted, all previous items are immutable because changing one item would change all subsequent hashes.
- **Key Properties:**
    - **Immutability:** Previous data items cannot be altered without changing all following links.
    - **Ordering:** Preserves the sequence of transactions/events.
- **Usage:** Cryptocurrencies (Bitcoin), smart contracts, and secure auditing logs.

## Related Concepts
- [[symmetric-primitives]] (Hash functions)
- [[cia-triad]] (Integrity)
- [[digital-signatures]]
