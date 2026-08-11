"""
System Information – Android, kernel, CPU, RAM, battery, storage.
"""

import os
import subprocess
import platform

def read_proc_file(path):
    try:
        with open(path, 'r') as f:
            return f.read().strip()
    except:
        return 'N/A'

def get_ram_usage():
    try:
        result = subprocess.run(['free', '-h'], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        if len(lines) >= 2:
            parts = lines[1].split()
            if len(parts) >= 3:
                return {'total': parts[1], 'used': parts[2], 'free': parts[3]}
    except:
        pass
    return None

def get_battery():
    try:
        # Termux API (if installed)
        result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
        if result.returncode == 0:
            import json
            data = json.loads(result.stdout)
            return f"{data.get('percentage', '?')}% (health: {data.get('health', 'unknown')})"
    except:
        pass
    return 'Not available (install termux-api)'

def run():
    print("\n🖥️  System Information")
    print("-" * 40)

    print(f"Android Version: {platform.version()}")
    print(f"Kernel:           {platform.release()}")
    print(f"Device:           {platform.machine()}")

    # CPU info
    cpu_info = read_proc_file('/proc/cpuinfo')
    if cpu_info != 'N/A':
        lines = cpu_info.splitlines()
        model = ''
        cores = 0
        for line in lines:
            if line.startswith('Processor') or line.startswith('model name'):
                model = line.split(':')[1].strip()
            if 'processor' in line:
                cores += 1
        print(f"CPU Model:        {model if model else 'N/A'}")
        print(f"CPU Cores:        {cores if cores else 'N/A'}")
    else:
        print("CPU Info:        N/A")

    # RAM
    ram = get_ram_usage()
    if ram:
        print(f"RAM Total:        {ram['total']}")
        print(f"RAM Used:         {ram['used']}")
        print(f"RAM Free:         {ram['free']}")
    else:
        print("RAM Info:        N/A")

    # Battery
    print(f"Battery:          {get_battery()}")

    # Storage (already covered in storage_analyzer, but we show df)
    try:
        df = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
        print("\nDisk Usage:")
        print(df.stdout)
    except:
        pass
