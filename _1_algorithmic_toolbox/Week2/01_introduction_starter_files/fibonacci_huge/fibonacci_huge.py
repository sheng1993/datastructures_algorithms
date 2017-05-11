# Uses python3
import sys

def gcd_efficient(a, b):
    if b == 0:
        return a
    a_ = a % b
    return gcd_efficient(b, a_)

def lcm_gcd(a, b):
    lcm = (a*b)//gcd_efficient(a, b)
    return lcm

def get_pisano_period(m):
    raise NotImplemented('')


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    n = n % get_pisano_period(m)

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
