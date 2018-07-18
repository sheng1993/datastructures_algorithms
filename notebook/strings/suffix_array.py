def sort_characters(s: str):
    order = [None] * len(s)
    count = [0] * 256

    for i in range(len(s)):
        count[ord(s[i])] += 1
    
    for j in range(1, 256):
        count[j] = count[j] + count[j - 1]
    
    for i in range(len(s) - 1, -1 , -1):
        c = s[i]
        count[ord(c)] -= 1
        order[count[ord(c)]] = i
    
    return order


def compute_char_classes(s: str, order: list):
    _class = [None] * len(s)
    _class[order[0]] = 0

    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            _class[order[i]] = _class[order[i - 1]] + 1
        else:
            _class[order[i]] = _class[order[i - 1]]
    return _class


def sort_double(s: str, l: int, order: list, _class: list):
    count = [0] * len(s)
    newOrder = [0] * len(s)

    for i in range(len(s)):
        count[_class[i]] += 1
    
    for j in range(1, len(s)):
        count[j] = count[j - 1] + count[j]

    for i in range(len(s) - 1, -1 , -1):
        start = (order[i] - l + len(s)) % len(s)
        cl = _class[start]
        count[cl] -= 1
        newOrder[count[cl]] = start

    return newOrder


def update_classes(newOrder: list, _class: list, l: int):
    n = len(newOrder)
    newClass = [None] * n
    newClass[newOrder[0]] = 0
    for i in range(1, n):
        # First half
        cur = newOrder[i]
        prev = newOrder[i - 1]
        # Second half
        mid = (cur + l) % n
        midPrev = (prev + l) % n
        if _class[cur] != _class[prev] or _class[mid] != _class[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass


def build_suffix_array(s: str):
    order = sort_characters(s)
    _class = compute_char_classes(s, order)

    l = 1

    while l < len(s):
        order = sort_double(s, l, order, _class)
        _class = update_classes(order, _class, l)
        l = 2*l
    return order

s = 'bbacbdeb$'
suffix_array = build_suffix_array(s)
print(suffix_array)
