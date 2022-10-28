def text_in_binary(text):
    return ''.join("{0:016b}".format(ord(c)) for c in text)


def encode(bin_text: str, mode: str = None) -> str:
    result = ''.join(chr(int(bin_text[i : i + 16], 2)) for i in range(0, len(bin_text), 16))
    if mode:
        return result.encode(mode)
    return result.encode()


def decode(bin_text: str, mode: str = None) -> str:
    result = encode(bin_text, mode)
    if mode:
        return result.decode(mode)
    return result.decode()


def xor(bin_txt: str, bin_key: str) -> str:
    bin_txt_size = len(bin_txt)
    bin_key_size = len(bin_key)
    return ''.join(str(int(bin_txt[i]) ^ int(bin_key[i % bin_key_size])) for i in range(bin_txt_size))
