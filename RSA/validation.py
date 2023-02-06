from exceptions import ValidationError


def expmod_validation(number: str, exp: str, mod: str) -> tuple[int, int, int]:
    try:
        n = int(number)
        e = int(exp)
        m = int(mod)
        if e < 0 or m < 0:
            raise ValidationError(f"{exp=}, {mod=}\nДолжны быть >= 0")
        return n, e, m
    except ValueError:
        raise ValidationError("Передай числа")


def euclidean_validation(row_a: str, row_b: str) -> tuple[int, int]:
    try:
        a = int(row_a)
        b = int(row_b)
        if a < 0 or b < 0:
            raise ValidationError(f"{a=}, {b=}\nДолжны быть >= 0")
        return a, b
    except ValueError:
        raise ValidationError("Передай числа")
