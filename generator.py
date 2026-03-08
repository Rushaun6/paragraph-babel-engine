import random
import string
import time

def generate_code():
    length = random.randint(16, 24)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

file_name = "database.txt"

print("Auto code generator started...")

while True:
    code = generate_code()

    with open(file_name, "a") as f:
        f.write(code + "\n")

    print("Added:", code)

    time.sleep(0.05)  # controls speed (lower = faster)
