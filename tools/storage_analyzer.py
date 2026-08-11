"""
Storage Analyzer – show disk usage and largest folders.
"""

import os
import subprocess
from datetime import datetime

def get_storage_info():
    """Get total, used, free space using `df -h /`."""
    try:
        result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        if len(lines) >= 2:
            parts = lines[1].split()
            if len(parts) >= 4:
                return {
                    'total': parts[1],
                    'used': parts[2],
                    'free': parts[3],
                    'percent': parts[4] if len(parts) > 4 else 'N/A'
                }
    except:
        pass
    return None

def find_largest_folders(root='.', top_n=10):
    """Find largest subdirectories (simple recursive size)."""
    # Using `du` command for speed
    try:
        cmd = f"du -b {root} | sort -nr | head -{top_n}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.splitlines()
            folders = []
            for line in lines:
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    size = int(parts[0])
                    name = parts[1]
                    folders.append((name, size))
            return folders
    except:
        pass
    return []

def run():
    print("\n💾 Storage Analyzer")
    print("-" * 40)

    # Show general storage
    info = get_storage_info()
    if info:
        print(f"Total:   {info['total']}")
        print(f"Used:    {info['used']} ({info['percent']})")
        print(f"Free:    {info['free']}")
    else:
        print("Could not retrieve storage info.")

    # Find largest folders
    print("\n📁 Largest folders (top 10):")
    root = input("Enter directory to scan (default: /sdcard): ").strip() or '/sdcard'
    if not os.path.isdir(root):
        print("Invalid directory.")
        return

    folders = find_largest_folders(root, 10)
    if folders:
        for name, size in folders:
            print(f"{name:60} {size/1024/1024:.2f} MB")
    else:
        print("Could not scan folders (permission or no du command).")

    # Export report
    export = input("\nExport report to file? (y/n): ").strip().lower()
    if export == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/storage_report_{timestamp}.txt"
        os.makedirs('reports', exist_ok=True)
        with open(filename, 'w') as f:
            f.write("Storage Report\n")
            f.write("==============\n\n")
            if info:
                f.write(f"Total: {info['total']}\nUsed: {info['used']} ({info['percent']})\nFree: {info['free']}\n\n")
            f.write("Largest folders:\n")
            for name, size in folders:
                f.write(f"{name}  {size/1024/1024:.2f} MB\n")
        print(f"Report saved to {filename}")
