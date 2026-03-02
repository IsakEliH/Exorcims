ALPHABET = " abcdefghijklmnopqrstuvwxyz"
REVERSE_ALPHABET = " zyxwvutsrqponmlkjihgfedcba"


def get_index(letter: str, alphabet: str) -> int:
    for index, alpha in enumerate(alphabet):
        if alpha == letter:
            return index

    return 0


def encoding_add(char: str, text: str) -> str:
    splitted: list[str] = text.split()
    if not splitted:
        return char

    if char == " ":
        return text

    last_part: str = splitted[-1]

    if len(last_part) == 5:
        return text + " " + char
    return text + char


def encode(plain_text: str):
    encoded = ""

    for letter in plain_text:
        if letter.isdigit():
            encoded = encoding_add(letter, encoded)
            continue

        index = get_index(letter.lower(), ALPHABET)
        enc_char = ALPHABET[-index]

        encoded = encoding_add(enc_char, encoded)

    return encoded


def decode(ciphered_text: str):
    decoded = ""

    new_ciphered_text: str = "".join(ciphered_text.split())

    for letter in new_ciphered_text:
        if letter.isdigit():
            decoded += letter
            continue

        index = get_index(letter.lower(), REVERSE_ALPHABET)

        decoded += REVERSE_ALPHABET[-index]

    return decoded
