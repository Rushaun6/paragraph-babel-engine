import sys
from babel_engine import decode

if len(sys.argv) < 3:
    print("Usage: python search.py <word> <key>")
    sys.exit()

word = sys.argv[1].lower()
key = sys.argv[2]

decoded = decode(key)

count = decoded.count(word)

if count > 0:
    print(f"Word found {count} time(s)!")
else:
    print("Word not found.")

print("\nDecoded text preview:")
print(decoded[:200])
