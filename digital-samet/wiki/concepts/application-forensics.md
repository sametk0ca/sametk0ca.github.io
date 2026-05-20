# Application Forensics

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #application #browser

## Overview
Application forensics is the process of establishing a data-centric theory of operation for specific software, focusing on causal links between user interaction and data output.

## Case Study: Web Browsers
Browsers provide convergent sources of information about user activity:
- **URL/Search History:** Logs of visited sites and specific user queries.
- **Form Data:** Saved passwords and auto-completing information (often encrypted).
- **Temporary Files:** Chronology of web activities and versions of downloaded objects.
- **Downloaded Files:** Valuable source of activity information (rarely deleted).
- **HTML5 Local Storage:** Persistent state for web applications.
- **Cookies:** Opaque data for tracking or access tokens.

## Storage Formats
- **SQLite Databases:** Most local browser data is stored in SQLite.
- **Vacuuming:** Deleted records often persist in these databases until the database is "vacuumed".

## Analytical Techniques
- Reading documentation/specifications.
- Reverse engineering (code, protocols, data structures).
- Black box differential analysis.
- Licensing code for proprietary structures.

## Related Concepts
- [[main-memory-forensics]]
- [[storage-abstraction-layers]]
- [[data-acquisition-methods]]
