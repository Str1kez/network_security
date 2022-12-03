import math
from collections import Counter
from itertools import zip_longest

from alphabets import digits, en_alphabet, ru_alphabet
from utils.grouper import grouper
from utils.quantity_analysis import quantity_analysis


def get_index_coincidence(row: tuple[str]) -> float:
    def index_coincidence(count: int, size: int) -> float:
        return count * (count - 1) / size / (size - 1)

    cnt = Counter(row)
    row_size = len(row) - row.count('')
    return sum(index_coincidence(cnt[c], row_size) for c in cnt if c != '')


def get_text_transposed(text: tuple, t: int) -> tuple[tuple[str]]:
    splitted_text = tuple(grouper(text, t, fillvalue=''))
    return tuple(zip(*splitted_text))


def find_key_size(text: tuple) -> int:
    coincidence_dict = {}
    t_list = []
    for t in range(1, min(31, len(text))):
        rows = get_text_transposed(text, t)
        division_index_coincidence = sum(get_index_coincidence(row) for row in rows) / t
        coincidence_dict[t] = division_index_coincidence
    for key, _ in sorted(coincidence_dict.items(), reverse=True, key=lambda x: x[1]):
        t_list.append(key)
    print(coincidence_dict)
    return math.gcd(*t_list[:3])


def vigenere_cipher_hack(raw_text: str, is_en: bool) -> tuple[str, str]:
    alphabet = en_alphabet if is_en else ru_alphabet
    alphabet += digits
    text = tuple(c for c in raw_text.lower() if c in alphabet)
    key_size = find_key_size(text)
    rows = get_text_transposed(text, key_size)
    decrypted_row_list = []
    key = ''
    for row in rows:
        decrypted_row, offset = quantity_analysis("".join(row), is_en)
        key += alphabet[offset]
        decrypted_row_list.append(decrypted_row)
    decrypted_text = "".join("".join(row) for row in zip_longest(*decrypted_row_list, fillvalue=''))
    result = []
    i = 0
    for c in raw_text:
        if c.lower() in alphabet:
            dc = decrypted_text[i]
            if c.isupper():
                result.append(dc.upper())
            else:
                result.append(dc)
            i += 1
        else:
            result.append(c)
    return "".join(result), key
