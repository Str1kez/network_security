from exceptions import ValidationError


def bit_validation(bit: str) -> int:
    try:
        int_bit = int(bit)
    except ValueError:
        raise ValidationError('Нужны цифры в поле битов')
    if int_bit < 8 or not bit:
        raise ValidationError('Неверный размер битов')
    return int_bit
