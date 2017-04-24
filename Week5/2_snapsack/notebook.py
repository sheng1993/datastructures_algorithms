import sys
import math

"""
Knapsack
1- fractional -> greedy algorithm
2- discrete -> DP
    2.1- with repetition
    2.2- without repetition
"""


def knapsack_repetition(W, weights, v):
    """Knapsack with repetitions problem
    Input: Weights w1...wn and values v1...vn and total weight W
    Output: The maximum value of items whose weight does not exceed W.
    """

    ws = [-1 for x in range(W + 1)]
    ws[0] = 0

    n = len(v)

    for w in range(W):
        ws[w + 1] = 0
        for i in range(n):
            if weights[i] <= w + 1:
                val = ws[(w + 1) - weights[i]] + v[i]
                if val > ws[w + 1]:
                    ws[w + 1] = val
    return ws[W]

def knapsack_with_repetition_recursive(W, weights, v, table={}):
    if W in table:
        return table[W]
    value = 0
    for i in range(len(v)):
        if weights[i] <= W:
            val = knapsack_with_repetition_recursive(W - weights[i], weights, v, table) + v[i]
            if val > value:
                value = val
    table[W] = value
    return table[W]


def knapsack_without_repetition(W, weights, v):
    """Knapsack without repetition problem
    """

    m = [[0 if y == 0 or x == 0 else -1 for x in range(W + 1)] for y in range(len(weights) + 1)]
    n = len(weights)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            m[i][w] = m[i - 1][w]
            if weights[i - 1] <= w:
                val = m[i - 1][w - weights[i - 1]] + v[i - 1]
                if m[i][w] < val:
                    m[i][w] = val

    [print(row) for row in m]

    solution = [False for x in range(n)]

    w = W
    i = n
    while w > 0 and i > 0:
        val = m[i][w]
        if val != m[i - 1][w]:
            solution[i - 1] = True
            w -= weights[i - 1]
        i -= 1
    print(solution)

    return m[n][W]

if __name__ == '__main__':
    print(knapsack_repetition(10, [6,3,4,2], [30,14,16,9]))
    print(knapsack_with_repetition_recursive(10, [6,3,4,2], [30,14,16,9]))
    # knapsack_without_repetition(10, [6, 3, 4, 2], [30, 14, 16, 9])