from typing import List

def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n == 1: 
        return [0] 
        
    adj = [set() for _ in range(n)]                     # type: List[set]
    leaves = [i for i in range(n) if len(adj) == 1]
 
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1: new_leaves.append(j)
        leaves = new_leaves
    return leaves


print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))