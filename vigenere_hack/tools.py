from collections import Counter
from pprint import pprint

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
    splitted_text = tuple(grouper(text, t, fillvalue='y'))
    return tuple(zip(*splitted_text))


def find_key_size(text: tuple) -> int:
    extremum = float("-inf")
    for t in range(2, len(text) // 2):
        rows = get_text_transposed(text, t)
        mean_index_coincidence = sum(get_index_coincidence(row) for row in rows) / t
        if extremum > mean_index_coincidence:
            return t - 1
        extremum = max(extremum, mean_index_coincidence)


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


def vigenere_cipher_hack(raw_text: str, is_en: bool) -> tuple[str, int]:
    """
    TODO: Надо сделать правильное нахождение ключа и подбор сдвигов
    """
    alphabet = en_alphabet if is_en else ru_alphabet
    text = tuple(c for c in raw_text.lower() if c in alphabet)
    key_size = testing("".join(text), len(alphabet))
    # key_size = find_key_size(text)
    rows = get_text_transposed(text, 6)
    print("".join(rows[0]))
    row_after_quantity_analysis = [caesar_cipher_hack("".join(row), is_en)[0] for row in rows]
    print("".join(row_after_quantity_analysis[0]))
    return "".join("".join(t) for t in zip(*row_after_quantity_analysis))
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
with open("tests/ru_encrypted_vigenere.txt") as f:
    text = f.read()
    pprint(vigenere_cipher_hack(text, False))
# print(testing())
