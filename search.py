import sys
from babel_engine import decode

if len(sys.argv) < 3:
    print("Usage: python search.py <word> <key>")
    sys.exit()

word = sys.argv[1].lower()
key = sys.argv[2]

decoded = decode(key)

if word in decoded:
    print("Word found!")
else:
    print("Word not found.")

print("\nDecoded text preview:")
print(decoded[:200])
