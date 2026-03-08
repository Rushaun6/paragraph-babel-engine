from babel_engine import encode, decode, key_to_number, number_to_key

def explore(text, range_size=20):

    key = encode(text)
    number = key_to_number(key)

    print("Original text:", text)
    print("Key:", key)
    print("\nNearby paragraphs:\n")

    for i in range(-range_size, range_size + 1):

        new_number = number + i

        if new_number < 0:
            continue

        new_key = number_to_key(new_number)
        paragraph = decode(new_key)

        print(new_key, ":", paragraph)


explore("do dogs have ears")
