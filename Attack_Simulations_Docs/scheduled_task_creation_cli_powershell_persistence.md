# ⚠️ scheduled_task_creation_cli_powershell_persistence

**Purpose:**  
Detects execution of executables from `Temp` directory — a common malware behavior.

**Simulation Steps:**  
- Copy a `.exe` file to `%TEMP%`
- Execute it manually or via script
- Monitor via Sysmon Event ID 1 and EventCode 4688

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/db082135-81a2-4d85-9fe1-8b105100b9bf) 

