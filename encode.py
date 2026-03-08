# encode.py
import sys
from babel_engine import encode

if len(sys.argv) < 2:
    print('Usage: python encode.py "your paragraph here"')
    sys.exit(1)

text = " ".join(sys.argv[1:])
key = encode(text)
print(key)
