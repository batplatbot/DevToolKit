#!/usr/bin/env python3
"""
DevToolKit - Main Entry Point
A toolbox for Android developers on Termux.
"""

import os
import sys
import subprocess
from tools import (
    apk_info,
    hash_checker,
    json_formatter,
    storage_analyzer,
    system_info,
    network_test,
    github_helper
)

# Colour definitions (ANSI)
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

def print_banner():
    """Display the ASCII banner from assets/banner.txt"""
    try:
        with open('assets/banner.txt', 'r') as f:
            banner = f.read()
        print(f"{COLORS['cyan']}{banner}{COLORS['reset']}")
    except FileNotFoundError:
        # Fallback banner
        print(f"{COLORS['bold']}{COLORS['blue']}")
        print("  ██████  ███████ ██    ██ ██   ██ ██ ████████")
        print("  ██   ██ ██      ██    ██ ██  ██  ██    ██")
        print("  ██   ██ █████   ██    ██ █████   ██    ██")
        print("  ██   ██ ██       ██  ██  ██  ██  ██    ██")
        print("  ██████  ███████   ████   ██   ██ ██    ██")
        print(f"{COLORS['reset']}")

def clear_screen():
    """Clear terminal screen (works on Termux)"""
    os.system('clear' if os.name == 'posix' else 'cls')

def show_menu():
    """Display the main menu"""
    print(f"\n{COLORS['bold']}{COLORS['yellow']}╔════════════════════════════════════╗")
    print(f"║        DevToolKit Main Menu      ║")
    print(f"╚════════════════════════════════════╝{COLORS['reset']}")
    print(f"{COLORS['green']}  1. APK Information Viewer")
    print(f"  2. Hash Checker")
    print(f"  3. JSON Formatter")
    print(f"  4. Storage Analyzer")
    print(f"  5. System Information")
    print(f"  6. Network Tester")
    print(f"  7. GitHub Helper")
    print(f"  0. Exit{COLORS['reset']}")
    print()

def main():
    clear_screen()
    print_banner()
    print(f"{COLORS['bold']}{COLORS['white']}Welcome to DevToolKit – your Android dev toolbox!{COLORS['reset']}")

    while True:
        show_menu()
        try:
            choice = input(f"{COLORS['cyan']}Enter your choice: {COLORS['reset']}").strip()
            if choice == '0':
                print(f"{COLORS['green']}Goodbye! Keep building. 👋{COLORS['reset']}")
                break
            elif choice == '1':
                apk_info.run()
            elif choice == '2':
                hash_checker.run()
            elif choice == '3':
                json_formatter.run()
            elif choice == '4':
                storage_analyzer.run()
            elif choice == '5':
                system_info.run()
            elif choice == '6':
                network_test.run()
            elif choice == '7':
                github_helper.run()
            else:
                print(f"{COLORS['red']}Invalid choice. Please try again.{COLORS['reset']}")
        except KeyboardInterrupt:
            print(f"\n{COLORS['yellow']}Interrupted. Exiting...{COLORS['reset']}")
            break
        except Exception as e:
            print(f"{COLORS['red']}Error: {e}{COLORS['reset']}")

        input(f"\n{COLORS['bold']}Press Enter to continue...{COLORS['reset']}")
        clear_screen()
        print_banner()

if __name__ == "__main__":
    main()
