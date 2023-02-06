from exceptions import ValidationError
from RSA.euclidean.tools import extended_euclidean_algorithm
from RSA.rsa.tools import euler_function, miller_rabin


def bit_validation(bit: str) -> int:
    try:
        int_bit = int(bit)
    except ValueError:
        raise ValidationError('Нужны цифры в поле битов')
    if int_bit < 8:
        raise ValidationError('Неверный (малый) размер битов')

    return int_bit


def params_validation(p: str, q: str, e: str) -> tuple[int, int, int]:
    try:
        temp_p = int(p)
        temp_q = int(q)
        temp_e = int(e)
    except ValueError:
        raise ValidationError("Нужны числа в полях p, q, e")
    if temp_p < 0 or temp_q < 0 or temp_e < 0:
        raise ValidationError("Числа должны быть >= 0")
    if len(e) < 3:
        raise ValidationError("Маленькое число для открытого ключа")
    if not miller_rabin(temp_p):
        raise ValidationError("p - не простое")
    if not miller_rabin(temp_q):
        raise ValidationError("q - не простое")
    if extended_euclidean_algorithm(temp_e, euler_function(temp_p, temp_q))[0] != 1:
        raise ValidationError("e - не взаимно простое")

    return temp_p, temp_q, temp_e
