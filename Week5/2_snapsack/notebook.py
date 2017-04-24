import sys
import math

'''
Knapsack
1- fractional -> greedy algorithm
2- discrete -> DP
    2.1- with repetition
    2.2- without repetition
'''

'''
Knapsack with repetitions problem
Input: Weights w1...wn and values v1...vn and total weight W
Output: The maximum value of items whose weight does not exceed W.
'''

def knapsack_repetition(W, weights, v):
    ws = [-1 for x in range(W + 1)]
    ws[0] = 0

    for w in range(W):
        ws[w + 1] = 0
        for i in range(len(v)):
            if weights[i] <= w + 1:
                val = ws[(w + 1) - weights[i]] + v[i]
                if val > ws[w + 1]:
                    ws[w + 1] = val
    return ws[W]

if __name__ == '__main__':
    print(knapsack_repetition(10, [6,3,4,2], [30,14,16,9]))