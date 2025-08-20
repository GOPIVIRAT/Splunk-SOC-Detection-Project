# 🔐 Failed Login Attempt

**Purpose:**  
Detects repeated failed login attempts (Event ID 4625) indicating possible brute force.

**Simulation Steps:**  
- Attempt login with wrong password 5+ times using the same account 
- Monitor Windows Security logs for Event ID 4625
- Validate trigger on Splunk
-This is the simple failed login attempt from insider threats someone access you laptop and tried multiple passwords or kind of brute force


**Screenshot:**  
My rule will be able to detect this attack here i have set the time for 30 days if you change the time it will give alert like someone tried password 5 times we will be able to see here

![Image](https://github.com/user-attachments/assets/eba15de0-384a-4f3b-9047-5ba9ec3e32cc)
