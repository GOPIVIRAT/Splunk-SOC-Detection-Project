# 📄 Office Macro Execution via PowerShell

**Purpose:**  
Detects Office macros executing suspicious PowerShell/MSHTA commands.The reason for the rule is we will get different types of emails from different types fo people attackers are used those emails and send the macro thry have their own payload on the file if you open that it will do different types of attacks like scdule task creation and other

**Simulation Steps:**  
- Rule triggered on Sysmon Process Creation or CommandLine
✅ How to Test This Rule in a Lab:
⚠️ Safe Simulation Method:
	1. Open Microsoft Word.
	2. Enable Macros (Developer → Visual Basic → Insert macro).
	3. Paste this simple macro payload:

vb
CopyEdit
Sub AutoOpen()
    Shell "powershell.exe -Command echo HelloFromMacro"
End Sub
	4. Save the document as .docm and reopen it to trigger the macro.
This will spawn powershell.exe from winword.exe, which will trigger the rule.![image](https://github.com/user-attachments/assets/e9c95a20-76ab-4138-aea1-110ab196311d)


**Screenshot:**  
![Image](https://github.com/user-attachments/assets/35541cd3-dba6-4a1b-a4a0-69e3e41c2a5b)

Here i have saved one sample file macro and when i reopend it my rule will be able to detect the attack 

![Image](https://github.com/user-attachments/assets/e5feb8a7-4bcc-4407-ae32-2010f5601c73)
