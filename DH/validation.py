from DH.tools import solovay_strassen
from exceptions import ValidationError


def diffie_hellman_validation(a: str, g_bit: str, p_bit: str) -> tuple[int, int, int] | None:
    try:
        temp_a = int(a)
        temp_g_bit = int(g_bit)
        temp_p_bit = int(p_bit)
    except ValueError:
        raise ValidationError("Введите числа")

    if temp_a < 1:
        raise ValidationError("а должно быть натуральным")

    if temp_g_bit < 8 or temp_p_bit < 8:
        raise ValidationError("Необходима разрядность больше 8 бит (не для теста, можно и большe)")

    return temp_a, temp_g_bit, temp_p_bit


def bsgs_validation(y: str, g: str, p: str) -> tuple[int, int, int] | None:
    try:
        temp_y = int(y)
        temp_g = int(g)
        temp_p = int(p)
    except ValueError:
        raise ValidationError("Введите числа")

    if temp_y < 2:
        raise ValidationError("y должен быть положительным и больше 1")

    if not solovay_strassen(temp_g):
        raise ValidationError("g дожен быть простым")

    if not solovay_strassen(temp_p):
        raise ValidationError("p должен быть простым")

    return temp_y, temp_g, temp_p
