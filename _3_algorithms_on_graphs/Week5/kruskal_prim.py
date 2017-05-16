from utility.disjointsets import DisjointSet
from utility.graphs import Graph, Vertex
from heapq import heappush, heappop, heapify
import math

"""Minimum spanning tree (MST)
    Input: A connected, undirected graph G = (V,E) with positive edge weights.
    Ouput: A subset of edges E' C E
    of minimum total weight such that the graph (V,E') is connected
"""


def kruskal(g: Graph):
    """
    Repeatedly add the next lightest edge if this doesn't produce a cycle;
    use disjoint sets to check whether the current edge joins two vertices
    from different components.
    O(|E|log|V|) if edges are sorted.
    :param g:
    :return:
    """
    v_set = DisjointSet()
    E = []
    for v in g.V.keys():
        v_set.make_set(v)

    X = set()

    for e in g.E:
        heappush(E, (e[0], e[1]))

    while len(E) != 0:
        e = heappop(E)
        if v_set.find(e[1][0]) != v_set.find(e[1][1]):
            X.add(e)
            v_set.union(e[1][0], e[1][1])

    return X


def prim(g: Graph):
    """
    Repeatedly attach a new vertex to the current tree by a lightest edge;
    use priority queue to quickly find the next lightest edge

    Pseudocode:
    for all u in V:
        cost[u] = inf, parent[u] = None
    pick any initial vertex u
    cost[u] = 0
    PrioQ = MakeQueue(V)
    while PrioQ is not empty:
        v = ExtractMin(PrioQ)
        for all {v,z} in E:
            if z in PrioQ and cost[z] > w(v,z):
                cost[z] = w(v,z), parent[z] = v
                ChangePriority(PrioQ, z, cost[z])

    Runtime: O(|E|log|V|)
    :param g:
    :return:
    """
    pass

if __name__ == '__main__':
    G = Graph()
    G.V[0] = Vertex()
    G.V[1] = Vertex()
    G.V[2] = Vertex()
    G.V[3] = Vertex()
    G.V[4] = Vertex()
    G.V[5] = Vertex()

    G.E.append((4, (0, 1)))
    G.E.append((8, (1, 2)))
    G.E.append((1, (2, 3)))
    G.E.append((9, (3, 4)))
    G.E.append((3, (4, 5)))
    G.E.append((2, (5, 0)))
    G.E.append((1, (0, 4)))
    G.E.append((6, (1, 3)))
    G.E.append((5, (1, 4)))
    print(kruskal(G))