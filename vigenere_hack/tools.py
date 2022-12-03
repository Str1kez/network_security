import math
from collections import Counter
from itertools import zip_longest

from alphabets import en_alphabet, ru_alphabet
from caesar_hack.tools import caesar_cipher_hack
from utils.grouper import grouper


def get_index_coincidence(row: tuple[str]) -> float:
    def index_coincidence(count: int, size: int) -> float:
        return count * (count - 1) / size / (size - 1)

    row_size = len(row)
    cnt = Counter(row)
    return sum(index_coincidence(cnt[c], row_size) for c in cnt)


def get_text_transposed(text: tuple, t: int) -> tuple[str]:
    splitted_text = tuple(grouper(text, t, fillvalue=''))
    return tuple(zip(*splitted_text))


def find_key_size(text: tuple) -> int:
    coincidence_dict = {}
    t_list = []
    for t in range(1, 30):
        rows = get_text_transposed(text, t)
        division_index_coincidence = sum(get_index_coincidence(row) for row in rows) / t
        coincidence_dict[t] = division_index_coincidence
    for key, _ in sorted(coincidence_dict.items(), reverse=True, key=lambda x: x[1]):
        t_list.append(key)
    return math.gcd(*t_list[:5])


def testing(text: str, alphabet_size: int) -> int:
    text_size = len(text)
    extremum = float("-inf")
    max_index = 0
    for i in range(1, min(text_size, alphabet_size)):
        text_shift = text[i:] + text[:i]
        coincidence = sum(t == ts for t, ts in zip(text, text_shift)) / text_size
        if extremum < coincidence:
            max_index = i
        extremum = max(extremum, coincidence)
    return max_index


def vigenere_cipher_hack(raw_text: str, is_en: bool) -> tuple[str, str]:
    """
    TODO: Надо сделать правильное нахождение ключа и подбор сдвигов
    """
    alphabet = en_alphabet if is_en else ru_alphabet
    text = tuple(c for c in raw_text.lower() if c in alphabet)
    key_size = find_key_size(text)
    rows = get_text_transposed(text, key_size)
    decrypted_row_list = []
    key = ''
    for row in rows:
        decrypted_row, offset = caesar_cipher_hack("".join(row), is_en)
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
    # return row_after_quantity_analysis


text = """влцдутжбюцхъяррмшбрхцэооэцгбрьцмйфктъъюьмшэсяцпунуящэйтаьэдкцибр
ьцгбрпачкъуцпъбьсэгкцъгуущарцёэвърюуоюэкааэбрняфукабъарпяъафкъиьжяффнйо
яфывбнэнфуюгбрьсшьжэтбэёчюъюръегофкбьчябашвёэуъъюаднчжчужцёэвлрнчулб
юпцуруньъшсэюъзкцхъяррнрювяспэмасчкпэужьжыатуфуярюравртубурьпэщлафоуф
бюацмнубсюкйтаьэдйюнооэгюожбгкбрънцэпотчмёодзцвбцшщвщепчдчдръюьскасэг
ъппэгюкдойрсрэвоопчщшоказръббнэугнялёкьсрбёуыэбдэулбюасшоуэтъшкрсдугэфл
бубуъчнчтртпэгюкиугюэмэгюккъъпэгяапуфуэзьрадзьжчюрмфцхраююанчёчюъыхьъ
цомэфъцпоирькнщпэтэузуябащущбаыэйчдфрпэцъьрьцъцпоилуфэдцойэдятррачкубу
фнйтаьэдкцкрннцюабугюуубурьпйюэъжтгюркующоъуфъэгясуоичщщчдцсфырэдщэ
ъуяфшёчцюйрщвяхвмкршрпгюопэуцчйтаьэдкцибрьцыяжтюрбуэтэбдуящэубъибрюв
ъежагибрбагбрымпуноцшяжцечкфодщоъчжшйуъцхчщвуэбдлдъэгясуахзцэбдэулькнъ
щбжяцэьрёдъьвювлрнуяфуоухфекьгцчччгэъжтанопчынажпачкъуъмэнкйрэфщэъьбуд
эндадъярьеюэлэтчоубъцэфэвлнёэгфдсэвэёкбсчоукгаутэыпуббцчкпэгючсаъбэнэфърк
ацхёваетуфяепьрювържадфёжбьфутощоявьъгупчршуитеачйчирамчюфчоуяюонкяжы
кгсцбрясшчйотъъжрсщчл"""
# with open("tests/ru_encrypted_vigenere.txt") as f:
    # text = f.read()
print(vigenere_cipher_hack(text, False))
# print(testing())
