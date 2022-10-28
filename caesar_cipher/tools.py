from alphabets import digits, en_alphabet, ru_alphabet


def caesar_cipher(text: str, key: int, is_en: bool) -> str:
    old_alphabet = en_alphabet if is_en else ru_alphabet
    size = len(old_alphabet)
    new_alphabet = [old_alphabet[(i + key) % size] for i in range(size)]
    conversion = {old_alphabet[i]: new_alphabet[i] for i in range(size)}
    new_digit = [digits[(i + key) % 10] for i in range(10)]
    conversion_digit = {digits[i]: new_digit[i] for i in range(10)}
    result = []
    for c in text:
        if c.isupper():
            result.append(conversion.get(c.lower(), c).upper())
        elif c.isdigit():
            result.append(conversion_digit.get(c))
        else:
            result.append(conversion.get(c, c))
    return "".join(result)
