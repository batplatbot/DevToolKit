"""
APK Information Viewer
Requires 'aapt' (Android Asset Packaging Tool) – install via `pkg install aapt`.
"""

import os
import subprocess
import hashlib

def get_apk_info(apk_path):
    """Extract package name, file size, and SHA256 hash from an APK."""
    info = {}
    if not os.path.isfile(apk_path):
        return None

    # File size
    info['size'] = os.path.getsize(apk_path)

    # SHA256 hash
    sha256 = hashlib.sha256()
    with open(apk_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    info['sha256'] = sha256.hexdigest()

    # Package name via aapt
    try:
        result = subprocess.run(
            ['aapt', 'dump', 'badging', apk_path],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith('package:'):
                    # Extract name and version
                    parts = line.split()
                    for part in parts:
                        if part.startswith("name='"):
                            info['package'] = part.split("'")[1]
                        elif part.startswith("versionName='"):
                            info['version'] = part.split("'")[1]
                    break
        else:
            info['package'] = 'Unknown (aapt failed)'
            info['version'] = 'Unknown'
    except FileNotFoundError:
        info['package'] = 'aapt not installed'
        info['version'] = 'N/A'

    return info

def run():
    """Main entry point for APK info tool."""
    print("\n📱 APK Information Viewer")
    print("-" * 40)
    apk_path = input("Enter path to APK file: ").strip()
    if not apk_path:
        print("No path entered.")
        return

    info = get_apk_info(apk_path)
    if info is None:
        print("File not found or invalid.")
        return

    print(f"Package:   {info.get('package', 'N/A')}")
    print(f"Version:   {info.get('version', 'N/A')}")
    print(f"Size:      {info['size']} bytes ({info['size']/1024:.2f} KB)")
    print(f"SHA256:    {info['sha256']}")
