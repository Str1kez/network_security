from itertools import cycle
from typing import Literal

from alphabets import en_alphabet, ru_alphabet, digits


def vigenere_cipher(text: str, key: str, is_en: bool, decr: Literal[1, -1] = 1) -> str:
    """
    Описать логику работы с заглавными буквами
    """
    alphabet = en_alphabet if is_en else ru_alphabet
    alphabet_upper = alphabet.upper()
    alphabet_size = len(alphabet)
    key_indexes = cycle(map(alphabet.index, key))
    result = []
    for c, i in zip(text, key_indexes):
        if c.lower() not in alphabet:
            if c.isdigit():
                result.append(digits[(digits.index(c) + i * decr) % 10])
            else:
                result.append(c)
            continue
        if c.isupper():
            result.append(alphabet_upper[(alphabet_upper.index(c) + i * decr) % alphabet_size])
        else:
            result.append(alphabet[(alphabet.index(c) + i * decr) % alphabet_size])
    return ''.join(result)
