import winreg
#to list all regKeys
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
try:
    i = 0
    while True:
        name, value, _ = winreg.EnumValue(key, i)
        
        print(f"{i+1}- {name}: {value}\n\n")
        i += 1
except WindowsError:
    pass  # No more values
winreg.CloseKey(key)