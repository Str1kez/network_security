def fast_bin_pow(number: int, exp: int, mod: int) -> int:
    result = 1
    while exp:
        if exp & 1:
            result = result * number % mod
        exp >>= 1
        number = number * number % mod
    return result
