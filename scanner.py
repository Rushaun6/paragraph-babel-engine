import sys
from babel_engine import decode

if len(sys.argv) < 2:
    print("Usage: python scanner.py <key>")
    sys.exit()

key = sys.argv[1]

decoded = decode(key)

print("Decoded text:")
print(decoded)
