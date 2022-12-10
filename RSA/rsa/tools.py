import random

from RSA.expmod.tools import fast_bin_pow


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def miller_rabin(num, rounds=5) -> bool:
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
    return True


def get_prime(bit_size: int) -> int:
    x = random.randint(2 ** (bit_size - 1), 2 ** bit_size)
    while not miller_rabin(x, 5):
        x = random.randint(2 ** (bit_size - 1), 2 ** bit_size)
    return x
