CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!'"
BASE = len(CHARSET)

KEY_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
KEY_BASE = len(KEY_CHARS)


def normalize(text):
    text = text.lower()
    cleaned = ""

    for char in text:
        if char in CHARSET:
            cleaned += char

    return cleaned


def encode_to_number(text):
    num = 0
    for char in text:
        value = CHARSET.index(char)
        num = num * BASE + value
    return num


def number_to_key(num):
    key = ""
    while num > 0:
        num, rem = divmod(num, KEY_BASE)
        key = KEY_CHARS[rem] + key
    return key


def key_to_number(key):
    num = 0
    for char in key:
        value = KEY_CHARS.index(char)
        num = num * KEY_BASE + value
    return num


def decode_from_number(num):
    text = ""
    while num > 0:
        num, rem = divmod(num, BASE)
        text = CHARSET[rem] + text
    return text


def encode(text):
    text = normalize(text)
    return number_to_key(encode_to_number(text))


def decode(key):
    return decode_from_number(key_to_number(key))
