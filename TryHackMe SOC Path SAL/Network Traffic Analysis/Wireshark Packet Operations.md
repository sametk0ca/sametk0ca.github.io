
## Statistics

This menu provides multiple statistics options ready to investigate to help users see the big picture in terms of the scope of the traffic, available protocols, endpoints and conversations, and some protocol-specific details like DHCP, DNS and HTTP/2. For a security analyst, it is crucial to know how to utilise the statical information. This section provides a quick summary of the processed pcap, which will help analysts create a hypothesis for an investigation. You can use the  **"Statistics"** menu to view all available options

## Display Filter Syntax

This is Wireshark's most powerful feature. It supports 3000 protocols and allows conducting packet-level searches under the protocol breakdown. The official "[Display Filter Reference](https://www.wireshark.org/docs/dfref/)" provides all supported protocols breakdown for filtering.

- **Sample filter to capture port 80 traffic:** `tcp.port == 80`

Wireshark has a built-in option (Display Filter Expression) that stores all supported protocol structures to help analysts create display filters. We will cover the "Display Filter Expression" menu later. Now let's understand the fundamentals of the display filter operations. A quick reference is available under the **"Analyse --> Display Filters"** menu.

![Wireshark - display filters|637](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/aa2ca30ccfff2d7eba16d031f0ab1f38.png)

## Comparison Operators

You can create display filters by using different comparison operators to find the event of interest. The primary operators are shown in the table below.

|   |   |   |   |
|---|---|---|---|
|**English**|**C-Like**|**Description**|**Example**|
|eq|==|Equal|`ip.src == 10.10.10.100`|
|ne|!=|Not equal|`ip.src != 10.10.10.100`|
|gt|>|Greater than|`ip.ttl > 250`|
|lt|<|Less Than|`ip.ttl < 10`|
|ge|>=|Greater than or equal to|`ip.ttl >= 0xFA`|
|le|<=|Less than or equal to|`ip.ttl <= 0xA`|

**Note:** Wireshark supports decimal and hexadecimal values in filtering. You can use any format you want according to the search you will conduct.

## Logical Expressions

Wireshark supports boolean syntax. You can create display filters by using logical operators as well.

|   |   |   |   |
|---|---|---|---|
|**English**|**C-Like**|**Description**|**Example**|
|and|&&|Logical AND|`(ip.src == 10.10.10.100) AND (ip.src == 10.10.10.111)`|
|or|\||Logical OR|`(ip.src == 10.10.10.100) OR (ip.src == 10.10.10.111)`|
|not|!|Logical NOT|`!(ip.src == 10.10.10.222)`<br><br>**Note:** Usage of `!=value` is deprecated; using it could provide inconsistent results. Using the `!(value)` style is suggested for more consistent results.|

## Packet Filter Toolbar

The filter toolbar is where you create and apply your display filters. It is a smart toolbar that helps you create valid display filters with ease. Before starting to filter packets, here are a few tips:

- Packet filters are defined in lowercase.
- Packet filters have an autocomplete feature to break down protocol details, and each detail is represented by a "dot".
- Packet filters have a three-colour representation explained below.

|   |   |
|---|---|
|**Green**|Valid filter|
|**Red**|Invalid filter|
|**Yellow**|Warning filter. This filter works, but it is unreliable, and it is suggested to change it with a valid filter.|

![Wireshark - filter colours](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/98be05db82a2b7a2fd449c2155512f87.png)

Filter toolbar features are shown below.

![Wireshark - toolbar features](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/b929ceb69199b99071fa95ce11d8ca44.png)  



## Filter: "contains"

Search a value inside packets. It is case-sensitive and provides similar functionality to the "Find" option by focusing on a specific field.

`http.server contains "Apache"`

## Filter: "matches"

Search a pattern of a regular expression. It is case insensitive, and complex queries have a margin of error.

`http.host matches "\.(php|html)"`

## Filter: "in"

Search a value or field inside of a specific scope/range.

`tcp.port in {80 443 8080}`http.server matches "Microsoft-IIS/7\.5"

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
