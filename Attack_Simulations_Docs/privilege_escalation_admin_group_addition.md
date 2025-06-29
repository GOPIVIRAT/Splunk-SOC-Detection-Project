# 🛡️ Privilege Escalation via Admin Group Addition

**Purpose:**  
Detects unauthorized user being added to Administrator group.

**Simulation Steps:**  
- Add a low-privileged user to local admins (`net localgroup`)
- Monitor Event ID 4732 in Security log
- Verify detection alert triggers

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/edd62081-fcde-454f-9936-f4d2e511f734)
