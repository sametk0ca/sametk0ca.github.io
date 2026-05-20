# Privacy-Preserving Contact Tracing (DP-3T)

- **Source:** [[ka-applied-cryptography]]
- **Tags:** #cryptography #privacy #covid19 #decentralization

## Overview
DP-3T (Decentralized Privacy-Preserving Proximity Tracing) is a protocol designed to automate contact tracing using mobile phones and Bluetooth Low Energy (BLE) while maintaining high user privacy.

## 1. Core Principles
- **Decentralization:** Matching of "beacons" (proximity contacts) happens on the user's phone, not on a central server.
- **Privacy by Design:** No location data (GPS) is used. No central database of "who met whom" is created.
- **Anonymity:** Users broadcast random-looking identifiers that change frequently.

## 2. Cryptographic Mechanism
1. **Key Generation:** Each phone generates a daily symmetric key.
2. **Beacon Generation:** This daily key is used with a PRNG (AES in CTR mode) to produce a sequence of short "beacons" (one every 15 minutes).
3. **Broadcasting:** The phone broadcasts the current beacon over BLE. Nearby phones pick it up and store it locally in a log with metadata (time, signal strength).
4. **Exposure Notification:** When a user tests positive, they upload their *daily keys* for the infectious period to a central server (authenticated by health authorities).
5. **Local Matching:** All phones download the list of infected daily keys from the server, regenerate the beacons, and check their local logs for matches.

## 3. Security and Privacy Benefits
- **Server Privacy:** The server only knows which keys belong to infected people; it has no information about non-infected users or their interactions.
- **Unlinkability:** Since beacons change every 15 minutes, an eavesdropper cannot easily track a user's movements throughout the day.

## 4. Impact
DP-3T became the basis for the **Google-Apple Exposure Notification (GAEN)** framework used in dozens of national COVID-19 apps worldwide.

## Related Concepts
- [[symmetric-primitives]]
- [[key-lifecycle-management]]
- [[mobile-security-basics]]
