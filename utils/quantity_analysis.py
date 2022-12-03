from collections import Counter

from alphabets import digits, en_alphabet, ru_alphabet


def quantity_analysis(text: str, is_en: bool) -> tuple[str, int]:
    if is_en:
        static_c = "e"
        alphabet = en_alphabet
    else:
        static_c = "о"
        alphabet = ru_alphabet
    alphabet += digits
    cnt = Counter(c for c in text.lower() if c in alphabet)
    most_common_letter = cnt.most_common(1)[0][0]
    # fmt: off
    offset = (alphabet.index(most_common_letter) - alphabet.index(static_c)) % len(alphabet)
    # fmt: on
    size = len(alphabet)
    new_alphabet = [alphabet[(i - offset) % size] for i in range(size)]
    conversion = {alphabet[i]: new_alphabet[i] for i in range(size)}
    result = []
    for c in text:
        if c.isupper():
            result.append(conversion.get(c.lower(), c).upper())
        else:
            result.append(conversion.get(c, c))
    return "".join(result), offset
