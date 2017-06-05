import math
import random


def is_prime_miller_rabin(n, k=10):
    from random import randrange
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def is_prime_fermat(num):
    if num == 2:
        return True
    if not num and num == 1:
        return False
    return pow(2, num - 1, num) == 1


def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime_miller_rabin(num):
        num += 1
    while True:
        if is_prime_miller_rabin(num):
            break
        num += 1
    return num


def poly_hash(s, p, x):
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h


def pre_compute_hashes(t, l_pattern, p, x):
    l_text = len(t)
    h = [0] * (l_text - l_pattern + 1)
    s = t[l_text - l_pattern:]
    h[l_text - l_pattern] = poly_hash(s, p, x)
    y = 1
    for i in range(1, l_pattern + 1):
        y = (y * x) % p
    for i in range(l_text - l_pattern - 1, -1, -1):
        h[i] = (x * h[i + 1] + (ord(t[i]) - y * ord(t[i + l_pattern]))) % p
    return h


def rabin_karp(text, pattern):
    """
    Average running time O(|T| + (q+1)|P|)
    Usually q is small, so this is much less than O(|T||P|)
    :param text:
    :param pattern:
    :return:
    """
    l_text = len(text)
    l_pattern = len(pattern)
    p = next_prime(l_text * l_pattern)
    x = random.randint(1, p - 1)
    result = []  # type: list
    p_hash = poly_hash(pattern, p, x)
    H = pre_compute_hashes(text, l_pattern, p, x)
    for i in range(0, l_text - l_pattern + 1):
        if p_hash != H[i]:
            continue
        if pattern == text[i: i + l_pattern]:
            result.append(i)
    return result


if __name__ == '__main__':
    pattern = 'st'
    text = 'sst'
    print(rabin_karp(text, pattern))