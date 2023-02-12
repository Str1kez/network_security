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

    if temp_g_bit < 64 or temp_p_bit < 64:
        raise ValidationError("Необходима разрядность больше 64 бит")

    return temp_a, temp_g_bit, temp_p_bit
