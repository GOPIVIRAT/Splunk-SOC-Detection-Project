# 🔁 Persistence via Startup Folder

**Purpose:**  
Detects file drop into Windows startup folder to achieve persistence.

**Simulation Steps:**  
- Drop `.bat` or `.exe` into `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- Monitor file write events or directory access
- Alert on suspicious file drop in that path

**Screenshot:**  

