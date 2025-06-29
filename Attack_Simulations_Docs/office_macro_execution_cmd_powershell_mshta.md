# 📄 Office Macro Execution via PowerShell

**Purpose:**  
Detects Office macros executing suspicious PowerShell/MSHTA commands.

**Simulation Steps:**  
- Open malicious Word/Excel file with embedded macro
- Macro runs PowerShell/MSHTA to drop/connect
- Rule triggered on Sysmon Process Creation or CommandLine

**Screenshot:**  

![Image](https://github.com/user-attachments/assets/e5feb8a7-4bcc-4407-ae32-2010f5601c73)
