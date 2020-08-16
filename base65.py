# base 65 encoder and decoder algorithm
from string import ascii_lowercase, ascii_uppercase, digits


characters = ascii_uppercase + ascii_lowercase + digits + "+/-"


def encode_base65(id):
    base = len(characters)
    encode = ""
    while id > 0:
        id, idx = divmod(id, base)
        encode = characters[idx] + encode

    return encode


def decode_base65(encoded_string):
    num = 0
    for idx, char in enumerate(encoded_string[::-1]):
        num += (len(characters) ** idx) * characters.index(char)
    return num


assert encode_base65(1000000) == 'Dpso'
assert decode_base65('Dpso') == 1000000

assert encode_base65(1) == 'B'
assert decode_base65('B') == 1
