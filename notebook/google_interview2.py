def longestRepeated(arr):
    n = len(arr)
    m = [[ 0 for i in range(n + 1)] for _ in range(n + 1)]

    max_count = 0

    for i in range(1, n + 1):
        for j in range(i+1, n + 1):
            if arr[i - 1] == arr[j - 1] and m[i][j] < (j - i):
                m[i][j] = m[i - 1][j - 1] + 1

                if m[i][j] > max_count:
                    max_count = m[i][j]
            
            else:
                m[i][j] = 0
    
    return max_count

print(longestRepeated([1,2,3,1,2,3]))