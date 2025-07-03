# 🛡️ Privilege Escalation via Admin Group Addition
# Purpose

This rule helps detect if someone secretly gives themselves admin rights on a system.
Attackers often try to add their user account to the Administrators group to gain full control.

# Why This Rule Is Important

Imagine an attacker gets access to a normal user account. Their next step is usually to make themselves an admin.
This rule helps catch that moment — when a user is added to a privileged group — so we can stop them early.

# Simulation Steps:
On Windows, ran this command to simulate privilege escalation:

net localgroup administrators attacker_user /add
This triggered Event ID 4732, which logs any time a user is added to a security group like "Administrators."
Splunk received the event and matched it using our custom rule.

Splunk Rule Triggered:
[T1068] Privilege Escalation – Admin Group Addition
Triggers when:EventCode is 4732

Target group is Administrators

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/edd62081-fcde-454f-9936-f4d2e511f734)


# Conclusion:
This rule helps detect sneaky privilege escalation attempts by attackers. It’s important for stopping lateral movement and blocking attacker persistence inside the network.
