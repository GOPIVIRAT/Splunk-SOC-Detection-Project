# 🧩 Suspicious Obfuscated PowerShell Execution

**Purpose:**  
Detects encoded, obfuscated, or suspicious PowerShell commands.

**Simulation Steps:**  
- Run a PowerShell command using `-EncodedCommand` or `iex (new-object)`
- Log should capture Sysmon Event ID 1
- Detect via command-line pattern matching

**Screenshot:** 

![Image](https://github.com/user-attachments/assets/3f595a7c-a676-4b50-8a6f-4e9a271b2453)  

