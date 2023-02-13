import random
from math import ceil, sqrt

from RSA.euclidean import euclidean_algorithm_simple
from RSA.expmod import fast_bin_pow


def jacoby_symbol(a: int, b: int) -> int:
    if euclidean_algorithm_simple(a, b) != 1:
        return 0
    r = 1
    # t = 0
    while True:
        while a & 1 == 0:
            # t += 1
            a >>= 1
            # if t & 1:
            if b % 8 == 3 or b % 8 == 5:
                r = -r
        if a % 4 == b % 4 == 3:
            r = -r
        a, b = b % a, a
        if a == 0:
            return r


def solovay_strassen(n: int, rounds: int | None = None) -> bool:
    if rounds is None:
        rounds = n.bit_length()
    for _ in range(rounds):
        a = random.randint(3, n - 1)
        if euclidean_algorithm_simple(a, n) > 1:
            return False
        r = jacoby_symbol(a, n) % n
        s = fast_bin_pow(a, (n - 1) // 2, n)
        if r != s:
            return False
    return True


def get_prime(bit_len: int) -> int:
    x = random.randint(2 ** (bit_len - 1), 2**bit_len)
    while not solovay_strassen(x):
        x = random.randint(2 ** (bit_len - 1), 2**bit_len)
    return x


def get_safe_prime(bit_len: int) -> int:
    x = random.randint(2 ** (bit_len - 1), 2**bit_len)
    while not solovay_strassen(x) or not solovay_strassen((x - 1) // 2):
        x = random.randint(2 ** (bit_len - 1), 2**bit_len)
    return x


def get_primitive_root(bit_len: int, p: int) -> int:
    euler = p - 1
    g = random.randint(2 ** (bit_len - 1), 2**bit_len)
    while True:
        if (
            fast_bin_pow(g, euler, p) == 1
            and euclidean_algorithm_simple(g, p) == 1
            and fast_bin_pow(g, euler // 2, p) != 1
            and solovay_strassen(g)
        ):
            return g
        g = random.randint(2 ** (bit_len - 1), 2**bit_len)


def bsgs(g: int, h: int, n: int) -> int | None:
    m = ceil(sqrt(n - 1))
    giant_step = {fast_bin_pow(g, i, n): i for i in range(m)}

    c = fast_bin_pow(g, m * (n - 2), n)
    for j in range(m):
        baby_step = h * fast_bin_pow(c, j, n) % n
        if baby_step in giant_step:
            return (m * j + giant_step[baby_step]) % n
    return None
