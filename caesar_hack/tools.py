from collections import Counter

from caesar_cipher.tools import caesar_cipher

en_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'


class ValidationError(Exception):
    pass


def validate(text: str, is_en: bool):
    if not text:
        raise ValidationError('Пустой текст')
    if not text.islower() and not text.isupper():
        raise ValidationError('Буквы не одного регистра')
    if is_en and not all(c in en_alphabet for c in text.lower()):
        raise ValidationError('Буквы не английские')
    if not is_en and not all(c in ru_alphabet for c in text.lower()):
        raise ValidationError('Буквы не русские')


def caesar_cipher_hack(text: str, is_en: bool) -> tuple[str, int]:
    if is_en:
        static_c = 'e'
        alphabet = en_alphabet
    else:
        static_c = 'о'
        alphabet = ru_alphabet
    if text.isupper():
        alphabet = alphabet.upper()
        static_c = static_c.upper()

    cnt = Counter(text)
    most_common_letter = cnt.most_common(1)[0][0]
    offset = (alphabet.index(most_common_letter) - alphabet.index(static_c)) % len(alphabet)

    return caesar_cipher(text, -offset, is_en), offset
