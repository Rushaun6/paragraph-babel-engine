from babel_engine import encode, decode

text = """
Technology continues to change the way people communicate and share ideas.
From simple messages to complex documents, computers allow information
to travel across the world in seconds. Understanding how data can be
encoded and decoded is an important concept in computer science.
"""

encoded, key = encode(text)
decoded = decode(encoded, key)

print("Original:", text)
print("Key:", key)
print("Encoded:", encoded)
print("Decoded:", decoded)

# simple validation test
if decoded.strip() == "" or len(decoded) < 10:
    raise Exception("Decoding failed!")

print("Test passed!")
