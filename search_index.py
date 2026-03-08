# search_index.py
import sys
from babel_engine import decode

if len(sys.argv) < 2:
    print("Usage: python search_index.py <word> [keys_file]")
    sys.exit(1)

word = sys.argv[1].lower()
keys_file = sys.argv[2] if len(sys.argv) > 2 else "database.txt"

try:
    with open(keys_file, "r") as f:
        keys = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Keys file not found:", keys_file)
    sys.exit(1)

found = 0
for i, k in enumerate(keys, start=1):
    decoded = decode(k)
    if word in decoded:
        print(f"\nFound in entry {i}: {k}")
        print("Preview:", decoded[:200])
        found += 1

if found == 0:
    print("No matches found.")
else:
    print(f"\nTotal matches: {found}")
