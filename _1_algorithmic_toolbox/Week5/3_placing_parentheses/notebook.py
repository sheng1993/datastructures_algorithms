import sys
import math


"""Placing parentheses
Input: A sequence of digits d1,...dn and a sequence of operation op1,...,opn E {+,-,x}
Output: An order of applying these operations that maximizes the value of the expression

d1 op1 d2 op2 ... opn-1 dn

                M(i,k) opk M(k+1,j)
M(i,j) = max {  M(i,k) opk m(k+1,j)                      
                m(i,k) opk M(k+1,j)
                m(i,k) opk m(k+1,j)
                
                M(i,k) opk M(k+1,j)
m(i,j) = min {  M(i,k) opk m(k+1,j)                      
                m(i,k) opk M(k+1,j)
                m(i,k) opk m(k+1,j)

"""


def add(a,b):
    return a + b


def sub(a,b):
    return a - b


def mult(a,b):
    return a * b

d = [5, 8, 7, 4, 8, 9]
op = [sub, add, mult, sub, add]
n = len(d)
m = [[-1 for x in range(n)] for y in range(n)]
M = [[-1 for x in range(n)] for y in range(n)]


def min_and_max(i,j):
    min_v = +math.inf
    max_v = -math.inf
    for k in range(i, j):
        opk = op[k]
        a = opk(M[i][k], M[k+1][j])
        b = opk(M[i][k], m[k+1][j])
        c = opk(m[i][k], M[k+1][j])
        d = opk(m[i][k], m[k+1][j])
        min_v = min(min_v, a, b, c, d)
        max_v = max(max_v, a, b, c, d)
    return min_v, max_v

def parentheses():
    for i in range(n):
        m[i][i] = M[i][i] = d[i]
    for s in range(1, n + 1):
        for i in range(1, (n + 1) - s):
            j = i + s
            min_v, max_v = min_and_max(i - 1, j - 1)
            m[i - 1][j - 1] = min_v
            M[i - 1][j - 1] = max_v
    return M[1][n - 1]

if __name__ == '__main__':
    parentheses()
    [print(row) for row in m]
    print('----------------')
    [print(row) for row in M]