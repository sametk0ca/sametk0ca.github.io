# Approximate Matching (AM)

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #analysis #similarity

## Overview
Approximate matching is a generic term describing any technique designed to identify similarities between two digital artifacts.

## Key Components
- **Features:** Atomic components (bits, sequences, parsed structures) derived from the artifact.
- **Similarity Function:** Maps two feature sets to a similarity score (increasingly monotonic with matching features).

## Classes of AM Algorithms
1. **Bytewise Matching:** Treats objects as byte sequences (e.g., fuzzy hashing). Works well for plain text, less for compressed data.
2. **Syntactic Matching:** Parses file formats to extract logical features (e.g., splitting a ZIP archive).
3. **Semantic Matching:** Interprets data content (e.g., perceptual hashes for images, natural language processing for text).

## Use Cases
- **Resemblance:** Comparing peers of comparable size to see how closely they are related (e.g., versions of the same file).
- **Containment:** Establishing whether a larger object contains pieces of a smaller one (e.g., embedded objects or network fragments).

## Forensic Applications
- Correlating versioned artifacts.
- Cross-correlating objects with shared components.
- Identifying fragments from bulk captures.

## Related Concepts
- [[hash-based-analysis]]
- [[data-carving]]
- [[forensic-traces]]
