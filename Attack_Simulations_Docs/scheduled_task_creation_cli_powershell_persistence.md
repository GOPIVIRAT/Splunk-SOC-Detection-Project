# ⚠️ scheduled_task_creation_cli_powershell_persistence

# 🔍 Purpose:
This rule detects when an attacker tries to maintain persistence by creating a scheduled task using the command line. This is a common way to make malicious programs run automatically after reboot.

# 💡 Why This Rule is Important:
Attackers often want their tools or malware to stay active even after a system restarts. One of the easiest ways to do that is by creating scheduled tasks using commands like schtasks.
This rule helps us catch those attempts — especially when they come through the CLI.

# 🧪 Simulation Steps:

Ran the following command on Windows to simulate a scheduled task creation:

schtasks /create /tn "Updater" /tr "malware.exe" /sc minute /mo 1
This command schedules malware.exe to run every minute.

It generates Windows Event ID 4698,Process Creation 1 which logs new task creations.

Splunk ingests this event and the rule checks for task creation via CLI.


# 🔍 Splunk Rule Triggered:

[T1053] Scheduled Task Creation via CLI – Persistence Attempt

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/db082135-81a2-4d85-9fe1-8b105100b9bf) 



# ✅ Conclusion:
This rule helps detect when someone creates a scheduled task via command line, which is often used by attackers to ensure their malicious tools stay persistent on the system.

