# OS-s-automation-and-security-

> A practical collection of automation scripts with a focus on system security, persistence, monitoring, and defensive programming.

This repository contains tools and examples that demonstrate **system automation** and **security concepts**, starting with a simple Python script that adds itself to Windows startup (persistence mechanism). Use responsibly and ethically.

## 🚀 Initial Script: Auto-Run at Startup (Persistence)

The first script in this repo demonstrates how a program can **persist across reboots** by adding itself to the Windows Registry (`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`).

### 🔍 Features
- Checks if already in autorun.
- Adds itself to Windows startup if not present.
- Uses safe registry access with proper error handling.
- Cross-compatible path resolution via `os.path.realpath`.

### ⚠️ Warning
This mimics behavior used by malware. **Use only for educational or ethical purposes** (e.g., learning security, creating legitimate startup utilities).

### 📦 Requirements
- Python 3.x
- Windows OS (uses `winreg` and `msvcrt`)
- `os`, `sys`, `winreg`, `msvcrt` (standard libraries)

### ▶️ How to Run
```bash
python hello_world_persistence.py

### After running:

Restart your computer.
You should see the message appear on login.
Press any key to close the console window (remove msvcrt.getch() if silent execution is desired).
