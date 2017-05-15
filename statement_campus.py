

def StairCase(n):
    for i in range(0, n):
        if i == n - 1:
            print('#' * n)
        else:
            print(' ' * (n - 1 - i), end="")
            print('#' * (i + 1))


def summation(numbers):
    return sum(numbers)


def decode(encoded):
    i = len(encoded) - 1
    decoded = []
    while i > 0:
        int_value = int(encoded[i:i - 2 if i > 1 else None:-1])
        if int_value == 32 or 64 <= int_value <= 90 or 97 <= int_value <= 99:
            decoded.append(int_value)
            i -= 2
        else:
            int_value = int(encoded[i:i - 3 if i > 2 else None:-1])
            if 100 <= int_value <= 122:
                decoded.append(int_value)
            i -= 3

    return ''.join(chr(i) for i in decoded)


def getJsonResponse(params):
    import urllib.request as request
    url = 'https://jsonmock.hackerrank.com/api/movies/search/'
    request.urlopen()


if __name__ == '__main__':
    param = {'Title':'spiderman'}
    for key in param:
        print(key)