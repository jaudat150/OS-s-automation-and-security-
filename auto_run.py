import os
#To get info about the script
import sys
#Allows interaction with registry
import winreg
#For console behaviour control
import msvcrt

# === CONFIGURATION ===
APP_NAME = "HelloWorldNotifier"  # Name for autorun entry

SCRIPT_PATH = os.path.realpath(sys.argv[0])  # Current script path (gets the path of the current script)

# === CHECK IF ALREADY IN AUTORUN ===
def is_persistent():
    try:
        #we use with to close properly after we are done with the key       
        #0 is always like this (reservered by microsoft)  
        #the key read is telling that we are only reading the key (no editing or else)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ) as key:
            i = 0
            while True:
                name, value, _ = winreg.EnumValue(key, i)
                if name == APP_NAME and value == f'"{SCRIPT_PATH}"':
                    return True
                i += 1
    except WindowsError:
        return False

# === ADD TO AUTORUN ===
def add_persistence():
    if is_persistent():
        print("[✓] Already in autorun!")
        return
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, f'"{SCRIPT_PATH}"')
        print("[+] Added to autorun!")
    except Exception as e:
        print(f"[!] Error adding to autorun: {e}")

# === MAIN FUNCTION ===
def main():
    add_persistence()
    print("Hello World! This script runs at startup now.")

if __name__ == "__main__":
    main()
    #keeps console up until a key is pressed 
    msvcrt.getch() #comment this line if you want the script to run without showing console windows 