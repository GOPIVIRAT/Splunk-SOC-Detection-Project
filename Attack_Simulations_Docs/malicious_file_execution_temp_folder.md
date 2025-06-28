# ⚠️ Malicious File Execution from Temp Folder

**Purpose:**  
Detects execution of executables from `Temp` directory — a common malware behavior.

**Simulation Steps:**  
- Copy a `.exe` file to `%TEMP%`
- Execute it manually or via script
- Monitor via Sysmon Event ID 1 and EventCode 4688

**Screenshot:**  

