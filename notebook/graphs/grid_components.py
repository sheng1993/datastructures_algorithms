lb = 0
rd = 1
bl = 2
m = [
    [lb, lb, bl, rd],
    [lb, bl, rd, bl],
    [rd, bl, bl, bl]
    ]

def is_valid(_m, i, j, curr, visited):
    return 0 <= i < len(_m) and 0 <= j < len(_m[0]) and _m[i][j] == curr and (i, j) not  in visited

def get_neighbors(_m, i, j, curr, visited):
    n = []
    if is_valid(_m, i-1, j, curr, visited):
        n.append((i-1, j))
    if is_valid(_m, i, j-1, curr, visited):
        n.append((i, j-1))
    if is_valid(_m, i, j+1, curr, visited):
        n.append((i, j + 1))
    if is_valid(_m, i+1, j, curr, visited):
        n.append((i+1, j))
    return n


def dfs(_m, i, j, visited):
    if (i, j) in visited:
        return -1
    
    q = [(i, j)]
    cont = 0
    curr = _m[i][j]

    while len(q) > 0:
        _i, _j = q.pop(0)
        visited[(_i, _j)] = True
        cont += 1
        for x, y in  get_neighbors(_m, _i, _j, curr, visited):
            q.append((x, y))
    
    return cont



def connected_components(_m):
    visited = dict()
    max = 0
    _max = None
    for i in range(len(_m)):
        for j in range(len(_m[0])):
            aux = dfs(_m, i, j, visited)
            if aux >= max:
                max = aux
                _max = (i, j)
    return max, _max

print(connected_components(m))