def euclidean_algorithm(a: int, b: int):
    if b == 0:
        return 1, 0
    s, t = euclidean_algorithm(b, a % b)
    return t, s - t * (a // b)


def euclidean_algorithm_simple(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while a % b:
        temp_b = b
        b = a % b
        a = temp_b
    return b
