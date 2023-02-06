def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    gcd, s, t = extended_euclidean_algorithm(b, a % b)
    return gcd, t, s - t * (a // b)


def euclidean_algorithm_simple(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while a % b:
        temp_b = b
        b = a % b
        a = temp_b
    return b
