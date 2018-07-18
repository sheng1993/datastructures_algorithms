
def apply_suffle(a, b, c):
    original_position = dict()
    for i in range(len(a)):
        if a[i] not in original_position:
            original_position[a[i]] = []
        original_position[a[i]].append(i)

    new_position = [0] * len(b)
    for i in range(len(b)):
        pos = original_position[b[i]].pop()
        new_position[pos] = i

    new_array = [None] * len(c)

    for i in range(len(c)):
        new_array[new_position[i]] = c[i]
    return new_array


print(apply_suffle([15, 2, 66, 20, 199], [2, 199, 15, 66, 20], [1, 2, 3, 4 ,5]))