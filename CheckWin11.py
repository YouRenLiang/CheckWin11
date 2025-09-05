import platform
import psutil
import os
import socket
import subprocess
import ctypes
import wmi

def get_cpu_name():
    try:
        c = wmi.WMI()
        cpu_list = c.Win32_Processor()
        if cpu_list:
            return cpu_list[0].Name.strip()
        else:
            return "Unknown CPU"
    except:
        return "Unknown CPU"

def check_ram():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    return ram_gb >= 4

def check_disk():
    disk_gb = psutil.disk_usage("C:\\").total / (1024 ** 3)
    return disk_gb >= 64

def check_tpm():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Get-WmiObject -Namespace Root\\CIMv2\\Security\\MicrosoftTpm -Class Win32_Tpm"],
            capture_output=True, text=True
        )
        return "SpecVersion" in result.stdout and "2.0" in result.stdout
    except:
        return False

def check_secureboot():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Confirm-SecureBootUEFI"],
            capture_output=True, text=True
        )
        return "True" in result.stdout
    except:
        return False

def show_message(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)

if __name__ == "__main__":
    hostname = socket.gethostname()
    cpu_name = get_cpu_name()

    ok_ram = check_ram()
    ok_disk = check_disk()
    ok_tpm = check_tpm()
    ok_sb = check_secureboot()

    if all([ok_ram, ok_disk, ok_tpm]):
        conclusion = f"This computer {hostname}\nCPU: {cpu_name} \nother conditions meets Windows 11 requirements."
    else:
        conclusion = f"This computer {hostname} does not meet Windows 11 requirements."

    show_message("Windows 11 Compatibility Check", conclusion)
