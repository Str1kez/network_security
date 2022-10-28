from alphabets import en_alphabet, ru_alphabet
from exceptions import ValidationError


def validate(text: str, key: str, is_en: bool):
    if not text:
        raise ValidationError("Пустой текст")
    if key == "":
        raise ValidationError("Пустой ключ")
    if is_en and any(c in ru_alphabet for c in text.lower()):
        raise ValidationError("Буквы не английские")
    if not is_en and any(c in en_alphabet for c in text.lower()):
        raise ValidationError("Буквы не русские")


def caesar_validate(text: str, key: str, is_en: bool):
    validate(text, key, is_en)
    try:
        int(key)
    except ValueError:
        raise ValidationError("Неверная запись ключа")


def vigenere_validate(text: str, key: str, is_en: bool):
    validate(text, key, is_en)
    if not all(c in en_alphabet for c in key if is_en) or not all(c in ru_alphabet for c in key if not is_en):
        raise ValidationError("В ключе могут быть только буквы нижнего регистра")


def xor_validate(source: str, key: str, bin_key: str):
    if not source:
        raise ValidationError("Вы не ввели текст")
    if not key and not bin_key:
        raise ValidationError("Вы не ввели ключ")
    if not all(b in ['0', '1'] for b in bin_key):
        raise ValidationError("Бинарный ключ не является бинарным")
