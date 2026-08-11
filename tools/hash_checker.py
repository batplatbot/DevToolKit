"""
Hash Checker – compute MD5, SHA1, SHA256 of a file.
"""

import os
import hashlib

def compute_hashes(filepath):
    """Return a dict with MD5, SHA1, SHA256 hex digests."""
    if not os.path.isfile(filepath):
        return None
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    return {
        'md5': md5.hexdigest(),
        'sha1': sha1.hexdigest(),
        'sha256': sha256.hexdigest()
    }

def run():
    print("\n🔐 Hash Checker")
    print("-" * 40)
    path = input("Enter file path: ").strip()
    if not path:
        print("No file specified.")
        return
    hashes = compute_hashes(path)
    if hashes is None:
        print("File not found.")
        return
    print(f"MD5:    {hashes['md5']}")
    print(f"SHA1:   {hashes['sha1']}")
    print(f"SHA256: {hashes['sha256']}")

    # Option to verify against a known hash
    verify = input("\nDo you want to verify against a known hash? (y/n): ").strip().lower()
    if verify == 'y':
        known = input("Enter the hash (any format): ").strip()
        if known:
            found = False
            for algo, h in hashes.items():
                if h == known:
                    print(f"✅ Matches {algo.upper()}!")
                    found = True
                    break
            if not found:
                print("❌ No match.")
