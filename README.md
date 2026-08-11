# DevToolKit – Android Developer Toolbox for Termux

DevToolKit is a collection of Python utilities designed to help Android developers and Termux users with everyday tasks. It's safe, beginner-friendly, and requires no root access.

## Features

- **APK Information Viewer** – extract package name, version, size, and SHA256 hash from APK files.
- **Hash Checker** – compute MD5, SHA1, SHA256 of any file and verify against known hashes.
- **JSON Formatter** – validate and pretty-print JSON files.
- **Storage Analyzer** – show disk usage and list largest folders; export reports.
- **System Information** – display Android version, kernel, CPU, RAM, battery, and storage.
- **Network Tester** – check internet, public IP, ping, and DNS lookup.
- **GitHub Helper** – generate README, LICENSE, .gitignore, and project folder structure.

## Installation

1. Install Termux from F-Droid or Google Play.
2. Install dependencies:

```bash
pkg update && pkg upgrade
pkg install python aapt   # aapt is optional but recommended
pip install -r requirements.txt
