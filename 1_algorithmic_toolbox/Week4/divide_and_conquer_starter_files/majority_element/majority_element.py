# Uses python3
import sys


def get_majority_element(a, left, right):
    m = -1  # element
    i = 0   # counter

    for x in range(right):
        if i == 0:
            m = a[x]
            i = 1
        elif m == a[x]:
            i += 1
        else:
            i -= 1

    cont = 0
    for x in range(right):
        if a[x] == m:
            cont += 1

    if cont > right/2:
        return m
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
