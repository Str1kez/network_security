import random

from RSA.euclidean.tools import extended_euclidean_algorithm
from RSA.expmod.tools import fast_bin_pow


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def miller_rabin(num: int, rounds: int = 5) -> bool:
    """
    Проверка на простоту
    """
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    t = num - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    for _ in range(rounds):
        a = random.randint(2, num - 1)
        x = fast_bin_pow(a, t, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = fast_bin_pow(x, 2, num)
            if x == 1:
                return False
            if x == num - 1:
                break
        else:
            return False
    return True


def get_prime(bit: int) -> int:
    x = random.randint(2 ** (bit - 1), 2**bit)
    while not miller_rabin(x):
        x = random.randint(2 ** (bit - 1), 2**bit)
    return x


def get_public_key(euler: int, length: int = 4) -> int:
    key_len = 10 ** (len(str(euler)) // 3)
    # key = random.randint(10 ** (key_len - 1), 10**key_len)
    key = random.randint(key_len, 10 * key_len)
    while extended_euclidean_algorithm(key, euler)[0] != 1:
        key = random.randint(key_len, 10 * key_len)
        # key = random.randint(10 ** (key_len - 1), 10**key_len)

    return key


def get_private_key(euler: int, public_key: int) -> int:
    return extended_euclidean_algorithm(public_key, euler)[1] % euler
