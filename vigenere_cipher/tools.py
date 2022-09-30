from itertools import cycle
from typing import Literal

en_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'


class ValidationError(Exception):
    pass


def validate(text: str, key: str, is_en: bool):
    if not text:
        raise ValidationError('Пустой текст')
    if not key:
        raise ValidationError('Пустой ключ')
    if not (text.islower() and key.islower()) and not (text.isupper() and key.isupper()):
        raise ValidationError('Буквы не одного регистра')
    if is_en and not (all(c in en_alphabet for c in text.lower()) and all(c in en_alphabet for c in key.lower())):
        raise ValidationError('Буквы не английские')
    if not is_en and not (all(c in ru_alphabet for c in text.lower()) and all(c in ru_alphabet for c in key.lower())):
        raise ValidationError('Буквы не русские')


def vigenere_cipher(text: str, key: str, is_en: bool, decr: Literal[1, -1] = 1) -> str:
    alphabet = en_alphabet if is_en else ru_alphabet
    alphabet = alphabet.upper() if text.isupper() else alphabet
    alphabet_size = len(alphabet)
    key_indexes = cycle(map(alphabet.index, key))
    return ''.join(alphabet[(alphabet.index(c) + i * decr) % alphabet_size] for c, i in zip(text, key_indexes))
