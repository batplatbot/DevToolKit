"""
Network Tester – check internet, public IP, ping, DNS.
"""

import subprocess
import socket
import requests

def check_internet():
    """Check connectivity by pinging Google DNS."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except:
        pass
    return 'N/A'

def ping_host(host):
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, timeout=10)
        return result.stdout
    except:
        return 'Ping failed.'

def dns_lookup(domain):
    try:
        ips = socket.gethostbyname_ex(domain)
        return ips[2]  # list of IPs
    except:
        return None

def run():
    print("\n🌐 Network Tester")
    print("-" * 40)

    # Internet connectivity
    online = check_internet()
    print(f"Internet: {'✅ Connected' if online else '❌ Disconnected'}")

    # Public IP
    if online:
        ip = get_public_ip()
        print(f"Public IP: {ip}")

    # Ping test
    host = input("\nEnter host to ping (default: google.com): ").strip() or 'google.com'
    print(f"\nPinging {host}...")
    print(ping_host(host))

    # DNS lookup
    domain = input("\nEnter domain for DNS lookup (default: google.com): ").strip() or 'google.com'
    ips = dns_lookup(domain)
    if ips:
        print(f"IP addresses for {domain}:")
        for ip in ips:
            print(f"  {ip}")
    else:
        print("DNS lookup failed.")
