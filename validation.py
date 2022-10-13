from alphabets import ru_alphabet, en_alphabet
from exceptions import ValidationError


def validate(text: str, key: str, is_en: bool):
    if not text:
        raise ValidationError('Пустой текст')
    if key == '':
        raise ValidationError('Пустой ключ')
    if is_en and any(c in ru_alphabet for c in text.lower()):
        raise ValidationError('Буквы не английские')
    if not is_en and any(c in en_alphabet for c in text.lower()):
        raise ValidationError('Буквы не русские')


def caesar_validate(text: str, key: str, is_en: bool):
    validate(text, key, is_en)
    try:
        int(key)
    except ValueError:
        raise ValidationError('Неверная запись ключа')


def vigenere_validate(text: str, key: str, is_en: bool):
    validate(text, key, is_en)
    if not all(c in en_alphabet for c in key if is_en) or not all(c in ru_alphabet for c in key if not is_en):
        raise ValidationError('В ключе могут быть только буквы нижнего регистра')
