from exceptions import ValidationError


def expmod_validation(number: str, exp: str, mod: str) -> tuple[int, int, int]:
    try:
        number = int(number)
        exp = int(exp)
        mod = int(mod)
        if exp < 0 or mod < 0:
            raise ValidationError(f"{exp=}, {mod=}\nДолжны быть >= 0")
        return number, exp, mod
    except ValueError:
        raise ValidationError("Передай числа")


def euclidean_validation(a: str, b: str) -> tuple[int, int]:
    try:
        a = int(a)
        b = int(b)
        if a < 0 or b < 0:
            raise ValidationError(f"{a=}, {b=}\nДолжны быть >= 0")
        return a, b
    except ValueError:
        raise ValidationError("Передай числа")
