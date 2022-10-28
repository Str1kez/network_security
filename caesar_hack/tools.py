from collections import Counter

from alphabets import en_alphabet, ru_alphabet
from caesar_cipher.tools import caesar_cipher


def caesar_cipher_hack(text: str, is_en: bool) -> tuple[str, int]:
    if is_en:
        static_c = "e"
        alphabet = en_alphabet
    else:
        static_c = "о"
        alphabet = ru_alphabet
    # if text.isupper():
    #     alphabet = alphabet.upper()
    #     static_c = static_c.upper()

    cnt = Counter((c for c in text.lower() if c in alphabet))
    most_common_letter = cnt.most_common(1)[0][0]
    # fmt: off
    offset = (alphabet.index(most_common_letter) - alphabet.index(static_c)) % len(alphabet)
    # fmt: on
    return caesar_cipher(text, -offset, is_en), offset
