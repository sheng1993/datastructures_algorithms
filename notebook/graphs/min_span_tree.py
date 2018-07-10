from heapq import heappush, heappop, heapify
from utils import disjointset

G = {
    ('A', 'B'): 4,
    ('A', 'E'): 1,
    ('A', 'D'): 2,
    ('D', 'E'): 3,
    ('B', 'E'): 5,
    ('B', 'C'): 8,
    ('B', 'F'): 6,
    ('E', 'F'): 9,
    ('C', 'F'): 1
}


def kruskal(g):
    """
    O(|E|log|V|)
    """
    dset = disjointset()
    q = []
    X = set()

    for (u, v) in g:
        if u not in dset:
            dset.add(u)
        if v not in dset:
            dset.add(v)
        heappush(q, (g[(u, v)], (u, v)))
    
    while len(q) > 0:
        (p, (u, v)) = heappop(q)
        if dset.find(u) !=  dset.find(v):
            X.add((u, v))
            dset.union(u, v)        
    
    return X
    
def prim():
    """
    Dijkstra like
    O(|V|^2) for array-based implementation
    O(|E|log|V|) for binary heap-based implementation
    """
    pass

print(kruskal(G))

