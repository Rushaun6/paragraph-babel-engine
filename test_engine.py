from babel_engine import encode, decode

text = """
Technology continues to change the way people communicate and share ideas.
From simple messages to complex documents, computers allow information
to travel across the world in seconds. Understanding how data can be
encoded and decoded is an important concept in computer science.
"""

# encode returns a single key string in the current engine
key = encode(text)

# decode takes that key and returns the (normalized) text
decoded = decode(key)

print("Original:", text)
print("Key:", key)
print("Decoded:", decoded)

# simple validation
if decoded.strip() == "" or len(decoded) < 10:
    raise Exception("Decoding failed!")

print("Test passed!")
