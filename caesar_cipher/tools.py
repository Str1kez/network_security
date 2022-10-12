en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
digit = '0123456789'
# en_alphabet_with_digit = en_alphabet + digit
# ru_alphabet_with_digit = ru_alphabet + digit


class ValidationError(Exception):
    pass


def validate(text: str, key: str, is_en: bool):
    if not text:
        raise ValidationError('Пустой текст')
    if not key:
        raise ValidationError('Пустой ключ')
    if is_en and (any(c in ru_alphabet for c in text.lower()) or any(c in ru_alphabet.upper() for c in text.upper())):
        raise ValidationError('Буквы не английские')
    if not is_en and (any(c in en_alphabet for c in text.lower()) or any(c in en_alphabet.upper() for c in text.upper())):
        raise ValidationError('Буквы не русские')
    try:
        int(key)
    except ValueError:
        raise ValidationError('Неверная запись ключа')


def caesar_cipher(text: str, key: int, is_en: bool) -> str:
    old_alphabet = en_alphabet if is_en else ru_alphabet
    size = len(old_alphabet)
    new_alphabet = [old_alphabet[(i + key) % size] for i in range(size)]
    conversion = {old_alphabet[i]: new_alphabet[i] for i in range(size)}
    new_digit = [digit[(i + key) % 10] for i in range(10)]
    conversion_digit = {digit[i]: new_digit[i] for i in range(10)}
    result = []
    for c in text:
        if c.isupper():
            result.append(conversion.get(c.lower(), c).upper())
        elif c.isdigit():
            result.append(conversion_digit.get(c))
        else:
            result.append(conversion.get(c, c))
    return ''.join(result)
