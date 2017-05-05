import sys
import math

'''
Optimal alignment
Input: Two strings, mismatch penalty 'u', and indel penalty 'o'
Output: An alignment of the strings maximizing the score.

Alignment score:
#matches - 'u' * #mismatches - 'o' * indels
'''

'''
Common Subsequence
Matches in an alignment of two strings form their common subsequence.

[A, T, -, G, T, T, A, T, A]
[A, T, C, G, T, -, C, -, C]
(ATGT)
'''

'''
Longest common subsequence
Input: Two strings.
Output: A longest common subsequence of these strings

Maximizing the length of a common subsequence corresponds to maximizing
the score of an alignment with 'u' = 'o' = 0.
'''

'''
Edit distance
Input: Two strings
Output: the minimum number of operations (insertion, deletions, and substitutions
of symbols) to transform one string into another.

The minimum number of insertions, deletions and mismatches in an alignment of two strings
(among all possible alignments).

[E,D,I,-,T,I,N,G,-]
[-,D,I,S,T,A,N,C,E]

Minimizing edit distance = maximizing alignment score

string A[1...n] and B[1...m]

Insertion:  +1
    A[1... i ]  -
    B[1...j-1] B[j]

Deletion:   +1
    A[1...i-1 ]  A[i]
    B[1... j  ]   -

Mismatch:   +1
    A[1...i-1] A[j]
    B[1...j-1] B[j]

Match:
    A[1...i-1] A[j]
    B[1...j-1] B[j]

D(i,j) = edit distance of i-prefix A[1...i] and a j-prefix B[1...j]

D(i,j) = min of:
    - D(i, j-1) + 1
    - D(i-1, j) + 1
    - D(i-1, j-1) + 1   if A[i] != B[j]
    - D(i-1, j-1)       if A[i] == B[j]
'''

def edit_distance(A, B):
    len_a = len(A) + 1
    len_b = len(B) + 1
    m = [[y if (x == 0) else (x if (y == 0) else -1) for x in range(len_b)] for y in range(len_a)]

    for i in range(1, len_a):
        for j in range(1, len_b):
            insertion = m[i][j-1] + 1
            deletion = m[i-1][j] + 1
            match = m[i-1][j-1]
            mismatch = m[i-1][j-1] + 1

            if A[i - 1] == B[j - 1]:
                d = min(insertion, deletion, match)
            else:
                d = min(insertion, deletion, mismatch)

            m[i][j] = d

    print('A= {}\nB= {}'.format(A, B))
    [print(row) for row in m]

    return m[len_a - 1][len_b - 1]

if __name__ == '__main__':
    A = 'EDITING'
    B = 'DISTANCE'

    print(edit_distance(A, B))
    print(edit_distance('bread', 'really'))