def euclidean_algorithm(a: int, b: int):
    if b == 0:
        return 1, 0
    s, t = euclidean_algorithm(b, a % b)
    return t, s - t * (a // b)
