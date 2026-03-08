from babel_engine import encode, decode

text = "dogs have ears"

key = encode(text)
decoded = decode(key)

print("Original:", text)
print("Key:", key)
print("Decoded:", decoded)
