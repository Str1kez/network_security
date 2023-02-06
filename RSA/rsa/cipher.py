from alphabets import digits, en_alphabet, ru_alphabet
from RSA.expmod.tools import fast_bin_pow

custom_alphabet = (
    ru_alphabet
    + ru_alphabet.upper()
    + en_alphabet
    + en_alphabet.upper()
    + digits
    + ' !"#$%&()*+,-–…№./\':;<=>?@[\\]^_{}|\n\t\r'
)
sym_to_code = {s: n for s, n in zip(custom_alphabet, range(len(custom_alphabet)))}
code_to_sym = {sym_to_code[sym]: sym for sym in sym_to_code}


def rsa_cipher(codes: list[int], e: int, n: int) -> list[int]:
    return [fast_bin_pow(c, e, n) for c in codes]


def parse_codes(text: str) -> list[int]:
    return [int(t) for t in text.strip().split()]


def text_to_code(text: str, block_size: int) -> list[int]:
    result = []
    for i in range((len(text) + block_size - 1) // block_size):
        block_result = [f'{sym_to_code[t]:08b}' for t in text[i * block_size : (i + 1) * block_size]]
        result.append(int(''.join(block_result), 2))

    return result


def code_to_text(codes: list[int], block_size: int) -> str:
    result = []
    for c in codes:
        bin_code = clean_code(format(c, f'0{block_size * 8}b'))
        for block in range(len(bin_code) // 8):
            code = int(bin_code[block * 8 : (block + 1) * 8], 2)
            result.append(code_to_sym[code])

    return ''.join(result).replace('\x00', '')


def clean_code(code: str) -> str:
    while code[:8] == '00000000':
        code = code[8:]
    return code
