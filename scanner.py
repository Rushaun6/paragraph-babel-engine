import random
from babel_engine import decode, number_to_key

KEY_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_key(length=12):
    return "".join(random.choice(KEY_CHARS) for _ in range(length))


def looks_like_sentence(text):

    words = text.split()

    if len(words) < 3:
        return False

    if len(words) > 40:
        return False

    return True


def scan(amount=20):

    print("Scanning random paragraphs...\n")

    found = 0

    while found < amount:

        key = random_key()
        paragraph = decode(key)

        if looks_like_sentence(paragraph):

            print(key, ":", paragraph)
            found += 1


if __name__ == "__main__":
    scan(20)
