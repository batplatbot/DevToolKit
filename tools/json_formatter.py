"""
JSON Formatter – pretty-print and validate JSON.
"""

import os
import json

def run():
    print("\n📄 JSON Formatter")
    print("-" * 40)
    filepath = input("Enter JSON file path: ").strip()
    if not filepath or not os.path.isfile(filepath):
        print("File not found.")
        return

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return

    # Format with indentation
    formatted = json.dumps(data, indent=4, sort_keys=True)
    print("\n✅ Formatted JSON:\n")
    print(formatted)

    # Option to save output
    save = input("\nSave formatted output to file? (y/n): ").strip().lower()
    if save == 'y':
        outpath = input("Output file path: ").strip()
        if outpath:
            with open(outpath, 'w') as f:
                f.write(formatted)
            print(f"Saved to {outpath}.")
