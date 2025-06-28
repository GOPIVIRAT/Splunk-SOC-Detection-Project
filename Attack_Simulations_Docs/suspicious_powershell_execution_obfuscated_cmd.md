# 🧩 Suspicious Obfuscated PowerShell Execution

**Purpose:**  
Detects encoded, obfuscated, or suspicious PowerShell commands.

**Simulation Steps:**  
- Run a PowerShell command using `-EncodedCommand` or `iex (new-object)`
- Log should capture Sysmon Event ID 1
- Detect via command-line pattern matching

**Screenshot:**  

