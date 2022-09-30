en_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'


class ValidationError(Exception):
    pass


def validate(text: str, key: str, is_en: bool):
    if not text:
        raise ValidationError('Пустой текст')
    if not key:
        raise ValidationError('Пустой ключ')
    if not text.islower() and not text.isupper():
        raise ValidationError('Буквы не одного регистра')
    if is_en and not all(c in en_alphabet for c in text.lower()):
        raise ValidationError('Буквы не английские')
    if not is_en and not all(c in ru_alphabet for c in text.lower()):
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
    return ''.join(conversion[c] for c in text)
