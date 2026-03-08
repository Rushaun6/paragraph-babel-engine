from babel_engine import encode, decode

text = """
Technology continues to change the way people communicate and share ideas.
From simple messages to complex documents, computers allow information
to travel across the world in seconds. Understanding how data can be
encoded and decoded is an important concept in computer science.
"""
key = encode(text)
decoded = decode(key)

print("Original:", text)
print("Key:", key)
print("Decoded:", decoded)
