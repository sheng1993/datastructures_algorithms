# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def targets(B, x, y):
    n = len(B)
    t = []
    
    #up-right
    i = x - 1
    j = y - 1
    while i > 0 and j > 0:
        if B[i][j] == 'X':
            if B[i - 1][j - 1] == '.':
                t.append((i - 1, j - 1))
            break
        i -= 1
        j -= 1
    
    #top-left
    i = x - 1
    j = y + 1
    while i > 0 and j < n - 1:
        if B[i][j] == 'X':
            if B[i - 1][j + 1] == '.':
                t.append((i - 1, j + 1))
            break
        i -= 1
        j += 1
    
    return t
    
def max_for_position(B, x, y):
    t = targets(B, x, y)
    if len(t) == 0: return 0
    
    v = []
    for (i, j) in t:
        v.append(1 + max_for_position(B, i, j))
    return max(v)
        
def solution(B):
    n = len(B)
    x = -1
    y = -1
    for i in range(n):
        for j in range(n):
            if B[i][j] == 'O':
                x = i
                y = j
                break
    
    return max_for_position(B, x, y)
        
        
print(solution(['X....', '.X...', '..O..', '...X.', '.....'] ))

